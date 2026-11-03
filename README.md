# Continuous and Smooth Plurisubharmonic Exhaustions

**Threefold Counterexamples and Surface Regularization**  
**Zhijian Chen and Bo Xiao** · Version 3 · Revised 3 November 2026

[Read the paper (v3)](papers/paper_v3.pdf) · [LaTeX source](papers/src/main.tex) · [Version 2](papers/paper_v2.pdf) · [Version 1](papers/paper_v1.pdf) · [Personal website](https://chen-zhijian.github.io/)

The paper constructs smooth Kähler and non-Kähler threefolds with locally Lipschitz plurisubharmonic exhaustions but no $C^1$ plurisubharmonic exhaustion; the Kähler example is quasi-projective. A regularity criterion identifies the classes in which a line bundle admits a semipositive metric with those in which its dual total space admits a plurisubharmonic exhaustion. The paper also proves continuous-to-smooth regularization for divisor complements in compact Kähler surfaces, hence for smooth quasi-projective surfaces, and holomorphic convexity for continuously exhausted reduced pure-dimensional spaces admitting a map to $\mathbb C^{n-1}$ with all fibers of dimension at most one.

## Results and scope

- The threefold construction uses Grauert's ruled surfaces, including Koike's modified example. Locally Lipschitz semipositive metrics, a $C^1$ obstruction proved on holomorphic graphs, and a compactly supported Hironaka modification establish the regularity gap.
- The regularity criterion applies to line bundles over compact complex manifolds in every $C^r$ class, for nonnegative integers $r$ and $r=\infty$, every local Hölder class $C^{k,\alpha}_{\mathrm{loc}}$ with $k\ge0$ and $0<\alpha\le1$, and the real analytic class $C^\omega$. It requires no Kähler or projectivity assumption on the base.
- The surface theorem allows singular and disconnected effective boundary divisors and nonminimal compactifiers. In the non-Stein-modification case, a positive integral divisor supported on the whole boundary has a flat metric near that boundary.
- The curve-fibering theorem includes reduced singular total spaces. Pure dimension, a continuous real-valued exhaustion, and the dimension bound on **every** fiber are required.
- Surface regularization means existence of a smooth exhaustion. The general regularization problem for noncompact complex surfaces remains open.
- Separate existence criteria use classification and neighborhood results. The elliptic-neighborhood criterion cites a September 2026 preprint; the main surface regularization theorem does not depend on it.

## Layout

```text
papers/
  paper_v1.pdf
  paper_v2.pdf
  paper_v3.pdf
  src/main.tex
supporting_notes/
prompts_and_logs/
  README.md
  revision_request.md
  review_notes/
verification/
  build_manifest.json
  scripts/
  lean/
archive/
  repository-2026-10-23/
  version-2-2026-10-30/
```

The complete repository preceding the 29 October revision is preserved in [the archive](archive/README.md), including its manuscripts, original review records, and provenance. The [version 2 source and build manifest](archive/version-2-2026-10-30/) and both earlier PDFs are retained. The current source is self-contained and has an embedded bibliography and table of contents.

Version 3 integrates the Grauert regularity and real analytic radius notes, strengthens the obstruction from $C^2$ to $C^1$, and expands the regularity criterion. The [3 November review](prompts_and_logs/review_notes/revision-2026-11-03.txt) records the mathematical audit, the direct check of Enoki's 1981 paper, and the final editorial pass. The 30-page manuscript contains 32 numbered theorem, proposition, lemma, and corollary statements and 99 labels. These statements and labels were preserved during the final editorial pass; version 3 makes substantive changes to version 2.

The [supporting notes](supporting_notes/) preserve the supplied Grauert regularity and radius-criterion documents and their available sources. They are inputs to the revision; the integrated, audited manuscript is the current statement of the results. Enoki's third-party article is cited and its use documented in the review notes, without redistributing the supplied PDF.

Version 2, dated 30 October 2026, expanded the proofs and shortened the abstract. Its [review record](prompts_and_logs/review_notes/revision-2026-10-30.txt) remains unchanged.

## Build and verify

Install Python 3 and a TeX distribution with pdfLaTeX, AMS classes/fonts, Latin Modern, mathtools, microtype, enumitem, booktabs, tools, placeins, xcolor, hyperref, and geometry. The paper uses 1.15-inch margins and an alphabetic bibliography matching the Grauert regularity note. Citation-page back-references from earlier versions have been removed.

```sh
python verification/scripts/build.py
python verification/scripts/verify.py
```

The first command builds into `build/` and checks compilation without replacing published files. To publish a locally checked build, use `python verification/scripts/build.py --publish`; this updates `papers/paper_v3.pdf` and its source/PDF hash manifest together. Windows users may run `powershell -File verification/scripts/build.ps1 -Publish`.

Inspect the rendered PDF after changes. [Verification notes](verification/README.md) distinguish compilation and consistency checks from mathematical review. No proof-assistant formalization is supplied. [Review notes](prompts_and_logs/review_notes/README.md) record the present mathematical audit and editorial changes; they are not a claim of journal refereeing.

Update the website's second entry and `papers/psh-exhaustion.pdf` from the same published PDF when releasing a revision. Refresh its source commit and checksum in the website manifest. No new recurring synchronization service is configured by this revision.

See [LICENSE-NOTICE.md](LICENSE-NOTICE.md) for the unchanged licensing status.
