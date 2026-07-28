# 📖 Operational vs Knowledge Artifacts

---

## Metadata

**Document:** `04-operational-vs-knowledge-artifacts.md`

**Type:** 📖 Foundation

**Owner:** Engineering

**Version:** 1.0 (Draft)

---

## Status

**As of:** 07.28.2026 15:30 PHT

🚧 In Progress

---

# Purpose

This document establishes the distinction between **Operational Artifacts** and **Knowledge Artifacts** within the Engineering Knowledge System (EKS).

Understanding this distinction is fundamental to AFK because not every document serves the same purpose.

Some documents help engineers **perform the work.**

Others preserve **what was learned from the work.**

Recognizing this difference helps keep documentation organized, reduces unnecessary maintenance, and allows engineering knowledge to mature naturally over time.

---

# The Core Principle

> **Operational artifacts guide the journey.**
>
> **Knowledge artifacts preserve the destination.**

Operational documents exist to support ongoing engineering work.

Knowledge documents exist to preserve validated understanding after the work has been completed.

---

# Why This Matters

One of the most common documentation problems is treating every document the same.

Some documents are expected to change daily.

Others should rarely change once validated.

Mixing these responsibilities often results in documentation that becomes difficult to maintain, quickly outdated, or impossible to trust.

AFK encourages separating documentation according to its purpose rather than simply by file type.

---

# Operational Artifacts

Operational Artifacts support active engineering activities.

Their purpose is to help engineers understand the current state of work, coordinate activities, and make progress.

They are expected to evolve continuously.

Examples include:

* WWAN (Where We Are Now)
* Roadmaps
* Kuwento Specs
* Discovery Plans
* Discovery Logs
* Scratch Notes
* Working Checklists
* Session Notes

Characteristics:

* Frequently updated
* Reflect the current state
* May contain assumptions
* May contain unanswered questions
* Guide ongoing work
* Temporary by nature

Operational artifacts answer questions such as:

> Where are we now?

> What are we trying to accomplish?

> What happens next?

---

# Knowledge Artifacts

Knowledge Artifacts preserve engineering understanding after discovery and validation.

Their purpose is not to manage work but to preserve what the work has revealed.

They are expected to stabilize over time.

Examples include:

* Current Platform documentation
* Folder Registries
* Component Documentation
* Architecture Documentation
* Validation Reports
* Engineering Standards
* Knowledge Packages

Characteristics:

* Evidence-based
* Reviewed
* Stable
* Intended for long-term reference
* Reusable
* Organizational assets

Knowledge artifacts answer questions such as:

> What do we know?

> How does the system work?

> Why was this decision made?

---

# The Knowledge Flow

Engineering knowledge typically evolves through several stages.

```text
Idea

↓

Operational Artifact

↓

Discovery

↓

Validation

↓

Knowledge Artifact

↓

Engineering Knowledge

↓

Organizational Knowledge
```

Operational artifacts create the environment where discovery happens.

Knowledge artifacts preserve the results of that discovery.

---

# AFK Perspective

AFK views documentation as a natural outcome of engineering understanding.

Operational documentation supports learning.

Knowledge documentation preserves learning.

Both are essential, but they serve different purposes.

Without Operational Artifacts, discovery becomes disorganized.

Without Knowledge Artifacts, discovery must be repeated.

---

# WWAN as an Example

The distinction becomes clear when examining WWAN.

WWAN is an Operational Artifact.

Its purpose is to answer one question:

> **Where are we now?**

Because of this, WWAN should always describe the current operational state.

Historical WWAN documents should not replace the current WWAN.

Instead, history should be preserved separately through session journals, milestones, release notes, or historical records.

WWAN should always remain the first document that an engineer—or AI companion—reads when resuming work.

---

# From Operational to Knowledge

One of AFK's objectives is helping engineers recognize when operational information has matured into reusable knowledge.

For example:

```text
Kuwento Specs
        ↓
Implementation
        ↓
Discovery
        ↓
Validation
        ↓
Current Platform Documentation
        ↓
Engineering Standard
```

Not every operational document becomes a knowledge artifact.

However, every knowledge artifact originates from operational work.

---

# Relationship to AFK

This distinction reinforces one of AFK's core beliefs:

> **Understanding is the real product.**

Operational artifacts help engineers reach understanding.

Knowledge artifacts ensure that understanding is never lost.

---

# Design Principles

* Separate work management from knowledge preservation.
* Allow operational documents to evolve freely.
* Preserve validated knowledge independently.
* Avoid treating temporary notes as permanent documentation.
* Promote gradual maturation of engineering knowledge.
* Recognize that understanding develops over time.

---

# Looking Forward

As the Engineering Knowledge System evolves, additional guidance will define how Operational Artifacts transition into Knowledge Artifacts.

Future foundations may explore topics such as:

* Knowledge Validation
* Knowledge Transfer
* Organizational Learning
* Knowledge Evolution

As with every AFK concept:

> **AFK will tell us when we get there.**

---

# Closing Thought

Every engineering effort begins with uncertainty.

Operational Artifacts help us navigate that uncertainty.

Knowledge Artifacts ensure that future engineers never have to start from the same place again.

---

# Related Documents

## Foundations

* `01-knowledge-lifecycle.md`
* `02-knowledge-hierarchy.md`
* `03-knowledge-extraction.md`

## Related

* AFK README
* Engineering Documentation System (EDS)
* Engineering Knowledge System (EKS)
