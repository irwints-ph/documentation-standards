# 🚀 Build Bootstrap

---

## Metadata

**Document:** `000-build-bootstrap.md`

**Category:** Build

**Status:** 🚧 Growing

**Parent:** Engineering Knowledge Publishing Portal (EKPP)

**Version:** 0.1

---

# Purpose

This document prepares both human engineers and AI collaborators before beginning a Build session.

Its objective is to establish enough operational context that implementation can begin from understanding rather than assumption.

The Build Bootstrap is intentionally lightweight.

It does not replace Discovery.

It points collaborators toward the knowledge they should understand before implementing.

---

# Before Building

Do not begin implementation immediately.

First, understand the current state of the project.

Engineering should continue from existing knowledge rather than reconstruct it.

---

# Read First

Before implementing, review the following documents.

## Operational Context

* 📍 Where We Are Now (WWAN)

This provides the current operational snapshot.

---

## Discovery

Understand the decisions that led to the current Build phase.

Recommended reading:

* Current Discovery
* Wish List
* Grant Strategy
* Initial Architecture
* Build Plan

---

## Current Build

Review the current Build Guide and Implementation Guide before performing work.

These describe:

* what is being built,
* why it is being built,
* and the smallest implementation required to support the current active wish.

---

# Current Wish

Every Build session should clearly identify the active wish.

Current implementation should support **one wish at a time**.

Avoid introducing functionality intended for future wishes.

---

# Source of Truth

Before creating new content, determine whether the knowledge already exists.

Prefer:

Read

↓

Understand

↓

Synthesize

Rather than:

Generate

↓

Assume

↓

Duplicate

Implementation should reflect the project's existing understanding rather than replacing it.

---

# AI Collaborator Guidance

When beginning a Build session:

* Read before generating.
* Preserve existing decisions.
* Do not invent architecture.
* Do not redefine project purpose.
* Build from the current understanding.
* Ask questions when uncertainty appears.

If existing documentation and implementation appear inconsistent:

Pause.

Raise the observation.

Collaborate before changing direction.

---

# Build Mindset

AFK encourages collaborators to ask:

* What are we trying to grant?
* What already exists?
* What is the smallest useful implementation?
* What can we observe after this build?

Build only enough to create the next meaningful observation.

---

# Build Flow

```text
Understand

↓

Read Existing Knowledge

↓

Implement the Smallest Useful Increment

↓

Observe

↓

Validate

↓

Learn

↓

Continue
```

---

# Exit Condition

A Build session does not end because every possible feature has been implemented.

It pauses when:

* the current wish has been advanced,
* observations have been recorded,
* WWAN has been updated,
* and the next collaborator can continue without reconstructing prior work.

AFK does not stop.

It preserves enough understanding for future collaboration to continue naturally.

---

# Closing Thought

A Build session should never begin with an empty context.

The first implementation is not writing code.

The first implementation is understanding what already exists.

As always:

> **Understand first. Build second. Learn always.**
