# 📘 WWAN — Operational Context Standard

---

## Metadata

| Field | Value |
|--------|-------|
| Document | `080-wwan-operational-context-standard.md` |
| Category | Engineering Standards |
| Type | Canonical Standard |
| Status | 🚧 Draft |
| Companion | `080r-wwan-operational-context-standard.md` |
| Owner | Engineering |
| Version | 0.1 |

---

# Purpose

Define the standard structure, purpose, and usage of the **WWAN (Where We Are Now)** document.

A WWAN provides the operational context required for engineers and AI assistants to resume productive work with minimal onboarding.

Rather than documenting an entire project, a WWAN captures the project's current operational state.

---

# Standard

## One WWAN Per Workstream

Each active engineering workstream should maintain one current WWAN document.

Examples include:

- Engineering Documentation System
- Frontend Discovery
- AFK Pilot
- Architecture Modernization
- API Migration

A workstream may archive historical WWANs as milestones are completed.

---

## WWAN Is the Context Bootstrap Document

A WWAN serves as the **Context Bootstrap Document** for a project or workstream.

It shall provide sufficient operational context for:

- returning engineers
- newly onboarded engineers
- AI assistants
- future maintainers

The objective is to minimize context reconstruction.

---

## Primary Audience

A WWAN shall be understandable without requiring previous conversations or undocumented knowledge.

It is written for:

- Humans
- AI companions
- Future contributors

---

## Operational Focus

A WWAN shall describe the **present**.

It is not intended to become:

- project history
- design documentation
- architecture documentation
- meeting minutes
- engineering journal

Historical information should be maintained elsewhere.

---

## Required Sections

A WWAN should normally include:

- Metadata
- Current Focus
- Current Milestone
- Current Objectives
- Current State
- Immediate Next Work
- Resume From
- Related Documents

Additional sections may be added when appropriate.

---

## Resume Point

Every WWAN shall contain a clearly defined **Resume From** section.

The Resume From section identifies the immediate next activity that should occur when work resumes.

The objective is to eliminate unnecessary project rediscovery.

---

## Currency

WWAN documents should be updated whenever meaningful progress occurs.

Typical updates include:

- milestone completion
- objective changes
- discovery progress
- roadmap adjustments
- priority changes

WWAN should always reflect the current engineering state.

---

## AI Companion Instructions

A WWAN may include a short instruction block intended for AI assistants.

Example:

```text
Assume no prior knowledge of this project.

Use this WWAN as the operational context for the current session.

Do not assume previous conversations.

Identify missing information rather than making assumptions.
```

This instruction allows AI assistants to begin productive collaboration using documented context rather than conversational memory.

---

## Relationship to AFK

Within the Assisted Flow of Knowledge (AFK) methodology, WWAN functions as the project's operational knowledge package.

It enables engineering knowledge to flow consistently between:

- engineering sessions
- engineers
- AI assistants
- future maintainers

without depending on individual memory.

---

# Principles

A WWAN shall be:

- Current
- Short
- Actionable
- Easy to update
- Easy to understand
- Version controlled
- Human friendly
- AI friendly

Its purpose is operational continuity.

---

# Engineering Philosophy

Engineering work should not pause because knowledge exists only inside someone's head.

A WWAN preserves enough operational understanding that another engineer—or an AI companion—can continue productive work with minimal onboarding.

The objective is continuity rather than memory.

---

# Related Documents

## Prerequisites

- `001-documentation-system-overview.md`
- `020-document-template-standard.md`

## Related

- `015-document-status-lifecycle.md`
- `040-document-reference-standard.md`

## Companion

- `080r-wwan-operational-context-standard.md`