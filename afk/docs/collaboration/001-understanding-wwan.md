# 📍 Understanding WWAN (Where We Are Now)

---

## Purpose

**WWAN (Where We Are Now)** is the operational snapshot of a project.

Its purpose is to rapidly synchronize a new collaborator—human or AI—with the current state of engineering work.

Rather than reconstructing the project from discovery documents, implementation history, or conversation context, a collaborator should be able to read the WWAN and immediately understand:

* what the project is currently doing,
* where the project currently stands,
* what is actively being worked on,
* and what should happen next.

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

# What WWAN Should Contain

A WWAN should typically include:

## Current Status

The overall operational state of the project.

Examples:

* 🚧 Discovery
* 🚧 Build
* 🚧 Validation
* ✅ Completed

---

## Current Focus

The single area receiving engineering attention.

Only one primary focus should exist at any time.

---

## Active Wish

The current engineering wish driving the project.

WWAN should identify the active wish and its status.

Example:

```text
Active Wish

EKPP-W002

Status

🚧 Discovery
```

---

## Recently Completed Work

Major milestones or wishes recently completed.

This provides immediate context without requiring collaborators to read historical documentation.

---

## Current State

A concise summary of what currently exists.

Examples include:

* completed discovery,
* completed implementation,
* emerging observations,
* validated architecture,
* available evidence.

---

## Current Objective

The immediate engineering objective.

This should answer:

> "What are we trying to accomplish next?"

---

## Next Step

The smallest useful next action.

WWAN should make it obvious where engineering should continue.

---

## Recent Learnings

Important discoveries that may influence future work.

These are not historical details—they are operational knowledge that changes current engineering decisions.

---

# What WWAN Should Not Contain

WWAN should avoid becoming:

* a design specification,
* a discovery document,
* an implementation guide,
* or a project history.

Those belong in their own documents.

WWAN should summarize rather than replace them.

---

# How AI Collaborators Should Use WWAN

When beginning a new collaboration session:

1. Read the WWAN first.
2. Understand the current operational state.
3. Identify the active wish.
4. Determine the immediate engineering objective.
5. Continue from the preserved project understanding.

WWAN should answer **where the project is**, not **how every system works**.

---

# Relationship to Other Documents

WWAN works alongside the broader documentation ecosystem.

```text
Bootstrap

↓

Knowledge Package

↓

WWAN

↓

Active Wish

↓

Discovery

↓

Build

↓

Implementation
```

The Bootstrap prepares the collaboration.

The Knowledge Package provides project understanding.

WWAN synchronizes the current operational state.

The remaining documents provide the detailed engineering knowledge required to continue.

---

# Guiding Principle

A collaborator should never need to reconstruct the current state of the project from conversation history.

Reading the WWAN should provide enough operational understanding to continue engineering work naturally.

---

# Closing Thought

WWAN exists to answer one question quickly and accurately:

> **"Where are we now?"**

Once that question has been answered, collaboration can focus on moving the project forward rather than rediscovering where it left off.
