# 📄 AFK Document Information Architecture

---

# Metadata

| Field    | Value                                          |
| -------- | ---------------------------------------------- |
| Document | `000-afk-document-information-architecture.md` |
| Scope    | AFK Documentation System                       |
| Category | Documentation Architecture                     |
| Status   | 🚧 Living                                      |
| Owner    | AFK                                            |
| Version  | 0.1                                            |

---

# Purpose

This document defines the engineering responsibilities of each folder within the AFK documentation system.

Rather than organizing documents by file type, AFK organizes documentation by **engineering responsibility**.

When a new document emerges, this document should be consulted before deciding where it belongs.

---

# Guiding Principle

> **Folders represent engineering responsibilities, not storage locations.**

Each folder exists because it answers a different engineering question.

---

# Current Information Architecture

```text
docs/
├── collaboration/
├── concepts/
├── culture/
├── emerging-practices/
├── engineering-artifacts/
├── future-concepts/
├── journeys/
├── methodology/
├── playbooks/
├── procedures/
├── reference-sessions/
└── showcase/
```

---

# Folder Responsibilities

---

## collaboration/

### Purpose

Defines how humans and AI collaborators interact during an AFK engineering session.

### Contains

* Boot prompt guidance
* Collaboration commands
* Session initialization
* Shared collaboration practices

### Does Not Contain

* Engineering standards
* Project documentation
* Methodology explanations

Engineering Question

> **How do collaborators work together?**

---

## concepts/

### Purpose

Introduces foundational AFK ideas.

### Contains

* Concept definitions
* Core philosophy
* Mental models

Engineering Question

> **What does this idea mean?**

---

## culture/

### Purpose

Captures the values and behaviors that emerged through AFK collaboration.

### Contains

* Cultural observations
* Collaboration values
* Engineering mindset

Engineering Question

> **How do we behave while engineering?**

---

## emerging-practices/

### Purpose

Documents practices that have demonstrated value but require additional validation before becoming accepted methodology.

### Contains

* Repeatable observations
* Candidate engineering practices
* Experimental workflows

Engineering Question

> **What appears to work repeatedly?**

---

## engineering-artifacts/

### Purpose

Defines the reusable engineering artifacts used throughout AFK.

Each artifact represents a reusable engineering interface.

Examples include:

* WWAN
* Engineering Replay
* Engineering Context
* Validation
* Knowledge Capture

Each artifact should describe:

* Purpose
* Inputs
* Outputs
* Relationships
* Recommended engineering prompts

Engineering Question

> **Which engineering artifact should I use?**

---

## future-concepts/

### Purpose

Stores ideas that have not yet reached proposal maturity.

### Contains

* Brainstorms
* Early observations
* Unvalidated concepts

Engineering Question

> **What might become valuable later?**

---

## journeys/

### Purpose

Documents complete engineering journeys from beginning to end.

### Contains

* Multi-stage engineering initiatives
* End-to-end project narratives
* Long-running objectives

Engineering Question

> **How did this engineering journey evolve?**

---

## methodology/

### Purpose

Defines how AFK performs engineering.

### Contains

* Engineering lifecycle
* Progressive methodology
* Discovery methodology
* Validation methodology
* Engineering workflows

Engineering Question

> **How does AFK perform engineering?**

---

## playbooks/

### Purpose

Provides repeatable engineering workflows for specific objectives.

Examples:

* Resume Engineering
* Opportunity Evaluation
* Documentation Validation

Engineering Question

> **How do I solve this recurring engineering problem?**

---

## procedures/

### Purpose

Provides operational, step-by-step instructions.

### Contains

* Tool usage
* Administrative procedures
* Operational tasks

Engineering Question

> **How do I execute this task?**

---

## reference-sessions/

### Purpose

Preserves complete engineering collaboration sessions that demonstrate AFK in practice.

These documents serve as reference implementations rather than methodology.

Engineering Question

> **Can I see a complete example?**

---

## showcase/

### Purpose

Demonstrates AFK outcomes.

### Contains

* Public demonstrations
* Images
* Success stories
* Presentation material

Engineering Question

> **What has AFK produced?**

---

# Folder Selection Process

When creating a new document, determine its engineering responsibility first.

Ask:

1. What engineering question does this document answer?
2. Which folder already owns that responsibility?
3. Does the document introduce a genuinely new responsibility?

Only introduce new folders when an entirely new engineering responsibility emerges.

---

# Evolution Policy

The documentation structure should evolve conservatively.

Preference order:

1. Extend an existing folder.
2. Refine folder responsibilities.
3. Create a new folder only when necessary.

---

# Current Assessment

The current AFK documentation architecture separates responsibilities clearly enough to support continued framework growth.

Future refinements should focus on clarifying responsibilities rather than increasing folder count.

---

# Guiding Principle

> **Every folder exists because it owns an engineering responsibility.**
