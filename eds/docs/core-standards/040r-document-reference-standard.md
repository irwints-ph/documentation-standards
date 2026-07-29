# 📖 Document Reference Reference

> **Reference documents to expand knowledge, not duplicate it.**

---

# Purpose

This document summarizes how engineering documents should reference one another.

The companion Standard defines the complete specification.

This Reference provides the practical guidance most engineers need during day-to-day documentation work.

---

# Why References Matter

Engineering documentation should function as a connected knowledge system rather than a collection of independent documents.

Instead of repeating information across multiple files, documents should guide readers toward the appropriate source.

Good references make documentation:

- easier to maintain,
- easier to navigate,
- easier to validate,
- easier for AI to understand,
- easier to evolve over time.

---

# The Reference Philosophy

Each document should focus on a single responsibility.

When additional context already exists elsewhere:

**Reference it.**

Don't duplicate it.

Knowledge grows through relationships.

---

# Standard Reference Types

## Required Reading

Documents that should be understood first.

Example

- 005 Documentation Level Standard
- 020 Document Template Standard

---

## Related Documents

Documents that expand or complement the current topic.

Example

- 025 Document Naming Standard
- 035 Documentation Terminology Standard

---

## Implements

Engineering documents or project artifacts that implement the current standard.

---

## External References

Authoritative resources maintained outside the Engineering Documentation System.

Examples include:

- Official language documentation
- Framework documentation
- Industry specifications
- RFCs

---

## Parent / Child Relationships

Use Parent and Child relationships when documents naturally form a hierarchy.

Example

```text
001 Documentation System Overview

    ├──005 Documentation Level Standard
    ├──010 Document Numbering Standard
    └──020 Document Template Standard
```

---

# Referencing Best Practices

Prefer:

> See **020 Document Template Standard**.

instead of:

> See `020-document-template-standard.md`.

Document numbers and titles communicate meaning.

Filenames exist only to support hyperlinks.

---

# Avoid Duplication

Incorrect

```text
(repeating document naming rules)
```

Correct

```text
See 025 Document Naming Standard.
```

The Engineering Documentation System encourages one authoritative source for every concept.

---

# Avoid Circular References

References should help readers move forward through the knowledge system.

Avoid documents that repeatedly point back to each other without adding new information.

---

# Placement

Document references are typically placed near the end of the document.

Recommended order:

1. Prerequisites
2. Related
3. Implements
4. External References
5. Companion

Maintaining a consistent order improves navigation across repositories.

---

# Relationship to AFK

AFK encourages engineers to preserve understanding.

References preserve relationships between ideas.

Rather than rewriting existing knowledge, engineers connect readers to the appropriate source.

---

# Relationship to EKS

The Engineering Knowledge System views documentation as a knowledge graph.

Document references become the relationships that connect engineering concepts together.

Consistent references improve discoverability and future automation.

---

# Frequently Asked Questions

## Why not duplicate information?

Duplicated knowledge eventually diverges.

References preserve a single source of truth.

---

## Should filenames appear in document text?

No.

Use document numbers and titles.

Reserve filenames for hyperlinks.

---

## Why distinguish Required Reading from Related Documents?

Required Reading establishes prerequisites.

Related Documents expand understanding but are optional.

---

# Engineering Philosophy

Documentation should resemble a network of ideas rather than isolated files.

Every reference strengthens the Engineering Knowledge Repository by preserving relationships between concepts.

---

# Related Documents

## Standard

- 040 Document Reference Standard

---

## Related

- 001 Documentation System Overview
- 020 Document Template Standard
- 035 Documentation Terminology Standard

---

## Metadata

| Field | Value |
|--------|-------|
| Document | `040r-document-reference-standard.md` |
| Category | Core Standards |
| Type | 📖 Reference |
| Companion Standard | `040-document-reference-standard.md` |
| Status | 📦 Official *(or ✅ Accepted while under validation)* |
| Version | 2.0 |
| As Of | 07.29.2026 09:28 PHT |