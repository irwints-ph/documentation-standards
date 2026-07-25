# 📘 Document Reference Standard

---

## Metadata

**Document:** `040-document-reference-standard.md`

**Type:** 📘 Canonical Standard

**Companion Reference:** [040r-document-reference-standard.md](./040r-document-reference-standard.md)

**Owner:** Engineering

**Version:** 1.0

---

## Status

**As of:** 07.25.2026 07:20 PHT

✅ Accepted

---

## Purpose

Define the standard for referencing related engineering documents.

Consistent document references improve navigation, reduce duplication, and establish relationships between engineering standards.

---

# Standard

Every engineering document shall include a **Related Documents** section.

The section identifies documents that are directly related to the current document.

Reference documents instead of duplicating their content.

---

# Reference Types

## Related

Documents closely associated with the current document.

## Companion

The matching Reference document for a Canonical standard.

## Parent

The higher-level document from which the current document derives.

## Children

Documents that extend or specialize the current document.

---

# Reference Format

Use repository-relative Markdown links.

Example

```md
- 010-document-numbering-standard.md
```

Reference documents by filename only.

Avoid inline URLs unless referencing external resources.

---

# Related Documents

## Related

- [001-documentation-system-overview.md](./001-documentation-system-overview.md)
- [025-document-naming-standard.md](./025-document-naming-standard.md)

## Companion

- [040r-document-reference-standard.md](./040r-document-reference-standard.md)