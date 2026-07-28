# 📄 Repository Organization

---

## Metadata

| Field    | Value                            |
| -------- | -------------------------------- |
| Document | `repository-organization.md`     |
| Scope    | Engineering Knowledge Repository |
| Category | Collaboration Framework          |
| Type     | Reference Guide                  |
| Status   | Active                           |

---

# Purpose

This document defines the organizational principles of the Engineering Knowledge Repository.

Its purpose is to ensure that Human collaborators and AI collaborators organize knowledge consistently across all projects.

Rather than prescribing a single project structure, this document explains **where engineering knowledge belongs** and **why it belongs there**.

---

# Design Philosophy

The repository is organized around four principles:

* Separation of concerns
* Reusable knowledge
* Project independence
* Human and AI readability

Every document should have a clear owner and a clear purpose.

---

# Repository Overview

```text
Repository

├── _collaboration/
├── _docs/
├── _tools/
│
├── afk/
├── eds/
├── eks/
│
├── README.md
└── wwan.md
```

---

# Repository Root

The repository root represents the entire Engineering Knowledge Repository.

Root-level files describe the repository as a whole.

Examples:

* README
* Repository WWAN

The root should remain lightweight.

---

# _collaboration

Purpose:

Reusable collaboration assets shared across every project.

Examples:

* Boot Prompt Templates
* Session Record Templates
* Repository Organization
* Collaboration Playbooks

These documents explain **how people and AI collaborate**, not how individual projects work.

---

# _docs

Purpose:

Repository-wide operational documents.

Examples include:

* Repository Discovery
* Repository Wishes
* Repository Build Plans

These documents describe improvements to the repository itself.

They are **not** part of AFK, EDS, or EKS.

---

# _tools

Purpose:

Reusable tooling.

Examples:

* Project bootstrap scripts
* Templates
* Automation
* Utilities

The tools should remain reusable and independent of any specific project.

---

# AFK

Purpose:

Assisted Flow of Knowledge.

AFK documents define the collaboration methodology.

Examples:

* Discovery
* WWAN
* Collaboration
* Journeys
* Methodology
* Culture

AFK answers:

> How do we collaborate?

---

# EDS

Purpose:

Engineering Documentation System.

EDS defines documentation standards.

Examples:

* Naming
* Templates
* Status Lifecycle
* References
* Git Workflow

EDS answers:

> How do we document engineering?

---

# EKS

Purpose:

Engineering Knowledge System.

EKS captures higher-level engineering thinking.

Examples:

* Knowledge Lifecycle
* Discovery Methodology
* Knowledge Taxonomy
* Knowledge Presentation

EKS answers:

> How is engineering knowledge preserved?

---

# Project Structure

Projects created using AFK should remain self-contained.

Typical structure:

```text
project/

docs/

implementation/

README.md

roadmap.md

scratch.md

wwan.md
```

Projects should never depend on the internal structure of another project.

---

# Living vs Historical Documents

Some documents evolve continuously.

Examples:

* WWAN
* Roadmap
* Scratch

These are **living documents**.

Others permanently capture a point in time.

Examples:

* Session Records
* Discovery Outputs
* Granted Wishes

These are **historical artifacts**.

---

# Document Ownership

Every document should have one primary owner.

| Area           | Owns                         |
| -------------- | ---------------------------- |
| _collaboration | Collaboration assets         |
| _docs          | Repository operations        |
| _tools         | Automation and templates     |
| AFK            | Collaboration methodology    |
| EDS            | Documentation standards      |
| EKS            | Knowledge methodology        |
| Project        | Project-specific engineering |

Ownership should never overlap unnecessarily.

---

# Organizational Rules

* Keep reusable assets outside individual projects.
* Keep project-specific knowledge inside the project.
* Avoid duplicate documents.
* Prefer references over copies.
* Separate methodology from implementation.
* Preserve engineering history.
* Optimize for Human and AI navigation.

---

# Guiding Principle

A collaborator should be able to locate any engineering artifact by asking two questions:

1. **What is it?**
2. **Who owns it?**

If those two questions cannot be answered immediately, the document is probably in the wrong place.

The goal of this repository is not only to preserve engineering knowledge—it is to make that knowledge easy to discover, understand, and extend across projects and collaboration sessions.
