# 🏗️ Code Architecture

---

# Purpose

This document captures the **current software architecture** of Project Foundation (PF).

Its purpose is to describe how the repository is organized from an engineering perspective, identify subsystem responsibilities, explain how components collaborate, and establish a baseline architectural understanding before any future improvements are introduced.

Unlike the Code Execution Flow document, which focuses on **runtime behavior**, this document focuses on the **static architecture** of the codebase.

---

# Architectural Philosophy

Project Foundation follows a lightweight layered architecture built around **single-responsibility engineering units**.

Each subsystem owns one clearly defined responsibility and communicates through well-defined interfaces.

The architecture emphasizes:

* Simplicity
* Maintainability
* Separation of concerns
* Testability
* Reusability

---

# Architectural Overview

Current architecture:

```text id="bpzl0x"
                 CLI
                  │
                  ▼
             Commands Layer
                  │
        ┌─────────┴─────────┐
        ▼                   ▼
   Repository          Tree Parser
    Scanner
        │                   │
        └─────────┬─────────┘
                  ▼
          Repository Model
                  │
                  ▼
            Tree Printer
```

The Repository Model serves as the central contract between all major subsystems.

---

# Layer Responsibilities

## CLI Layer

Location

```text id="k97x5t"
src/pf/__main__.py
```

Responsibilities

* Application entry point
* CLI initialization
* Argument parsing
* Runtime startup

This layer should contain almost no business logic.

---

## Command Layer

Location

```text id="9m7hwb"
src/pf/cli/
```

Responsibilities

* Orchestrate workflows
* Coordinate subsystem interaction
* Validate command inputs
* Return user-facing output

This layer acts as the controller of the application.

---

## Discovery Layer

Location

```text id="7l7p64"
src/pf/scanner/
```

Responsibilities

* Filesystem traversal
* Ignore rule application
* Repository discovery
* Repository construction

This layer converts the operating system filesystem into the internal Repository model.

---

## Serialization Layer

Location

```text id="xeh58n"
src/pf/parsers/
```

Responsibilities

* Deserialize repository trees
* Reconstruct Repository objects
* Parse exported structures

Unlike the Scanner, this layer operates on serialized representations rather than the filesystem.

---

## Presentation Layer

Location

```text id="phz1qu"
src/pf/printers/
```

Responsibilities

* Repository visualization
* Tree rendering
* Console presentation

Presentation remains isolated from repository discovery.

---

## Domain Layer

Location

```text id="f2e7p6"
src/pf/models/
```

Responsibilities

* Repository abstraction
* Directory representation
* File representation
* Parent-child relationships

This layer represents the business domain of Project Foundation.

Every major subsystem depends on this layer.

---

## Configuration Layer

Location

```text id="u57msv"
pyproject.toml
```

Responsibilities

* Project metadata
* Packaging
* Build configuration
* CLI registration

This layer exists outside the runtime architecture but defines how the project is executed.

---

# Dependency Relationships

The architectural dependency direction is intentionally one-way.

```text id="0k2i7y"
CLI
        │
        ▼
Commands
        │
        ▼
Scanner / Parser
        │
        ▼
Repository Model
        ▲
        │
Printer
```

Notice that:

* The Scanner builds the Repository.
* The Parser reconstructs the Repository.
* The Printer consumes the Repository.
* None of these depend on each other directly.

Instead, they communicate through the shared domain model.

---

# Repository Model

The Repository Model represents the architectural center of PF.

```text id="r9eb20"
Repository
        │
        ▼
Directory
        │
        ├── Directory
        │
        └── File
```

Every subsystem either:

* Creates
* Modifies
* Reads

the Repository model.

This makes it the core contract of the application.

---

# Architectural Characteristics

## High Cohesion

Each subsystem performs one engineering responsibility.

Examples:

| Subsystem | Responsibility        |
| --------- | --------------------- |
| Scanner   | Discovery             |
| Parser    | Reconstruction        |
| Printer   | Presentation          |
| Models    | Domain representation |

---

## Low Coupling

Subsystems communicate almost exclusively through the Repository model.

Direct subsystem dependencies remain minimal.

---

## Layer Independence

Presentation does not know how discovery works.

Discovery does not know how rendering works.

Parsing does not know how discovery works.

This separation improves maintainability.

---

# Current Architectural Strengths

✅ Clear layering

✅ Central domain model

✅ Small orchestration layer

✅ Modern packaging

✅ Clean dependency direction

✅ Easy to understand

---

# Architectural Opportunities

Future architectural growth may introduce additional layers such as:

```text id="p8otgr"
Export

Archive

Discovery Package

Configuration Profiles

Plugin System

Repository Comparison

Workspace Support
```

These should remain independent subsystems rather than expanding existing layers.

---

# Relationship to AFK

One important discovery during this engineering review was that the architecture naturally aligns with the AFK Discovery methodology.

Instead of documenting arbitrary folders, the repository organizes naturally into **Discovery Units**.

```text id="j3ibyr"
Architecture

↓

Engineering Responsibilities

↓

Discovery Units

↓

Engineering Documentation
```

This validation strengthened the AFK framework itself.

---

# Related Discovery Documents

## Repository Discovery

* `01-current-pf-codebase.md`

## Validation

* `02-pf-code-validation.md`

## Runtime

* `code-execution-flow/main-flow.md`

## Handoff

* `_docs/02-handoff/01-engineering-handoff.md`

---

# Discovery Notes

The architecture documented here represents the repository at the completion of Journey 1 (Discovery).

Future engineering work should preserve the architectural principles established here whenever possible.

Architectural changes introduced in later journeys should be documented separately to maintain the historical evolution of the project.

---

## Metadata

| Field    | Value                     |
| -------- | ------------------------- |
| Document | `03-code-architecture.md` |
| Scope    | Project Foundation        |
| Category | Discovery                 |
| Type     | Software Architecture     |
| Status   | Reviewed                  |
| Version  | 1.0                       |
| As Of    | 07.30.2026                |
