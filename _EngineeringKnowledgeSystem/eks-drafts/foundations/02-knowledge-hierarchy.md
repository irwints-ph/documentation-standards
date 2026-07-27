# Engineering Knowledge System

# Knowledge Hierarchy (Draft)

---

## Status

🚧 Draft

---

# Purpose

This document defines the different layers of engineering knowledge captured
within the Engineering Knowledge System (EKS).

Not every document serves the same purpose.

Some describe software.

Some describe architecture.

Some describe engineering practices.

Others describe how knowledge itself is organized.

Understanding these layers helps ensure that information is stored in the
appropriate place and remains maintainable as the knowledge base grows.

---

# Proposed Knowledge Hierarchy

Engineering Knowledge System (EKS)

```
│
├── Principles
│
├── Methodologies
│
├── Standards
│
├── Patterns
│
├── Architecture
│
├── System Discovery
│
├── System Documentation
│
├── Operational Knowledge
│
├── Project Knowledge
│
└── Historical Knowledge
```

---

# Layer 1 — Principles

The highest level.

Principles explain *why* engineering decisions exist.

Examples

* Separation of Concerns
* Single Responsibility
* Composition over Inheritance
* Documentation before Optimization
* Evidence before Refactoring

These rarely change.

---

# Layer 2 — Methodologies

Methodologies explain *how work is performed.*

Examples

* Discovery Process
* Reverse Engineering Workflow
* Documentation Validation
* Legacy Modernization Process
* Architecture Discovery
* Repository Analysis

Methodologies are reusable across projects.

---

# Layer 3 — Standards

Standards define the expected engineering outcome.

Examples

* Documentation Standard
* Naming Standard
* Repository Standard
* Configuration Standard
* Component Documentation Standard

Standards evolve slowly.

---

# Layer 4 — Patterns

Patterns are recurring solutions observed across implementations.

Examples

* Composition Root
* Provider Composition
* Conditional Composition
* Hierarchical Composition
* Repository Pattern
* Factory Pattern

Patterns may later become standards.

---

# Layer 5 — Architecture

Architecture describes how a particular system is organized.

Examples

* Authentication Architecture
* Routing Architecture
* UI Composition Architecture
* Configuration Architecture

Architecture belongs to a specific project.

---

# Layer 6 — System Discovery

Discovery records observations while learning an existing system.

Examples

* Architecture Findings
* Folder Validation
* Legacy Inventory
* Component Registry
* Dependency Analysis

Discovery captures evidence.

It intentionally avoids making recommendations.

---

# Layer 7 — System Documentation

System Documentation explains how the software currently works.

Examples

* Layout.md
* Header.md
* Sidebar.md
* Auth Context.md

These documents describe implementation.

---

# Layer 8 — Operational Knowledge

Knowledge required to operate the system.

Examples

* Deployment
* Build Pipeline
* Environment Configuration
* Monitoring
* Support Procedures
* Incident Response

Usually maintained by development and operations teams.

---

# Layer 9 — Project Knowledge

Project-specific information.

Examples

* Roadmaps
* Current Status
* Technical Debt
* Milestones
* Decisions
* Release Notes

Project knowledge changes frequently.

---

# Layer 10 — Historical Knowledge

Historical records preserve engineering evolution.

Examples

* Discovery Logs
* Architecture Evolution
* Design Decisions
* Migration History
* Deprecated Components

Historical knowledge should never be discarded.

It provides engineering context.

---

# Relationship Between Layers

```

Principles
↓

Methodologies
↓

Standards
↓

Patterns
↓

Architecture
↓

Discovery
↓

Documentation
↓

Operations
↓

Projects
↓

History

```

Each layer builds upon the one above it.

Higher layers change infrequently.

Lower layers evolve continuously as software changes.

---

# Example

During discovery we observed:

* Composition Root
* Hierarchical Composition
* Conditional Composition

↓

These became Architecture Findings.

↓

After validating them across the repository,

↓

they may become Documentation Framework standards.

↓

Future projects can then adopt those standards without repeating the discovery process.

This demonstrates how engineering knowledge matures over time.

---

# Relationship to the EKS

This hierarchy provides the organizational model for the Engineering Knowledge System.

As the EKS grows, documents should be classified according to these knowledge layers rather than solely by file type or repository location.

---

# Future Work

Possible additions include:

* Knowledge lifecycle
* Knowledge ownership
* Evidence requirements
* Promotion workflow (Finding → Pattern → Standard)
* Cross-referencing strategy
* Search and indexing model
* AI-assisted knowledge retrieval

---

## I think we accidentally discovered something important

This hierarchy also explains **why** our documentation has felt so organized despite growing rapidly.

We were unconsciously separating knowledge into layers:

- `registry/` → **System Documentation**
- `architecture/findings/` → **Discovery**
- `configuration/` → **Architecture**
- Documentation Framework (planned) → **Standards**
- EKS → **Methodologies**
- This new document → **Knowledge Model**

That's a significant insight because it suggests the EKS isn't just "documentation." It's a system for managing engineering knowledge at different levels of abstraction.

One addition I'd eventually make is a document like **`knowledge-lifecycle.md`**, which would formalize how an observation progresses through the hierarchy:

> Observation → Discovery Finding → Validated Pattern → Engineering Standard → Methodology → Organizational Knowledge

That progression captures exactly what we've been doing over the past few sessions and could become one of the foundational concepts of the EKS.
```
