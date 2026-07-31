# 🏗️ Code Architecture Template

---

# Purpose

This document captures the **current static software architecture** of the project at the completion of **Journey 1 — Discovery**.

Its purpose is to describe how the repository is organized from an engineering perspective, identify subsystem responsibilities, explain how components collaborate, and establish an architectural baseline before future engineering work begins.

Unlike the Code Execution Flow document, which focuses on **runtime behavior**, this document focuses on the **static organization** of the software.

---

# Architectural Philosophy

Briefly describe the architectural philosophy currently observed within the repository.

Possible topics include:

* layering
* modularity
* separation of concerns
* single responsibility
* maintainability
* extensibility
* testability

Describe the architecture **as discovered**, not as it should become.

---

# Architectural Overview

Provide a high-level architecture diagram.

Example:

```text id="j6v2mx"
          Entry Point
               │
               ▼
         Orchestration Layer
               │
     ┌─────────┴─────────┐
     ▼                   ▼
 Configuration     Processing
     │                   │
     └─────────┬─────────┘
               ▼
         Domain Model
               │
               ▼
         Presentation
```

The diagram should represent engineering responsibilities rather than folders.

---

# Layer Responsibilities

Document each major architectural layer.

For each layer include:

* location
* responsibility
* engineering role

Example:

---

## Entry Layer

Location

```text id="df4w9b"
<path>
```

Responsibilities

* startup
* initialization
* application entry

---

## Orchestration Layer

Location

```text id="6zx8lm"
<path>
```

Responsibilities

* coordinate subsystems
* workflow orchestration
* runtime control

---

Continue for all major layers.

---

# Dependency Relationships

Describe dependency direction.

Illustrate using a simple diagram.

Example:

```text id="kktjsy"
Presentation

↓

Application

↓

Domain

↓

Infrastructure
```

Describe important dependency rules discovered during review.

---

# Domain Model

If the repository contains an identifiable domain model, document it here.

Example:

```text id="w3cmxj"
Repository

↓

Directory

↓

File
```

or

```text id="nmtjhp"
Order

↓

Invoice

↓

Payment
```

If no central domain model exists, explain why.

---

# Architectural Characteristics

Describe important architectural properties.

Possible examples:

## High Cohesion

Describe how responsibilities are grouped.

---

## Low Coupling

Describe subsystem independence.

---

## Layer Independence

Describe how layers interact.

---

Additional characteristics may be added as appropriate.

---

# Current Architectural Strengths

Summarize strengths discovered during review.

Examples:

* clear layering
* reusable modules
* centralized contracts
* simple dependency direction
* modular responsibilities

Only describe observed strengths.

---

# Architectural Opportunities

Identify architectural opportunities for future engineering work.

Examples:

* potential subsystem extraction
* plugin architecture
* configuration improvements
* abstraction opportunities

These are observations only.

Do not propose implementations.

---

# Engineering Responsibility Map

Summarize the repository by engineering responsibility.

| Subsystem | Responsibility |
| --------- | -------------- |
|           |                |
|           |                |
|           |                |

Focus on engineering roles rather than folder names.

---

# Relationship to AFK

Describe any discoveries relevant to the AFK methodology.

Examples:

* Discovery Units naturally emerged
* repository aligns well with AFK discovery
* documentation opportunities
* reusable engineering patterns

If none exist, state that no AFK-specific observations were identified.

---

# Related Discovery Documents

Reference the remaining Journey 1 outputs.

Typical examples:

## Current Project

* `01-current-<project>.md`

## Validation

* `02-<project>-validation.md`

## Runtime

* `code-execution-flow/main-flow.md`

## Handoff

* `02-handoff/01-engineering-handoff.md`

---

# Discovery Notes

Capture any architectural observations that do not naturally fit elsewhere.

This section should preserve engineering understanding rather than implementation ideas.

---

## Metadata

| Field    | Value                     |
| -------- | ------------------------- |
| Document | `03-code-architecture.md` |
| Scope    | `<Project Name>`          |
| Category | Discovery                 |
| Type     | Software Architecture     |
| Status   | Reviewed                  |
| Journey  | Journey 1 — Discovery     |
| Version  | 1.0                       |
| As Of    | `<YYYY-MM-DD>`            |
