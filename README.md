# Continuous and Smooth Plurisubharmonic Exhaustions

**Threefold Counterexamples and Surface Regularization**  
**Zhijian Chen and Bo Xiao** · Revised 29 October 2026

[Read the paper](papers/paper_v1.pdf) · [LaTeX source](papers/src/main.tex) · [Personal website](https://chen-zhijian.github.io/)

The paper constructs smooth Kähler and non-Kähler threefolds with locally Lipschitz plurisubharmonic exhaustions but no $C^2$ plurisubharmonic exhaustion. It proves continuous-to-smooth regularization for divisor complements in compact Kähler surfaces, hence for smooth quasi-projective surfaces, and holomorphic convexity for continuously exhausted reduced pure-dimensional spaces admitting a map to $\mathbb C^{n-1}$ with all fibers of dimension at most one.

## Results and scope

- The threefold construction starts from Koike's modified Grauert example. An explicit continuous metric, a line-bundle radius criterion, and a compactly supported Hironaka modification establish the stated regularity gap.
- The surface theorem allows singular and disconnected effective boundary divisors and nonminimal compactifiers. In the non-Stein-modification case, a positive integral divisor supported on the whole boundary has a flat metric near that boundary.
- The curve-fibering theorem includes reduced singular total spaces. Pure dimension, a continuous real-valued exhaustion, and the dimension bound on **every** fiber are required.
- The conclusions give a new smooth exhaustion, not smooth approximation of the original one. General noncompact surface regularization and the $C^1$ threshold remain unresolved here.
- Separate existence criteria use classification and neighborhood results. The elliptic-neighborhood criterion cites a September 2026 preprint; the main surface regularization theorem does not depend on it.

## Layout

```text
papers/
  paper_v1.pdf
  src/main.tex
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
```

This layout follows [harmonic-direct-images](https://github.com/chen-zhijian/harmonic-direct-images). The complete previously tracked repository is preserved in [the archive](archive/README.md), including its manuscripts, original review records, and provenance. The current source is self-contained and has an embedded bibliography and table of contents.

## Build and verify

Install Python 3 and a TeX distribution with pdfLaTeX, AMS classes/fonts, Latin Modern, mathtools, microtype, enumitem, booktabs, tools, placeins, xcolor, and hyperref.

```sh
python verification/scripts/build.py
python verification/scripts/verify.py
```

The first command builds into `build/` and checks compilation without replacing published files. To publish a locally checked build, use `python verification/scripts/build.py --publish`; this updates the PDF and its source/PDF hash manifest together. Windows users may run `powershell -File verification/scripts/build.ps1 -Publish`.

Inspect the rendered PDF after changes. [Verification notes](verification/README.md) distinguish compilation and consistency checks from mathematical review. No proof-assistant formalization is supplied. [Review notes](prompts_and_logs/review_notes/README.md) record the present mathematical audit and editorial changes; they are not a claim of journal refereeing.

Update the website's second entry and `papers/psh-exhaustion.pdf` from the same published PDF when releasing a revision. Refresh its source commit and checksum in the website manifest. No new recurring synchronization service is configured by this revision.

See [LICENSE-NOTICE.md](LICENSE-NOTICE.md) for the unchanged licensing status.
