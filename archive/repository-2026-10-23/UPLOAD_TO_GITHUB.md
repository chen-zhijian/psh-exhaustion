# Upload this repository to GitHub

The local folder is ready to use. It contains the revised manuscript, supplied
previous version, research catalogue, provenance records, and build workflow.
For first publication, follow the steps below. If your copy is already connected
to GitHub, follow **Later updates** to upload revisions to the same repository.

Suggested repository name: **psh-exhaustion**.

Suggested description: **Continuous and smooth plurisubharmonic exhaustions: revised manuscript, prior version, provenance, and research notes.**

## Recommended: GitHub Desktop

This route preserves the folder structure and makes later updates easy.

1. Install [GitHub Desktop](https://desktop.github.com/) and sign in to your account.
2. Choose **File → Add local repository** and select the prepared `psh-exhaustion-repository` folder. Choose the folder that directly contains `README.md`, `overview.pdf`, and `preprints`.
3. If your commit identity is not set, use **File → Options → Git** to choose your name and an email associated with your GitHub account, then save.
4. In **Changes**, keep the prepared files selected. Enter **Initial psh exhaustion research collection** in the summary box and click **Commit to main**.
5. Click **Publish repository**. Enter `psh-exhaustion` as the name and optionally paste the description above.
6. Choose visibility: leave **Keep this code private** checked for a private repository, or clear it for a public one. Select your account or organization.
7. Click **Publish repository**. When publication finishes, choose **Repository → View on GitHub** to see the result.

These steps follow GitHub's instructions for
[adding a local repository](https://docs.github.com/en/desktop/adding-and-cloning-repositories/adding-a-repository-from-your-local-computer-to-github-desktop),
[setting commit identity](https://docs.github.com/en/desktop/configuring-and-customizing-github-desktop/configuring-git-for-github-desktop), and
[publishing an existing project](https://docs.github.com/en/desktop/adding-and-cloning-repositories/adding-an-existing-project-to-github-using-github-desktop).

If you use the ZIP archive instead of the prepared local folder, it contains the
repository files but no `.git` history. The browser method below works with that
archive after extraction.

## Alternative: upload through the website

1. Extract the supplied repository ZIP. Open the extracted folder that contains `README.md`.
2. Visit [GitHub's new-repository page](https://github.com/new). Select the owner, enter `psh-exhaustion`, and choose public or private visibility.
3. Leave the automatic README, `.gitignore`, and license initialization options unselected, because this upload supplies the prepared files. Click **Create repository**.
4. Choose **uploading an existing file**, or **Add file → Upload files**.
5. Drag the **contents** of the extracted folder into the upload area, including the `preprints`, `archive`, `reviews`, `reasoning_traces`, `notes`, `lean`, `scripts`, and `.github` folders. Include `.gitignore`, `.gitattributes`, and the root files. Upload the extracted contents, not the ZIP itself or an extra outer folder.
6. Enter a short commit message and complete the upload using **Commit changes** or GitHub's proposed-branch flow if it requests one.

GitHub currently allows up to 100 files per browser upload and 25 MiB per file;
this collection is below both limits. See
[GitHub's upload documentation](https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository).

## After uploading

- The repository home page should show the psh exhaustion research collection, with working links to the revised paper, overview, and earlier version.
- Open **Actions** to see the latest document checks. They verify original archive integrity, active references, links, and compilation. A local successful check does not establish the outcome of a future GitHub run.
- Suggested topics are `complex-analysis`, `several-complex-variables`, `plurisubharmonic-functions`, `mathematics`, and `latex`.
- The active manuscript and citation name Zhijian Chen and Bo Xiao, as supplied in the edited source. Licensing terms remain for the authors to decide.

## Later updates

With GitHub Desktop, edit the active manuscript under `preprints/` or the overview,
compile its PDF in your LaTeX editor, review the **Changes** list, commit the source
and PDF together, and click **Push origin**. See [BUILDING.md](BUILDING.md) for the
workflow without local Python and the optional scripted build. Preserve the
original files under `archive/` and `reviews/source/`; their hashes remain fixed.
Active manuscript edits do not require changing the integrity manifest. Record
substantive changes in [history.md](history.md).

With browser uploads, replace changed documentation at its existing path and
record a commit message. Keep each new manuscript version's LaTeX source and PDF
synchronized. See the [paper README](preprints/001-psh-exhaustion/README.md) for
citation and version information.
