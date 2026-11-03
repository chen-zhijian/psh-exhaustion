# Verification

`scripts/build.py` compiles the self-contained source three times with pdfLaTeX, rejects undefined references/citations and overfull boxes, and optionally publishes `papers/paper_v3.pdf` with a hash manifest. `scripts/verify.py` checks the current source/PDF hashes, all TeX references and citations, the table of contents, the supporting notes, preserved release files, and every file in the original repository snapshot. CI runs the checks and a fresh compilation.

[revision-v3.json](revision-v3.json) records the final editorial checks on the 30-page third version. Its preservation statements compare the audited Version 3 draft before and after the editorial pass. Version 3 contains mathematical additions relative to Version 2. The published PDF is the checked workspace PDF, copied without changing its bytes; a fresh repository build validates the packaged source but may differ in PDF metadata and file hash.

The release was also rendered and visually inspected. The checks establish build and packaging consistency; they do not mechanically verify the mathematical arguments. The section-by-section mathematical audit is recorded under `prompts_and_logs/review_notes/`. No Lean formalization is supplied.
