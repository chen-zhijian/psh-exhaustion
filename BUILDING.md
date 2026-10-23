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
[source-manifest.json](source-manifest.json). The archived manuscript is not an
active TeX check or build target; its original bytes are checked instead.

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

## Preserve the supplied manuscript and archive

The supplied current manuscript, PDF, previous version, and revision records
are preserved byte for byte. Ordinary builds do not change them. Different TeX
versions can produce different PDF bytes even when the typeset content agrees;
the fresh build under `build/paper/` is for comparison with the supplied PDF.

The repository overview can be refreshed explicitly:

```text
python scripts/build.py overview --publish
python scripts/check.py
```

The `--publish` option is limited to the overview in this intake snapshot. It
cannot replace the supplied manuscript PDF or archived files. Future revisions
are possible: retain the incoming version and its hashes, add the new manuscript
as a new version, and update the catalogue, integrity manifest, provenance record,
and active build target together. Any deliberate change to a preserved file must
be reflected accurately in those records, rather than merely refreshing a hash
to silence a failed check.

## GitHub checks

The [workflow](.github/workflows/validate.yml) runs the structural and integrity
checks plus a fresh LaTeX build after a push or pull request. It can also be
started manually. It has read-only repository permissions and never commits or
publishes PDFs. The workflow uses the versions documented in the official
[checkout](https://github.com/actions/checkout) and
[setup-python](https://github.com/actions/setup-python) action repositories when
it was prepared. Successful checks confirm file integrity and compilation; they
do not constitute mathematical review or formal verification.
