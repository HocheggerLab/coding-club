# 1. Git

## Recap of git basics

git status

git add

git commit -m "commit message"

git log

## New git commands

### A. git diff

`git diff` is a command used in the Git version control system to show the differences between various commits, the working directory, and the staging area. It's a powerful tool for reviewing changes before committing them, understanding changes made by others, or comparing different versions of code. Here's how it works and some common ways it is used:

#### Basic Usage

* **Comparing Working Directory and Staging Area** : By default, running `git diff` without any arguments will show the differences between your working directory and the staging area. This lets you see what changes you've made that have not yet been staged for commit.
* **Comparing Staging Area and Last Commit** : To see what has been staged (with `git add`) but not yet committed compared to the last commit, use `git diff --staged` or `git diff --cached`. This shows the changes that will be included in your next commit.

#### Comparing Commits

* **Comparing Two Commits** : You can compare the contents of two commits by specifying their commit hashes (or other references, like branch names) with `git diff <commit1> <commit2>`. This shows the differences between the snapshots of the code at those two points.

#### Comparing Files

* **Comparing Specific Files** : To compare changes in specific files, you can append the file paths to the end of the command, like `git diff <commit1> <commit2> -- <file1> <file2>`.

#### Options and Flags

* **Showing Statistics** : Adding the `--stat` option will display a summary of the changes (files changed, lines added/removed) instead of the full diff.
* **Color Words** : The `--color-words` option highlights the changed words instead of showing line-by-line differences, which can be more readable for small changes.
* **Patching Format** : The output of `git diff` is in a patch format, which can be applied to another codebase with the `git apply` command. This is useful for transferring changes from one repository to another.
* **Ignoring Space Changes** : Options like `-w` or `--ignore-all-space` can be used to ignore whitespace changes, which is helpful for focusing on substantial changes.

## B. git reset

`git reset` is a command in Git, a distributed version control system, that is used to undo changes. It has the capability to revert the staging area (index), working directory, and commit history to a previous state, depending on the options provided. The command can be very powerful and, if not used carefully, might lead to loss of data that is not committed. Here are the key concepts and uses of `git reset`:

### Basic Forms

1. **Soft Reset (`git reset --soft`)** : This form of reset moves the current branch's tip backwards to the specified commit, but it leaves your staging area (index) and working directory unchanged. Changes from the commits ahead of the reset point are preserved in the staging area, ready to be committed again.
2. **Mixed Reset (`git reset --mixed` or simply `git reset`)** : This is the default mode of `git reset`. It moves the current branch's tip back to the specified commit and also resets the staging area to match this commit. However, it leaves your working directory (the actual files on your computer) unchanged. Changes that were staged and committed after the reset point will be unstaged but still present in your working directory.
3. **Hard Reset (`git reset --hard`)** : This mode moves the branch's tip back to the specified commit, resets the staging area, and also changes your working directory to match the commit. This effectively discards all changes in the staging area and working directory since the commit to which you're resetting. It's a powerful command that can lead to loss of uncommitted changes, so it should be used with caution.

### Usage Scenarios

* **Undoing Local Commits** : If you have made commits that you want to undo, `git reset` can be used to move the branch pointer back to a previous commit, effectively removing the subsequent commits from the branch's history.
* **Cleaning the Staging Area** : If you have staged changes that you decide not to commit, you can use `git reset` (without specifying a commit, which defaults to `HEAD`) to unstage them.
* **Combining Changes into a Single Commit** : After making several commits, if you want to combine all changes into a single commit, you can use `git reset` to move the branch pointer back without changing your working directory, and then commit again.

### Important Considerations

* **Local vs. Remote Repositories** : `git reset` affects the local repository. If you've already pushed commits to a remote repository that you're resetting, you'll have to use `git push --force` to update the remote repository with your local history changes, which can disrupt collaborators. It's generally best to avoid rewriting history on shared branches.
* **Working Directory Safety** : The `--hard` option can lead to loss of uncommitted changes. Always make sure your work is committed or backed up before using `git reset --hard`.
* **Choosing a Commit** : When using `git reset`, you can specify the commit to reset to in several ways, such as using the commit hash, `HEAD~1` (for the previous commit), or a branch name.

In essence, `git reset` is a powerful tool for managing your commit history and staging area. It offers flexibility in how you undo changes, prepare commits, and manage your project's history, but it requires careful use to avoid unintentional data loss.

# 2. Napari

Napari the "ImageJ for Python". It was developed in 2019 and is maintained by the Chan-Zuckerberg Initiative. I am using it to expand the capabilities of our Omero Screen software. At the moment the following plugins are available

1. Load well data, masks and metadata -> useful to check apearance of cells in a well and quality of segmentation.
2. Stitching. At the moment only single channel and no masks. -> plan to expand. Useful to look at entire well!
3. Galleries -> produce ranomised galleries of cells or nuceli with selected channels

Planned / im progress classification, interactive plotting.

### Generate conda env to use napari omero plugins

1. download code from github:

in the destination directory : git clone https://github.com/HocheggerLab/Omero-Screen-Napari.git

2. conda update -n base conda
3. conda install -n base -c conda-forge mamba
4. conda create --name omero-napari python=3.10
5. conda activate omero-napari
6. mamba install napari pyqt
7. mamba install omero-py
8. pip install ezomero
9. pip install python-dotenv
10. pip install -e 'path to omero-screen-napari package'

To get napari started type napari in the terminal. The load the read-well plugin. 


# 3. Matplotlib practice

see notebook
