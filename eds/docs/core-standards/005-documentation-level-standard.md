# 📘 Documentation Level Standard

> **Different documents serve different purposes. Separate learning from execution.**

---

# Purpose

Define the documentation levels used throughout the Engineering Documentation System (EDS).

Documentation levels ensure engineering knowledge remains easy to learn while also being efficient to apply during day-to-day engineering work.

The Engineering Documentation System intentionally separates **understanding** from **implementation**.

---

# Documentation Levels

EDS defines two complementary documentation levels.

```text
Engineering Standard

│

├── 📘 Standard
│       Learn
│
└── 📑 Reference
        Implement
```

Both documents describe the same engineering standard but serve different audiences and purposes.

---

# 📘 Engineering Standard

The Engineering Standard is the authoritative engineering document.

Its purpose is to explain the standard completely.

Characteristics

- Authoritative source
- Human-readable
- AI-readable
- Explains concepts
- Documents rationale
- May include examples
- Evolves with engineering practice

The Engineering Standard answers questions such as:

- What is this standard?
- Why does it exist?
- How should it be applied?
- What should engineers understand?

---

# 📑 Reference

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

# Rules

The Engineering Documentation System follows these principles:

- Every engineering standard shall have one authoritative Engineering Standard document.
- A Reference document may accompany the Engineering Standard.
- References summarize the standard but do not redefine it.
- References shall not introduce new engineering rules.
- If a conflict exists, the Engineering Standard always takes precedence.
- Some standards may not require a companion Reference when the Standard is already sufficiently concise.

---

# Naming Convention

Engineering Standard

```text
005-documentation-level-standard.md
```

Reference

```text
005r-documentation-level-standard.md
```

The `r` suffix identifies the companion operational reference.

---

# Why Two Levels?

Engineers have different needs depending on context.

When learning a framework:

- understanding is more important than speed.

When implementing a framework:

- speed is more important than explanation.

Separating Standards and References allows documentation to support both activities without compromising either.

---

# Relationship to Other Standards

This standard establishes how documentation itself is structured.

Related Standards include:

- Documentation System Overview
- Document Numbering
- Document Template
- Document Naming
- Document References

---

# Companion Reference

For quick implementation guidance, see:

**`005r-documentation-level-standard.md`**

---

## Metadata

| Field | Value |
|------|------|
| Document | `005-documentation-level-standard.md` |
| Category | Engineering Documentation System |
| Type | 📘 Engineering Standard |
| Companion | `005r-documentation-level-standard.md` |
| Version | 2.0 |
| Status | ✅ Accepted |
| As Of | 07.29.2026 |
| Owner | Engineering |