# Reviewing and improving the collection

Specific mathematical corrections are welcome. Identify the theorem or equation, the implication in question, and any needed hypothesis. For a priority claim, provide the earlier theorem, page, and precise overlap.

1. Edit the [current manuscript](preprints/001-psh-exhaustion/psh_exhaustion_refereed.tex) in `preprints/`; the [archive](archive/README.md) contains immutable historical snapshots.
2. Record a substantive change in [history.md](history.md), with its effect on the statement and proof.
3. Keep [CONTENTS.md](CONTENTS.md), [overview.tex](overview.tex), the manuscript README, and the scope notes consistent.
4. Follow [BUILDING.md](BUILDING.md) to compile and inspect the revised source and PDF.
5. Keep the original files under `archive/` and `reviews/source/` unchanged. Normal edits to the active source and rebuilds of its PDF do **not** require updating `source-manifest.json` or recomputing the original hashes. Those hashes protect the historical snapshots, not the active paper. If deliberately adding a new archived snapshot, record its provenance separately without relabeling it as an original supplied file.

Distinguish dimension three from dimension two, locally Lipschitz from $C^1$ or $C^2$, and a compactification-specific criterion from a statement about every noncompact surface. Inherited citations are not evidence of a new source check. A successful build does not validate a proof; formal verification requires the actual proof-assistant artifacts and reproducible checks.
