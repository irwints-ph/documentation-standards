# 📄 Document Template Standard

> **Good documentation communicates purpose before administration.**

---

# Purpose

This standard defines the recommended structure for engineering documentation within the Engineering Documentation System (EDS).

The objective is to produce documentation that is:

- Easy to read
- Easy to navigate
- Easy to maintain
- Human-friendly
- AI-friendly
- Consistent across repositories

The template should support engineering understanding first, while remaining flexible enough to accommodate different document types.

---

# Documentation Philosophy

Documentation exists to improve understanding.

Administrative information supports the document—it should not become the document.

A reader should immediately understand:

- What this document is about.
- Why it exists.
- How it can help.

Only after that should metadata, lifecycle information, and administrative details be presented.

---

# Document Categories

Engineering documentation generally falls into two categories.

```text
Engineering Documentation

│

├── Specification Documents
│
│   Standards
│   Policies
│   Procedures
│   References
│
└── Knowledge Documents

    Guides
    Journeys
    Playbooks
    Learning Paths
    WWAN
```

Each category has different priorities and therefore may use different template layouts.

---

# Specification Documents

Specification documents define reusable engineering rules.

Examples include:

- Standards
- Policies
- Procedures
- Reference specifications

These documents typically prioritize governance, lifecycle, and version management.

Recommended structure:

```text
Title

↓

Metadata

↓

Purpose

↓

Content

↓

References
```

---

# Knowledge Documents

Knowledge documents primarily support learning, collaboration, and operational continuity.

Examples include:

- Guides
- Journeys
- Playbooks
- Learning Paths
- WWAN

These documents prioritize readability and should minimize interruption during reading.

Recommended structure:

```text
Title

↓

Guiding Principle

↓

Purpose

↓

Content

↓

Notes

↓

Metadata
```

---

# Guiding Principle

Knowledge-oriented documents should include a short guiding principle immediately after the title.

The guiding principle communicates the central idea of the document in one sentence.

Example:

> Understanding is the first deliverable.

The guiding principle helps both humans and AI quickly establish context before reading the document.

---

# Metadata Placement

Two metadata placements are supported.

## Header Metadata

Recommended for:

- Standards
- Procedures
- Policies
- Reference documents

Example:

```text
Metadata

Version
Status
Owner
Approved
Last Updated
```

---

## Footer Metadata

Recommended for:

- Guides
- Journeys
- Playbooks
- Learning Paths
- WWAN

Example:

```text
Metadata

Document
Version
Status
Last Updated
```

Footer metadata allows the document to begin immediately with its purpose.

---

# Reader-First Structure

Whenever practical, documents should follow this reading flow.

```text
Title

↓

Guiding Principle

↓

Purpose

↓

Main Content

↓

Related Documents

↓

Metadata
```

This ordering reduces onboarding friction and allows readers to immediately understand the intent of the document.

---

# Reusable Documentation

Documents should avoid duplicating information already maintained elsewhere.

Instead, related artifacts should reference one another.

Example:

```text
Journey

↓

Learning Path

↓

Playbook

↓

Supporting Standards
```

This keeps documentation easier to maintain while improving discoverability.

---

# Related Documents

Documents should provide links to relevant supporting documentation when appropriate.

Examples include:

- Standards
- Procedures
- Journeys
- Learning Paths
- Playbooks
- Reference documents

Navigation should encourage progressive learning rather than overwhelming the reader.

---

# Template Selection Guide

| Document Type | Primary Goal | Recommended Metadata |
|---------------|--------------|----------------------|
| Standard | Define reusable rules | Header |
| Procedure | Execute repeatable work | Header |
| Policy | Define governance | Header |
| Reference | Provide authoritative information | Header |
| Guide | Explain | Footer |
| Journey | Learn | Footer |
| Playbook | Reuse | Footer |
| Learning Path | Navigate | Footer |
| WWAN | Operational continuity | Footer |

---

# Design Principles

Engineering documentation should:

- Communicate purpose before administration.
- Optimize for understanding.
- Support progressive learning.
- Minimize duplicated information.
- Encourage reusable documentation.
- Remain consistent across repositories.
- Be equally useful to humans and AI collaborators.

---

# Relationship to AFK

The Assisted Flow of Knowledge (AFK) methodology applies this standard to collaborative engineering activities.

AFK extends the template by introducing:

- Journeys
- Learning Paths
- Playbooks
- Operational Context (WWAN)

These artifacts follow the Knowledge Document template described in this standard.

---

# Relationship to EKS

The Engineering Knowledge System (EKS) studies how engineering knowledge evolves.

This standard defines how that knowledge should be documented once it has been discovered and validated.

---

## Metadata

| Field | Value |
|------|------|
| Document | `020-document-template-standard.md` |
| Version | 2.0 |
| Status | Active |
| Last Updated | 2026-07-29 |