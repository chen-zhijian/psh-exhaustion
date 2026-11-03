# Verification

`scripts/build.py` compiles the self-contained source three times with pdfLaTeX, rejects undefined references/citations and overfull boxes, and optionally publishes `papers/paper_v3.pdf` with a hash manifest. `scripts/verify.py` checks the current source/PDF hashes, all TeX references and citations, the table of contents, the supporting notes, preserved release files, and every file in the original repository snapshot. CI runs the checks and a fresh compilation.

[revision-v3.json](revision-v3.json) preserves the checks on the initial 30-page editorial revision of Version 3. Its preservation statements compare that draft before and after the editorial pass. The subsequent [introduction revision](../prompts_and_logs/review_notes/introduction-2026-11-03.txt) updates the abstract, historical applications, bibliography, and front-matter spacing. Version 3 contains mathematical additions relative to Version 2.

The current published PDF is generated from the packaged source by the repository build. Its hashes, page count, and release checks are recorded in the [current build manifest](build_manifest.json). Rebuilding may change PDF metadata and the file hash. Build checks and rendered-page inspection establish technical consistency; they do not mechanically verify the mathematical arguments. The section-by-section mathematical audit is recorded under `prompts_and_logs/review_notes/`. No Lean formalization is supplied.

## Build and release

Install Python 3 and a TeX distribution with pdfLaTeX, AMS classes/fonts, Latin Modern, mathtools, microtype, enumitem, etoolbox, booktabs, tools, placeins, xcolor, hyperref, and geometry. The source has an embedded bibliography; no BibTeX step is required.

```sh
python verification/scripts/build.py
python verification/scripts/verify.py
```

Inspect the PDF in `build/`, then use `python verification/scripts/build.py --publish` to update `papers/paper_v3.pdf` and the build manifest together. Windows users may run `powershell -File verification/scripts/build.ps1 -Publish`. Run verification again after publishing.

For a manuscript release, copy the same published PDF to the website's `papers/psh-exhaustion.pdf` and update its source commit and checksum in `papers/manifest.json`. Review the website's paper entry when the title, results, or version changes.
