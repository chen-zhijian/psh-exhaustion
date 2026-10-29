# PSH exhaustions

A **vibemath** research collection on continuous and smooth plurisubharmonic exhaustions, threefold counterexamples, and partial affirmative results for complex surfaces.

[Read the paper](preprints/001-psh-exhaustion/psh_exhaustion_refereed.pdf) · [Overview](overview.pdf) · [Manuscript map](CONTENTS.md) · [Revision history](history.md)

The collection contains one active manuscript, two archived source/PDF snapshots, and the supplied surface-revision record. The current paper is **Continuous and Smooth Plurisubharmonic Exhaustions: Threefold Counterexamples and Partial Results for Surfaces**, by **Zhijian Chen and Bo Xiao**, dated 23 October 2026 (28 pages).

| Result in the manuscript | Scope | Location |
|---|---|---|
| Kähler counterexample | A smooth quasi-projective threefold has a locally Lipschitz psh exhaustion but no $C^2$ psh exhaustion. | Theorem 1.1 |
| Non-Kähler counterexample | A modification over one point produces a smooth non-Kähler threefold with the same exhaustion regularity gap. | Theorem 1.2 |
| Radius criterion | For a line bundle $A$ over a compact complex manifold, a $C^r$ psh exhaustion of $\operatorname{Tot}(A^{-1})$ is equivalent to a $C^r$ semipositive metric on $A$, for $r=2,\infty$. | Corollary 3.4 |
| Surface boundary criteria | Continuous and smooth exhaustibility are equivalent for divisor complements in nonprojective compact surfaces, and for reduced SNC boundary complements in smooth rulings. | Theorems 5.4–5.5 |

The surface section includes further sufficient conditions. It does **not** resolve the unrestricted regularization question in dimension two. The manuscript also leaves the $C^1$ threshold and minimal counterexample dimension undetermined. See the [precise catalogue](CONTENTS.md) and [questions left untreated](notes/open-directions.md).

## Navigating the collection

- [Overview](overview.pdf) and its [LaTeX source](overview.tex): a short research catalogue.
- [preprints/](preprints/001-psh-exhaustion/README.md): current source, PDF, and provisional citation.
- [archive/](archive/README.md): the original 27-page surface revision and its 47-page predecessor, preserved as historical snapshots.
- [reviews/](reviews/README.md): scope and verification notes, the original Chinese revision summary, patch, and revision manifest.
- [Research summary](reasoning_traces/001-psh-exhaustion.md): an editorial description of the mathematical argument.
- [Formalization status](lean/README.md): no Lean or other proof-assistant files are included.
- [Provenance](PROVENANCE.md) and [source manifest](source-manifest.json): the eight supplied files, their repository locations, and integrity hashes.

## Verification and attribution

The eight supplied files are preserved byte for byte in the historical archive and revision records. Their hashes protect those snapshots; the active manuscript in `preprints/` may be revised and rebuilt normally. It is checked for structure, references, and compilation rather than equality to the original hash. The original surface revision retained Sections 2–4 and the two principal theorem statements from its predecessor. Repository checks do not constitute an independent proof audit or exhaustive novelty review.

The paper attributes the ruled-surface obstruction to prior work and identifies its Hironaka, classification, abundance, and neighborhood-theory inputs. The surface revision retains explicit qualifications concerning a September 2026 preprint and incomplete access to Vâjâitu's published full text. See [scope and status](reviews/scope-and-status.md).

The inherited filename `psh_exhaustion_refereed` does not establish external journal review. The active source now names Zhijian Chen and Bo Xiao and supplies its date; the original archived surface revision retains its empty author and date fields. The label **vibemath** identifies the research context named by the repository owner; it is not an author attribution. See [provenance](PROVENANCE.md) and [licensing status](LICENSE-NOTICE.md).

## Build and upload

The PDFs are ready to read. [BUILDING.md](BUILDING.md) explains reproducible local checks; [CONTRIBUTING.md](CONTRIBUTING.md) explains how to record mathematical corrections. [UPLOAD_TO_GITHUB.md](UPLOAD_TO_GITHUB.md) gives GitHub Desktop and browser instructions.

The organization is inspired by [openai/math](https://github.com/openai/math): a catalogue, source/PDF pairs, research summaries, and revision history. This is a separate collection with its own content and verification status.
