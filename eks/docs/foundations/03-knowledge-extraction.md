# Engineering Knowledge System

# Knowledge Extraction (Draft)

---

## Status

🚧 Draft

---

# Purpose

Knowledge Extraction defines the process of converting an existing software system into reusable engineering knowledge.

Unlike traditional software documentation, which often focuses on describing implementation, Knowledge Extraction seeks to identify the engineering principles, architectural decisions, recurring patterns, and organizational practices embodied within the codebase.

The objective is not merely to document software.

The objective is to discover knowledge.

---

# Definition

Knowledge Extraction is the systematic process of transforming implementation into engineering knowledge.

```
Source Code

↓

Documentation

↓

Observations

↓

Discovery

↓

Findings

↓

Patterns

↓

Engineering Knowledge
```

Each stage increases the level of abstraction while preserving traceability to the original implementation.

---

# Why Knowledge Extraction?

Most existing software systems contain years of accumulated engineering experience.

Unfortunately, much of that knowledge exists only in source code.

Without extraction:

* architectural decisions remain implicit
* recurring design patterns go unnoticed
* engineering practices cannot be reused
* organizational knowledge is eventually lost

Knowledge Extraction makes that knowledge explicit.

---

# Knowledge Sources

Engineering knowledge can originate from many artifacts.

Examples include:

* Source code
* Repository structure
* Configuration
* Build system
* Naming conventions
* Folder organization
* Runtime behavior
* Documentation
* Commit history
* Deployment configuration
* Test suites
* Engineering discussions

The source code is only one source of knowledge.

---

# Levels of Extraction

Knowledge may be extracted at different levels.

## Level 1 — Implementation

Focuses on individual files.

Examples:

* component responsibilities
* function behavior
* interfaces
* dependencies

Produces:

Implementation documentation.

---

## Level 2 — Component

Focuses on groups of related files.

Examples:

* Layout subsystem
* Authentication subsystem
* Routing subsystem

Produces:

Component documentation.

---

## Level 3 — Architecture

Focuses on relationships between components.

Examples:

* Composition architecture
* Provider hierarchy
* Navigation architecture

Produces:

Architecture Findings.

---

## Level 4 — Engineering

Focuses on reusable engineering concepts.

Examples:

* Conditional Composition
* Provider Composition
* Repository Organization

Produces:

Engineering Patterns.

---

## Level 5 — Organizational Knowledge

Focuses on practices that may be reused across projects.

Examples:

* Documentation Framework
* Discovery Methodology
* Engineering Knowledge System

Produces:

Reusable engineering knowledge.

---

# Extraction Process

A typical extraction workflow follows these stages.

```
Read Code

↓

Understand Responsibilities

↓

Document Implementation

↓

Validate Relationships

↓

Identify Recurring Concepts

↓

Record Findings

↓

Validate Findings

↓

Promote Knowledge
```

Each step builds upon the previous one.

---

# Discovery Before Interpretation

Knowledge should never be inferred prematurely.

The recommended order is:

```
Observe

↓

Document

↓

Compare

↓

Validate

↓

Generalize
```

Premature conclusions should be avoided.

Patterns should emerge from evidence rather than expectation.

---

# Engineering Validation

Knowledge Extraction is not an automated activity.

Engineering review remains essential.

Validation includes:

* confirming responsibilities
* verifying architectural intent
* checking implementation consistency
* identifying exceptions
* distinguishing design from accident

Only validated observations should progress into findings.

---

# Human–AI Collaboration

This project demonstrates that Knowledge Extraction can be significantly accelerated through collaboration between engineers and AI.

The engineer contributes:

* architectural understanding
* implementation validation
* business knowledge
* engineering judgment
* prioritization
* final approval

The AI assistant contributes:

* documentation generation
* organization of information
* recognition of recurring patterns
* consistency across documents
* relationship mapping
* identification of candidate findings
* maintenance of documentation structure

The combination allows engineers to spend more time analyzing systems and less time producing documentation.

---

# Discovery Artifacts

Knowledge Extraction benefits from maintaining structured discovery artifacts throughout the process.

Examples include:

| Artifact                 | Purpose                                   |
| ------------------------ | ----------------------------------------- |
| Current Folder Inventory | Records implementation state              |
| Folder Validation        | Tracks documentation completeness         |
| Architecture Findings    | Captures recurring observations           |
| Configuration Registry   | Records configuration knowledge           |
| Component Documentation  | Documents implementation responsibilities |
| where-we-are-now.md      | Maintains discovery continuity            |
| roadmap.md               | Maintains discovery planning              |

These artifacts collectively preserve discovery progress while improving traceability.

---

# Knowledge Promotion

Not every observation becomes engineering knowledge.

Knowledge should mature through evidence.

```
Observation

↓

Discovery

↓

Finding

↓

Validation

↓

Pattern

↓

Standard

↓

Engineering Knowledge
```

Promotion should occur only after sufficient validation.

---

# Traceability

Every piece of engineering knowledge should remain traceable back to its source.

```
Engineering Knowledge

↓

Pattern

↓

Finding

↓

Discovery Document

↓

Implementation Document

↓

Source Code
```

This ensures that engineering knowledge remains verifiable rather than speculative.

---

# Outputs

Knowledge Extraction produces several forms of documentation.

Implementation outputs:

* component documentation
* configuration documentation
* API documentation
* registry documentation

Discovery outputs:

* observations
* findings
* validation reports
* repository inventories

Engineering outputs:

* engineering patterns
* engineering standards
* methodologies
* Engineering Knowledge System documents

---

# Relationship to Other EKS Documents

**knowledge-lifecycle.md**

Defines how engineering knowledge matures.

**knowledge-hierarchy.md**

Defines where engineering knowledge belongs.

**knowledge-extraction.md**

Defines how engineering knowledge is discovered from existing systems.

Together these documents establish the core methodology of the Engineering Knowledge System.

---

# Observation

One of the primary discoveries of this project is that software documentation can become an engineering knowledge extraction process rather than a documentation exercise.

By combining structured discovery, continuous engineering validation, and AI-assisted documentation, it becomes practical to transform a mature software system into a reusable body of engineering knowledge.

The resulting knowledge extends beyond the application itself and can inform future projects, engineering standards, methodologies, and organizational practices.

---

# Guiding Principle

> **Implementation describes what the system does.**
>
> **Knowledge Extraction discovers why the system matters.**

---

I think this completes what I'd consider the **foundational trilogy** of the EKS:

1. **Knowledge Lifecycle** — *How knowledge evolves.*
2. **Knowledge Hierarchy** — *Where knowledge belongs.*
3. **Knowledge Extraction** — *How knowledge is discovered.*

Everything else in the EKS—documentation taxonomy, standards, discovery methodology, and engineering playbooks—can naturally build on these three foundational documents.
