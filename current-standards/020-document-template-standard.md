# 📘 Document Template Standard

---

## Metadata

**Document:** `020-document-template-standard.md`

**Type:** 📘 Canonical Standard

**Companion Reference:** [020r-document-template-standard.md](./020r-document-template-standard.md)

**Owner:** Engineering

**Version:** 1.0

---

## Status

**As of:** 07.26.2026 HH:MM TZ

✅ Accepted

---

# Purpose

Define the standard structure used for engineering documentation.

This template provides a consistent layout for all engineering documents, improving readability, navigation, maintenance, and AI-assisted workflows.

---

# Standard

Every Official document should follow the structure below.

```text
Title

Metadata

Status

Purpose

Standard

Related Documents
```

Section names should remain consistent across all Official documents.

---

# Document Structure

## Title

The document title should be written for human readers.

Titles should describe the document subject rather than the filename.

Example:

```text
📘 Document Template Standard
```

---

## Metadata

Metadata identifies the document within the documentation system.

Every Official document should include:

| Field               | Purpose                       |
| ------------------- | ----------------------------- |
| Document            | Exact filename                |
| Type                | Document classification       |
| Companion Reference | Related reference document    |
| Owner               | Responsible engineering group |
| Version             | Document version              |

Example:

```markdown
## Metadata

**Document:** 020-document-template-standard.md

**Type:** 📘 Canonical Standard

**Companion Reference:** 020r-document-template-standard.md

**Owner:** Engineering

**Version:** 1.0
```

---

## Status

The Status section indicates the document's current lifecycle stage.

Every document should include:

* Current date/time
* Current lifecycle status

Example:

```markdown
## Status

**As of:** MM.DD.YYYY HH:MM TZ

✅ Accepted
```

Lifecycle definitions are maintained by:

015-document-status-lifecycle.md

---

# Purpose

The Purpose section explains why the document exists.

It should answer:

* What is this document about?
* Why does this document exist?

---

# Standard

The Standard section defines current engineering rules.

Official documents should:

* define the current standard,
* avoid historical discussion,
* remain concise,
* provide implementation guidance.

Historical context, rationale, and examples belong in the companion Reference document.

---

# Related Documents

The final section links to associated documentation.

Recommended groups:

* Prerequisites
* Related
* Companion

---

# Template Principles

Official documents should be:

* concise,
* easy to scan,
* readable in under 30 seconds,
* AI optimized,
* focused on current engineering standards.

Historical discussion, rationale, migration guidance, and extensive examples belong in companion Reference documents.

---

# Naming Convention

Document filenames identify documents within the repository.

Document titles identify documents for human readers.

Example:

Filename:

```text
020-document-template-standard.md
```

Title:

```text
📘 Document Template Standard
```

Reference documents use the `r` suffix.

Example:

```text
020r-document-template-standard.md
```

Title:

```text
📖 Document Template Standard (Reference)
```

---

# Related Documents

## Prerequisites

* [001-documentation-system-overview.md](./001-documentation-system-overview.md)
* [005-documentation-level-standard.md](./005-documentation-level-standard.md)
* [010-document-numbering-standard.md](./010-document-numbering-standard.md)
* [015-document-status-lifecycle.md](./015-document-status-lifecycle.md)

## Related

* [025-document-naming-standard.md](./025-document-naming-standard.md)
* [030-document-icons-and-statuses-standard.md](./030-document-icons-and-statuses-standard.md)

## Companion

* [020r-document-template-standard.md](./020r-document-template-standard.md)
