# 🛠️ Initialize Git Repository

---

## Metadata

**Document:** `initialize-git-repository.md`

**Type:** 🛠️ Procedure

**Related Standard:** [045-git-workflow-standard.md](../../current-standards/045-git-workflow-standard.md)

**Owner:** Engineering

**Version:** 1.0

---

## Status

**As of:** 07.26.2026 HH:MM PHT

✅ Accepted

---

# Purpose

Provide the standard procedure for initializing a new Git repository following the Engineering Git Workflow Standard.

This procedure establishes the initial repository baseline, connects the remote repository, and creates the initial version tag.

---

# Prerequisites

Before starting, ensure that:

* The Engineering Documentation Foundation has been added to the repository.
* A `.gitignore` file has been created and reviewed.
* Any personal or temporary files have been excluded from version control.

> **See also:** [Managing `.gitignore`](../../kb/git/managing-gitignore.md)

---

# Solution

## Step 1 — Initialize the Repository

From the repository root:

```bash
git init
```

This creates the Git repository metadata:

```text
.git/
```

---

## Step 2 — Review Repository Status

Before staging files, review the repository.

```bash
git status
```

Verify that only the intended project files will be committed.

---

## Step 3 — Stage Repository Files

Stage all repository files.

```bash
git add .
```

---

## Step 4 — Review Staged Changes

Verify the staged files.

```bash
git status
```

The staged files should represent the repository baseline.

If you notice files that should remain local (such as personal notes or temporary files), update `.gitignore` before continuing.

> **See also:** [Managing `.gitignore`](../../kb/git/managing-gitignore.md)

> **See also:** [Stop Tracking Files and Folders](../../kb/git/stop-tracking-files-and-folders.md)

---

## Step 5 — Create the Initial Commit

Create the baseline commit.

```bash
git commit -m "docs: establish Engineering Documentation Foundation v1"
```

This commit represents the initial engineering documentation baseline.

---

## Step 6 — Rename the Default Branch

Rename the default branch.

```bash
git branch -M main
```

---

## Step 7 — Configure the Remote Repository

Replace the URL with your repository.

```bash
git remote add origin https://github.com/.../documentation-standards.git
```

Verify:

```bash
git remote -v
```

---

## Step 8 — Push the Repository

Push the repository to GitHub.

```bash
git push -u origin main
```

---

## Step 9 — Create the Initial Version Tag

Create an annotated version tag.

```bash
git tag -a v1.0.0 -m "Engineering Documentation Foundation v1"
```

Verify:

```bash
git tag
```

Expected:

```text
v1.0.0
```

---

## Step 10 — Push the Version Tag

Push the tag to the remote repository.

```bash
git push origin v1.0.0
```

---

# Verify

Verify that:

* The repository has been initialized.
* The `main` branch exists.
* The remote repository is configured.
* The initial commit has been pushed.
* The version tag is available on the remote repository.

---

# Example

The repository history should resemble:

```text
v1.0.0
   │
   ▼

docs: establish Engineering Documentation Foundation v1
```

---

# Common Use Cases

* Creating a new repository.
* Publishing a reusable framework.
* Establishing the initial engineering baseline.
* Bootstrapping a new project.

---

# Official Documentation

For additional information, refer to the official Git documentation:

* Git Documentation — Repository Setup
* Git Documentation — `git init`
* Git Documentation — `git commit`
* Git Documentation — `git tag`

---

# Related Documents

## Standards

* `045-git-workflow-standard.md`

## References

* `045r-git-workflow-reference.md`

## Knowledge Base

* `kb/git/managing-gitignore.md`
* `kb/git/stop-tracking-files-and-folders.md`
