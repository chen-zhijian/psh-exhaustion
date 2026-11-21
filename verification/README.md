# Verification

Version 6 publishes the authors’ `paper_CX.tex` as [papers/src/main.tex](../papers/src/main.tex) and their `paper_CX.pdf` as [papers/paper_v6.pdf](../papers/paper_v6.pdf). The manuscript is dated 13 November 2026. The [release manifest](build_manifest.json) records the SHA-256 checksums, byte counts and 45-page extent of the original files. The [Version 5 archive](../archive/version-5-2026-11-08/) preserves the preceding source and build manifest.

## Check the release

```sh
python verification/scripts/verify.py
python verification/scripts/build.py
python verification/scripts/build.py --engine pdflatex
```

The first command checks the source and PDF hashes, source references and citations, table of contents, repository links, supporting files and archived releases. The last two commands each compile the self-contained manuscript three times in a separate output directory, using XeLaTeX by default (`build/xelatex/main.pdf`) or pdfLaTeX (`build/main.pdf`). The source uses `\today`, so a later build shows the day of recompilation. The published PDF retains the authors’ date.

The source uses AMS classes and fonts, Latin Modern, geometry, mathtools, TikZ-CD/PGF, microtype, enumitem, etoolbox, booktabs, tabularx, placeins, needspace, xcolor and hyperref. The bibliography is embedded. To use a compiler outside the system path, pass `--executable PATH` with the corresponding engine selection.

## Observed diagnostics

The supplied XeLaTeX log and the independent XeLaTeX build each report one missing left and one missing right double quotation mark around “continuous semipositive Hermitian metric” in the introduction. Latin Modern’s T1 font omits these two punctuation marks in the supplied PDF. For the exact Version 6 source, the XeLaTeX check reports these two diagnostics and accepts a single occurrence of each. Additional missing characters, unresolved references and overfull or underfull boxes still fail the build.

Both local three-pass builds produced 45 pages and resolved the references. The pdfLaTeX build produced the quotation marks and reported that shell escape for automatic EPS conversion was disabled. The source uses no external EPS illustrations. The [changes since Version 5](../CHANGES_V6.md) describe the mathematical scope. The automated checks cover file integrity and typesetting.

## Publication

The published files are the supplied pair. In this release, `--publish` compiles a local copy and verifies the current source and publication PDF against the supplied-file checksums. To restore the PDF from the original file, use `python verification/scripts/build.py --publish --intake-pdf /path/to/paper_CX.pdf`. The website serves the same PDF at `papers/psh-exhaustion.pdf` and records its source commit and checksum in `papers/manifest.json`.

The [review index](../prompts_and_logs/review_notes/README.md) and [archived manifests](../archive/README.md) document earlier releases.
