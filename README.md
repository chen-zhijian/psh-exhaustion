# Regularity of plurisubharmonic exhaustions and related problems

**Zhijian Chen and Bo Xiao** · Version 6 · Manuscript dated 13 November 2026 · Published here 21 November 2026

[Read the paper (45 pages)](papers/paper_v6.pdf) · [LaTeX source](papers/src/main.tex) · [Changes in Version 6](CHANGES_V6.md) · [Personal website](https://chen-zhijian.github.io/)

The paper answers Nakano’s smoothing question negatively in dimension three. It constructs quasi-projective and non-Kähler threefolds with locally Lipschitz plurisubharmonic (psh) exhaustions on which no $C^1$ psh exhaustion exists.

In dimension two, a continuous psh exhaustion can be replaced by a smooth one on the complement of a nonzero effective Weil divisor in a normal compact connected Kähler surface, and on every normal complex quasi-projective surface. A cuspidal projective example shows that a reduced irreducible surface can fail this conclusion. This manuscript leaves the unrestricted smoothing question for smooth complex surfaces open.

For a holomorphic vector bundle over a compact complex manifold, the higher-rank criterion relates exhaustions on the dual total space to semipositive metrics on the tautological line bundle over the projectivized dual. The holomorphic convexity criterion over a Stein base now allows a discontinuous psh exhaustion, including one taking the value $-\infty$.

## Versions and supporting material

- [Version 5](papers/paper_v5.pdf), [Version 4](papers/paper_v4.pdf), [Version 3](papers/paper_v3.pdf), [Version 2](papers/paper_v2.pdf), and [Version 1](papers/paper_v1.pdf). Earlier sources and release records are listed in the [archive](archive/README.md).
- The [supporting notes](supporting_notes/) contain the Grauert regularity and radius-criterion documents integrated into Version 3.
- The [review records](prompts_and_logs/review_notes/README.md) include earlier mathematical and editorial audits.
- The [verification notes](verification/README.md) and [release manifest](verification/build_manifest.json) document the corrected source, rebuilt PDF and compilation checks.

## Build and verify

With Python 3 and a TeX distribution installed, run the following from the repository root.

```sh
python verification/scripts/verify.py
python verification/scripts/build.py
python verification/scripts/build.py --engine pdflatex
```

The default XeLaTeX build writes to `build/xelatex/`. The alternate pdfLaTeX build writes to `build/`. The published Version 6 PDF was rebuilt after correcting the quotation marks around “continuous semipositive Hermitian metric” in the introduction. See the [verification notes](verification/README.md) for the build details.

See [LICENSE-NOTICE.md](LICENSE-NOTICE.md) for licensing status.
