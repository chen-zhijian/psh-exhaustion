# Verification

`scripts/build.py` compiles the self-contained source three times with pdfLaTeX, rejects undefined references/citations and unrecorded overfull boxes, and optionally publishes `papers/paper_v5.pdf` with a hash manifest. `scripts/verify.py` checks the current source/PDF hashes, all TeX references and citations, the table of contents, the supporting notes, preserved release files, and every file in the original repository snapshot. CI runs the checks and a fresh compilation.

The [Version 5 publication record](../prompts_and_logs/review_notes/publication-2026-11-08.txt) records the unchanged author-supplied source and 40-page PDF, dated 8 November 2026. See [Changes in Version 5](../CHANGES_V5.md) for the manuscript changes. The Version 4 source and build manifest are preserved in the [dated archive](../archive/version-4-2026-11-05/), and its PDF remains at `papers/paper_v4.pdf`.

[revision-v3.json](revision-v3.json) preserves the checks on the initial 30-page editorial revision of Version 3. Its preservation statements compare that draft before and after the editorial pass. The subsequent [introduction revision](../prompts_and_logs/review_notes/introduction-2026-11-03.txt) updates the abstract, historical applications, bibliography, and front-matter spacing. Version 3 contains mathematical additions relative to Version 2.

The current published PDF is the author's supplied XeLaTeX output, copied without altering its bytes. The repository's separate pdfLaTeX build also produces 40 pages. Compiler differences can change typography, PDF metadata, and hashes; the fresh build does not replace the supplied PDF. Source/PDF identity, page count, and release checks are recorded in the [current build manifest](build_manifest.json). Earlier mathematical audits are retained under `prompts_and_logs/review_notes/`; no new mathematical audit or Lean formalization is supplied for this publication.

The supplied PDF has minor existing typography warnings: omitted curly quotation marks on page 2 and three short lines extending slightly into the right margin. All 40 pages were visually reviewed; the affected text remains legible. The separate pdfLaTeX build has one 3.53885-point overfull line at source lines 2832–2836. The manifest records a narrow allowance for that line, bound to the exact source SHA-256 and a 3.54-point maximum. The build prints the accepted warning and continues to reject unmatched overfull boxes, changed-source allowances, unresolved references, and missing characters. The supplied manuscript was not edited to remove these warnings.

## Build and release

Install Python 3 and a TeX distribution with pdfLaTeX, AMS classes/fonts, Latin Modern, mathtools, microtype, enumitem, etoolbox, booktabs, tools, placeins, needspace, tikz-cd/PGF, xcolor, hyperref, and geometry. The source has an embedded bibliography; no BibTeX step is required.

```sh
python verification/scripts/build.py
python verification/scripts/verify.py
```

Inspect the PDF in `build/`, then use `python verification/scripts/build.py --publish` only when intentionally replacing `papers/paper_v5.pdf` with a new repository build and updating its manifest. Windows users may run `powershell -File verification/scripts/build.ps1 -Publish`. Review provenance and warning records when replacing an author-supplied PDF, and run verification again after publishing.

For a manuscript release, copy the same published PDF to the website's `papers/psh-exhaustion.pdf` and update its source commit and checksum in `papers/manifest.json`. Review the website's paper entry when the title, results, or version changes.
