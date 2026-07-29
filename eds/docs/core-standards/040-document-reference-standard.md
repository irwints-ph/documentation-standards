# 📘 Document Reference Standard

> **Knowledge grows through connections, not duplication.**

---

# Purpose

Define the standard for creating relationships between engineering documents.

Consistent references transform documentation from isolated files into a connected engineering knowledge system that is easier to navigate, maintain, and evolve.

---

# Goals

The Engineering Documentation System reference model shall:

- Reduce duplicated information.
- Encourage reuse of existing standards.
- Keep documents focused on a single responsibility.
- Make navigation predictable.
- Support future documentation automation.

---

# Standard

Engineering documents should contain only the information necessary for their intended purpose.

When additional information already exists elsewhere, reference the appropriate document instead of duplicating its contents.

Good documentation is connected.

Not repeated.

---

# Reference Types

## Required Reading

Documents that should be understood before reading the current document.

Example

- 005 Documentation Level Standard
- 020 Document Template Standard

---

## Related Documents

Documents that complement or expand the current topic.

Example

- 025 Document Naming Standard
- 035 Documentation Terminology Standard

---

## Implements

Engineering documents or project artifacts that implement this standard.

Example

- Frontend Documentation Guide
- Backend Documentation Guide

---

## External References

Authoritative resources maintained outside the Engineering Documentation System.

Examples include:

- Python Documentation
- React Documentation
- RFC Documents
- Microsoft Documentation

---

## Supersedes

Identifies previous guidance replaced by the current document.

---

## Superseded By

Identifies the document that replaces the current guidance.

---

## Parent Document

Identifies the higher-level document from which this document derives.

Example

- 001 Documentation System Overview

---

## Child Documents

Documents that expand upon this standard.

Example

- 040a Examples
- 040b Best Practices
- 040c Frequently Asked Questions

---

# Reference Format

Within document text, references should use the document number followed by the document title.

Example

- 040 Document Reference Standard
- 025 Document Naming Standard
- 035 Documentation Terminology Standard

Avoid referring to filenames within explanatory text.

---

# File References

Filenames should only be used when creating hyperlinks.

Example

```markdown
[040 Document Reference Standard](040-document-reference-standard.md)
```

Avoid writing:

> See `040-document-reference-standard.md`.

Instead write:

> See **040 Document Reference Standard**.

---

# Avoid Circular References

Document relationships should remain hierarchical whenever possible.

Good

```text
001
 ├──020
 └──025
```

Avoid

```text
020 → 025 → 020
```

---

# Avoid Duplicate Content

Do not copy guidance already maintained elsewhere.

Instead, reference the authoritative source.

Instead of repeating naming rules, write:

> See **025 Document Naming Standard**.

---

# Reference Placement

Document references should appear near the end of a document.

Recommended order:

1. Required Reading
2. Related Documents
3. Implements
4. External References

---

# Future Automation

A standardized reference model enables future tooling to generate:

- documentation dependency graphs,
- knowledge maps,
- backlinks,
- broken reference reports,
- impact analysis,
- navigation aids,

without modifying existing documentation.

---

# Engineering Philosophy

Engineering knowledge should behave like a network rather than a collection of isolated documents.

Each document should contribute one idea while clearly pointing readers toward related knowledge.

References preserve context without introducing duplication.

---

# Related Documents

## Prerequisites

- 001 Documentation System Overview
- 005 Documentation Level Standard

---

## Related

- 020 Document Template Standard
- 025 Document Naming Standard
- 035 Documentation Terminology Standard

---

## Companion

- 040r-document-reference-standard.md
- 040a-document-reference-cheat-sheet.md *(if applicable)*

---

## Metadata

| Field | Value |
|--------|-------|
| Document | `040-document-reference-standard.md` |
| Category | Core Standards |
| Type | 📘 Standard |
| Companion Reference | `040r-document-reference-standard.md` |
| Companion Quick Reference | `040a-document-reference-cheat-sheet.md` *(optional)* |
| Status | 📦 Official *(or ✅ Accepted while under validation)* |
| Version | 2.0 |
| As Of | 07.29.2026 09:28 PHT |