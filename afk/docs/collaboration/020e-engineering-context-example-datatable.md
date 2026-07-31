# 020e — Engineering Context Example (Data Table)

---

# Status

Example

---

# Purpose

This document demonstrates how to construct an **Engineering Context Prompt** by applying the guidance described in:

**Reference**

* `020-engineering-context-prompt-guide.md`

Unlike the Template, this document is intentionally annotated.

Each section explains:

* why it exists;
* what information belongs there;
* what information should **not** be included.

---

# Engineering Context

---

## Purpose

> 📖 **Guide Reference**
>
> Section 1 — Purpose
>
> The Purpose introduces the project and explains the objective of the current collaboration.
>
> It provides enough context for the AI Collaborator to understand **why** the engineering activity exists.
>
> It should not describe implementation details.

### Example

This project is an existing React frontend application.

The objective of this collaboration is incremental engineering improvement while preserving existing production behavior.

---

## Current State

> 📖 **Guide Reference**
>
> Section 2 — Current State
>
> Describe today's engineering reality.
>
> Avoid describing future plans.
>
> Avoid describing implementation.

### Example

The frontend application has been incrementally modernized.

Some engineering units have already been refactored away from Bootstrap while others still contain Bootstrap dependencies.

The overall application architecture is still being documented through incremental discovery.

Engineering understanding currently comes from:

* existing source code;
* repository structure;
* engineering observations;
* previous discovery work.

---

## Discovery Strategy

> 📖 **Guide Reference**
>
> Section 3 — Discovery Strategy
>
> Explain how engineering work will be performed.
>
> This establishes expectations for both Human and AI collaborators.

### Example

The application will be documented and improved one Engineering Unit at a time.

Each Engineering Unit will undergo:

* Discovery
* Engineering Design
* Implementation
* Validation
* Knowledge Capture

The overall architecture will evolve as engineering units are completed.

---

## Current Engineering Unit

> 📖 **Guide Reference**
>
> Section 4 — Current Engineering Unit
>
> This section defines the engineering scope.
>
> It answers:
>
> "What part of the system are we working on?"

### Example

Engineering Unit

```text id="2bmb8y"
Data Table
```

Purpose

Reusable component responsible for displaying business data in tabular form throughout the application.

Typical Responsibilities

* Display tabular data
* Sorting
* Paging
* Filtering
* Row selection
* Export
* Responsive presentation

---

## Current Wish

> 📖 **Guide Reference**
>
> Section 5 — Current Wish
>
> Describe **what** should change.
>
> Do not describe **how** it should be implemented.
>
> Implementation belongs to Engineering Design.

### Example

Wish Identifier

```text id="w6j66t"
WL-002
```

Wish

```text id="gqulqe"
Enable automatic Card View on mobile devices while preserving the existing desktop table experience.
```

---

## Additional Objectives

> 📖 **Guide Reference**
>
> Section 6 — Additional Objectives
>
> These are engineering goals that support the primary wish but are not themselves the wish.

### Example

* Capture Data Table execution flow.
* Document Data Table architecture.
* Improve maintainability.
* Preserve existing functionality.
* Record engineering decisions.

---

## Constraints

> 📖 **Guide Reference**
>
> Section 7 — Constraints
>
> Constraints define what engineering must preserve.
>
> They reduce ambiguity during implementation.

### Example

* Preserve current desktop behavior.
* Preserve existing public interfaces.
* Avoid unrelated refactoring.
* Maintain compatibility with existing consumers.
* Do not introduce unnecessary dependencies.

---

## Known Information

> 📖 **Guide Reference**
>
> Section 8 — Known Information
>
> Record engineering knowledge already available before Discovery begins.
>
> This avoids rediscovering known facts.

### Example

Current observations

* Bootstrap dependency has already been removed from the Data Table implementation.
* Mobile rendering currently remains table-based.
* The next engineering objective is responsive presentation rather than Bootstrap migration.

---

## AI Collaboration Rules

> 📖 **Guide Reference**
>
> Section 9 — AI Collaboration Rules
>
> These define the operating boundaries of the AI Collaborator.

### Example

The AI Collaborator should:

* Understand only the current Engineering Unit.
* Preserve existing behavior.
* Avoid assumptions.
* Avoid redesigning unrelated components.
* Produce only the requested engineering artifact.
* HOLD after each requested artifact.

---

# Why This Structure Works

Notice how each section answers a different engineering question.

| Section                | Engineering Question         |
| ---------------------- | ---------------------------- |
| Purpose                | Why are we doing this?       |
| Current State          | Where are we today?          |
| Discovery Strategy     | How will we collaborate?     |
| Engineering Unit       | What are we working on?      |
| Current Wish           | What should change?          |
| Additional Objectives  | What else should we capture? |
| Constraints            | What must remain unchanged?  |
| Known Information      | What do we already know?     |
| AI Collaboration Rules | How should the AI behave?    |

Keeping these questions separate reduces ambiguity and produces consistent Engineering Contexts.

---

# Relationship to the Guide

This document demonstrates the practical application of:

* `020-engineering-context-prompt-guide.md`

using the reusable structure provided by:

* `020a-engineering-context-template.md`

---

# Final Engineering Context

After following the Guide and completing the Template, the resulting Engineering Context becomes a project artifact.

Example destination

```text id="k7i91u"
docs/03-engineering/Journey2/WL-002/engineering-context.md
```

Readers are encouraged to compare:

```text id="ajzj56"
Guide
    ↓
Template
    ↓
Annotated Example
    ↓
Actual Engineering Context
```

to understand how the Engineering Context evolves from a learning artifact into an engineering artifact.
