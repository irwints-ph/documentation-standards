# 📄 Project Boot Prompt Creation Guide

---

# Metadata

| Field | Value |
|--------|-------|
| Document | `025-project-boot-prompt-creation-guide.md` |
| Category | AFK Framework |
| Type | Canonical Engineering Standard |
| Status | 🟢 Active |
| Version | 1.0 |
| As Of | 2026-08-04 |

---

# Purpose

This document defines how an AFK **Project Boot Prompt** is created.

A Project Boot Prompt is **not** the project.

It is **not** the replay.

It is an operational artifact that tells an AI collaborator **how to reconstruct engineering state before engineering work begins.**

Its purpose is to minimize startup friction while ensuring every collaboration begins from sufficient engineering understanding.

---

# Why Project Boot Prompts Exist

AI collaborators should never begin work from assumptions.

Before implementation begins they must reconstruct engineering state.

The Project Boot Prompt provides the shortest path toward that reconstruction.

It tells the AI:

- what documents to read,
- in what order,
- what repository to inspect,
- what engineering context exists,
- when to stop,
- and when engineering work may begin.

---

# Relationship to Project Foundation

Project Foundation answers:

> **What is this project?**

Project Boot Prompt answers:

> **How should an AI reconstruct this project's engineering state?**

Project Foundation establishes purpose.

Project Boot Prompt establishes collaboration.

---

# Relationship to Replay Documents

Replay Documents preserve engineering knowledge.

The Project Boot Prompt does **not** duplicate Replay Documents.

Instead it orchestrates them.

```text
Replay Documents

        ↓

Project Boot Prompt

        ↓

Engineering State Reconstruction
```

---

# Relationship to AFK Collaboration

Every engineering collaboration follows:

```text
AFK Collaboration Principles

        ↓

AFK Operating Model

        ↓

Project Boot Prompt

        ↓

Replay Sequence

        ↓

Engineering State Reconstructed

        ↓

Engineering Work
```

---

# Lifecycle

## New Project

When no engineering knowledge exists:

```text
Kuwento Specs

↓

Project Foundation

↓

Engineering Begins
```

No replay exists yet.

The Project Boot Prompt is minimal.

---

## Established Project

Once sufficient engineering state exists:

```text
Project Foundation

↓

Replay Documents

↓

Project Boot Prompt

↓

Future Sessions
```

---

# Inputs

A Project Boot Prompt is generated from engineering artifacts.

## Required Inputs

- AFK Collaboration Principles
- AFK Operating Model
- Project Foundation
- Current Replay Documents

## Optional Inputs

- Repository Navigation Snapshot
- Context Shift Documents
- Current Validation Target
- Repository-specific onboarding notes

---

# Output

Produces:

```text
000-project-boot-prompt.md
```

This file becomes the operational entry point for future engineering sessions.

---

# Responsibilities

The Project Boot Prompt should:

- establish collaboration,
- define repository scope,
- identify current engineering objective,
- identify replay sequence,
- define repository inspection rules,
- define hold behaviour.

The Project Boot Prompt should **not**:

- duplicate replay documents,
- duplicate AFK principles,
- duplicate project foundation,
- contain implementation details,
- become a repository specification.

---

# Required Sections

Every Project Boot Prompt should contain:

---

## 1. Session Purpose

Why this collaboration exists.

Example:

> This session validates the Python implementation of the laboratory.

---

## 2. Repository Scope

Which repository is in scope.

Example:

```text
Current discovery target:

api/
```

---

## 3. Validation Target

Current engineering objective.

Examples:

- Discovery
- Documentation
- Validation
- Migration
- Refactoring
- Architecture Review

---

## 4. Required Documents

Documents to read before repository inspection.

Example:

```text
Read:

- AFK Collaboration Principles
- AFK Operating Model
- Project Foundation
- Replay Documents
```

---

## 5. Replay Sequence

Documents to reconstruct engineering state.

Example:

```text
Read:

000-project-boot-prompt.md

↓

000-repository-navigation-snapshot.md

↓

001-context-shift.md

↓

WWAN

↓

Session Handoff
```

---

## 6. Repository Rules

Specify whether repository inspection is available.

Examples:

### Workspace Mode

Repository inspection available.

Inspect repository directly.

Repository becomes source of truth.

### Document Mode

Repository unavailable.

Use Repository Navigation Snapshot.

Validate later when repository becomes available.

---

## 7. AI Behaviour

Define collaboration expectations.

Example:

- reconstruct engineering state first
- avoid assumptions
- separate observations from conclusions
- explain reasoning
- preserve engineering history
- ask questions when evidence is insufficient

---

## 8. Hold Behaviour

Example:

```text
After sufficient engineering state has been reconstructed:

HOLD

Await next engineering command.
```

---

# Creation Rules

When generating a Project Boot Prompt:

✔ Use current engineering state.

✔ Reference canonical documents.

✔ Reference replay documents.

✔ Keep prompts concise.

✔ Prefer references over duplication.

✔ Keep prompts AI-friendly.

✔ Keep prompts human-readable.

---

Do **not**:

✘ duplicate engineering knowledge,

✘ duplicate AFK framework documentation,

✘ embed large repository structures,

✘ embed large replay documents,

✘ embed implementation details.

---

# AI Generation Workflow

When creating a Project Boot Prompt:

```text
Read Project Foundation

↓

Read Replay Documents

↓

Identify engineering objective

↓

Identify replay sequence

↓

Determine repository access mode

↓

Generate concise operational prompt

↓

Validate against checklist
```

---

# Validation Checklist

A Project Boot Prompt is complete when:

☐ Project purpose is defined.

☐ Repository scope is defined.

☐ Current engineering objective is defined.

☐ Replay sequence is defined.

☐ Repository inspection rules are defined.

☐ AI behaviour is defined.

☐ Hold behaviour is defined.

☐ References canonical artifacts.

☐ Does not duplicate replay contents.

☐ Does not duplicate AFK documentation.

---

# Relationship to Replay Configuration

Conceptually:

```text
Project Foundation

↓

Replay Documents

↓

Replay Configuration

↓

Project Boot Prompt
```

Replay Configuration determines:

- what engineering state must be reconstructed,
- what order it should be reconstructed,
- what engineering objective is active.

The Project Boot Prompt is simply the operational rendering of that configuration.

---

# Guiding Principle

> **The Project Boot Prompt is not engineering knowledge. It is the operational recipe that tells an AI collaborator how to reconstruct engineering knowledge before engineering work begins.**

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 1.0 | 2026-08-04 | Initial Project Boot Prompt Creation Guide. |