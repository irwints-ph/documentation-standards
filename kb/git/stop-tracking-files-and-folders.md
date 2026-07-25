# 🆘 Stop Tracking Files and Folders

---

## Metadata

**Document:** `kb/git/stop-tracking-files-and-folders.md`

**Type:** 🆘 Knowledge Base

**Category:** Git

**Owner:** Engineering

**Version:** 1.0

---

## Status

**As of:** 07.26.2026 HH:MM PHT

✅ Accepted

---

# Purpose

Describe how to remove files or folders from Git version control while keeping the local copies.

This procedure is commonly used when files or directories were accidentally committed and should no longer be tracked by the repository.

---

# Scenario

A file or folder has already been committed to the repository but should no longer be tracked by Git.

You want to:

* Remove it from the repository.
* Keep the local copy.
* Prevent Git from tracking future changes.

Common examples include:

* `scratch.md`
* `ignored-docs/`
* `.vscode/`
* Temporary files
* Personal notes
* Generated files

---

# Solution

## Step 1 — Update `.gitignore`

Add the file or folder to your `.gitignore` file.

Example:

```text
scratch.md

ignored-docs/

.vscode/
```

This prevents Git from tracking the item after it has been removed from the repository.

> **See also:** [Managing `.gitignore`](managing-gitignore.md) for common patterns, examples, and best practices.

---

## Step 2 — Verify `.gitignore`

Confirm that the correct file or folder has been added.

For example:

```text
scratch.md
```

or

```text
ignored-docs/
```

---

## Step 3 — Stop Tracking the File or Folder

Remove the item from Git's index while keeping the local copy.

### File

```bash
git rm --cached scratch.md
```

### Folder

```bash
git rm -r --cached ignored-docs/
```

The `--cached` option removes the item from Git's index but leaves the local files untouched.

---

## Step 4 — Commit the Change

Commit the updated repository state.

```bash
git commit -m "chore: stop tracking scratch files"
```

---

## Step 5 — Push the Change

Push the commit to the remote repository.

```bash
git push
```

The file or folder is removed from the repository but remains available on your local machine.

---

# Verify

Run:

```bash
git status
```

The file or folder should no longer appear as a tracked change.

Future modifications should also be ignored because the item is now listed in `.gitignore`.

---

# Example

Suppose `scratch.md` was accidentally committed.

Update `.gitignore`:

```text
scratch.md
```

Stop tracking the file:

```bash
git rm --cached scratch.md
```

Commit and push:

```bash
git commit -m "chore: stop tracking scratch.md"
git push
```

Result:

```text
Repository
❌ scratch.md

Local Computer
✅ scratch.md
```

---

# Common Use Cases

* Personal working notes
* Scratch files
* IDE configuration
* Temporary documentation
* Generated files
* Local experiment folders

---

# Important

Do **not** use:

```bash
git rm scratch.md
```

This removes both the Git-tracked file **and** the local copy.

To keep the local file, always use:

```bash
git rm --cached scratch.md
```

For directories, use:

```bash
git rm -r --cached ignored-docs/
```

---

# Summary

```text
File or folder was accidentally committed

        │
        ▼

Add it to .gitignore

        │
        ▼

Verify the .gitignore entry

        │
        ▼

Stop tracking it

git rm --cached

        │
        ▼

Commit

        │
        ▼

Push

        │
        ▼

Repository
❌ File removed

Local Computer
✅ File preserved
```

---

# Related Documents

## Knowledge Base

* `initialize-git-repository.md`
* `managing-gitignore.md`

## Standards

* `045-git-workflow-standard.md`

## References

* `045r-git-workflow-reference.md`
