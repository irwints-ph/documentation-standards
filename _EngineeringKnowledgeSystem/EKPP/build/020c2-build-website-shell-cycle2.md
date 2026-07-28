# 🌐 Website Shell — Build Cycle 2

---

## Metadata

**Document:** `020c2-build-website-shell-cycle2.md`

**Category:** Build

**Status:** 🚧 Growing

**Parent:** Engineering Knowledge Publishing Portal (EKPP)

**Version:** 0.1

**Related Wish:**

* EKPP-W001 — *I wish I could see the initial output of EKPP.*

**Previous Build:**

* 020-build-website-shell.md

---

# Purpose

This document defines the second implementation cycle for the EKPP Website Shell.

Unlike the initial Website Shell, this cycle is **not** intended to create the first observable output.

The objective is to refine that output using observations collected during the first implementation cycle.

This Build Cycle demonstrates one of AFK's core engineering principles:

> Observations refine implementation.

---

# Context

Website Shell Cycle 1 successfully produced the first observable implementation of EKPP.

The implementation allowed the Human Collaborator to evaluate the experience rather than speculate about it.

Following review, several observations emerged regarding the reading experience.

These observations now guide the next implementation cycle.

---

# Inputs

Before beginning this Build Cycle, review:

* Current WWAN
* Reader Journey
* Website Shell Build Cycle 1
* Website Shell Cycle 1 Evidence
* Active Wish (EKPP-W001)

---

# Trigger

This Build Cycle was initiated following Human Collaborator observations including:

* The overall presentation did not yet feel like EKPP.
* The footer felt visually disconnected.
* The color palette was not inviting.
* The website should feel comfortable to read rather than simply display information.

These observations are documented as part of the Reader Journey.

---

# Build Objectives

The objective of this cycle is to improve the reading experience.

Focus areas include:

## Reading Comfort

* Improve typography.
* Improve reading rhythm.
* Reduce visual clutter.
* Improve information hierarchy.

---

## Visual Identity

Develop a calmer presentation that better reflects engineering knowledge.

The visual language should communicate:

* confidence,
* clarity,
* professionalism,
* and long-form readability.

---

## Reader Journey

Refine the implementation using current Reader Journey observations, including:

* Knowledge should be comfortable to read anywhere.
* Reading is the primary interaction.
* Content is the primary interface.
* Responsive design supports reading rather than existing as an isolated technical feature.

---

## Mobile Experience

Assume that readers may consume engineering knowledge:

* while commuting,
* while waiting,
* during short breaks,
* or during deep work.

The implementation should remain comfortable across all supported devices.

---

# Non-Objectives

This Build Cycle does **not** include:

* publishing automation,
* search,
* generated navigation,
* document rendering,
* publishing pipeline,
* deployment automation,
* or additional functionality unrelated to the Reader Journey.

The focus remains on refining the Website Shell.

---

# Expected Deliverables

Update the active implementation:

```text
website/

index.html

assets/css/style.css

assets/js/
```

---

Preserve completed implementation as evidence under:

```text
implementation/

evidence/

artifacts/

002-website-shell-cycle2/
```

---

# Observation Criteria

Following implementation, evaluate:

* Does the website feel calmer?
* Is reading more comfortable?
* Does the hierarchy naturally guide the reader?
* Does the experience feel appropriate on mobile devices?
* Does the presentation better represent EKPP?

---

# Exit Condition

This Build Cycle concludes when:

* the Website Shell has been refined,
* the Human Collaborator has reviewed the result,
* new observations have been captured,
* and a decision has been made whether EKPP-W001 has been sufficiently granted or whether another refinement cycle is required.

---

# AFK Observation

This document represents the first implementation cycle initiated directly from observations rather than from a new wish.

It reinforces the emerging AFK principle:

> Wishes establish direction.

> Observations improve implementation.

Multiple implementation cycles may contribute toward granting a single wish.

---

# Closing Thought

The purpose of this Build Cycle is not to produce a newer version of the website.

Its purpose is to improve understanding through iterative observation.

Each cycle should leave the implementation better aligned with the experience EKPP intends to provide.
