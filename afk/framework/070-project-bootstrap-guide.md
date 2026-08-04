# 📄 Project Bootstrap Guide

---

# Metadata

| Field    | Value                            |
| -------- | -------------------------------- |
| Document | `070-project-bootstrap-guide.md` |
| Category | AFK Framework                    |
| Type     | Collaboration Guide              |
| Status   | 🟢 Active                        |
| Version  | 2.0                              |
| As Of    | 2026-08-04                       |

---

# Purpose

This document defines how an engineering collaboration is **bootstrapped** after the AFK Collaboration Boot Prompt has completed.

Its purpose is to explain how a Project Boot Prompt is used to reconstruct **project-specific engineering state** before discovery or implementation begins.

The Project Boot Prompt acts as the operational bridge between the generic AFK collaboration model and an individual engineering project.

---

# Relationship Within AFK

The canonical collaboration flow is:

```text
AFK Collaboration Boot Prompt
        ↓
Project Boot Prompt
        ↓
Repository Access Decision
        ├── Workspace Mode
        └── Document Mode
        ↓
Engineering State Reconstruction
        ↓
Replay Validation
        ↓
Discovery
        ↓
Replay Update
        ↓
Implementation
```

The AFK Collaboration Boot Prompt establishes **how collaboration works**.

The Project Boot Prompt establishes **what project is being reconstructed**.

---

# Responsibilities

A Project Boot Prompt is responsible for:

* establishing project identity,
* establishing the current engineering objective,
* defining repository scope,
* selecting the repository access model,
* defining repository inspection rules,
* defining the replay sequence,
* defining the engineering scope,
* defining collaboration hold points.

It should not duplicate permanent engineering documentation.

---

# Relationship to Project Foundation

Project Foundation defines:

> Why the project exists.

The Project Boot Prompt defines:

> What engineering work is being performed during this collaboration.

Project Foundation remains stable.

The Project Boot Prompt changes between sessions.

---

# Relationship to Replay

Replay reconstructs engineering state.

The Project Boot Prompt determines:

* which replay artifacts are required,
* in what order they should be reconstructed,
* and whether repository inspection occurs before or after replay.

---

# Repository Access Modes

AFK supports two repository access models.

---

## Workspace Mode

Used when the AI has direct repository access.

Examples:

* VS Code
* GitHub Copilot
* Cursor
* Windsurf
* Local AI agents

Repository becomes the primary engineering source of truth.

The AI should:

* inspect the repository directly,
* reconstruct engineering state from implementation,
* validate replay artifacts against implementation,
* use replay artifacts to preserve engineering continuity.

Repository maps should not be required.

---

## Document Mode

Used when repository access is unavailable.

Examples:

* ChatGPT Web
* ChatGPT Desktop
* Claude
* Gemini

The AI should reconstruct engineering state from:

* Project Boot Prompt,
* Repository Navigation Snapshot,
* WWAN,
* Session Handoff,
* additional uploaded documentation.

Repository inspection should not be inferred.

When repository access becomes available later, replay artifacts should be validated against implementation.

---

# Repository Inspection Rules

The Project Boot Prompt must clearly define whether repository inspection is permitted.

Examples:

### Workspace Mode

```text
Inspect the repository directly.

Treat the repository implementation as the primary source of truth.

Validate replay artifacts against implementation.
```

### Document Mode

```text
Do not inspect the repository.

Use the Repository Navigation Snapshot.

Wait until repository access becomes available.
```

---

# Required Sections

Every Project Boot Prompt should include:

1. Project Identity
2. Current Implementation Under Review
3. Session Objective
4. Repository Access Mode
5. Repository Inspection Rules
6. Engineering Scope
7. Replay Sequence
8. Expected Workflow
9. Hold Point

---

# Project Identity

Describe:

* project name,
* parent system (if applicable),
* laboratory or product,
* overall purpose,
* documentation framework.

This section should remain relatively stable.

---

# Current Implementation Under Review

Clearly identify the implementation currently being reconstructed.

Example:

| Item            | Value   |
| --------------- | ------- |
| Language        | Python  |
| Framework       | FastAPI |
| Repository Area | `api/`  |

If multiple implementations exist, explicitly state which are:

* in scope,
* out of scope.

Example:

```text
The React frontend exists under:

client/

It is outside the scope of this discovery session unless explicitly requested.
```

---

# Session Objective

Describe the engineering objective for the session.

Examples:

* Discovery Pass 1 – Foundation
* Replay Validation
* Feature Discovery – Authentication
* Architecture Review
* Bug Investigation
* Implementation

---

# Engineering Scope

Clearly define what engineering areas should be reconstructed.

Examples:

* Architecture
* Structure
* Runtime
* Configuration
* Registry
* UI
* Feature Discovery

Avoid vague instructions such as:

> Document everything.

---

# Replay Sequence

The Project Boot Prompt should explicitly define the replay order.

Typical sequence:

```text
Project Boot Prompt

↓

Repository Navigation Snapshot
(if required)

↓

Context Shift
(if applicable)

↓

WWAN

↓

Session Handoff

↓

Repository Inspection
(if Workspace Mode)

↓

Engineering State Reconstruction
```

---

# Expected Workflow

Typical engineering flow:

```text
Reconstruct Engineering State

↓

Validate Replay

↓

Perform Discovery

↓

Summarize Findings

↓

Update Replay

↓

HOLD
```

---

# Hold Point

Every Project Boot Prompt should explicitly define where the AI pauses.

Example:

```text
After Discovery Pass 1:

- summarize findings,
- list created artifacts,
- identify evidence gaps,

then HOLD.
```

---

# Dynamic Values

These values normally change between sessions:

* session objective,
* current implementation,
* engineering scope,
* replay sequence,
* milestone,
* hold point.

Project identity should change rarely.

---

# AI Expected Behavior

During project bootstrap the AI should:

* reconstruct engineering state before implementation,
* explain reasoning where appropriate,
* distinguish evidence from interpretation,
* distinguish observations from conclusions,
* preserve historical traceability,
* identify assumptions,
* ask questions whenever evidence is insufficient,
* avoid inferring undocumented project intent,
* HOLD after completing the requested engineering milestone.

The AI should not:

* infer repository structure,
* infer project architecture,
* perform implementation before reconstruction,
* overwrite canonical documentation,
* silently modify replay artifacts.

---

# Using Generated Dates

If tooling automatically inserts timestamps, place them only in document metadata.

Example:

| Field   | Value      |
| ------- | ---------- |
| Created | 2026-08-04 |
| Updated | 2026-08-04 |

Do not reference session dates inside engineering content unless they are historically relevant.

---

# Example

Example Workspace Mode session:

* Project Identity → Multi-language Standardization Laboratory
* Current Implementation → Python / FastAPI
* Repository Access → Workspace Mode
* Session Objective → Discovery Pass 1 – Foundation
* Engineering Scope → Architecture, Structure, Runtime, Configuration, Registry
* Hold Point → Discovery summary

Example Document Mode session:

* Project Identity → Multi-language Standardization Laboratory
* Current Implementation → React Frontend
* Repository Access → Document Mode
* Repository Navigation Snapshot provided
* Replay reconstructed from uploaded documentation
* Repository validation deferred

---

# Relationship to Other AFK Standards

| Standard                                | Responsibility                        |
| --------------------------------------- | ------------------------------------- |
| 000 — AFK Collaboration Principles      | Defines collaboration behaviour       |
| 010 — Project Foundation Standard       | Defines project identity and purpose  |
| 020 — Replay Document Creation Guide    | Defines replay artifact creation      |
| 030 — Understanding WWAN                | Defines operational project state     |
| 040 — Understanding Session Handoff     | Defines session continuity            |
| 050 — AFK Session Lifecycle             | Defines engineering session execution |
| 060 — Discovery Artifact Creation Guide | Defines discovery documentation       |

---

# Guiding Principle

> **The Project Boot Prompt is the operational bridge between the AFK framework and a specific engineering project. It orchestrates engineering state reconstruction by selecting the appropriate replay sequence, repository access model, and collaboration scope before engineering work begins.**

---

# Revision History

| Version | Date       | Description                                                                                                                                                            |
| ------- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1.0     | 2026-08-04 | Initial Project Boot Prompt Guide.                                                                                                                                     |
| 2.0     | 2026-08-04 | Expanded into Project Bootstrap Guide covering repository access modes, replay sequencing, engineering scope, repository inspection rules, and AI operating behaviour. |
