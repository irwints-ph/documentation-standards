# 📄 Project Foundation Standard

---

# Metadata

| Field | Value |
|--------|-------|
| Document | `010-project-foundation-standard.md` |
| Category | AFK Framework |
| Type | Canonical Engineering Standard |
| Status | 🟢 Active |
| Version | 1.0 |
| As Of | 2026-08-04 |

---

# Purpose

This document defines the **Project Foundation** within the Assisted Flow of Knowledge (AFK) framework.

Project Foundation establishes the minimum engineering understanding required before implementation begins.

It provides the initial engineering context from which all future engineering knowledge evolves.

---

# Why Project Foundation Exists

Engineering cannot begin without a shared understanding of the problem.

Traditional projects often jump directly into implementation, leaving assumptions undocumented and project intent fragmented.

Project Foundation prevents this by establishing a shared understanding before engineering decisions are made.

It answers questions such as:

- What are we building?
- Why does it exist?
- Who does it serve?
- What problem does it solve?
- What are the goals?
- What constraints exist?
- What defines success?

---

# Relationship to Kuwento Specs

Within AFK, **Kuwento Specs** is the preferred method for establishing Project Foundation.

Kuwento Specs guides collaborators through a structured conversation that captures the project's purpose, context, and engineering intent.

Rather than producing requirements immediately, Kuwento Specs builds a shared understanding that becomes the project's canonical foundation.

Once completed, Project Foundation becomes the source from which all future engineering artifacts derive.

---

# Project Foundation Lifecycle

A project should establish its Project Foundation only once.

```text
New Project

↓

Kuwento Specs

↓

Project Foundation Established

↓

Engineering Begins
```

Project Foundation is considered stable unless the project's mission or scope fundamentally changes.

---

# Required Elements

A Project Foundation should establish the following:

## Project Identity

- Project name
- Parent system (if applicable)
- Documentation framework
- Repository (if known)

---

## Purpose

Clearly describe why the project exists.

Purpose should remain stable throughout the project's lifetime.

---

## Context

Describe the environment in which the project operates.

Examples include:

- business domain
- engineering domain
- operational environment
- stakeholders
- existing systems

---

## Problem Statement

Describe the engineering problem being solved.

The focus should remain on the underlying problem rather than implementation details.

---

## Goals

Identify the desired engineering outcomes.

Goals should describe what success looks like rather than how success will be achieved.

---

## Constraints

Document known limitations.

Examples include:

- technical constraints
- business constraints
- operational constraints
- regulatory constraints
- resource constraints

---

## Success Criteria

Describe how the project determines whether it has achieved its purpose.

---

# Relationship to Replay

Project Foundation is required only when sufficient engineering state does not already exist.

Once Replay Documents have been established, new collaborations should reconstruct engineering state from replay artifacts rather than repeating Project Foundation.

Decision flow:

```text
Replay Documents Available?

├── No
│     ↓
│  Establish Project Foundation
│  using Kuwento Specs
│
└── Yes
      ↓
  Reconstruct Engineering State
  from Replay Documents
```

Replay replaces conversation.

Replay does **not** replace Project Foundation.

Replay preserves the previously established Project Foundation.

---

# Relationship to Replay Documents

Project Foundation becomes embedded within the Replay Documents.

Typical flow:

```text
Project Foundation

↓

Engineering Work

↓

Replay Documents

↓

Future Sessions

↓

Engineering State Reconstruction
```

The Project Foundation should rarely require modification after replay has been established.

---

# Relationship to WWAN

WWAN (Where We Are Now) describes the project's **current operational state**.

Project Foundation describes the project's **purpose and identity**.

They serve different purposes.

| Artifact | Purpose |
|----------|----------|
| Project Foundation | Why the project exists |
| WWAN | Where the project currently is |

---

# Engineering Principles

Project Foundation should:

- remain implementation independent;
- avoid technology decisions;
- avoid architectural assumptions;
- establish shared understanding;
- become the canonical engineering reference.

---

# Guiding Principle

> **Engineering begins with shared understanding. Project Foundation establishes that understanding once so it can be preserved, replayed, and continuously refined without rediscovering the project's purpose.**

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 1.0 | 2026-08-04 | Initial Project Foundation Standard. |