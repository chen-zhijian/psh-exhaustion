#!/usr/bin/env python3
"""Check links, LaTeX references, and preserved source bytes without modifying files.

This is a structural check. It does not verify proofs, bibliographic accuracy,
novelty, external websites, or agreement between source and checked-in PDFs.
"""

from __future__ import annotations

from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
EXCLUDED = {".git", "build", "__pycache__", ".venv", "venv"}
# Historical sources are retained as evidence, not treated as active build roots.
TEX_ROOTS = ("overview.tex", "preprints/001-psh-exhaustion/psh_exhaustion_refereed.tex")
PDFS = ("overview.pdf", "preprints/001-psh-exhaustion/psh_exhaustion_refereed.pdf")


def visible_files(suffix: str):
    for path in ROOT.rglob(f"*{suffix}"):
        if not (set(path.relative_to(ROOT).parts) & EXCLUDED):
            yield path


def location(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def without_markdown_code(text: str) -> str:
    # Fences must start a line; matching opening and closing characters matter.
    lines = []
    fence = None
    for line in text.splitlines():
        opening = re.match(r"^\s{0,3}(`{3,}|~{3,})", line)
        if fence is None and opening:
            fence = opening.group(1)
            lines.append("")
        elif fence is not None:
            if re.match(r"^\s{0,3}" + re.escape(fence[0]) + "{" + str(len(fence)) + r",}\s*$", line):
                fence = None
            lines.append("")
        else:
            lines.append(line)
    return re.sub(r"(`+).*?\1", "", "\n".join(lines))


def markdown_targets(text: str):
    # Angle-bracket destinations support spaces. Ordinary destinations support
    # balanced parentheses, e.g. papers/Example_(revised).pdf.
    for opening in re.finditer(r"!?\[[^\]\n]*\]\(", text):
        start = opening.end()
        if start < len(text) and text[start] == "<":
            end = text.find(">", start + 1)
            if end >= 0:
                yield text[start + 1 : end]
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
    # Reference-style definitions: [paper]: path "optional title".
    for match in re.finditer(r"^\s{0,3}\[[^\]\n]+\]:\s*(<[^>]+>|\S+)", text, re.M):
        yield match.group(1).strip("<>")
    # Repository documentation may use simple HTML links or images.
    for match in re.finditer(r"\b(?:href|src)=[\"']([^\"']+)[\"']", text, re.I):
        yield match.group(1)


def check_markdown(path: Path, problems: list[str]) -> int:
    text = without_markdown_code(path.read_text(encoding="utf-8"))
    checked = 0
    for target in markdown_targets(text):
        parsed = urlsplit(target)
        if parsed.scheme in {"http", "https", "mailto", "tel", "data"} or parsed.netloc:
            continue
        if parsed.scheme or target.startswith(("/", "\\")):
            problems.append(f"{location(path)}: nonportable local link {target!r}")
            continue
        if not parsed.path:
            continue  # Fragment anchors are outside this check's scope.
        decoded = unquote(re.sub(r"\\([()])", r"\1", parsed.path))
        destination = (path.parent / decoded).resolve()
        if not destination.is_relative_to(ROOT):
            problems.append(f"{location(path)}: link escapes the repository: {target!r}")
        elif not destination.exists():
            problems.append(f"{location(path)}: missing link target {target!r}")
        checked += 1
    return checked


def strip_tex_comments(text: str) -> str:
    lines = []
    for line in text.splitlines():
        for index, char in enumerate(line):
            if char != "%":
                continue
            previous = index - 1
            while previous >= 0 and line[previous] == "\\":
                previous -= 1
            if (index - 1 - previous) % 2 == 0:
                line = line[:index]
                break
        lines.append(line)
    return "\n".join(lines)


def read_tex_tree(path: Path, problems: list[str], seen: set[Path]) -> str:
    if path in seen:
        problems.append(f"{location(path)}: repeated or circular TeX inclusion")
        return ""
    seen.add(path)
    if not path.is_file():
        problems.append(f"Missing TeX file: {location(path)}")
        return ""
    text = strip_tex_comments(path.read_text(encoding="utf-8"))
    result = [text]
    for included in re.findall(r"\\(?:input|include)\s*\{([^}]+)\}", text):
        child = path.parent / included
        if not child.suffix:
            child = child.with_suffix(".tex")
        child = child.resolve()
        if not child.is_relative_to(ROOT):
            problems.append(f"{location(path)}: TeX inclusion escapes the repository")
        else:
            result.append(read_tex_tree(child, problems, seen))
    return "\n".join(result)


def check_tex(relative: str, problems: list[str]) -> tuple[int, int]:
    path = ROOT / relative
    text = read_tex_tree(path, problems, set())
    labels = re.findall(r"\\label\s*\{([^}]+)\}", text)
    citations = re.findall(r"\\bibitem(?:\[[^\]]*\])?\s*\{([^}]+)\}", text)
    for bib in re.findall(r"\\bibliography\s*\{([^}]+)\}", text):
        for name in bib.split(","):
            bibpath = path.parent / name.strip()
            if not bibpath.suffix:
                bibpath = bibpath.with_suffix(".bib")
            if not bibpath.is_file():
                problems.append(f"{relative}: missing bibliography {name!r}")
            else:
                citations.extend(re.findall(r"@\w+\s*\{\s*([^,\s]+)\s*,", bibpath.read_text(encoding="utf-8")))
    for kind, values in (("label", labels), ("bibliography key", citations)):
        for key, count in Counter(values).items():
            if count > 1:
                problems.append(f"{relative}: duplicate {kind} {key!r}")
    references = re.findall(r"\\(?:ref|eqref|pageref|autoref|nameref|cref|Cref)\*?\s*\{([^}]+)\}", text)
    for group in references:
        for key in group.split(","):
            if key.strip() not in labels:
                problems.append(f"{relative}: undefined label {key.strip()!r}")
    uses = re.findall(r"\\(?:cite\w*|nocite)\*?\s*(?:\[[^\]]*\]\s*)*\{([^}]+)\}", text)
    for group in uses:
        for key in group.split(","):
            key = key.strip()
            if key != "*" and key not in citations:
                problems.append(f"{relative}: undefined citation {key!r}")
    return len(labels), len(citations)


def check_source_manifest(problems: list[str]) -> int:
    """Verify preserved supplied files against the repository's intake record."""
    manifest = ROOT / "source-manifest.json"
    try:
        data = json.loads(manifest.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        problems.append(f"Cannot read source-manifest.json: {exc}")
        return 0
    entries = data.get("files") if isinstance(data, dict) else None
    if not isinstance(entries, list) or not entries:
        problems.append("source-manifest.json: expected a nonempty files list")
        return 0
    seen = set()
    checked = 0
    for entry in entries:
        if not isinstance(entry, dict):
            problems.append("source-manifest.json: file entries must be objects")
            continue
        relative = entry.get("repository_path")
        if (
            not isinstance(relative, str)
            or not relative
            or relative.startswith("/")
            or "\\" in relative
            or ":" in relative
            or ".." in relative.split("/")
        ):
            problems.append(f"source-manifest.json: invalid repository_path {relative!r}")
            continue
        if relative in seen:
            problems.append(f"source-manifest.json: duplicate repository_path {relative!r}")
            continue
        seen.add(relative)
        path = (ROOT / relative).resolve()
        if not path.is_relative_to(ROOT):
            problems.append(f"source-manifest.json: path escapes the repository: {relative!r}")
            continue
        expected_hash = entry.get("sha256")
        expected_bytes = entry.get("bytes")
        if not isinstance(expected_hash, str) or not re.fullmatch(r"[0-9a-fA-F]{64}", expected_hash):
            problems.append(f"source-manifest.json: invalid SHA-256 for {relative}")
            continue
        if type(expected_bytes) is not int or expected_bytes < 0:
            problems.append(f"source-manifest.json: invalid byte count for {relative}")
            continue
        try:
            payload = path.read_bytes()
        except OSError as exc:
            problems.append(f"Cannot read preserved source {relative}: {exc}")
            continue
        if len(payload) != expected_bytes:
            problems.append(f"Preserved-source size mismatch: {relative}")
        if hashlib.sha256(payload).hexdigest() != expected_hash.lower():
            problems.append(f"Preserved-source SHA-256 mismatch: {relative}")
        checked += 1
    return checked


def main() -> int:
    problems: list[str] = []
    markdown_files = list(visible_files(".md"))
    links = sum(check_markdown(path, problems) for path in markdown_files)
    preserved = check_source_manifest(problems)
    labels = citations = 0
    for relative in TEX_ROOTS:
        label_count, citation_count = check_tex(relative, problems)
        labels += label_count
        citations += citation_count
    for relative in PDFS:
        path = ROOT / relative
        if not path.is_file():
            problems.append(f"Missing published PDF: {relative}")
        else:
            with path.open("rb") as source:
                if source.read(5) != b"%PDF-":
                    problems.append(f"Invalid PDF header: {relative}")
    if problems:
        print("Structural checks failed:", file=sys.stderr)
        for problem in problems:
            print(f"- {problem}", file=sys.stderr)
        return 1
    print(
        f"Structural checks passed: {len(markdown_files)} Markdown files, "
        f"{links} local file links, {labels} TeX labels, {citations} bibliography keys, "
        f"{preserved} preserved source files."
    )
    print("These checks do not verify mathematical correctness or novelty.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
