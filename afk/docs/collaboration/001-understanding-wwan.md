# 📍 Understanding WWAN (Where We Are Now)

> **WWAN preserves operational context so collaboration can continue naturally.**

---

# Purpose

**WWAN (Where We Are Now)** is the operational snapshot of a project.

Its purpose is to rapidly synchronize a new collaborator—human or AI—with the current state of engineering work.

Rather than reconstructing the project from discovery documents, implementation history, or conversation context, a collaborator should be able to read the WWAN and immediately understand:

- what the project is currently doing,
- where the project currently stands,
- what is actively being worked on,
- and what should happen next.

WWAN minimizes reconstruction and maximizes continuity.

---

# What WWAN Is

WWAN is **not** a specification.

WWAN is **not** a design document.

WWAN is **not** a historical record.

WWAN is an **operational dashboard**.

It answers one simple question:

> **"If I join the project right now, what do I need to know before continuing?"**

---

# Why WWAN Exists

Engineering projects often span weeks, months, or years.

People change projects.

Conversations end.

Context windows expire.

Without a shared operational snapshot, collaborators spend valuable time reconstructing the current state before they can contribute.

WWAN exists to eliminate that reconstruction effort.

It captures only the information required to resume productive engineering work.

---

# Relationship to EDS

The **Engineering Documentation System (EDS)** defines **how a WWAN document is written**.

AFK explains **how collaborators should use a WWAN during engineering work**.

When creating or updating a WWAN, follow the Engineering Documentation System standard:

- [`eds/docs/engineering-standards/080-wwan-operational-context-standard.md](../../../eds/docs/engineering-standards/080-wwan-operational-context-standard.md)

The EDS standard defines:

- required sections,
- document structure,
- writing conventions,
- metadata,
- lifecycle,
- update guidance.

AFK focuses on collaboration.

EDS focuses on documentation standards.

---

# How AI Collaborators Should Use WWAN

At the beginning of every engineering session:

1. Read the WWAN first.
2. Understand the current operational state.
3. Identify the active objective or engineering wish.
4. Review recently completed work.
5. Continue from the preserved project understanding.

The WWAN should answer **where the project is**.

Detailed understanding should come from discovery documents, engineering standards, and implementation artifacts referenced by the WWAN.

---

# Updating WWAN

WWAN should evolve alongside the project.

After completing meaningful work, collaborators should ask:

- Has the project focus changed?
- Has a milestone been completed?
- Has the active wish changed?
- Has the next recommended step changed?
- Has new operational knowledge been discovered?

If the answer is yes, the WWAN should be updated before ending the session.

---

# Relationship to Other AFK Artifacts

WWAN is one part of the Assisted Flow of Knowledge methodology.

```text
Session Bootstrap
        ↓
Knowledge Package
        ↓
WWAN
        ↓
Active Wish
        ↓
Discovery
        ↓
Implementation
        ↓
WWAN Update
```

Each artifact has a distinct responsibility.

The Bootstrap prepares the collaboration.

The Knowledge Package builds understanding.

The WWAN synchronizes operational context.

The remaining artifacts capture the engineering work itself.

---

# Guiding Principle

A collaborator should never need to reconstruct the current state of a project from conversation history.

Reading the WWAN should provide enough operational understanding to continue engineering work naturally.

---

# Closing Thought

WWAN exists to answer one question quickly and accurately:

> **"Where are we now?"**

Once that question has been answered, collaboration can focus on creating value rather than rediscovering context.

---

## Metadata

| Field | Value |
|-------|-------|
| Document | `001-understanding-wwan.md` |
| Category | AFK Collaboration |
| Type | Collaboration Guide |
| Status | 🚧 Active Development |
| Related Standard | `EDS → 080 — WWAN Operational Context Standard` |
| Version | 2.0 |