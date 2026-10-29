#!/usr/bin/env python3
"""Compile the repository's LaTeX documents using Python's standard library."""

from __future__ import annotations

import argparse
from pathlib import Path
import re
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
TARGETS = {
    "overview": (Path("overview.tex"), Path("overview.pdf")),
    "paper": (
        Path("preprints/001-psh-exhaustion/psh_exhaustion_refereed.tex"),
        Path("preprints/001-psh-exhaustion/psh_exhaustion_refereed.pdf"),
    ),
}


def build(name: str, engine: str) -> tuple[Path, Path]:
    source_rel, published_rel = TARGETS[name]
    source = ROOT / source_rel
    if not source.is_file():
        raise RuntimeError(f"Missing source: {source_rel.as_posix()}")
    output = ROOT / "build" / name
    output.mkdir(parents=True, exist_ok=True)
    command = [
        engine,
        "-no-shell-escape",
        "-interaction=nonstopmode",
        "-halt-on-error",
        "-file-line-error",
        f"-output-directory={output}",
        source.name,
    ]
    # The manuscripts use inline thebibliography; no BibTeX step is necessary.
    for number in range(1, 4):
        print(f"Compiling {name}, pass {number}/3 ...", flush=True)
        result = subprocess.run(
            command,
            cwd=source.parent,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            encoding="utf-8",
            errors="replace",
            check=False,
        )
        transcript = output / f"pass-{number}.txt"
        transcript.write_text(result.stdout, encoding="utf-8")
        if result.returncode:
            raise RuntimeError(
                f"LaTeX failed for {name}; see {transcript.relative_to(ROOT)}\n"
                + "\n".join(result.stdout.splitlines()[-25:])
            )
    log = (output / f"{source.stem}.log").read_text(
        encoding="utf-8", errors="replace"
    )
    unresolved = re.search(
        r"(?:Reference|Citation) .+? undefined|"
        r"There were undefined (?:references|citations)|"
        r"Label\(s\) may have changed",
        log,
    )
    if unresolved:
        raise RuntimeError(
            f"Unresolved references after three passes for {name}; "
            f"see build/{name}/{source.stem}.log"
        )
    generated = output / f"{source.stem}.pdf"
    if not generated.is_file() or not generated.read_bytes().startswith(b"%PDF-"):
        raise RuntimeError(f"No valid PDF header in the output for {name}")
    print(f"Built {generated.relative_to(ROOT).as_posix()}")
    return generated, ROOT / published_rel


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "target", choices=["all", *TARGETS], nargs="?", default="all"
    )
    parser.add_argument(
        "--publish",
        action="store_true",
        help="update selected active PDFs after all selected builds succeed; archived PDFs are preserved",
    )
    args = parser.parse_args()
    engine = shutil.which("pdflatex")
    if engine is None:
        parser.error("pdflatex was not found. Install TeX Live or MiKTeX; see BUILDING.md.")
    names = TARGETS if args.target == "all" else [args.target]
    try:
        completed = [build(name, engine) for name in names]
        if args.publish:
            for generated, published in completed:
                shutil.copyfile(generated, published)
                print(f"Updated {published.relative_to(ROOT).as_posix()}")
        else:
            print("Build complete. Checked-in PDFs were left unchanged.")
        return 0
    except (OSError, RuntimeError) as exc:
        print(f"Build error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
