# 📖 Document Icons and Statuses Reference

---

## Metadata

| Field | Value |
|--------|-------|
| Document | `030r-document-icons-and-statuses-standard.md` |
| Category | Core Standards |
| Type | Reference |
| Status | ✅ Accepted |
| Companion | `030-document-icons-and-statuses-standard.md` |
| Version | 1.1 |

---

# Purpose

This document explains the philosophy, design decisions, and evolution of the **Document Icons and Statuses Standard**.

While the companion standard defines the engineering rules, this reference explains why the visual language exists, how it evolved, and how it should continue to grow alongside the Engineering Documentation System (EDS).

---

# Background

As engineering documentation grows, navigating information becomes increasingly important.

Before reading a document, engineers typically want to answer two questions:

1. **What kind of document is this?**
2. **How mature or trustworthy is it?**

The Engineering Documentation System answers these questions visually.

Every document communicates:

- its purpose through a **Document Icon**
- its maturity through a **Lifecycle Status**

This allows engineers to quickly understand documentation before reading its contents.

---

# Design Philosophy

The visual language of EDS follows a simple principle:

> **Icons improve recognition—not decoration.**

Icons exist to reduce cognitive effort.

They should help engineers recognize documentation categories immediately while remaining simple, consistent, and reusable.

---

# Two Independent Concepts

The Engineering Documentation System intentionally separates:

## Document Purpose

Represented by the **Document Icon**.

Examples include:

- 📘 Standard
- 📖 Reference
- 📍 WWAN
- 🗺️ Roadmap
- 🛠️ Procedure
- 🏛️ Architecture Finding

The icon answers:

> **What is this document?**

---

## Document Lifecycle

Represented by the **Status Icon**.

Examples include:

- 📝 Planning
- 🚧 In Progress
- 👀 Under Review
- 🧪 Experimental
- ✅ Accepted
- 📦 Official
- 🗃️ Archived

The status answers:

> **How mature is this document?**

---

# Why Separate Purpose and Status?

A document's purpose rarely changes.

Its lifecycle naturally evolves.

Example:

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

Separating these concepts allows readers to understand both the document category and its maturity without reading the document itself.

---

# Why One Primary Document Icon?

Some documents could reasonably belong to multiple categories.

For example:

- A roadmap containing architecture ideas.
- A procedure containing troubleshooting.
- A discovery report documenting an API.

Assigning multiple document icons reduces consistency and increases visual noise.

Instead, every document identifies its **primary engineering purpose**.

Additional context should be communicated through:

- document title
- metadata
- folder structure
- related documents

---

# Evolution of the Visual Language

The original Engineering Documentation System primarily consisted of:

- Standards
- References
- Procedures
- Roadmaps

As the framework matured through real engineering projects, additional document types naturally emerged.

Examples include:

- WWAN (Where We Are Now)
- Folder Registries
- Folder Validation
- Component Documentation
- Architecture Findings
- Discovery Documentation

Rather than inventing icons in advance, the visual language continues to evolve through practical engineering use.

This reflects a broader EDS philosophy:

> Standards evolve through validated engineering practice.

---

# Relationship to Metadata

Earlier versions of the documentation framework placed lifecycle status in a dedicated **Status** section.

As the framework matured, status became part of the standardized Metadata table.

Example:

```markdown
## Metadata

| Field | Value |
|--------|-------|
| Status | 🚧 Discovery In Progress |
```

This keeps operational information together while making documents easier to scan.

---

# Relationship to the Document Template

This document defines **which icons** should be used.

The Document Template Standard defines **where they appear**.

Responsibilities remain intentionally separated.

- Document Template Standard → document structure
- Document Icons Standard → visual language
- Document Lifecycle Standard → lifecycle rules

---

# Relationship to Discovery

The Frontend Discovery project demonstrated that visual consistency becomes increasingly valuable as documentation expands.

Document icons now help engineers distinguish between:

- operational documents
- engineering standards
- discovery artifacts
- reusable knowledge
- architecture observations

without relying solely on filenames.

---

# The Role of the Cheatsheet

The companion Cheatsheet serves a different audience.

The Standard defines engineering rules.

The Cheatsheet provides quick copy-and-paste references for engineers producing documentation.

Keeping them separate allows each document to remain focused.

---

# Future Evolution

The visual language should continue evolving conservatively.

Potential future categories may include:

- Security Reviews
- Performance Analysis
- Testing Documentation
- Operational Runbooks
- Engineering Playbooks
- Knowledge Packages

New icons should only be introduced after repeated use demonstrates that they represent a reusable engineering concept.

---

# Frequently Asked Questions

## Why not rely on colors?

Colors vary across editors, terminals, themes, and documentation viewers.

Icons remain recognizable regardless of presentation.

---

## Why not allow project-specific icons?

Project-specific icons reduce consistency between repositories.

The Engineering Documentation System encourages one shared visual language.

---

## Should every heading contain icons?

No.

Icons are primarily intended for document identification.

Using icons excessively reduces their usefulness.

---

## Why maintain both a Standard and a Cheatsheet?

The Standard explains the engineering rules.

The Cheatsheet supports everyday engineering work.

Separating them keeps both concise and easy to maintain.

---

# Engineering Philosophy

The visual language of the Engineering Documentation System is intentionally minimal.

Icons should never compete with content.

They should quietly help engineers navigate knowledge while allowing the documentation itself to remain the primary source of understanding.

Like the documentation framework itself, the icon system exists to reduce friction rather than create it.

---

# Related Documents

## Prerequisites

- [001-documentation-system-overview.md](./001-documentation-system-overview.md)
- [020-document-template-standard.md](./020-document-template-standard.md)

## Related

- [015-document-status-lifecycle.md](./015-document-status-lifecycle.md)

## Companion

- [030-document-icons-and-statuses-standard.md](./030-document-icons-and-statuses-standard.md)
- [030a-document-icons-and-statuses-cheatsheet.md](./030a-document-icons-and-statuses-cheatsheet.md)