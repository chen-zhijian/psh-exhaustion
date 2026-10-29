# Building and checking the documents

The PDFs are included, so no software is needed to read them. The scripts use
Python's standard library and work on Windows, macOS, and Linux. Run the commands
below from the repository's top-level directory.

## Check the repository

Install Python 3.10 or later, then run:

```text
python scripts/check.py
```

On Windows, `py -3` can replace `python` if that is how Python is installed.
On macOS or Linux, the command may be `python3`.

This checks local Markdown file links, labels and citations in the current
manuscript and overview, and their PDF headers. It also checks every preserved
supplied file against the byte count and SHA-256 recorded in
[source-manifest.json](source-manifest.json). The original manuscript pair is in
`archive/surface-revision-2026-10-23/`; the older predecessor is in
`archive/previous_version/`. Both archived versions retain their original bytes.
The active files under `preprints/` are editable and are not locked to intake hashes.

The checker does not access external websites, check Markdown heading anchors,
verify mathematical correctness or novelty, confirm bibliographic accuracy, or
establish agreement between PDF content and LaTeX source. Matching hashes confirm
file integrity against the intake record, not the truth of claims in those files.

## Compile the current LaTeX

Install a TeX distribution that provides `pdflatex`, such as
[TeX Live](https://www.tug.org/texlive/) or [MiKTeX](https://miktex.org/).
The documents use standard AMS/LaTeX packages. On Ubuntu, the packages used by
the workflow are:

```text
sudo apt-get update
sudo apt-get install -y --no-install-recommends texlive-latex-base texlive-latex-recommended texlive-latex-extra texlive-fonts-recommended lmodern
```

Compile the overview and current manuscript:

```text
python scripts/build.py
```

The script runs `pdflatex` three times for each document, with shell escape
disabled. It stops on a compilation failure or unresolved references. Outputs
and logs stay in the ignored `build/` directory:

| Document | Source | Freshly compiled PDF |
| --- | --- | --- |
| Overview | [overview.tex](overview.tex) | `build/overview/overview.pdf` |
| Current manuscript | [psh_exhaustion_refereed.tex](preprints/001-psh-exhaustion/psh_exhaustion_refereed.tex) | `build/paper/psh_exhaustion_refereed.pdf` |

Use `python scripts/build.py overview` or `python scripts/build.py paper` to
compile only one document. The manuscript has an inline `thebibliography`
environment; no BibTeX step or external figures are required. The separate
`citation.bib` records a suggested citation for the manuscript itself.

## Edit locally without Python

Open `preprints/001-psh-exhaustion/psh_exhaustion_refereed.tex` in your LaTeX editor,
edit and save it, then compile with pdfLaTeX until the references settle (usually
two or three passes). Save the resulting PDF beside the source as
`psh_exhaustion_refereed.pdf`, replacing the active PDF. For the catalogue, edit
`overview.tex` and compile it to `overview.pdf` in the repository root.

Inspect the PDFs, then commit the edited sources and their PDFs together in
GitHub Desktop and click **Push origin**. The remote workflow runs the automated
checks. No local Python command is required for this editing route. Record
substantive revisions in [history.md](history.md); keep the original files under
`archive/` and `reviews/source/` unchanged.

## Optional scripted PDF updates

Ordinary scripted builds leave the active PDFs unchanged. To compile and update
both active PDFs after every selected build succeeds:

```text
python scripts/build.py all --publish
python scripts/check.py
```

Use `paper --publish` or `overview --publish` to update only one active PDF.
Here `--publish` copies files locally; it does not upload to GitHub. Archived PDFs
are never build targets. TeX versions may produce different PDF bytes even when
the typeset content agrees, which is why active PDFs are not compared to original
intake hashes. Ordinary manuscript edits require no change to the integrity
manifest. That manifest remains a record of the archived original materials.

## GitHub checks

The [workflow](.github/workflows/validate.yml) runs the structural and integrity
checks plus a fresh LaTeX build after a push or pull request. It can also be
started manually. It has read-only repository permissions and never commits or
publishes PDFs. The workflow uses the versions documented in the official
[checkout](https://github.com/actions/checkout) and
[setup-python](https://github.com/actions/setup-python) action repositories when
it was prepared. Successful checks confirm file integrity and compilation; they
do not constitute mathematical review or formal verification.
