# 📑 Document Numbering Standard — Reference

> **Quick guide for numbering Engineering Documentation System documents.**

---

# Purpose

Provide a concise operational reference for assigning and maintaining document numbers within the Engineering Documentation System (EDS).

For the complete rationale and philosophy, see:

**`010-document-numbering-standard.md`**

---

# Quick Rules

✅ Every Engineering Standard receives a unique three-digit number.

✅ Use increments of **5**.

✅ Document numbers are permanent identifiers.

✅ Never renumber published standards.

✅ Companion References inherit the same number with the `r` suffix.

---

# Standard Format

Engineering Standard

```text
001-documentation-system-overview.md
```

Reference

```text
001r-documentation-system-overview.md
```

---

# Number Sequence

Recommended numbering:

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
050
```

Leave unused numbers available for future expansion.

---

# Reserved Numbers

Unused numbers are intentional.

Example

```text
010 Document Numbering

015 Document Status Lifecycle

020 Document Template
```

This allows related standards to be inserted later without renumbering existing documents.

---

# Companion Documents

References always inherit the same number.

Example

```text
020-document-template-standard.md

020r-document-template-standard.md
```

The suffix identifies the companion operational reference.

---

# Reading Order

Follow document numbers when learning EDS.

```text
001

↓

005

↓

010

↓

015

↓

020

↓

...
```

Lower numbers introduce foundational concepts.

Higher numbers build upon previous standards.

---

# Checklist

Before publishing a new standard:

- ☐ Assign the next available document number.
- ☐ Use a three-digit prefix.
- ☐ Leave numbering gaps when appropriate.
- ☐ Create the companion Reference if required.
- ☐ Do not renumber existing standards.

---

# Examples

```text
001-documentation-system-overview.md
001r-documentation-system-overview.md

005-documentation-level-standard.md
005r-documentation-level-standard.md

010-document-numbering-standard.md
010r-document-numbering-standard.md

020-document-template-standard.md
020r-document-template-standard.md
```

---

# Related Standards

Core Standards

- `001` Documentation System Overview
- `005` Documentation Levels
- `015` Document Status Lifecycle
- `020` Document Template
- `025` Document Naming

---

# Companion Standard

For the complete explanation and design philosophy, see:

**`010-document-numbering-standard.md`**

---

## Metadata

| Field | Value |
|------|------|
| Document | `010r-document-numbering-standard.md` |
| Category | Engineering Documentation System |
| Type | 📑 Reference |
| Companion | `010-document-numbering-standard.md` |
| Version | 2.0 |
| Status | ✅ Accepted |
| As Of | 07.29.2026 |
| Owner | Engineering |