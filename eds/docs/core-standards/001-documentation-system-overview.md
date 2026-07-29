# 📘 Documentation System Overview

> **Engineering knowledge is preserved through understanding before implementation.**

---

# Purpose

Define the structure, philosophy, and organization of the Engineering Documentation System (EDS).

This document is the authoritative source for understanding how engineering documentation is organized, why the framework exists, and how the standards relate to one another.

For quick implementation guidance, refer to the companion reference document.

---

# Documentation Model

The Engineering Documentation System intentionally separates **learning** from **execution**.

```text
Engineering Documentation Standard

│

├── Standard
│       Explains
│       • What
│       • Why
│       • Philosophy
│       • Examples
│       • Rationale
│
└── Reference
        Summarizes
        • Rules
        • Checklists
        • Templates
        • Quick lookup
```

The Standard develops understanding.

The Reference supports implementation.

Together they create documentation that is both durable and practical.

---

# Engineering Standards

Every Engineering Documentation Standard consists of two companion documents.

## 📘 Standard

The Standard is the authoritative engineering document.

Its purpose is to explain the standard completely.

Characteristics

- Authoritative source
- Human-readable
- AI-readable
- Explains concepts
- Provides rationale
- May include examples
- Evolves alongside engineering practice

The Standard answers questions such as:

- What is this standard?
- Why does it exist?
- How should it be applied?
- What should engineers understand before using it?

---

## 📑 Reference

The Reference is the operational companion.

Its purpose is to support implementation with minimal reading.

Characteristics

- Quick lookup
- Implementation-focused
- AI-friendly
- Checklist-oriented
- Template-oriented
- Copy-and-use friendly

The Reference answers questions such as:

- What do I need to do?
- Which template should I use?
- What are the required rules?
- What should I copy into my project?

---

# Naming Convention

Every Engineering Standard follows a consistent naming pattern.

Engineering Standard

```text
001-documentation-system-overview.md
```

Companion Reference

```text
001r-documentation-system-overview.md
```

The `r` suffix identifies the operational reference associated with the Engineering Standard.

---

# Design Philosophy

Engineers do not always require the complete explanation during daily work.

Most of the time they need the rules.

However, engineering frameworks only remain sustainable when their rationale is preserved.

The Engineering Documentation System therefore keeps both:

- complete engineering knowledge (Standard)
- practical implementation guidance (Reference)

This separation encourages learning without slowing implementation.

---

# Relationship to Other Standards

This document provides the foundation for the remainder of the Engineering Documentation System.

Related Standards include:

- Documentation Levels
- Document Numbering
- Document Template
- Document Naming
- Document References
- Git Workflow

Each standard follows the same Standard + Reference structure.

---

# Companion Reference

For day-to-day implementation guidance, templates, and quick lookup, see:

**`001r-documentation-system-overview.md`**

---

## Metadata

| Field | Value |
|------|------|
| Document | `001-documentation-system-overview.md` |
| Category | Engineering Documentation System |
| Type | 📘 Engineering Standard |
| Companion | `001r-documentation-system-overview.md` |
| Version | 2.0 |
| Status | ✅ Accepted |
| As Of | 07.29.2026 |
| Owner | Engineering |