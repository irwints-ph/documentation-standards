# 📘 Document Template Standard

---

## Metadata

| Field     | Value                                |
| --------- | ------------------------------------ |
| As of     | 07.26.2026 23:15 PHT                 |
| Document  | `020-document-template-standard.md`  |
| Category  | Core Standards                       |
| Type      | Canonical Standard                   |
| Status    | ✅ Accepted                           |
| Companion | `020r-document-template-standard.md` |
| Version   | 2.0                                  |

---

# Purpose

Define the standard structure used for engineering documentation.

This standard establishes a consistent document layout and metadata model across the Engineering Documentation System, improving readability, navigation, maintainability, automation, and AI-assisted workflows.

---

# Standard

Every official document shall follow a consistent structure appropriate to its document type.

All documents begin with:

```text
Title

Metadata

Purpose
```

The remaining sections are determined by the document type.

This allows different engineering artifacts to expose the information they require while maintaining a consistent overall structure.

---

# Metadata Standard

Every official document begins with a Metadata section.

Metadata describes the artifact being documented rather than the document itself.

The Metadata section shall use the following format.

```markdown
## Metadata

| Field | Value |
|--------|-------|
| ... | ... |
```

The table structure remains consistent throughout the documentation system.

Individual document types use only the fields applicable to that artifact.

---

# Standard Metadata Fields

The following metadata fields are standardized throughout the documentation system.

| Field     | Purpose                                       |
| --------- | --------------------------------------------- |
| As of     | Date and time of the current revision         |
| Document  | Documentation filename                        |
| File      | Source implementation filename                |
| Scope     | Folder, subsystem, or module being documented |
| Category  | Documentation family or engineering domain    |
| Component | Logical subsystem                             |
| Type      | Classification of the artifact                |
| Status    | Lifecycle status                              |
| Companion | Associated companion document                 |
| Version   | Document revision                             |

Not every document requires every field.

Only applicable fields should be included.

---

# Document Templates

## Canonical Standard

```markdown
# Title

---

## Metadata

| Field | Value |
|--------|-------|
| As of | |
| Document | |
| Category | |
| Type | |
| Status | |
| Companion | |
| Version | |

---

# Purpose

...

---

# Standard

...

---

# Related Documents

...
```

---

## Companion Reference

```markdown
# Title

---

## Metadata

| Field | Value |
|--------|-------|
| As of | |
| Document | |
| Category | |
| Type | Companion Reference |
| Status | |
| Related Standard | |
| Version | |

---

# Purpose

...

---

# Background

...

---

# Examples

...

---

# References

...
```

---

## Folder Registry

```markdown
# Title

---

## Metadata

| Field | Value |
|--------|-------|
| As of | |
| Scope | |
| Category | |
| Type | Folder Registry |
| Status | |

---

# Purpose

...

---

# Folder Responsibility

...

---

# Current Contents

...

---

# Assessment

...
```

---

## Source Documentation

```markdown
# Title

---

## Metadata

| Field | Value |
|--------|-------|
| As of | |
| File | |
| Category | |
| Component | |
| Type | |
| Status | |

---

# Purpose

...

---

# Responsibilities

...

---

# Dependencies

...

---

# Assessment

...
```

---

## Architecture Finding

```markdown
# Title

---

## Metadata

| Field | Value |
|--------|-------|
| As of | |
| Finding | |
| Category | |
| Type | |
| Status | |

---

# Observation

...

---

# Evidence

...

---

# Assessment

...
```

---

# Section Definitions

## Title

Titles should describe the subject for human readers.

Titles should not simply repeat filenames.

Example

```text
📘 Document Template Standard
```

---

## Metadata

Metadata identifies the engineering artifact.

It should provide enough information for both humans and tools to classify the artifact without inspecting the remainder of the document.

---

## Purpose

The Purpose section explains why the artifact exists.

It should answer:

* What is this artifact?
* Why does it exist?

---

## Standard

Canonical Standards define engineering rules.

They should:

* define current engineering practices
* avoid historical discussion
* remain concise
* provide implementation guidance

Background information belongs in companion reference documents.

---

## Assessment

Discovery documents may include assessment sections describing observations made during discovery.

Assessments should remain implementation-neutral.

Recommendations belong in separate engineering discussions or future standards.

---

# Template Principles

Engineering documentation should be:

* Consistent
* Easy to scan
* Human friendly
* AI friendly
* Repository independent
* Language independent
* Maintainable
* Automation ready

The document structure should remain predictable regardless of artifact type.

---

# Metadata Principles

Metadata exists to identify the engineering artifact.

Good metadata should be:

* concise
* structured
* machine-readable
* human-readable
* stable over time

Metadata should avoid duplication whenever possible.

---

# Naming Convention

Document titles identify artifacts for human readers.

Filenames uniquely identify artifacts within the repository.

Example

Filename

```text
020-document-template-standard.md
```

Title

```text
📘 Document Template Standard
```

Companion documents follow the companion naming standard.

Example

```text
020r-document-template-standard.md
```

---

# Related Documents

## Prerequisites

* 001-documentation-system-overview.md
* 005-documentation-level-standard.md
* 010-document-numbering-standard.md
* 015-document-status-lifecycle.md

---

## Related

* 025-document-naming-standard.md
* 030-document-icons-and-statuses-standard.md
* 040-document-reference-standard.md

---

## Companion

* 020r-document-template-standard.md

---

# Notes

This standard defines the common structure used throughout the Engineering Documentation System.

Individual document types may extend the template with additional sections as appropriate, but every document begins with a standardized Metadata section and follows the same overall organizational principles.

The objective is to make documentation predictable for engineers, maintainable for teams, and easily consumable by automation and AI-assisted workflows.
