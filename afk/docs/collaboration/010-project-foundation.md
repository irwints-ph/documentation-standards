# 🤝 Project Foundation

> **Every engineering session begins by reconstructing the project's engineering state before understanding its implementation.**

---

# Purpose

The Project Foundation establishes the initial **engineering state** shared between Human Collaborators (HC) and AI Collaborators (AC).

Before reading source code, both collaborators should understand:

* why the project exists;
* who it serves;
* what it currently does;
* what engineering work is currently being performed;
* what is already known.

This creates the initial engineering context that allows future discovery, design, implementation, validation, and knowledge capture to build upon a common understanding.

---

# Objective

Capture the minimum engineering understanding required to begin collaborating on an existing project.

The objective is **engineering state reconstruction**, not complete documentation.

---

# Engineering State Reconstruction

AFK does **not** attempt to preserve conversations.

AFK preserves **engineering state**.

Engineering state allows any Human or AI Collaborator to safely continue engineering work without requiring access to previous conversations.

The Project Foundation establishes the first layer of that engineering state.

---

# What to Capture

## Project Overview

Describe the project at a high level.

Examples:

* Internal business application
* Customer-facing website
* API service
* Shared component library
* Mobile application

---

## Purpose

Why does this project exist?

What business problem does it solve?

---

## Users

Who uses the system?

Examples:

* Customers
* Internal users
* Administrators
* Engineers
* External systems

---

## Current Engineering Objective

Describe the current engineering objective.

Examples:

* Understand the existing implementation
* Validate architecture
* Continue engineering
* Improve maintainability
* Add new functionality
* Prepare for migration

This describes the engineering mission rather than a specific wish.

---

## Technology Stack

Record only technologies immediately relevant to engineering.

Examples:

* React
* Angular
* Vue
* TypeScript
* .NET
* Java
* Node.js
* PostgreSQL

Detailed technical discovery belongs to Journey 1.

---

## Known Constraints

Capture important information already known.

Examples:

* Legacy system
* Production application
* Active users
* Active development
* Regulatory requirements
* Performance requirements

---

## Current Engineering State

Summarize what is already known.

Examples:

* Discovery has begun.
* Architecture is partially documented.
* Engineering is performed incrementally.
* Bootstrap migration is partially complete.
* Repository documentation framework is established.

This section provides continuity between engineering sessions.

---

# Example

```markdown
## Project Overview

Internal frontend application used to manage customer transactions.

---

## Purpose

Provide operational staff with a unified interface for managing customer workflows.

---

## Users

- Operations Team
- Customer Support
- Administrators

---

## Current Engineering Objective

Incrementally improve and document the system while preserving production behavior.

---

## Technology Stack

- React
- TypeScript
- OIDC
- REST APIs

---

## Known Constraints

- Large existing codebase
- Production system
- Active development

---

## Current Engineering State

- Incremental engineering workflow established.
- Discovery performed one Engineering Unit at a time.
- Documentation evolves alongside engineering.
```

---

# Engineering Notes

Keep this document concise.

Avoid documenting:

* implementation details;
* architecture;
* APIs;
* folder structures;
* components;
* execution flows.

Those belong to Discovery.

The Project Foundation answers one question:

> **"What engineering state are we entering?"**

---

# Relationship to Other Documents

The Project Foundation establishes the initial engineering state.

After completing it:

➡ Read the project's WWAN (if available)

Then continue with:

* Repository Structure
* Engineering Context
* Engineering Unit Discovery

---

# Guiding Principles

> **Understand the engineering state before understanding the implementation.**

> **AFK preserves engineering state, not conversations.**

A reconstructed engineering state allows any collaborator to safely continue engineering work, even in a completely new session.

---

## Metadata

| Field    | Value                       |
| -------- | --------------------------- |
| Document | `010-project-foundation.md` |
| Type     | Collaboration               |
| Version  | 3.0                         |
| Status   | ✅ Active                    |
| As of    | 07.31.2026                  |
