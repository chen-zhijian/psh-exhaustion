# Scope, provenance, and review status

## What this collection contains

The title is *Continuous and Smooth Plurisubharmonic Exhaustions: Threefold Counterexamples and Partial Results for Surfaces*. The active manuscript in `preprints/001-psh-exhaustion/` now names Zhijian Chen and Bo Xiao and is dated 23 October 2026. Its source and PDF may be revised normally.

The original `psh_exhaustion_refereed.tex` and 27-page PDF from the user's `psh_exhaustion_surface_revision.zip` are preserved in [archive/surface-revision-2026-10-23/](../archive/README.md). That original source retains empty author and date commands; the supplied accompanying materials identify its revision date as 23 October 2026.

The revised source and PDF take precedence over the earlier filename `psh_exhaustion.tex` mentioned in the project discussion. The archive also supplies a [Chinese change summary](source/psh_exhaustion_surface_changes_zh.md), a [JSON manifest](source/psh_exhaustion_surface_revision_manifest.json), a patch, a README, and a [previous-version source](../archive/previous_version/psh_exhaustion_refereed.tex)/[PDF](../archive/previous_version/psh_exhaustion_refereed.pdf) pair. Those are a revision trail, not additional current manuscripts.

## What has and has not been reviewed here

For the initial catalogue, the complete supplied revised LaTeX source, change summary, manifest, and numbered statements in the supplied PDF were read. The catalogue was checked against those statements for dimensions, regularity, compactification hypotheses, and attribution limits. This was a statement-level consistency review conducted during repository preparation. The subsequent metadata and integrity-check repair is not a new proof review.

It is **not** a new independent referee examination of every proof, an exhaustive priority check, or formal verification. No proof-assistant files or machine-checked proofs were supplied. No journal decision or identified external referee report was supplied.

The word `refereed` in a filename does not establish journal peer review. The source header refers to a separate referee report and an original file named `psh_exhaustion(1).tex`; those items are not present under those names in the supplied package. The available Chinese change summary should be described as an inherited revision report, not relabeled as an independent referee report.

## Main claims and their exact limits

- **Threefolds:** Theorems 1.1 and 1.2 claim locally Lipschitz psh exhaustions and nonexistence of any $C^2$ psh exhaustion, first on a smooth quasi-projective Kähler threefold and then on a non-Kähler modification of the same dimension. They do not determine $C^1$ regularity or minimal counterexample dimension.
- **Line-bundle criterion:** Corollary 3.4 is an equivalence at $C^2$ and $C^\infty$ regularity over a compact complex base. It is not a continuous-regularity equivalence in arbitrary dimension.
- **Surfaces:** Section 5 proves stated affirmative cases and necessary conditions on hypothetical remaining examples. It does not construct a surface counterexample or settle general continuous-to-$C^2$ regularization.
- **Classification table:** Table 1 assumes a compact minimal smooth surface, nonempty reduced SNC boundary, and a continuous psh exhaustion on the complement. Its partial entries mean untreated by these arguments. Its excluded entries cannot satisfy the hypotheses; they are not regularity counterexamples.

The [catalogue](../CONTENTS.md) lists exact statement numbers and the additional hypotheses of each surface result.

## Attribution and external inputs

The manuscript expressly identifies Koike's modified Grauert ruled surface and its non-semipositivity obstruction as prior work. It also credits Hironaka's opposite-order blowups, Ueda theory, surface classification inputs, the holomorphic-convexity implication, the affine-line-bundle construction, and surface log abundance. The repository should not present those ingredients as independently new results.

The proposed threefold contribution is the combination of the explicit bounded-potential metric, the radius obstruction to every $C^2$ exhaustion, and the compactly supported non-Kähler modification. No exhaustive novelty determination was carried out as part of packaging these supplied files.

Two source qualifications in the supplied revision report are material:

1. **Recent elliptic-neighborhood input.** The Hopf branch of Theorem 5.4 and the elliptic case of Proposition 5.8 invoke Theorem 1.6 of Chen–Filip–Sun–Tosatti–Zhang, *Compact Kähler surfaces with semipositive anticanonical bundle*, listed as [arXiv:2609.26716v1](https://arxiv.org/abs/2609.26716v1), submitted 22 September 2026. This is an inherited citation and stated dependency, not a newly verified source in this repository preparation. The input is independent of the threefold counterexamples.
2. **Vâjâitu full-text access.** The supplied report says the full published article *Holomorphic convexity of pseudoconvex surfaces* was not obtained during the earlier revision; its restricted theorem statement was checked through the publisher's indexed account. Proposition 5.1 cites it explicitly. The remaining full-text check should not be represented as completed here. The manuscript gives [DOI 10.2422/2036-2145.202011_018](https://doi.org/10.2422/2036-2145.202011_018).

Other bibliography entries likewise remain inherited unless a separate verification record says otherwise. Their presence in the manuscript is not evidence that every source was freshly retrieved and checked for this repository.

## Revision evidence

The supplied manifest records a reduction from 47 to 27 pages, an unchanged Sections 2–4 core, unchanged principal theorem statements, source and PDF hashes, 17 bibliography entries, and clean compilation checks at the time of that revision. The Chinese summary explains that four surface sections were merged into the present Section 5, with narrower claims and explicit recent-source dependencies.

These records support traceability of the supplied revision. Original hashes are validated against the immutable archived copies and inherited records; they do not constrain ordinary revisions of the active source or PDF. The active paper receives structural, reference, and compilation checks. File hashes and successful compilation establish integrity and build consistency, not mathematical correctness. Removing material from the earlier version does not by itself imply that the removed statements were false.

## Suggested next review

An independent mathematical review should check the full source dependencies, especially the recent elliptic-neighborhood theorem and the holomorphic-convexity input, then inspect each use under the manuscript's exact hypotheses. Any future correction should identify its effect on the main threefold statements, the separate surface branches, and the repository catalogue.
