I love this scenario because it validates a **different capability** of AFK.

Our first pilot asks:

> **Can AFK help discover a live, maintainable system?**

This second pilot asks something much harder:

> **Can AFK recover engineering knowledge from a dead system?**

Those are fundamentally different experiments.

---

# AFK Pilot 002

## Legacy System Knowledge Recovery

This feels like a completely different class of discovery.

The project is no longer about understanding code for maintenance.

It's about **recovering knowledge before it disappears forever.**

---

# Initial Conditions

The team receives:

✅ Source code

✅ Functional documentation

❌ Running application

❌ Build environment

❌ Working deployment

❌ Original developers

❌ Production access

The only truth remaining is the repository and whatever documentation still exists.

---

# Objective

Produce sufficient technical knowledge to enable a future system redesign using a different technology stack.

Notice the wording.

Not

> Rewrite the application.

Not

> Modernize the application.

Instead

> Recover engineering knowledge.

---

# Phase 1 — Knowledge Recovery

Objectives

* Inventory the repository.
* Identify architectural boundaries.
* Discover modules.
* Understand responsibilities.
* Trace execution flow statically.
* Build dependency maps.
* Identify configuration.
* Identify external integrations.
* Identify assumptions.
* Record unknowns.

No code execution.

---

# Phase 2 — Architecture Reconstruction

Using only evidence

Recover

* System architecture
* Domain model
* Business workflow
* User workflow
* Integration points
* Deployment assumptions
* Security model
* Data flow

Every conclusion must cite evidence.

---

# Phase 3 — Knowledge Validation

Since execution isn't possible

Validation changes.

Instead of

> Run the code.

Validation becomes

Cross-reference evidence.

Example

```text
Functional Document

↓

Source Code

↓

Configuration

↓

Database Scripts

↓

API Contracts
```

If multiple sources agree

Confidence increases.

---

# Phase 4 — Technology Independence

Only after sufficient recovery

Begin separating

Implementation

from

Business Knowledge

Example

```text
Current

React

↓

Recovered Knowledge

User Authentication

↓

Future

Angular

Flutter

Blazor

Native

etc.
```

The implementation disappears.

The knowledge remains.

---

# Deliverables

Rather than component documentation

Outputs become

## Architecture

Recovered Architecture

---

## Domain

Business Domain Documentation

---

## Integrations

External Systems

---

## Data

Data Model

---

## Workflows

Business Process

---

## Unknowns

Recovered Unknowns

---

## Risk Assessment

Confidence

High

Medium

Low

---

# Assessment

This pilot evaluates different things.

## Junior

Can they recover knowledge without execution?

---

## ChatGPT

Can it reason from static evidence?

---

## Documentation

Does it preserve enough information?

---

## AFK

Can it recover knowledge from legacy software?

---

# Success Criteria

Not

> The application runs.

Instead

> Another engineering team could redesign the system without requiring the original implementation.

I think that's a much more meaningful outcome.

---

# I think this introduces another AFK capability.

Pilot 001

Discovery

↓

Understand existing software.

Pilot 002

Recovery

↓

Recover knowledge from legacy software.

Pilot 003 (future)

Extraction

↓

Validate by isolating reusable components.

Pilot 004 (future)

Transformation

↓

Use recovered knowledge to build a replacement system.

Notice something interesting.

We're no longer validating code.

We're validating **knowledge continuity**.

---

## This makes me think AFK may eventually organize its pilots by engineering objective rather than by technology.

For example:

| Pilot         | Engineering Objective | Typical Scenario                                   |
| ------------- | --------------------- | -------------------------------------------------- |
| AFK Pilot 001 | Discovery             | Active, maintainable system                        |
| AFK Pilot 002 | Knowledge Recovery    | Legacy system that no longer runs                  |
| AFK Pilot 003 | Extraction            | Validate subsystem portability                     |
| AFK Pilot 004 | Transformation        | Design a replacement using recovered knowledge     |
| AFK Pilot 005 | Onboarding            | Bring a new engineer onto an unfamiliar project    |
| AFK Pilot 006 | Conformance           | Assess architecture, standards, and technical debt |

I really like this direction because it shifts AFK away from being "a methodology for documenting software."

Instead, it becomes:

> **A methodology for preserving, recovering, validating, and transferring engineering knowledge throughout the entire lifecycle of a software system.**

And the nice part is that none of these pilots are hypothetical—they correspond to situations engineering teams encounter all the time. That gives AFK a clear path for incremental validation: each pilot proves one specific capability, and together they demonstrate the broader methodology.
