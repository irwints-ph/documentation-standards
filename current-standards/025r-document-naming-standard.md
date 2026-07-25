# 📖 Document Naming Standard (Reference)

---

## Metadata

**Document:** `025r-document-naming-standard.md`

**Type:** 📖 Reference

**Companion Standard:** [025-document-naming-standard.md](./025-document-naming-standard.md)

**Owner:** Engineering

**Version:** 1.0

---

## Status

**As of:** 07.25.2026 06:50 PHT

✅ Accepted

---

# Purpose

This document explains the philosophy, rationale, and evolution of the Engineering Document Naming Standard.

The companion Official document defines the required naming convention. This Reference document explains why the convention exists, the engineering decisions behind it, and the best practices for maintaining a consistent documentation system over time.

---

# Why Standardize Document Names?

Documentation is a long-term engineering asset.

Over the lifetime of a project, hundreds or even thousands of documents may be created by different authors across multiple repositories. Without a consistent naming convention, documentation gradually becomes difficult to navigate and maintain.

Common problems include:

- Similar documents using different naming styles.
- Multiple names for the same concept.
- Inconsistent capitalization.
- Duplicate documents that cannot be easily identified.
- Poor search results.
- Broken cross-references after renaming files.

A standardized naming convention makes documentation predictable for both humans and automation.

---

# Design Goals

The naming standard was designed to achieve several objectives.

- Make documents easy to locate.
- Encourage consistent organization.
- Improve readability.
- Simplify cross-referencing.
- Support documentation automation.
- Improve compatibility across operating systems.
- Provide stable filenames that rarely require renaming.
- Produce AI-friendly document identifiers.

---

# Naming Philosophy

A document name should communicate its purpose before the document is opened.

Good names are:

- concise
- descriptive
- predictable
- stable
- technology independent

The filename should identify *what the document is*, not *who wrote it*, *when it was created*, or *what project it currently belongs to*.

---

# Numbering and Naming Work Together

The documentation system separates **ordering** from **description**.

The numeric prefix defines the recommended reading sequence.

The descriptive name identifies the document's subject.

Example:

```text
001-documentation-system-overview.md
010-document-numbering-standard.md
025-document-naming-standard.md
```

Even if two documents have similar names, their numbering immediately identifies their place within the documentation system.

---

# Why Lowercase?

Lowercase filenames improve consistency across different operating systems.

Advantages include:

- Easier typing.
- Consistent appearance.
- Reduced risk of case-sensitive file issues.
- Cleaner URLs.
- Simpler automation scripts.

Using a single capitalization style also prevents accidental duplicates such as:

```text
Readme.md
README.md
readme.md
```

---

# Why Hyphens Instead of Spaces?

The engineering standard uses hyphens (`-`) as the word separator.

Advantages include:

- Easier command-line usage.
- Better URL compatibility.
- Cleaner Markdown links.
- Consistent behavior across operating systems.
- Improved readability.

Example:

```text
document-status-lifecycle.md
```

instead of:

```text
Document Status Lifecycle.md
```

or

```text
document_status_lifecycle.md
```

---

# Why Avoid Underscores?

Underscores are technically valid, but they reduce readability and create inconsistency when mixed with hyphenated names.

For example:

```text
document_status_lifecycle.md
```

is generally harder to scan than:

```text
document-status-lifecycle.md
```

For consistency, the Engineering Documentation System reserves hyphens as the standard word separator.

---

# Reference Documents

Reference documents append the suffix `r` immediately after the document number.

Example:

```text
020-document-template-standard.md
020r-document-template-standard.md
```

This convention keeps the Official and Reference documents grouped together when sorted alphabetically while clearly identifying their relationship.

The `r` suffix was chosen because it is:

- short
- recognizable
- easy to type
- visually distinct
- simple to automate

---

# Folder Naming

Folders follow the same philosophy as document names.

Folder names should be:

- lowercase
- descriptive
- hyphen-separated
- stable

Example:

```text
engineering-history/
roadmaps/
knowledge-base/
templates/
git/
```

Avoid mixing naming styles within the same repository.

---

# Renaming Documents

Published documentation should be renamed only when necessary.

Renaming a document may require updating:

- internal links
- repository indexes
- README files
- cross-references
- automation scripts
- AI context references

When a rename is required:

1. Update all links.
2. Update related documentation.
3. Update generated indexes.
4. Verify navigation.
5. Record significant renames in the project history if appropriate.

---

# Common Mistakes

Avoid the following naming patterns.

Using spaces:

```text
Document Naming Standard.md
```

Using underscores:

```text
document_naming_standard.md
```

Using inconsistent capitalization:

```text
Document-Naming-Standard.md
```

Using version numbers in filenames:

```text
document-standard-v2.md
```

Using temporary filenames:

```text
new-document.md
test.md
draft-final.md
```

Temporary or experimental documents should instead be managed through the Document Status Lifecycle rather than by embedding workflow state into the filename.

---

# Best Practices

- Choose descriptive names.
- Keep filenames short.
- Use lowercase consistently.
- Separate words with hyphens.
- Preserve stable filenames.
- Keep numbering independent from document titles.
- Rename documents only when necessary.
- Use the Reference companion instead of creating duplicate documents.

---

# Future Evolution

Future tooling may automatically validate:

- filename format
- numbering consistency
- companion document relationships
- duplicate filenames
- broken cross-references

Maintaining a predictable naming convention enables these automation capabilities without requiring repository-specific rules.

---

# Frequently Asked Questions

### Why not use spaces?

Spaces complicate command-line operations, URLs, Markdown links, and automation. Hyphens provide a simple and consistent alternative.

---

### Why not use underscores?

Hyphens are generally more readable and have become the standard separator used throughout the Engineering Documentation System.

---

### Why use the `r` suffix?

The `r` suffix clearly identifies a Reference companion while keeping it adjacent to its Official document in directory listings.

---

### Can filenames include version numbers?

No.

Document versions are managed through the Document Status Lifecycle and engineering history, not through filenames.

---

### Can a published filename change?

Yes, but only when there is a compelling engineering reason. Renaming should be rare because filenames become part of links, indexes, automation, and AI project context.

---

# Related Documents

## Prerequisites

- [001-documentation-system-overview.md](./001-documentation-system-overview.md)
- [005-documentation-level-standard.md](./005-documentation-level-standard.md)
- [010-document-numbering-standard.md](./010-document-numbering-standard.md)

## Related

- [015-document-status-lifecycle.md](./015-document-status-lifecycle.md)
- [020-document-template-standard.md](./020-document-template-standard.md)
- [035-terminology-standard.md](./035-terminology-standard.md)

## Companion

- [025-document-naming-standard.md](./025-document-naming-standard.md)