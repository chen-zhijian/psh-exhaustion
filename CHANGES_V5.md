# Changes in Version 5

**8 November 2026** · [Version 5](papers/paper_v5.pdf) · [Version 4](papers/paper_v4.pdf)

Version 5 broadens the holomorphic convexity theorem, expands the surface arguments, and revises the exposition and references. It also includes a formatting correction to quotation marks and line wrapping, followed by a fresh PDF build, under the same version number.

## Holomorphic convexity over Stein spaces

Theorem 1.4, restated in Section 6, now concerns a holomorphic map from a reduced complex space with a continuous plurisubharmonic exhaustion to an arbitrary Stein space. If every irreducible component of every reduced fiber is compact or Stein, the source is holomorphically convex. Fiber components may have arbitrary dimension, and no purity assumption on the source is required.

The new proof uses exhaustion levels, Stein neighborhoods, and Vîjîitu’s local convexity criterion. Section 6 adds a consequence formulated through local fiber dimension, directly recovers Vîjîitu’s rank criterion, and gives two product examples distinguishing the hypotheses. It also describes the positive-dimensional fibers of the Remmert reduction as maximal connected unions of positive-dimensional compact fiber components; each such union is finite.

## Surface arguments and exposition

The surface proofs give more detail on the boundary intersection-matrix alternatives, construction of positive boundary metrics, level-current averaging, the Dinh–Nguyên–Sibony energy inequality, and the resulting flat boundary metrics and pluriharmonic collars. The quasi-projective corollary explicitly handles isolated boundary points and disconnected surfaces. A separate remark explains why finite-dimensional holomorphically convex reduced complex spaces admit smooth plurisubharmonic exhaustions.

Sections 2–4 clarify the local-to-global Lipschitz metric construction, regularity conventions, modification invariance, and the Hironaka construction. The introduction and historical comparisons are revised. The threefold obstruction at $C^1$ regularity and the line-bundle regularity criterion remain the principal earlier conclusions.

The manuscript adds bibliography page back-references, seven references, a Remmert-reduction diagram, and an acknowledgement and AI-disclosure paragraph. Three references associated with the replaced fiber-cycle proof are removed from the typeset bibliography. It contains 100 labels, 30 bibliography entries, and 35 numbered statements.

## Release records

The [initial publication record](prompts_and_logs/review_notes/publication-2026-11-08.txt) describes the unchanged supplied source and 40-page PDF at the first upload. The subsequent [formatting record](prompts_and_logs/review_notes/formatting-2026-11-08.txt) describes the quotation-mark and line-wrapping corrections, the pagination adjustment keeping the final corollary and diagram together, and the replacement 40-page PDF. The corrected source builds without overfull or underfull boxes, missing characters, or unresolved references. These formatting changes preserve the mathematical content and the Version 5 designation.

A further [XeLaTeX follow-up](prompts_and_logs/review_notes/xelatex-2026-11-08.txt) adds a discretionary hyphen in “Lelong-pseudoconvex,” a paragraph break in the proof of Theorem 5.12, and a break opportunity in one bibliography entry. The build supports both pdfLaTeX and XeLaTeX with separate auxiliary files and strict checks for overfull and underfull boxes. pdfLaTeX remains the canonical publication engine. These typesetting and build changes retain Version 5 and its mathematical content.

The Version 4 source and build manifest are preserved in the [archive](archive/README.md), and its PDF remains available. The [current build manifest](verification/build_manifest.json) records the current Version 5 source and PDF hashes and release checks. These release notes do not constitute a new mathematical audit.
