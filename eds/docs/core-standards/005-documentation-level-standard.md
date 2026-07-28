# 📘 Documentation Level Standard

---

## Metadata

**Document:** `005-documentation-level-standard.md`

**Type:** 📘 Official Standard

**Companion Reference:** [005r-documentation-level-standard.md](./005r-documentation-level-standard.md)

**Owner:** Engineering

**Version:** 1.0

---

## Status

**As of:** 07.25.2026 06:45 PHT

✅ Accepted

---

# Purpose

Define the standard documentation levels used throughout the Engineering Documentation System.

Documentation levels organize information according to its intended purpose, ensuring standards remain concise while supporting detailed reference material.

---

# Standard

The Engineering Documentation System defines two documentation levels.

## Level 1 — Official

Official documents define the current engineering standard.

Characteristics

* Concise and implementation-focused
* AI optimized
* Human quick reference
* Readable in under 30 seconds
* Contains only the current standard
* May be used directly as AI project context

Official documents answer:

* What is the standard?
* How should it be implemented?
* Where can additional information be found?

---

## Level 2 — Reference

Reference documents provide supporting information for an Official document.

Characteristics

* Human optimized
* No practical length limit
* Explains rationale and historical context
* Includes examples and implementation guidance
* Supplements, but never replaces, the Official document

Reference documents answer:

* Why was this standard created?
* How did it evolve?
* What alternatives were considered?
* What implementation patterns are recommended?

---

# Rules

* Every engineering standard shall be defined only in an Official document.
* A Reference document may accompany an Official document when additional explanation provides long-term value.
* Reference documents shall not introduce or modify engineering standards.
* If a conflict exists, the Official document always takes precedence.
* Some Official documents may not require a companion Reference document.

---

# Naming Convention

Official document

```text
005-documentation-level-standard.md
```

Reference document

```text
005r-documentation-level-standard.md
```

The `r` suffix identifies the companion Reference document.

---

# Related Documents

## Prerequisite

* [001-documentation-system-overview.md](./001-documentation-system-overview.md)

## Related

* [010-document-numbering-standard.md](./010-document-numbering-standard.md)
* [015-document-status-lifecycle.md](./015-document-status-lifecycle.md)
* [020-document-template-standard.md](./020-document-template-standard.md)
* [025-document-naming-standard.md](./025-document-naming-standard.md)

## Companion

* [005r-documentation-level-standard.md](./005r-documentation-level-standard.md)
