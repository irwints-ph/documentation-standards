# 💡 Proposal — Engineering Replay

> **Capture how today's architecture came to exist.**

---

# Metadata

| Field    | Value                         |
| -------- | ----------------------------- |
| Document | `002-engineering-replay.md`   |
| Category | Emerging Engineering Concepts |
| Type     | Proposal                      |
| Status   | 🚧 Draft                      |
| Owner    | Engineering                   |
| Version  | 0.1                           |

---

# Purpose

This proposal introduces the concept of an **Engineering Replay**.

An Engineering Replay is a concise engineering narrative that explains how the current architecture evolved from the previous major engineering milestone.

Unlike a project history or implementation log, a Replay intentionally summarizes only the architectural changes necessary for future engineers and AI collaborators to understand the current system.

Its objective is to minimize context reconstruction after significant project evolution.

---

# Background

During long-running engineering projects, software naturally evolves.

Major refactors, migrations, architectural improvements, and production releases often leave behind a large collection of valuable engineering artifacts:

* discovery documents
* architecture documents
* implementation notes
* validation reports
* source code
* tests

Although these artifacts preserve engineering decisions, understanding the current system may still require reading dozens of documents.

This creates unnecessary reconstruction effort for both humans and AI collaborators.

---

# The Observation

WWAN answers:

> **Where are we now?**

Replay answers:

> **How did today's architecture become today's architecture?**

These are different engineering questions.

WWAN provides operational continuity.

Replay provides architectural continuity.

---

# Proposed Definition

An **Engineering Replay** is a concise architectural narrative that explains how the current system evolved from the previous major engineering milestone.

Rather than documenting every engineering event, Replay summarizes only the changes that shaped the architecture that exists today.

---

# Characteristics

An Engineering Replay should:

* remain concise
* focus on architectural evolution
* explain *why* major changes occurred
* avoid implementation detail inside the document
* reference supporting engineering artifacts
* serve as the primary onboarding narrative for the current architecture

Replay is intended to reduce reading effort rather than increase documentation volume.

---

# Engineering Philosophy

Replay is **not** intended to replace engineering documentation.

Instead, it connects existing documentation into a coherent engineering story.

A Replay should explain:

* what changed
* why it changed
* what emerged
* where supporting evidence can be found

---

# Relationship to Engineering Artifacts

Replay summarizes.

Artifacts provide the evidence.

Every major Replay section should reference the supporting engineering artifacts.

Examples include:

## Documentation

* Architecture documents
* Discovery reports
* Validation reports
* Standards

## Source

* Major source folders
* Refactored components
* Entry points

## Verification

* Tests
* Benchmarks
* Validation evidence

Replay becomes the navigation layer rather than the implementation itself.

---

# Relationship to WWAN

WWAN answers:

> **Where are we now?**

Replay answers:

> **How did today's architecture become today's architecture?**

A collaborator typically consumes them in this order:

```text
Latest Replay
        ↓
Current WWAN
        ↓
Continue Engineering
```

---

# Relationship to AFK

Within AFK, Replay supports collaboration continuity after major engineering evolution.

Instead of reconstructing months of engineering work from conversation history or scattered documentation, collaborators begin with the latest Replay.

Replay provides shared understanding before operational work resumes.

---

# Relationship to EKS

Replay may eventually become one mechanism for engineering knowledge extraction.

Rather than preserving every engineering event, Replay captures the architectural lessons that remain valuable after implementation.

Potential future flow:

```text
Engineering Work
        ↓
Discovery
        ↓
Architecture
        ↓
Implementation
        ↓
Validation
        ↓
Major Milestone
        ↓
Engineering Replay
        ↓
Knowledge Extraction
```

This relationship remains under evaluation.

---

# Proposed Lifecycle

```text
Replay 001
        ↓
Major Engineering Evolution
        ↓
Replay 002
        ↓
Major Engineering Evolution
        ↓
Replay 003
```

Each Replay builds upon the previous Replay rather than attempting to document the project's entire history.

---

# Potential Triggers

An Engineering Replay may be created after:

* major production release
* significant architectural refactor
* migration completion
* platform transition
* major capability expansion
* other engineering milestones that materially change the architecture

---

# Non-Goals

Replay is not intended to become:

* project history
* implementation guide
* meeting minutes
* discovery journal
* architecture specification

Those artifacts continue to exist independently.

Replay summarizes them.

---

# Open Questions

The following areas require practical validation before standardization:

* Recommended document size
* Naming convention
* Folder location
* Versioning strategy
* Relationship with Knowledge Packages
* Relationship with Canon Events
* Whether Replay belongs primarily to AFK, EKS, or EDS

---

# Current Assessment

Engineering Replay appears to complement existing AFK concepts by preserving architectural understanding after significant project evolution.

Additional validation across multiple engineering projects is recommended before promoting this concept into an official framework.

---

# Guiding Principle

> **Replay tells the story. Artifacts prove the story.**
