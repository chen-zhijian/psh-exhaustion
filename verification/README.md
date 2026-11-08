# Verification

`scripts/build.py` compiles the self-contained source three times with pdfLaTeX, rejects undefined references/citations and overfull boxes, and optionally publishes `papers/paper_v5.pdf` with a hash manifest. `scripts/verify.py` checks the current source/PDF hashes, all TeX references and citations, the table of contents, the supporting notes, preserved release files, and every file in the original repository snapshot. CI runs the checks and a fresh compilation.

The [initial Version 5 publication record](../prompts_and_logs/review_notes/publication-2026-11-08.txt) records the unchanged author-supplied source and 40-page PDF at the first upload on 8 November 2026. The [subsequent formatting record](../prompts_and_logs/review_notes/formatting-2026-11-08.txt) describes the corrected quotation marks and line wrapping and the new PDF built from the corrected source, retaining Version 5. See [Changes in Version 5](../CHANGES_V5.md) for the manuscript changes. The Version 4 source and build manifest are preserved in the [dated archive](../archive/version-4-2026-11-05/), and its PDF remains at `papers/paper_v4.pdf`.

[revision-v3.json](revision-v3.json) preserves the checks on the initial 30-page editorial revision of Version 3. Its preservation statements compare that draft before and after the editorial pass. The subsequent [introduction revision](../prompts_and_logs/review_notes/introduction-2026-11-03.txt) updates the abstract, historical applications, bibliography, and front-matter spacing. Version 3 contains mathematical additions relative to Version 2.

The current release uses the corrected repository source and its new pdfLaTeX output. The published PDF and the website copy are synchronized from that build. Compiler differences can change typography, PDF metadata, and hashes. Source/PDF provenance, page count, and release checks are recorded in the [current build manifest](build_manifest.json). Earlier mathematical audits are retained under `prompts_and_logs/review_notes/`; no new mathematical audit or Lean formalization is supplied for this formatting correction.

The initial upload retained omitted curly quotation marks and slight margin protrusions in the supplied PDF, and allowed one documented overfull line in the separate pdfLaTeX build. That warning allowance describes the initial upload only. The formatting correction replaces the problematic quotation marks with TeX quotation syntax and adjusts the K3-surface paragraph's wrapping. The current build rejects overfull boxes without a warning allowance; the correction addresses the source rather than suppressing diagnostics. Final checks are documented in the formatting record and current manifest.

## Build and release

Install Python 3 and a TeX distribution with pdfLaTeX, AMS classes/fonts, Latin Modern, mathtools, microtype, enumitem, etoolbox, booktabs, tools, placeins, needspace, tikz-cd/PGF, xcolor, hyperref, and geometry. The source has an embedded bibliography; no BibTeX step is required.

```sh
python verification/scripts/build.py
python verification/scripts/verify.py
```

Inspect the PDF in `build/`, then use `python verification/scripts/build.py --publish` to update `papers/paper_v5.pdf` and its manifest together. Windows users may run `powershell -File verification/scripts/build.ps1 -Publish`. Update the release provenance and run verification again after publishing.

For a manuscript release, copy the same published PDF to the website's `papers/psh-exhaustion.pdf` and update its source commit and checksum in `papers/manifest.json`. Review the website's paper entry when the title, results, or version changes.
