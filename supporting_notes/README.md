# Supporting notes for Version 3

These two notes supplied the results integrated into the [Version 3 manuscript](../papers/paper_v3.pdf). They are preserved as development inputs; the integrated manuscript includes the subsequent mathematical audit and editorial corrections.

| Note | PDF | Standalone source |
| --- | --- | --- |
| Grauert's ruled surfaces and semipositive metrics: Lipschitz existence and a C¹ obstruction, 3 November 2026 | [PDF](grauert-regularity/grauert-regularity.pdf) | [LaTeX](grauert-regularity/grauert-regularity.tex) |
| The Radius Criterion in Real Analytic and Lower Regularity: An Expanded Proof and Audit, 2 November 2026 | [PDF](real-analytic-radius-criterion/real-analytic-radius-criterion.pdf) | [LaTeX](real-analytic-radius-criterion/real-analytic-radius-criterion.tex) |

Each standalone source has an embedded bibliography. Compile it three times with `pdflatex -no-shell-escape`. The Grauert note's [BibTeX database](grauert-regularity/references.bib) is also preserved as bibliographic data; it is not needed to compile the standalone source. The modular working files and temporary build files are omitted.

The [build manifest](../verification/build_manifest.json) records the bytes and SHA-256 hashes of these five files. The [Version 3 review](../prompts_and_logs/review_notes/revision-2026-11-03.txt) records how the notes were integrated and audited, including the direct check of Enoki's 1981 paper. Third-party journal PDFs are cited rather than bundled.
