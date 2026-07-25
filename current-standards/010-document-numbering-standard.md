# 📘 Document Numbering Standard

---

## Metadata

**Document:** 010-document-numbering-standard.md

**Type:** 📘 Official Standard

**Companion Reference:** 010r-document-numbering-standard.md

**Owner:** Engineering

**Version:** 1.0

---

## Status

**As of:** 07.25.2026 07:10 PHT

✅ Accepted

---

# Purpose

Define the standard numbering convention used throughout the Engineering Documentation System.

Document numbering provides a predictable reading order, improves discoverability, and allows related documents to grow without requiring widespread renumbering.

---

# Standard

All engineering documents shall begin with a three-digit numeric prefix.

Example

```text
001-documentation-system-overview.md
005-documentation-level-standard.md
010-document-numbering-standard.md
```

The numeric prefix determines the recommended reading sequence.

Lower numbers introduce foundational concepts.

Higher numbers build upon earlier documents.

---

# Numbering Rules

* Use a three-digit numeric prefix.
* Increment numbers in logical groups.
* Reserve gaps between numbers for future expansion.
* Do not renumber existing published documents.
* Document numbers are permanent identifiers.

---

# Number Increments

The standard increment is **5**.

Example

```text
001
005
010
015
020
025
030
```

Using increments of five provides space for future standards without disrupting existing document numbers.

---

# Reserved Numbers

Unused numbers between standards are intentionally reserved.

Example

```text
010-document-numbering-standard.md

015-document-status-lifecycle.md

020-document-template-standard.md
```

If a closely related standard is added later, it may occupy an available number without requiring existing documents to be renamed.

---

# Companion Documents

Reference documents inherit the same document number.

Example

```text
010-document-numbering-standard.md
010r-document-numbering-standard.md
```

The `r` suffix identifies the companion Reference document.

---

# Reading Order

Document numbers define the recommended learning sequence.

Readers should generally begin with the lowest numbered document before progressing to higher numbered standards.

Exceptions may be made when a document explicitly states different prerequisites.

---

# Rules

* Every Official document shall have a unique document number.
* Reference documents shall reuse the same document number as their companion Official document.
* Document numbers shall not be reused for unrelated topics.
* Published document numbers should remain stable over time.
* Superseded documents retain their original number for historical traceability.

---

# Examples

```text
001-documentation-system-overview.md
001r-documentation-system-overview.md

005-documentation-level-standard.md
005r-documentation-level-standard.md

010-document-numbering-standard.md
010r-document-numbering-standard.md
```

---

# Related Documents

## Prerequisite

* 001-documentation-system-overview.md
* 005-documentation-level-standard.md

## Related

* 020-document-status-lifecycle.md
* 030-document-template-standard.md
* 040-document-naming-standard.md

## Companion

* 010r-document-numbering-standard.md
