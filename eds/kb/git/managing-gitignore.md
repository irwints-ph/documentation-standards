# 🆘 Managing `.gitignore`

---

## Metadata

**Document:** `kb/git/managing-gitignore.md`

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

Explain how to configure a `.gitignore` file to prevent Git from tracking files and directories that should not be committed to the repository.

This document focuses on the most commonly used `.gitignore` patterns in day-to-day engineering work.

---

# Scenario

You want Git to ignore files or folders that should remain local or are generated automatically.

Common examples include:

* Personal notes
* Scratch files
* Build output
* IDE configuration
* Log files
* Temporary files
* Operating system files

---

# Solution

## Ignore a Single File

Ignore one specific file.

```text
scratch.md
```

Only `scratch.md` will be ignored.

---

## Ignore a Directory

Ignore an entire directory.

```text
ignored-docs/
```

Everything inside the directory will be ignored.

---

## Ignore a File Extension

Ignore all files matching an extension.

```text
*.log
```

Examples:

```text
application.log
build.log
error.log
```

---

## Ignore Files by Prefix

Ignore files beginning with a prefix.

```text
temp*
```

Examples:

```text
temp
temp.txt
temporary.md
temp-backup.json
```

---

## Ignore Files by Name Pattern

Ignore files containing a pattern.

```text
*temp*
```

Examples:

```text
mytemp.txt
build-temp.log
temporary.md
```

---

## Ignore Root Directory Only

Ignore only the repository root directory.

```text
/build
```

This does **not** ignore nested `build` directories.

---

## Ignore Every Directory Named `build`

```text
build/
```

Any directory named `build` will be ignored regardless of its location.

---

## Re-Include a File

Sometimes a file should remain tracked even though a broader rule ignores it.

```text
*.log
!important.log
```

All log files are ignored except `important.log`.

---

# Common Patterns

| Pattern         | Description                          | Example                    |
| --------------- | ------------------------------------ | -------------------------- |
| `scratch.md`    | Ignore one file                      | Personal notes             |
| `ignored-docs/` | Ignore one directory                 | Local working documents    |
| `*.log`         | Ignore file extension                | Log files                  |
| `*.tmp`         | Ignore temporary files               | Cache files                |
| `build/`        | Ignore build directories             | Build output               |
| `/build`        | Ignore only the root build directory | Repository root            |
| `.vscode/`      | Ignore VS Code settings              | Personal IDE configuration |
| `.idea/`        | Ignore JetBrains IDE settings        | IntelliJ, Rider, WebStorm  |
| `.DS_Store`     | Ignore macOS metadata                | Finder                     |
| `Thumbs.db`     | Ignore Windows metadata              | Windows Explorer           |

---

# Common Mistakes

## `tmp`

```text
tmp
```

Matches both:

* a file named `tmp`
* a directory named `tmp`

---

## `tmp/`

```text
tmp/
```

Matches only a directory named `tmp`.

---

## `tmp*`

```text
tmp*
```

Matches anything beginning with `tmp`.

Examples:

```text
tmp
tmp.txt
tmp-backup
temporary.md
```

---

## `*tmp*`

```text
*tmp*
```

Matches anything containing `tmp`.

Examples:

```text
mytmp.txt
build-tmp.log
temporary.md
```

---

# Example

```text
# Personal notes
scratch.md

# Local working documents
ignored-docs/

# Build output
build/
dist/

# Dependency folders
node_modules/

# Log files
*.log

# Temporary files
*.tmp

# IDE
.vscode/
.idea/

# Operating System
.DS_Store
Thumbs.db
```

---

# Verify

Check whether Git is ignoring the expected files.

```bash
git status
```

Ignored files should not appear as untracked files.

If a file still appears, verify:

* The `.gitignore` pattern is correct.
* The file has not already been committed.

If the file is already tracked by Git, see:

```text
kb/git/stop-tracking-files-and-folders.md
```

---

# Frequently Asked Questions

### I added a file to `.gitignore`, but Git still tracks it.

The file was likely committed before it was added to `.gitignore`.

Follow the procedure:

```text
kb/git/stop-tracking-files-and-folders.md
```

---

### Should `.gitignore` be committed?

Yes.

The `.gitignore` file is part of the repository and should be shared with the team.

---

### Should personal notes be ignored?

Yes.

Files such as `scratch.md` or local working folders should normally remain outside the repository.

---

# Official Documentation

For the complete `.gitignore` specification and advanced pattern matching, refer to:

* Git Documentation — `.gitignore` Manual

  * https://git-scm.com/docs/gitignore

---

# Related Documents

## Knowledge Base

* `initialize-git-repository.md`
* `stop-tracking-files-and-folders.md`

## Standards

* `045-git-workflow-standard.md`

## References

* `045r-git-workflow-reference.md`
