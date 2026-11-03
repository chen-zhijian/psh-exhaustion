# Continuous and Smooth Plurisubharmonic Exhaustions

**Threefold Counterexamples and Surface Regularization**  
**Zhijian Chen and Bo Xiao** · Version 3 · 3 November 2026 · 30 pages

[Read the paper](papers/paper_v3.pdf) · [LaTeX source](papers/src/main.tex) · [Changes in Version 3](CHANGES_V3.md) · [Personal website](https://chen-zhijian.github.io/)

The paper constructs Kähler and non-Kähler threefolds with locally Lipschitz plurisubharmonic exhaustions but no $C^1$ plurisubharmonic exhaustion; the Kähler example is quasi-projective. It establishes a regularity criterion for semipositive line-bundle metrics and exhaustions of their dual total spaces, smooth regularization for divisor complements in compact Kähler surfaces, and a holomorphic convexity criterion for spaces fibered by curves. The general regularization problem for noncompact complex surfaces remains open.

## Versions and supporting material

- [Version 2](papers/paper_v2.pdf) and [Version 1](papers/paper_v1.pdf), with earlier sources and records in the [archive](archive/README.md).
- [Supporting notes](supporting_notes/): the Grauert regularity and radius-criterion documents integrated into Version 3.
- [Review records](prompts_and_logs/review_notes/README.md): mathematical and editorial audits, including the Enoki source check.
- [Verification](verification/README.md) and [build manifest](verification/build_manifest.json): checks and source/PDF hashes.

## Build and verify

Requires Python 3 and a TeX distribution with pdfLaTeX. The source is self-contained, including its bibliography.

```sh
python verification/scripts/build.py
python verification/scripts/verify.py
```

The build writes to `build/`. After inspecting the PDF, use `python verification/scripts/build.py --publish` to update the published PDF and manifest together. See [verification notes](verification/README.md) for package requirements and release instructions. Automated checks establish technical consistency; no proof-assistant formalization is supplied.

See [LICENSE-NOTICE.md](LICENSE-NOTICE.md) for licensing status.
