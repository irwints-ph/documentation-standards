# 📖 Document Template Standard (Reference)

---

## Metadata

**Document:** `020r-document-template-standard.md`

**Type:** 📖 Reference Document

**Companion Standard:** [020-document-template-standard.md](./020-document-template-standard.md)

**Owner:** Engineering

**Version:** 1.0

---

## Status

**As of:** 07.26.2026

✅ Accepted

---

# Purpose

Provide supporting information, rationale, examples, and implementation guidance for the Document Template Standard.

This document explains why the documentation structure exists and how it should be applied across engineering repositories.

The companion standard defines the required structure.

This document explains:

- Why the structure exists
- How each section should be used
- Common documentation patterns
- Examples and recommendations

---

# Background

Engineering documentation often becomes inconsistent when teams create documents without an agreed structure.

Common problems include:

- Important information placed in different locations
- Missing metadata
- Inconsistent status tracking
- Difficulty locating related documents
- Different writing styles across repositories
- Increased effort for AI-assisted workflows

A standardized document template creates a predictable structure that improves:

- Human readability
- Engineering collaboration
- Document discovery
- Long-term maintenance
- AI context processing

---

# Why Standardize Document Structure?

Without a common structure, documentation evolves differently across projects.

Examples:

Project A:

```text
Purpose
Architecture
History
References
```

Project B:

```text
Overview
Details
Notes
Links
```

Project C:

```text
Background
Decision
Implementation
```

Although each may contain useful information, the inconsistency increases the effort required to understand new documents.

A standard structure allows engineers to immediately recognize where information belongs.

---

# Document Anatomy

Official engineering documents follow this structure:

```text
Title

Metadata

Status

Purpose

Standard

Related Documents
```

Each section has a specific responsibility.

---

# Title

## Purpose

The title provides a human-readable description of the document.

The title should describe the subject, not the filename.

Example:

Filename:

```text
020-document-template-standard.md
```

Title:

```text
📘 Document Template Standard
```

---

## Why Separate Title and Filename?

Filenames are optimized for:

* Repository organization
* Searching
* Automation
* Version control

Titles are optimized for:

* Human understanding
* Documentation navigation
* Reading experience

Keeping them separate improves both use cases.

---

# Metadata

## Purpose

Metadata identifies the document within the documentation system.

Standard metadata fields:

| Field               | Purpose                            |
| ------------------- | ---------------------------------- |
| Document            | Identifies the exact file          |
| Type                | Identifies document classification |
| Companion Reference | Links supporting documentation     |
| Owner               | Identifies responsible group       |
| Version             | Tracks document version            |

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

# Why Metadata Matters

Metadata enables:

* Automated documentation tools
* Document indexing
* AI context preparation
* Ownership tracking
* Version management

Without metadata, documents become isolated files rather than part of a documentation system.

---

# Status

## Purpose

The Status section communicates the current lifecycle stage of the document.

Example:

```markdown
## Status

**As of:** 07.26.2026

✅ Accepted
```

---

## Relationship With Document Lifecycle

Status follows:

015-document-status-lifecycle.md

The lifecycle defines states such as:

* Planning
* In Progress
* Under Review
* Accepted
* Official
* Superseded
* Archived

The template only defines where the status appears.

It does not define lifecycle rules.

---

# Purpose Section

## Purpose

The Purpose section provides a short explanation of why the document exists.

A reader should understand the reason for the document within seconds.

Good purpose:

```text
Define the standard naming convention used
for engineering documentation files.
```

Poor purpose:

```text
This document contains information about
how names should work.
```

The purpose should be specific and actionable.

---

# Standard Section

## Purpose

The Standard section contains the actual engineering rules.

This is the authoritative part of a Canonical Standard.

It should define:

* Required practices
* Approved conventions
* Expected behavior
* Implementation guidance

---

## What Does Not Belong Here?

Avoid including:

* Historical discussions
* Alternative approaches
* Long explanations
* Previous versions
* Lessons learned

Those belong in the Reference document.

Example:

Standard:

```text
All documents must include a Status section.
```

Reference:

```text
Before this standard existed, projects used
different status formats.
```

---

# Related Documents

## Purpose

The Related Documents section connects documentation within the ecosystem.

Common categories:

```text
Prerequisites

Related

Companion
```

Example:

```markdown
# Related Documents

## Prerequisites

- 001-documentation-system-overview.md

## Related

- 025-document-naming-standard.md

## Companion

- 020r-document-template-standard.md
```

---

# Canonical and Reference Relationship

The Engineering Documentation System separates:

## Canonical Standard

Answers:

> What is the current rule?

Characteristics:

* Short
* Current
* Direct
* Implementation focused

## Reference Document

Answers:

> Why does this rule exist?

Characteristics:

* Detailed
* Explanatory
* Historical context
* Examples
* Guidance

Relationship:

```text
Canonical Standard

        defines

        ↓

Current Engineering Rule


Reference Document

        explains

        ↓

Reasoning and Application
```

---

# Why Keep Reference Documents Separate?

Combining standards and explanations creates several problems:

* Standards become too long
* Important rules become harder to find
* Historical information becomes mixed with current rules
* AI systems receive unnecessary context

Separating them provides:

* Fast standards lookup
* Detailed learning material
* Better maintainability

---

# AI Optimization Considerations

The document structure supports AI-assisted engineering.

A predictable format allows AI systems to identify:

* Document purpose
* Authority level
* Current status
* Related documents
* Applicable rules

The separation between Canonical and Reference documents also allows different usage patterns:

Canonical:

```text
Quick engineering context
```

Reference:

```text
Deep understanding and explanation
```

---

# Common Mistakes

## Mixing History With Standards

Incorrect:

```text
The team originally tried approach A,
then changed to approach B.
```

Better:

Standard:

```text
Use approach B.
```

Reference:

```text
Approach A was evaluated before selecting B.
```

---

## Missing Status Information

Incorrect:

```text
# Document Title

Purpose
```

Correct:

```text
# Document Title

Metadata

Status

Purpose
```

---

## Creating Reference Documents Without Standards

Reference documents should support an existing standard.

They should not become independent sources of rules.

---

# Evolution of This Standard

The Document Template Standard is expected to evolve as the documentation system matures.

Future improvements may include:

* Additional metadata fields
* Automation requirements
* Validation rules
* Documentation generation support

Changes should follow the document lifecycle process.

---

# Related Documents

## Companion Standard

* [020-document-template-standard.md](./020-document-template-standard.md)

## Related Standards

* [001-documentation-system-overview.md](./001-documentation-system-overview.md)
* [005-documentation-level-standard.md](./005-documentation-level-standard.md)
* [015-document-status-lifecycle.md](./015-document-status-lifecycle.md)
* [025-document-naming-standard.md](./025-document-naming-standard.md)
* [030-document-icons-and-statuses-standard.md](./030-document-icons-and-statuses-standard.md)
