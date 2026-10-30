#!/usr/bin/env python3
"""Read-only source, link, PDF-hash, and archive-integrity checks.

These checks do not verify mathematical proofs or external citations. They
also do not establish binary reproducibility across different TeX versions.
"""
from __future__ import annotations

from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[2]
SOURCE_REL = "papers/src/main.tex"
PDF_REL = "papers/paper_v2.pdf"
ARCHIVE = ROOT / "archive/repository-2026-10-23"


def strip_tex_comments(text: str) -> str:
    lines = []
    for line in text.splitlines():
        for index, character in enumerate(line):
            if character == "%":
                previous = index - 1
                while previous >= 0 and line[previous] == "\\":
                    previous -= 1
                if (index - 1 - previous) % 2 == 0:
                    line = line[:index]
                    break
        lines.append(line)
    return "\n".join(lines)


def check_tex(errors: list[str]) -> tuple[int, int]:
    try:
        text = strip_tex_comments((ROOT / SOURCE_REL).read_text(encoding="utf-8"))
    except OSError as exc:
        errors.append(f"Cannot read {SOURCE_REL}: {exc}")
        return 0, 0
    # The published manifest hashes one self-contained source.
    if re.search(r"\\(?:input|include|bibliography|addbibresource)\b", text):
        errors.append("The paper must remain self-contained; external TeX/bibliography inputs are not hashed")
    if not re.search(r"\\tableofcontents\b", text):
        errors.append("The paper has no table of contents")
    labels = re.findall(r"\\label\s*\{([^}]+)\}", text)
    keys = re.findall(r"\\bibitem(?:\[[^\]]*\])?\s*\{([^}]+)\}", text)
    for kind, values in (("label", labels), ("bibliography key", keys)):
        for key, count in Counter(values).items():
            if count > 1:
                errors.append(f"Duplicate {kind}: {key}")
    groups = re.findall(r"\\(?:ref|eqref|pageref|autoref|nameref|cref|Cref)\*?\s*\{([^}]+)\}", text)
    groups += re.findall(r"\\hyperref\s*\[([^\]]+)\]", text)
    for group in groups:
        for key in group.split(","):
            if key.strip() not in labels:
                errors.append(f"Undefined label: {key.strip()}")
    uses = re.findall(r"\\(?:cite\w*|nocite)\*?\s*(?:\[[^\]]*\]\s*)*\{([^}]+)\}", text)
    for group in uses:
        for key in group.split(","):
            if key.strip() != "*" and key.strip() not in keys:
                errors.append(f"Undefined citation: {key.strip()}")
    if not keys:
        errors.append("The embedded bibliography is missing")
    return len(labels), len(keys)


def read_json(path: Path, errors: list[str]):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        errors.append(f"Cannot read {path.relative_to(ROOT)}: {exc}")
        return None


def check_manifest(errors: list[str]) -> None:
    manifest = read_json(ROOT / "verification/build_manifest.json", errors)
    if not isinstance(manifest, dict):
        if manifest is not None:
            errors.append("Build manifest must be a JSON object")
        return
    for name, expected_path in (("source", SOURCE_REL), ("pdf", PDF_REL)):
        record = manifest.get(name)
        if not isinstance(record, dict) or record.get("path") != expected_path:
            errors.append(f"Build manifest needs {name}.path = {expected_path}")
            continue
        try:
            data = (ROOT / expected_path).read_bytes()
        except OSError as exc:
            errors.append(f"Cannot read {expected_path}: {exc}")
            continue
        if not re.fullmatch(r"[0-9a-f]{64}", str(record.get("sha256", ""))):
            errors.append(f"Invalid SHA-256 in {name} manifest record")
        elif hashlib.sha256(data).hexdigest() != record["sha256"]:
            errors.append(f"SHA-256 mismatch: {expected_path}; build with --publish after reviewing changes")
        if type(record.get("bytes")) is not int or record["bytes"] != len(data):
            errors.append(f"Byte-count mismatch: {expected_path}")
        if name == "pdf":
            if not data.startswith(b"%PDF-") or b"%%EOF" not in data[-2048:]:
                errors.append("Published PDF has a missing header or end marker")
            if "pages" in record and (type(record["pages"]) is not int or record["pages"] < 1):
                errors.append("Invalid page count in PDF manifest record")


def check_archive(errors: list[str]) -> int:
    manifest = read_json(ARCHIVE / "snapshot-manifest.json", errors)
    if not isinstance(manifest, dict) or not isinstance(manifest.get("files"), dict):
        if manifest is not None:
            errors.append("Archive manifest must contain a files mapping")
        return 0
    files = manifest["files"]
    if not files:
        errors.append("Archive manifest is empty")
    if not re.fullmatch(r"[0-9a-f]{40}", str(manifest.get("source_commit", ""))):
        errors.append("Archive manifest has no valid source commit")
    actual = {path.relative_to(ARCHIVE).as_posix() for path in ARCHIVE.rglob("*") if path.is_file()}
    actual.discard("snapshot-manifest.json")
    for relative in sorted(actual - set(files)):
        errors.append(f"Unrecorded file in historical snapshot: {relative}")
    for relative in sorted(set(files) - actual):
        errors.append(f"Missing historical snapshot file: {relative}")
    checked = 0
    for relative, expected_hash in files.items():
        if (not relative or relative.startswith("/") or "\\" in relative or ":" in relative
                or ".." in relative.split("/") or relative == "snapshot-manifest.json"):
            errors.append(f"Invalid archive manifest path: {relative!r}")
            continue
        path = (ARCHIVE / relative).resolve()
        if not path.is_relative_to(ARCHIVE.resolve()) or not path.is_file():
            continue
        if not re.fullmatch(r"[0-9a-f]{64}", str(expected_hash)):
            errors.append(f"Invalid historical snapshot SHA-256: {relative}")
            continue
        if hashlib.sha256(path.read_bytes()).hexdigest() != expected_hash:
            errors.append(f"Historical snapshot bytes changed: {relative}")
        checked += 1
    return checked


def without_markdown_code(text: str) -> str:
    lines, fence = [], None
    for line in text.splitlines():
        opening = re.match(r"^\s{0,3}(`{3,}|~{3,})", line)
        if fence is None and opening:
            fence = opening.group(1)
        elif fence is not None:
            if re.match(r"^\s{0,3}" + re.escape(fence[0]) + "{" + str(len(fence)) + r",}\s*$", line):
                fence = None
        else:
            lines.append(line)
    return re.sub(r"(`+).*?\1", "", "\n".join(lines))


def markdown_targets(text: str):
    for opening in re.finditer(r"!?\[[^\]\n]*\]\(", text):
        start = opening.end()
        if start < len(text) and text[start] == "<":
            end = text.find(">", start + 1)
            if end >= 0:
                yield text[start + 1:end]
            continue
        index, depth = start, 0
        while index < len(text):
            char = text[index]
            if char == "\\":
                index += 2
                continue
            if char == "(":
                depth += 1
            elif char == ")":
                if depth == 0:
                    break
                depth -= 1
            elif char.isspace() and depth == 0:
                break
            index += 1
        if index > start:
            yield text[start:index]
    for match in re.finditer(r"^\s{0,3}\[[^\]\n]+\]:\s*(<[^>]+>|\S+)", text, re.M):
        yield match.group(1).strip("<>")
    for match in re.finditer(r"\b(?:href|src)=[\"']([^\"']+)[\"']", text, re.I):
        yield match.group(1)


def check_links(errors: list[str]) -> int:
    count = 0
    for path in ROOT.rglob("*.md"):
        relative = path.relative_to(ROOT)
        if any(part in {".git", "build", "__pycache__"} for part in relative.parts):
            continue
        if path.is_relative_to(ARCHIVE):
            continue  # Historical links remain immutable; their hashes are checked instead.
        for target in markdown_targets(without_markdown_code(path.read_text(encoding="utf-8"))):
            parsed = urlsplit(target)
            if parsed.scheme in {"http", "https", "mailto", "tel", "data"} or parsed.netloc:
                continue
            if parsed.scheme or target.startswith(("/", "\\")):
                errors.append(f"{relative}: nonportable local link {target!r}")
                continue
            if not parsed.path:
                continue  # Heading fragments and external availability are not checked.
            decoded = unquote(re.sub(r"\\([()])", r"\1", parsed.path))
            destination = (path.parent / decoded).resolve()
            if not destination.is_relative_to(ROOT):
                errors.append(f"{relative}: link escapes repository: {target!r}")
            elif not destination.exists():
                errors.append(f"{relative}: missing local link target {target!r}")
            count += 1
    return count


def main() -> int:
    errors: list[str] = []
    try:
        labels, citations = check_tex(errors)
        check_manifest(errors)
        archived = check_archive(errors)
        links = check_links(errors)
    except (OSError, ValueError, TypeError) as exc:
        errors.append(f"Verification could not complete: {exc}")
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(f"Verified {labels} labels, {citations} bibliography keys, {links} local links, "
          f"source/PDF hashes, and {archived} unchanged archived files.")
    print("Technical consistency checks passed; mathematical arguments are not mechanically verified.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
