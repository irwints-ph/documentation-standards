# 📘 EKPP Grant Strategy

---

## Metadata

**Document:** `04-ekpp-grant-strategy.md`

**Type:** 📘 Grant Strategy

**Project:** Engineering Knowledge Publishing Portal (EKPP)

**Owner:** Engineering

**Version:** 1.0

---

## Status

**As of:** 07.28.2026 23:10 PHT

🚧 Discovery

---

# Purpose

This document describes how the currently active wish will be granted.

Unlike the Wish List, which captures **what** we hope to achieve, the Grant Strategy explores **how we intend to grant the wish** without prematurely designing the implementation.

This document intentionally precedes architecture.

---

# Current Active Wish

## 💭 EKPP-W001

> **I wish I could see the initial output of EKPP.**

---

# Grant Objective

Provide a simple but complete publishing experience that allows someone to:

* discover EKPP,
* understand its purpose,
* navigate between EDS, EKS, and AFK,
* read the published documentation,
* complete their visit without unnecessary complexity.

The objective is not feature completeness.

The objective is granting one meaningful wish well.

---

# Reader Journey

The intended experience is intentionally simple.

```text
Landing Page

↓

Understand EKPP

↓

Choose

EDS

EKS

AFK

↓

Read

↓

Navigate

↓

Leave
```

If a first-time reader can complete this journey comfortably, the wish is considered successfully granted.

---

# Success Criteria

The initial wish is considered granted when a reader can:

* Access the EKPP website.
* Understand what EKPP is.
* Navigate between EDS, EKS, and AFK.
* Read the published documentation.
* Return to the home page without confusion.

No additional functionality is required for this initial grant.

---

# Engineering Scope

Current implementation should remain intentionally small.

Included:

* Landing page
* Shared navigation
* Published documentation
* Consistent styling
* Static deployment

Excluded:

* Search
* Versioning
* Comments
* Automation
* Analytics
* Authentication
* Dynamic content

These remain outside the scope of EKPP-W001.

---

# Guiding Principle

When uncertainty exists, choose the simpler implementation.

Operational experience will determine whether additional capabilities are genuinely needed.

---

# Risks

Current risks include:

* Navigation becoming unclear.
* Readers misunderstanding EKPP's purpose.
* Publishing becoming unnecessarily complicated.
* Premature implementation of features before operational evidence exists.

These risks will be reassessed after the initial release.

---

# Emerging Wishes

The following observations emerged while defining this Grant Strategy.

They are intentionally **not** part of the official Wish List.

Additional operational experience is required before deciding whether they should become active wishes.

---

## Candidate Observation 001

> **I wish I knew whether readers successfully completed the intended journey.**

### Context

While defining success criteria, the team naturally asked:

> "How do we know the wish was actually granted?"

Several implementation ideas emerged, including:

* Reader feedback
* Observation sessions
* Journey tracking
* Analytics
* Surveys

No implementation decision has been made.

### Current Decision

Observe the initial release first.

If this need consistently appears during operational experience, it may later be promoted to the official Wish List.

---

# Relationship to Architecture

The Grant Strategy intentionally separates human intent from technical design.

Expected flow:

```text
Wish

↓

Grant Strategy

↓

Architecture

↓

Implementation

↓

Validation

↓

Granted
```

Architecture should emerge from understanding the wish rather than from assumptions about implementation.

---

# Next Step

Use this Grant Strategy as the input for:

**05-ekpp-initial-architecture.md**

The architecture should support granting EKPP-W001 with the least amount of engineering necessary while remaining maintainable and aligned with AFK principles.

---

# Closing Thought

A wish does not become reality simply because it exists.

Understanding how to grant it is the bridge between intention and implementation.

As always:

> **Experiment. Observe. Learn. Improve.**
