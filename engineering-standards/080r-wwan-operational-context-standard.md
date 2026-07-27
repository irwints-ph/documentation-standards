# 📖 WWAN — Operational Context Reference

---

## Metadata

| Field | Value |
|--------|-------|
| Document | `080r-wwan-operational-context-standard.md` |
| Category | Engineering Standards |
| Type | Reference |
| Status | 🚧 Draft |
| Companion Standard | `080-wwan-operational-context-standard.md` |
| Owner | Engineering |
| Version | 0.1 |

---

# Purpose

This document explains the philosophy, evolution, and practical application of the **WWAN (Where We Are Now)** concept.

Unlike the companion standard, which defines the required structure of a WWAN, this document explains why WWAN exists, how it evolved, and why it has become one of the central concepts within the Assisted Flow of Knowledge (AFK) methodology.

---

# Background

Traditional engineering documentation often focuses on describing software.

Examples include:

- Requirements
- Architecture
- Design
- APIs
- Components

These documents explain **what the system is**.

However, they rarely answer a different engineering question:

> **Where do we continue today?**

As projects become larger and engineering work spans weeks, months, or years, reconstructing the current project context becomes increasingly expensive.

The WWAN concept emerged as a practical solution to this problem.

---

# Discovery of WWAN

WWAN was not originally intended to become an engineering standard.

During development of the Engineering Documentation System (EDS), a small operational document was maintained simply to record current progress.

Its original purpose was project tracking.

Over time, an unexpected pattern emerged.

Every new engineering session began with the same activity:

- Read the WWAN.
- Understand the current context.
- Continue working.

When AI-assisted collaboration became part of the workflow, another observation appeared.

Instead of relying on conversation history, the AI assistant could resume productive collaboration using only the WWAN.

The document had unintentionally become something much more valuable than a status report.

It had become a **Context Bootstrap Document**.

---

# The Canon Event

Within the AFK methodology, this realization became the defining moment for WWAN.

The question changed from:

> "How do we record project status?"

to

> "How do we transfer operational knowledge between engineering sessions?"

That shift transformed WWAN from documentation into an operational engineering artifact.

---

# Context Bootstrap Document

A WWAN is best understood as a **Context Bootstrap Document**.

Its purpose is not to describe everything that has happened.

Its purpose is to provide just enough verified operational context to allow productive work to resume immediately.

Instead of reconstructing weeks or months of engineering history, an engineer—or an AI assistant—can begin from a shared operational snapshot.

---

# Why Not Conversation History?

AI systems often maintain conversational context during a single session.

Engineering projects, however, frequently span far longer than any individual conversation.

Conversation history also has practical limitations:

- sessions end
- context windows are limited
- information becomes difficult to locate
- important decisions become buried inside discussions

WWAN externalizes operational knowledge into a version-controlled engineering artifact.

Knowledge belongs to the project rather than to the conversation.

---

# WWAN and AFK

Within the Assisted Flow of Knowledge methodology, WWAN acts as the bridge between engineering sessions.

```
Yesterday

    │

    ▼

Engineering Work

    │

    ▼

WWAN

    │

    ▼

Today

    │

    ▼

Engineer + AI

    │

    ▼

Continue Working
```

Rather than depending on memory, AFK depends on documented operational context.

---

# Primary Audience

WWAN intentionally serves multiple audiences.

## Returning Engineer

Allows an engineer to quickly regain project context after time away.

---

## New Engineer

Provides an operational starting point during onboarding.

---

## AI Companion

Provides the initial engineering context for AI-assisted collaboration.

A WWAN is typically the first document shared with the AI at the beginning of a new session.

---

## Future Maintainer

Reduces the effort required to understand the project's current direction.

---

# What WWAN Is Not

A WWAN should not become:

- a project history
- meeting minutes
- architecture documentation
- design documentation
- implementation documentation
- daily journal

Those artifacts have their own purpose.

WWAN summarizes only the operational state required to continue work.

---

# Engineering Learning

One unexpected benefit of WWAN is that it encourages deliberate engineering learning.

Maintaining a WWAN requires engineers to periodically stop implementation and answer questions such as:

- What have we learned?
- What remains uncertain?
- What should happen next?
- What knowledge should not be lost?

This reflection naturally improves engineering understanding.

---

# Relationship to EDS

The Engineering Documentation System (EDS) defines how engineering documentation is written.

WWAN is one engineering standard within that framework.

EDS provides the structure.

WWAN provides operational continuity.

---

# Relationship to EKS

The Engineering Knowledge System (EKS) studies how engineering knowledge is created, validated, preserved, and reused.

WWAN demonstrates one practical mechanism for preserving operational knowledge.

Lessons learned through WWAN contribute directly to the evolution of EKS.

---

# Relationship to AFK

AFK extends the concept even further.

Instead of viewing documentation as the final product, AFK views documentation as one stage within a larger flow of knowledge.

```
Engineering Work

        │

        ▼

Discovery

        │

        ▼

Documentation

        │

        ▼

WWAN

        │

        ▼

Engineering Knowledge

        │

        ▼

Organizational Knowledge
```

WWAN is therefore one of the operational artifacts that enables knowledge to continue flowing.

---

# Engineering Philosophy

A project should never depend on a single person's memory.

Operational understanding should exist independently of individual contributors.

WWAN helps achieve that goal by preserving current engineering context as a shared artifact.

Knowledge becomes part of the project rather than remaining inside conversations or individuals.

---

# Future Evolution

Future versions of WWAN may evolve to include:

- standardized AI Companion Instructions
- automated WWAN generation
- milestone templates
- workstream linking
- multi-project operational dashboards

The fundamental purpose is expected to remain unchanged.

WWAN exists to minimize context reconstruction.

---

# Closing Thought

The most valuable engineering knowledge is often not hidden in architecture diagrams or source code.

It is the operational understanding of **where the project is today**.

WWAN preserves that understanding.

It allows engineers—and AI companions—to spend less time reconstructing context and more time creating value.

---

# Related Documents

## Companion Standard

- `080-wwan-operational-context-standard.md`

## Related

- `001-documentation-system-overview.md`
- `020-document-template-standard.md`
- `040-document-reference-standard.md`

## Methodology

- AFK README
- EKS README

---

> **A WWAN is not a status report. It is a Context Bootstrap Document.**

> **Every undocumented system has a story. Let's AFK it before it's forgotten.**