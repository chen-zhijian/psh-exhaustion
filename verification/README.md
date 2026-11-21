# Verification

The [corrected Version 6 source](../papers/src/main.tex) restores the quotation marks around “continuous semipositive Hermitian metric” on page 2 of the [rebuilt 45-page PDF](../papers/paper_v6.pdf). The manuscript is dated 13 November 2026. The [release manifest](build_manifest.json) records the corrected source and PDF checksums alongside the checksums of the authors’ original files.

## Check the release

```sh
python verification/scripts/verify.py
python verification/scripts/build.py
python verification/scripts/build.py --engine pdflatex
```

The first command checks the source and PDF hashes, source references and citations, table of contents, repository links, supporting files and archived releases. The last two commands each compile the self-contained manuscript three times in a separate output directory, using XeLaTeX by default (`build/xelatex/main.pdf`) or pdfLaTeX (`build/main.pdf`). The build script sets TeX’s calendar to the manuscript date in the manifest so that the source’s `\today` prints 13 November 2026.

The source uses AMS classes and fonts, Latin Modern, geometry, mathtools, TikZ-CD/PGF, microtype, enumitem, etoolbox, booktabs, tabularx, placeins, needspace, xcolor, hyperref and backref. The bibliography is embedded. To use a compiler outside the system path, pass `--executable PATH` with the corresponding engine selection.

## Typesetting checks

The original Version 6 PDF omitted the opening and closing quotation marks on page 2. The correction replaces those two Unicode punctuation characters with TeX quotation syntax. Three XeLaTeX passes with the original MiKTeX 26.5 installation produced the release PDF. Both marks are visible and present in the extracted text. An image comparison of all 45 pages found differences confined to two lines on page 2. The title-page date, all 267 link annotations and the named destinations were preserved.

Independent three-pass XeLaTeX and pdfLaTeX builds with TeX Live 2026 each produced 45 pages with resolved references and no missing characters or overfull or underfull boxes. Any missing character now fails the build. pdfLaTeX reported that shell escape for automatic EPS conversion was disabled. The source uses no external EPS illustrations.

## Publication

The [initial Version 6 release](https://github.com/chen-zhijian/psh-exhaustion/tree/f5ea6ca596d06765bb40ea49fdb1b233e64d110c) preserves the original files. The website serves the corrected PDF at `papers/psh-exhaustion.pdf` and records its source commit and checksum in `papers/manifest.json`.

The [review index](../prompts_and_logs/review_notes/README.md) and [archived manifests](../archive/README.md) document earlier releases.
