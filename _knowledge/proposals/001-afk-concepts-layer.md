# 📝 Draft Proposal — AFK Concepts Layer

> **Proposal:** Introduce a dedicated "Concepts" layer within AFK to define core AFK terminology and artifacts.

---

# Status

🚧 Draft

---

# Purpose

Separate **AFK operational concepts** from **EKS engineering foundations**.

This proposal aims to preserve the original intent of EKS Foundations while providing AFK with a clear place to explain its own vocabulary.

---

# Problem

During the evolution of AFK, several documents naturally emerged to explain concepts such as:

- WWAN
- Wishes
- Grants
- Knowledge Packages
- Engineering Sessions
- Project Foundation

These documents explain **what an AFK artifact is**, not the broader philosophy of engineering knowledge.

Placing them under **Foundations** risks mixing AFK implementation concepts with EKS theoretical foundations.

---

# Proposed Structure

```text
Engineering Knowledge Repository

AFK
├── Concepts
│   ├── 001 Project Foundation
│   ├── 002 Wishes
│   ├── 003 WWAN
│   ├── 004 Grants
│   ├── 005 Knowledge Packages
│   ├── 006 Discovery
│   └── 007 Engineering Sessions
│
├── Procedures
├── Playbooks
├── Journeys
├── Methodologies
└── Culture

EDS
├── Core Standards
├── Engineering Standards
└── References

EKS
└── Foundations
    ├── Knowledge Lifecycle
    ├── Knowledge Hierarchy
    ├── Knowledge Extraction
    ├── Engineering Learning
    └── Organizational Knowledge
```

---

# Responsibilities

## AFK Concepts

Answer:

> **"What is this AFK artifact?"**

Examples:

- What is a WWAN?
- What is a Wish?
- What is a Grant?
- What is a Knowledge Package?

---

## AFK Procedures

Answer:

> **"How do I perform this activity?"**

Examples:

- Initialize an engineering project
- Update a WWAN
- Create a Knowledge Package

---

## AFK Playbooks

Answer:

> **"How do I accomplish this engineering objective?"**

Examples:

- Existing Codebase Playbook
- Discovery Playbook

---

## AFK Journeys

Answer:

> **"Teach me by doing."**

Guided learning experiences that combine Concepts, Procedures, and Playbooks.

---

## AFK Methodologies

Answer:

> **"How does the overall engineering process work?"**

Examples:

- Discovery Methodology
- Validation Methodology

---

## EKS Foundations

Answer:

> **"Why does engineering knowledge exist and evolve this way?"**

These are long-lived engineering principles that extend beyond AFK itself.

Examples:

- Knowledge Lifecycle
- Organizational Knowledge
- Engineering Learning

---

# Benefits

Separating Concepts from Foundations would:

- Preserve the original intent of EKS.
- Keep AFK self-contained.
- Improve onboarding.
- Reduce ambiguity.
- Make navigation more intuitive.
- Clarify document ownership across AFK, EDS, and EKS.

---

# Current Status

This proposal is under evaluation and has **not yet been adopted**.

If validated through continued use, the AFK repository structure may be updated in a future milestone.

---

## Metadata

| Field | Value |
|-------|-------|
| Document | `draft-afk-concepts-layer.md` |
| Status | 🚧 Draft |
| Version | 0.1 |
| As of | 2026-07-29 |