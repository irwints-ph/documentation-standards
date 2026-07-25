# 📖 Document Icons and Statuses Reference

---

## Metadata

**Document:** `030r-document-icons-and-statuses-standard.md`

**Type:** 📖 Reference

**Companion Standard:** [030-document-icons-and-statuses-standard.md](./030-document-icons-and-statuses-standard.md)

**Owner:** Engineering

**Version:** 1.0

---

## Status

**As of:** 07.25.2026 07:10 PHT

✅ Accepted

---

# Purpose

This document explains the philosophy, design decisions, and evolution of the **Document Icons and Statuses Standard**.

Unlike the companion standard, this reference document provides the reasoning behind the icon and status system, recommended usage patterns, and guidance for extending the visual language while maintaining consistency.

---

# Why Use Icons and Statuses?

As documentation grows, readers often need to identify both a document's purpose and its maturity before reading its contents.

Document Type icons provide immediate visual recognition, while Status icons communicate a document's current lifecycle stage.

Together they improve navigation without replacing descriptive document titles.

---

# Design Goals

The Document Icons and Statuses Standard was designed with the following objectives:

* Improve document recognition.
* Make documentation easier to scan.
* Clearly communicate document maturity.
* Reduce the time required to locate information.
* Encourage consistent documentation across repositories.
* Provide recognizable visual cues for both humans and AI-assisted workflows.
* Keep the visual language simple and easy to maintain.

---

# Two Icon Categories

The Engineering Documentation System intentionally separates icons into two categories.

## Document Type Icons

Document Type icons identify the primary purpose of a document.

Examples include:

* Standard
* Architecture
* Session
* Procedure
* Knowledge
* Roadmap

Every document should have exactly one Document Type icon.

---

## Document Status Icons

Status icons represent a document's current lifecycle stage.

Examples include:

* Planning
* In Progress
* Under Review
* Accepted
* Official
* Archived

Status icons may change throughout the life of a document, while the Document Type icon normally remains unchanged.

---

# Why Separate Type and Status?

A document's purpose rarely changes.

Its lifecycle, however, changes as the document matures.

For example:

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

Separating these concepts allows readers to immediately understand both **what** a document is and **how mature** it is.

---

# Why Only One Document Type?

Some documents could reasonably belong to multiple categories.

For example:

* A roadmap containing architecture ideas.
* A procedure that includes troubleshooting information.
* A knowledge article containing design recommendations.

Allowing multiple Document Type icons would reduce consistency and make documentation more difficult to scan.

The standard therefore assigns one primary Document Type to every document.

Additional context should be conveyed through the document title, metadata, folder structure, and related document links.

---

# Why Standardize Icons?

Without a shared standard, repositories naturally accumulate inconsistent visual conventions.

Examples include:

```text
📚 Standard
📘 Standard
📖 Standard
📄 Standard
```

Although each choice may seem reasonable, inconsistent icon usage makes repositories more difficult to navigate.

A standardized icon set establishes a consistent visual language across engineering projects.

---

# Choosing New Icons

New icons should be introduced only when they represent a meaningful document category expected to be reused across multiple repositories.

When selecting an icon:

* Prefer widely recognized symbols.
* Choose icons with clear meaning.
* Avoid visually similar alternatives.
* Avoid duplicate meanings.
* Keep the overall icon set manageable.

The goal is consistency rather than completeness.

---

# The Role of the Cheatsheet

The companion cheatsheet serves a different purpose from the standard.

The standard defines the rules.

The cheatsheet provides quick copy/paste references for everyday documentation work.

Separating the two keeps the standard concise while providing a practical reference for document authors.

---

# Future Evolution

The visual language is expected to evolve gradually.

Possible future additions include:

* AI documentation
* Security documentation
* Performance analysis
* Testing documentation
* API documentation
* Operations documentation

New icons should be introduced only after demonstrating lasting value across multiple engineering projects.

---

# Frequently Asked Questions

### Why not use colors instead of icons?

Colors are not consistently displayed across all tools and themes.

Icons remain recognizable in terminals, editors, Git repositories, and documentation viewers.

---

### Can projects define their own icons?

Projects may introduce temporary icons for experimentation.

However, engineering documentation should use only the standardized icon set.

---

### Should every heading use icons?

No.

Icons are intended primarily for document identification.

Using icons excessively within document bodies reduces their effectiveness.

---

### Why maintain both a standard and a cheatsheet?

The standard defines the rules.

The cheatsheet provides a practical reference for document authors.

Separating the two keeps each document focused on its intended audience.

---

# Related Documents

## Prerequisites

* [001-documentation-system-overview.md](./001-documentation-system-overview.md)
* [005-documentation-level-standard.md](./005-documentation-level-standard.md)

## Related

* [015-document-status-lifecycle.md](./015-document-status-lifecycle.md)
* [020-document-template-standard.md](./020-document-template-standard.md)

## Companion

* [030-document-icons-and-statuses-standard.md](./030-document-icons-and-statuses-standard.md)
* [030a-document-icons-and-statuses-cheatsheet.md](./030a-document-icons-and-statuses-cheatsheet.md)
