# 📖 Documentation Terminology Standard (Reference)

---

## Metadata

**Document:** `035r-terminology-standard.md`

**Type:** 📖 Reference

**Companion Standard:** [035-terminology-standard.md](./035-terminology-standard.md)

**Owner:** Engineering

**Version:** 1.0

---

## Status

**As of:** 07.25.2026 07:30 PHT

✅ Accepted

---

# Purpose

This document explains the philosophy, rationale, and evolution of the Documentation Terminology Standard.

Unlike the Official standard, this reference document provides guidance for maintaining a shared engineering language, bridging communication between technical and non-technical stakeholders, and ensuring terminology remains consistent across repositories and AI-assisted workflows.

---

# Why a Terminology Standard?

Engineering projects naturally develop their own vocabulary over time.

Different teams, business stakeholders, and software tools often describe the same concept using different words.

Without a shared terminology, documentation gradually becomes inconsistent, leading to misunderstandings, duplicated concepts, and unnecessary translation between teams.

The Terminology Standard establishes a common language that allows documentation to remain clear, predictable, and maintainable over many years.

---

# Design Goals

The Terminology Standard was designed to:

- Establish a common engineering vocabulary.
- Reduce ambiguity across documentation.
- Improve communication between business and engineering teams.
- Support AI-assisted development with consistent terminology.
- Make documentation easier to search and maintain.
- Preserve historical terminology while defining preferred terms.

---

# Multiple Audiences

Engineering documentation is read by many different audiences.

These include:

- Software engineers
- Architects
- Project managers
- Business analysts
- Product owners
- Technical writers
- Future maintainers
- AI assistants

Each audience may interpret the same word differently.

The terminology standard provides a common reference that minimizes these differences.

---

# Business Language vs Engineering Language

Business users and engineers often describe the same concept using different terminology.

For example:

| Business | Engineering |
|----------|-------------|
| Feature | Capability |
| Screen | Page / View |
| Customer | User |
| Request | Requirement |
| Problem | Defect / Bug |

Neither vocabulary is inherently correct.

Documentation should acknowledge both perspectives while clearly identifying the preferred engineering terminology.

This approach allows documentation to remain accessible without sacrificing technical precision.

---

# Preferred Terminology

The Engineering Documentation System intentionally selects one preferred term whenever multiple commonly used terms exist.

For example:

```text
Official
    instead of
Canonical
```

This decision reflects readability rather than technical correctness.

"Official" is generally easier to understand for engineers, business stakeholders, and new contributors.

The engineering term "Canonical" remains valid and may appear in technical discussions, academic literature, or external tools.

---

# Canonical vs Official

One of the earliest terminology decisions in the documentation system was replacing the user-facing term **Canonical** with **Official**.

The reasons included:

- easier for non-engineers to understand
- more intuitive for new contributors
- simpler AI prompts
- reduced need for explanation

However, "Canonical" remains part of the engineering vocabulary and is documented as an equivalent term rather than being eliminated.

This preserves compatibility with existing engineering literature while improving the readability of the documentation system.

---

# A Living Vocabulary

Terminology should evolve as the documentation framework matures.

When introducing new terminology:

- define it before widespread adoption
- avoid creating synonyms unnecessarily
- document deprecated terminology
- update the Terminology Standard before updating multiple repositories

This keeps terminology changes deliberate rather than accidental.

---

# Project-Specific Terminology

Projects may define additional terminology when needed.

Examples include:

- domain-specific business concepts
- product-specific terminology
- industry abbreviations
- internal acronyms

Project-specific terminology should supplement, not replace, the Engineering Documentation System terminology.

Whenever possible, project glossaries should reference this standard rather than redefining common engineering terms.

---

# AI-Assisted Engineering

Consistent terminology significantly improves AI-assisted development.

Stable terminology helps AI systems:

- interpret documentation consistently
- generate reusable documents
- understand project context
- reduce conflicting terminology across conversations
- produce more predictable responses

The concise Official standard serves as efficient AI context, while this reference document provides the additional background needed for long-term understanding.

---

# Future Evolution

The terminology framework is expected to grow alongside the documentation system.

Possible future additions include:

- engineering glossary generation
- business-to-engineering terminology mapping
- domain-specific vocabulary packages
- multilingual terminology support
- AI terminology validation
- repository-wide terminology consistency checks

These enhancements should extend the terminology framework without changing its core principles.

---

# Frequently Asked Questions

### Why not allow teams to use whatever terminology they prefer?

Teams may develop local terminology, but shared engineering documentation benefits from a common language.

Standard terminology improves consistency, onboarding, and cross-project collaboration.

---

### Can business terminology appear in engineering documentation?

Yes.

Business terminology should be recognized when it improves communication, especially when collaborating with non-technical stakeholders.

When different terms describe the same concept, the preferred engineering term should also be identified.

---

### Should historical documents be updated when terminology changes?

Not necessarily.

Historical documents should generally remain unchanged unless corrections are required.

New documents should adopt the current terminology standard.

---

### Is "Canonical" incorrect?

No.

"Canonical" is an established engineering term.

Within this documentation framework, **Official** is simply the preferred user-facing term because it is easier for a broader audience to understand.

---

### Who approves new terminology?

New terminology should be reviewed as part of the documentation standards process before becoming the preferred term across repositories.

---

# Lessons Learned

Several terminology decisions were made while developing this documentation framework.

Key lessons include:

- Familiar language is often more effective than technically precise language.
- Consistency is more valuable than perfect wording.
- One preferred term reduces ambiguity.
- Documentation should be understandable by both engineers and business users.
- AI-assisted workflows benefit from stable, well-defined terminology.

---

# Related Documents

## Prerequisites

- [001-documentation-system-overview.md](./001-documentation-system-overview.md)
- [005-documentation-level-standard.md](./005-documentation-level-standard.md)

## Related

- [020-document-template-standard.md](./020-document-template-standard.md)
- [025-document-naming-standard.md](./025-document-naming-standard.md)
- [030-document-icons-and-statuses-standard.md](./030-document-icons-and-statuses-standard.md)

## Companion

- [035-terminology-standard.md](./035-terminology-standard.md)