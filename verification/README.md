# Verification

`scripts/build.py` compiles the self-contained source three times with pdfLaTeX, rejects undefined references/citations and overfull boxes, and optionally publishes `papers/paper_v3.pdf` with a hash manifest. `scripts/verify.py` checks the current source/PDF hashes, all TeX references and citations, the table of contents, the supporting notes, preserved release files, and every file in the original repository snapshot. CI runs the checks and a fresh compilation.

[revision-v3.json](revision-v3.json) records the final editorial checks on the 30-page third version. Its preservation statements compare the audited Version 3 draft before and after the editorial pass. Version 3 contains mathematical additions relative to Version 2. The published PDF is the checked workspace PDF, copied without changing its bytes; a fresh repository build validates the packaged source but may differ in PDF metadata and file hash.

The release was also rendered and visually inspected. The checks establish build and packaging consistency; they do not mechanically verify the mathematical arguments. The section-by-section mathematical audit is recorded under `prompts_and_logs/review_notes/`. No Lean formalization is supplied.

## Build and release

Install Python 3 and a TeX distribution with pdfLaTeX, AMS classes/fonts, Latin Modern, mathtools, microtype, enumitem, booktabs, tools, placeins, xcolor, hyperref, and geometry. The source has an embedded bibliography; no BibTeX step is required.

```sh
python verification/scripts/build.py
python verification/scripts/verify.py
```

Inspect the PDF in `build/`, then use `python verification/scripts/build.py --publish` to update `papers/paper_v3.pdf` and the build manifest together. Windows users may run `powershell -File verification/scripts/build.ps1 -Publish`. Run verification again after publishing.

For a manuscript release, copy the same published PDF to the website's `papers/psh-exhaustion.pdf` and update its source commit and checksum in `papers/manifest.json`. Review the website's paper entry when the title, results, or version changes.
