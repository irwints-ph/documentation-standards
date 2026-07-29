# 📘 Document Numbering Standard

> **Stable numbering creates stable knowledge.**

---

# Purpose

Define the document numbering convention used throughout the Engineering Documentation System (EDS).

Document numbering provides a predictable reading order, improves discoverability, enables long-term maintenance, and allows the documentation framework to evolve without disrupting existing references.

---

# Numbering Philosophy

Document numbers are permanent identifiers.

A document's number should remain stable throughout its lifecycle, even if the document is revised, expanded, or superseded.

The numbering system is designed to support both:

- Human navigation
- AI-assisted document discovery

---

# Standard

Every Engineering Documentation Standard shall begin with a three-digit numeric prefix.

Examples

```text
001-documentation-system-overview.md

005-documentation-level-standard.md

010-document-numbering-standard.md
```

The numeric prefix establishes the recommended learning order.

Lower numbers introduce foundational concepts.

Higher numbers build upon earlier standards.

---

# Numbering Rules

The Engineering Documentation System follows these rules:

- Use a three-digit numeric prefix.
- Assign a unique number to every Engineering Standard.
- Increase numbers in logical groups.
- Leave intentional gaps for future standards.
- Never renumber published standards.
- Treat document numbers as permanent identifiers.

---

# Standard Increment

The recommended increment is **5**.

Example

```text
001
005
010
015
020
025
030
035
040
045
```

Using increments of five provides flexibility for inserting future standards without affecting existing numbering.

---

# Reserved Numbers

Unused numbers are intentionally reserved.

Example

```text
010 Document Numbering

015 Document Status Lifecycle

020 Document Template
```

If a closely related standard is introduced later, it may occupy an available number without requiring existing documents to be renamed.

---

# Companion References

Reference documents inherit the same document number as their corresponding Engineering Standard.

Example

```text
010-document-numbering-standard.md

010r-document-numbering-standard.md
```

The `r` suffix identifies the operational reference.

---

# Reading Order

Document numbers establish the recommended learning sequence.

Readers should generally begin with lower-numbered standards before progressing to higher-numbered standards.

Exceptions may exist when a document explicitly defines different prerequisites.

---

# Number Stability

Once published:

- document numbers should remain unchanged,
- references should continue pointing to the same identifier,
- superseded documents retain their original number for historical traceability.

Changing document numbers should be considered an exceptional event.

---

# Why Stable Numbering Matters

Stable numbering benefits both humans and AI.

It enables:

- predictable navigation,
- durable references,
- repository evolution,
- easier cross-linking,
- long-term engineering continuity.

The goal is for a document identifier to remain meaningful even as the documentation system grows.

---

# Relationship to Other Standards

This standard defines how Engineering Documentation Standards are identified.

Related Standards include:

- Documentation System Overview
- Documentation Levels
- Document Template
- Document Naming
- Document References

---

# Companion Reference

For quick implementation guidance, see:

**`010r-document-numbering-standard.md`**

---

## Metadata

| Field | Value |
|------|------|
| Document | `010-document-numbering-standard.md` |
| Category | Engineering Documentation System |
| Type | 📘 Engineering Standard |
| Companion | `010r-document-numbering-standard.md` |
| Version | 2.0 |
| Status | ✅ Accepted |
| As Of | 07.29.2026 |
| Owner | Engineering |