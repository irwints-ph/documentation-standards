# 📖 Document Icon Standard (Reference)

---

## Metadata

**Document:** 030r-document-icon-standard.md

**Type:** 📖 Reference

**Companion Standard:** 030-document-icon-standard.md

**Owner:** Engineering

**Version:** 1.0

---

## Status

**As of:** 07.25.2026 07:10 PHT

✅ Accepted

---

# Purpose

This document explains the philosophy, design decisions, and evolution of the Document Icon Standard.

Unlike the Official standard, this reference document provides the reasoning behind the icon system, recommended usage patterns, and guidance for extending the icon set while maintaining consistency.

---

# Why Use Icons?

As documentation grows, readers often need to identify a document's purpose before reading its contents.

Icons provide immediate visual recognition, allowing engineers to quickly distinguish between standards, architecture documents, procedures, roadmaps, session histories, and other document types.

The icon system is intended to improve navigation without replacing descriptive document titles.

---

# Design Goals

The Document Icon Standard was designed with the following objectives:

- Improve document recognition.
- Make documentation easier to scan.
- Reduce the time required to locate information.
- Encourage consistent documentation across repositories.
- Provide recognizable visual cues for both humans and AI-assisted workflows.
- Keep the icon system simple and easy to maintain.

---

# Two Icon Categories

The icon system is intentionally divided into two independent categories.

## Document Type

The Document Type icon identifies the purpose of a document.

Examples include:

- Standard
- Architecture
- Session
- Procedure
- Knowledge
- Roadmap

A document should have exactly one primary Document Type.

---

## Document Status

The Status icon represents the document's current position within its lifecycle.

Examples include:

- Planning
- In Progress
- Under Review
- Accepted
- Official
- Archived

Status icons may change throughout the life of a document, while the Document Type icon normally remains unchanged.

---

# Why Separate Type and Status?

A document's purpose rarely changes.

Its lifecycle, however, changes frequently.

For example:

```text
📘 Standard

Planning
    ↓
In Progress
    ↓
Under Review
    ↓
Accepted
    ↓
Official
```

Separating these concepts prevents confusion and allows readers to immediately understand both what a document is and where it is in its lifecycle.

---

# Why Only One Document Type?

Some documents could reasonably belong to multiple categories.

For example:

- A roadmap containing architecture ideas.
- A procedure that includes troubleshooting information.
- A knowledge article containing design recommendations.

Allowing multiple Document Type icons would quickly reduce consistency and make visual scanning less effective.

The standard therefore assigns one primary purpose to every document.

Additional context should be conveyed through the document title, folder location, metadata, and related document links.

---

# Why Standardize Icons?

Without a shared standard, repositories tend to accumulate inconsistent symbols over time.

Examples include:

```text
📚 Standard
📘 Standard
📖 Standard
📄 Standard
```

Although individually reasonable, inconsistent choices make repositories more difficult to navigate.

The standardized icon list ensures a consistent visual language across all projects.

---

# Choosing New Icons

New icons should be added only when they represent a meaningful document category that is expected to be reused across multiple repositories.

When selecting an icon:

- Prefer widely recognized symbols.
- Choose icons with clear meaning.
- Avoid visually similar alternatives.
- Avoid duplicate meanings.
- Keep the total number of icons manageable.

The goal is consistency rather than completeness.

---

# The Role of the Cheatsheet

The companion cheatsheet serves a different purpose from the standard.

The standard defines the rules.

The cheatsheet provides quick copy/paste references for daily documentation work.

This separation keeps the Official standard concise while providing a practical reference for authors.

---

# Future Evolution

The icon system is expected to evolve gradually.

Possible future additions include:

- AI-related documents
- Security documentation
- Performance analysis
- Testing documentation
- API documentation
- Operations documentation

New icons should be introduced only after they demonstrate lasting value across multiple projects.

---

# Frequently Asked Questions

### Why not use colors instead of icons?

Colors are not consistently displayed across all tools and themes.

Icons remain recognizable in terminals, editors, Git repositories, and documentation viewers.

---

### Can projects define their own icons?

Projects may introduce temporary icons for internal experimentation.

However, Official engineering documentation should use only the standardized icon set.

---

### Should every heading use icons?

No.

Icons are intended primarily for document identification.

Using icons excessively within document bodies reduces their effectiveness.

---

### Why maintain both a standard and a cheatsheet?

The standard defines the rules.

The cheatsheet provides a practical reference for authors.

Separating the two keeps each document focused on its intended audience.

---

# Related Documents

## Prerequisites

- 001-documentation-system-overview.md
- 005-documentation-level-standard.md

## Related

- 015-document-status-lifecycle.md
- 020-document-template-standard.md

## Companion

- 030-document-icon-standard.md
- 030a-document-icon-cheatsheet.md