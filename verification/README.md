# Verification

`scripts/build.py` compiles the self-contained source three times with pdfLaTeX, rejects undefined references/citations and overfull boxes, and optionally publishes the result with a hash manifest. `scripts/verify.py` checks the current source/PDF hashes, all TeX references and citations, the table of contents, and every archived file's integrity. CI runs the checks and a fresh compilation.

The release was also rendered and visually inspected. The checks establish build and packaging consistency; they do not mechanically verify the mathematical arguments. The section-by-section mathematical audit is recorded under `prompts_and_logs/review_notes/`. No Lean formalization is supplied.
