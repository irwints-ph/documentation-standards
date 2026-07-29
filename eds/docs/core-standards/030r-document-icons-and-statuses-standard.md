# 📖 Document Icons and Statuses Reference

> **Visual consistency reduces cognitive load and helps engineers recognize information before they read it.**

---

# Purpose

This document explains the philosophy, rationale, and evolution of the Engineering Documentation System's visual language.

While the companion Standard defines **what icons and statuses shall be used**, this Reference explains **why** the visual language exists, how it evolved, and the principles that guide its continued growth.

---

# Background

As engineering documentation grows, navigation becomes increasingly important.

Before opening a document, engineers typically want to answer two questions:

1. **What kind of document is this?**
2. **How mature or trustworthy is it?**

The Engineering Documentation System answers these questions visually.

Every document communicates:

- its **purpose** through a Document Icon
- its **maturity** through a Lifecycle Status

This allows engineers to quickly understand documentation before reading its contents.

---

# Design Philosophy

The visual language follows a simple principle:

> **Icons improve recognition—not decoration.**

Icons exist to reduce cognitive effort.

They should quietly help engineers recognize documentation categories while allowing the content itself to remain the primary source of understanding.

---

# Two Independent Concepts

The Engineering Documentation System intentionally separates two ideas.

## Document Purpose

Represented by the **Document Icon**.

The icon answers:

> **"What is this document?"**

Examples include:

- 📘 Standard
- 📖 Reference
- 📍 WWAN
- 🗺️ Roadmap
- 🛠️ Procedure
- 🏛️ Architecture Finding

Document purpose rarely changes.

---

## Document Lifecycle

Represented by the **Lifecycle Status**.

The status answers:

> **"How mature is this document?"**

Examples include:

- 📝 Planning
- 🚧 In Progress
- 👀 Under Review
- ✅ Accepted
- 📦 Official
- 🗃️ Archived

Document maturity naturally evolves over time.

---

# Why Separate Purpose and Status?

A document's purpose usually remains constant throughout its lifetime.

Its maturity changes as engineering work progresses.

```text
📘 Standard

📝 Planning
      ↓
🚧 In Progress
      ↓
👀 Under Review
      ↓
✅ Accepted
      ↓
📦 Official
```

Separating these concepts allows engineers to immediately understand both **what the document is** and **how much confidence they should place in it**.

---

# Why One Primary Document Icon?

Many documents could reasonably fit into multiple categories.

For example:

- a roadmap discussing architecture,
- a procedure containing troubleshooting guidance,
- a discovery report documenting APIs.

Assigning multiple document-purpose icons creates inconsistency and visual noise.

Instead, every document identifies its **primary engineering purpose**.

Additional context should be communicated through:

- the document title,
- metadata,
- folder organization,
- related documents.

---

# Evolution of the Visual Language

The Engineering Documentation System originally consisted of only a few document types:

- Standards
- References
- Procedures
- Roadmaps

As real engineering work accumulated, new reusable document categories naturally emerged.

Examples include:

- WWAN
- Folder Registries
- Folder Validation
- Component Documentation
- Architecture Findings
- Discovery Documentation
- Knowledge Packages

Rather than designing an exhaustive taxonomy up front, the visual language continues to evolve through practical engineering experience.

This reflects a broader EDS principle:

> **Standards evolve through validated engineering practice.**

---

# Relationship to the Document Template

The Engineering Documentation System intentionally separates responsibilities.

| Standard | Responsibility |
|-----------|----------------|
| 020 | Defines document structure |
| 015 | Defines lifecycle states |
| 030 | Defines the visual language |

This separation keeps each standard focused and easier to maintain.

---

# Three-Document Model

The Document Icons and Statuses Standard follows the Engineering Documentation System's three-document model.

## 📘 Standard

Defines the engineering rules.

Answers:

- Which icons are approved?
- How should they be used?

---

## 📖 Reference *(this document)*

Explains the engineering reasoning.

Answers:

- Why were these icons chosen?
- How did the system evolve?
- What design principles guide future additions?

---

## 📋 Quick Reference

Provides fast day-to-day lookup.

Supports engineers during documentation work without requiring them to read the full standard.

---

# Discovery and Real-World Validation

The current icon system emerged through practical use across engineering activities, including:

- legacy application discovery,
- frontend documentation,
- architecture reviews,
- engineering standards development,
- AFK methodology,
- Engineering Knowledge System research.

Every newly introduced document category was validated through repeated engineering use before becoming part of the standard.

---

# Future Evolution

The visual language should continue evolving conservatively.

Potential future document categories include:

- Security Reviews
- Performance Analysis
- Operational Runbooks
- Engineering Playbooks
- Decision Records

New icons should only be introduced after repeated evidence demonstrates that they represent a reusable engineering concept rather than a project-specific need.

---

# Frequently Asked Questions

## Why not rely on colors?

Colors vary across editors, terminals, documentation generators, and accessibility settings.

Icons remain recognizable regardless of presentation.

---

## Why not allow project-specific icons?

Project-specific icons reduce consistency between repositories.

The Engineering Documentation System promotes one shared visual language across projects.

---

## Why not use multiple icons?

Every document should communicate one primary purpose.

Multiple icons dilute meaning and reduce recognition speed.

---

## Why maintain both a Reference and a Quick Reference?

They serve different purposes.

The Reference explains the reasoning.

The Quick Reference supports everyday execution.

Keeping them separate makes both more effective.

---

# Engineering Philosophy

Good documentation should reduce friction.

The icon system exists to make engineering knowledge easier to navigate—not to decorate documents.

Like every Engineering Documentation System standard, the visual language should quietly improve understanding while remaining almost invisible during everyday engineering work.

---

# Related Documents

## Standard

- 030-document-icons-and-statuses-standard.md

---

## Quick Reference

- 030a-document-icons-and-statuses-cheatsheet.md

---

## Related

- 015-document-status-lifecycle.md
- 020-document-template-standard.md
- 025-document-naming-standard.md

---

## Metadata

| Field | Value |
|--------|-------|
| Document | `030r-document-icons-and-statuses-standard.md` |
| Category | Core Standards |
| Type | 📖 Reference |
| Companion Standard | `030-document-icons-and-statuses-standard.md` |
| Quick Reference | `030a-document-icons-and-statuses-cheatsheet.md` |
| Status | 📦 Official *(or ✅ Accepted)* |
| Version | 2.0 |
| As Of | YYYY-MM-DD HH:MM TZ |