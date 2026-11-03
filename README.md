# Continuous and Smooth Plurisubharmonic Exhaustions

**Threefold Counterexamples and Surface Regularization**  
**Zhijian Chen and Bo Xiao** · Version 3 · 3 November 2026

[Read the paper](papers/paper_v3.pdf) · [LaTeX source](papers/src/main.tex) · [Changes in Version 3](CHANGES_V3.md) · [Personal website](https://chen-zhijian.github.io/)

The paper answers Nakano’s smoothing question negatively by constructing quasi-projective and non-Kähler threefolds with locally Lipschitz plurisubharmonic exhaustions but no $C^1$ exhaustion of this kind. It proves an affirmative result for divisor complements in compact Kähler surfaces, a regularity criterion for line-bundle metrics and dual total-space exhaustions, and a holomorphic convexity criterion for spaces fibered by curves. The introduction records the precise applications to problems and results of Nakano, Filip–Tosatti, Zhang, Koike, Ohsawa, and Vîjîitu. The unrestricted surface smoothing question remains open.

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
