#!/usr/bin/env python3
"""Build the paper; optionally publish its PDF and checksum record.

Compilation and checksums establish technical consistency, not mathematical
correctness. Only Python's standard library and pdfLaTeX are required.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "papers/src/main.tex"
PUBLISHED = ROOT / "papers/paper_v1.pdf"
MANIFEST = ROOT / "verification/build_manifest.json"
OUTPUT = ROOT / "build"


def digest(path: Path, relative: str) -> dict:
    data = path.read_bytes()
    return {"path": relative, "sha256": hashlib.sha256(data).hexdigest(), "bytes": len(data)}


def run_engine(engine: str) -> tuple[Path, dict]:
    if not SOURCE.is_file():
        raise RuntimeError("Missing papers/src/main.tex")
    # Imported lazily so --help is available even in an incomplete checkout.
    from verify import check_tex
    errors: list[str] = []
    check_tex(errors)
    if errors:
        raise RuntimeError("Source checks failed:\n" + "\n".join(errors))
    source_record = digest(SOURCE, "papers/src/main.tex")
    OUTPUT.mkdir(parents=True, exist_ok=True)
    command = [engine, "-no-shell-escape", "-interaction=nonstopmode",
               "-halt-on-error", "-file-line-error", f"-output-directory={OUTPUT}", SOURCE.name]
    # The source contains the bibliography; no BibTeX step is needed.
    for number in range(1, 4):
        print(f"Compiling paper, pass {number}/3 ...", flush=True)
        result = subprocess.run(command, cwd=SOURCE.parent, stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT, encoding="utf-8", errors="replace")
        transcript = OUTPUT / f"pass-{number}.txt"
        transcript.write_text(result.stdout, encoding="utf-8")
        if result.returncode:
            raise RuntimeError(f"pdfLaTeX failed; see {transcript.relative_to(ROOT)}\n"
                               + "\n".join(result.stdout.splitlines()[-20:]))
    log_path = OUTPUT / "main.log"
    log = log_path.read_text(encoding="utf-8", errors="replace")
    failures = []
    for expression, message in (
        (r"(?:Reference|Citation)[^\n]*undefined|There were undefined (?:references|citations)",
         "undefined references or citations"),
        (r"Label\(s\) may have changed|Rerun to get (?:cross-references|outlines) right",
         "references or outlines still require another pass"),
        (r"multiply[- ]defined|multiply defined", "multiply defined labels"),
        (r"Overfull \\[hv]box", "overfull boxes"),
        (r"Missing character:", "missing font characters"),
    ):
        if re.search(expression, log, re.I):
            failures.append(message)
    if failures:
        raise RuntimeError("Final compilation has " + ", ".join(failures) + "; see build/main.log")
    if digest(SOURCE, "papers/src/main.tex") != source_record:
        raise RuntimeError("Source changed during compilation; rebuild the settled source")
    generated = OUTPUT / "main.pdf"
    if not generated.is_file() or not generated.read_bytes().startswith(b"%PDF-"):
        raise RuntimeError("Build did not produce a PDF with a valid header")
    toc = OUTPUT / "main.toc"
    if not toc.is_file() or "contentsline" not in toc.read_text(encoding="utf-8", errors="replace"):
        raise RuntimeError("The compiled table of contents is missing or empty")
    version = subprocess.run([engine, "--version"], stdout=subprocess.PIPE,
                             stderr=subprocess.STDOUT, encoding="utf-8", errors="replace", check=True)
    version_lines = version.stdout.splitlines()
    page_match = re.search(r"Output written on[^\n]*(?:\n[^\n]*)?\((\d+) pages?[,)]", log)
    pdf_record = digest(generated, "papers/paper_v1.pdf")
    if page_match:
        pdf_record["pages"] = int(page_match.group(1))
    record = {
        "source": source_record,
        "pdf": pdf_record,
        "built_at_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "compiler": version_lines[0] if version_lines else "pdfLaTeX",
        "passes": 3,
        "technical_checks": ["source labels and citations", "table of contents",
                             "no unresolved references", "no overfull boxes", "no missing characters"],
        "mathematical_verification": "Not performed by this script; see the review notes.",
    }
    print("Built build/main.pdf with resolved references and no overfull boxes.")
    return generated, record


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pdflatex", help="pdfLaTeX executable or full path; default: search PATH")
    parser.add_argument("--publish", action="store_true", help="replace the published PDF and update its manifest")
    parser.add_argument("--intake-source", type=Path, help="record the original supplied source's SHA-256 when publishing")
    args = parser.parse_args()
    if args.intake_source and not args.publish:
        parser.error("--intake-source is meaningful only with --publish")
    engine = shutil.which(args.pdflatex or "pdflatex")
    if engine is None:
        parser.error("pdfLaTeX was not found; install a TeX distribution or pass --pdflatex PATH")
    try:
        existing = {}
        if args.publish and MANIFEST.exists():
            existing = json.loads(MANIFEST.read_text(encoding="utf-8"))
            if not isinstance(existing, dict):
                raise RuntimeError("Existing build manifest must be a JSON object")
        intake = None
        if args.intake_source:
            intake_path = args.intake_source.resolve(strict=True)
            intake = digest(intake_path, intake_path.relative_to(ROOT).as_posix()
                            if intake_path.is_relative_to(ROOT) else intake_path.name)
        generated, record = run_engine(engine)
        if args.publish:
            existing.update(record)
            if intake is not None:
                existing["intake_source"] = intake
            # Stage both complete outputs before replacing either published file.
            pdf_temp = PUBLISHED.with_suffix(".pdf.tmp")
            manifest_temp = MANIFEST.with_suffix(".json.tmp")
            shutil.copyfile(generated, pdf_temp)
            manifest_temp.write_text(json.dumps(existing, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
            os.replace(pdf_temp, PUBLISHED)
            os.replace(manifest_temp, MANIFEST)
            print("Published papers/paper_v1.pdf and verification/build_manifest.json.")
        else:
            print("Compilation checked. Published files were not changed.")
        return 0
    except (OSError, ValueError, RuntimeError, subprocess.SubprocessError) as exc:
        print(f"Build error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
