# 🛠️ Project Foundation

---

## Metadata

**Document:** `project-foundation.md`

**Type:** 🛠️ Implementation Guide

**Project:** Engineering Knowledge Publishing Portal (EKPP)

**Parent Build Guide:** `build/010-project-foundation.md`

**Version:** 0.4

**Status:** 🚧 Ready

---

# Purpose

This implementation guide explains how to establish the initial implementation foundation for the Engineering Knowledge Publishing Portal (EKPP).

The objective is to prepare the environment required to begin implementation.

This guide **does not** implement EKPP.

It establishes the places where future implementation will occur.

---

# Current Active Wish

## 💭 EKPP-W001

> **I wish I could see the initial output of EKPP.**

Project Foundation establishes the minimum environment required to begin granting this wish.

---

# Prerequisites

Before beginning this implementation, confirm the following already exist.

## AFK Session

* AFK Session Bootstrap completed.

## Discovery

* Current Platform documented.
* Platform Validation completed.
* Wish List completed.
* Grant Strategy completed.
* Initial Architecture completed.
* Build Plan completed.

## Operational Context

* Current WWAN available.
* Current Discovery Registry available.

## Build

* Current Build Guide available.

Project Foundation assumes these engineering artifacts already exist.

It does **not** recreate them.

---

# Guiding Principles

Before beginning:

* Build only what the current wish needs.
* Understand before implementing.
* Evidence before assumption.
* If confusion appears, pause and AFK it.
* Establish places before implementing features.
* Preserve a single source of truth.

---

# Expected Outcome

At the completion of this guide:

* EKPP has a deployable website structure.
* Published knowledge locations exist.
* Shared website assets have a home.
* Generated output has a destination.

No publishing functionality should exist yet.

No application behavior should exist yet.

---

# Implementation

## Step 1 — Create the Implementation Scaffold

Create the following structure.

```text
EKPP/
│
└── website/
    │
    ├── index.html
    │
    ├── assets/
    │   ├── css/
    │   └── js/
    └── output/
        ├── afk/
        ├── eks/
        ├── eds/
        └── ekpp/
  

```

---

# Folder Responsibilities

| Folder                | Responsibility                                                          |
| --------------------- | ----------------------------------------------------------------------- |
| `website/`            | Deployable website.                                                     |
| `website/assets/`     | Shared website assets.                                                  |
| `website/assets/css/` | Stylesheets.                                                            |
| `website/assets/js/`  | JavaScript.                                                             |
| `website/outputafk/`  | Published AFK documents generated from AFK Markdown.                    |
| `website/outputeks/`  | Published Engineering Knowledge System documents.                       |
| `website/outputeds/`  | Published Engineering Documentation System documents.                   |
| `website/outputekpp/` | Published EKPP documentation.                                           |

---

# Source of Truth

The folders inside `website/` are **not authoring locations**.

They contain published output only.

The authoritative source remains inside the Engineering Knowledge System.

Publishing should follow this flow:

```text
Markdown Source

↓

EKPP Publisher

↓

Generated HTML

↓

website/
```

Generated content should always be reproducible from its source.

Published HTML should never become the maintained copy.

---

# Placeholder Files

Create the following placeholder file.

| File                 | Purpose                                                                                             |
| -------------------- | --------------------------------------------------------------------------------------------------- |
| `website/index.html` | Entry point of the published website. Leave the file empty. Future implementation will populate it. |

A placeholder should remain a placeholder.

Do not begin implementing the Website Shell during this phase.

---

## Step 2 — Review the Scaffold

Pause and review the implementation scaffold.

Ask:

* Does every folder have a single responsibility?
* Does every folder support the current wish?
* Is there only one source of truth?
* Has unnecessary future complexity been introduced?

If unnecessary structure exists, simplify before continuing.

---

## Step 3 — Confirm Readiness

Project Foundation is complete when:

* The scaffold exists.
* The Build Guide has been satisfied.
* Folder responsibilities are clear.
* Future implementation has a well-defined starting point.

Only then should implementation proceed to the next Build Guide.

---

# Validation

Confirm that:

* The implementation scaffold matches this guide.
* Required folders exist.
* Placeholder files exist.
* No application functionality has been implemented.
* No generated content exists yet.
* The project is ready for Website Shell implementation.

---

# Implementation Evidence

Implementation evidence is maintained separately.

See:

`implementation/evidence/001-project-foundation.md`

Expected evidence includes:

* Repository tree
* Folder screenshots
* Validation notes
* Observations

One evidence document may validate multiple implementation activities when appropriate.

---

# Observations

*Record implementation observations.*

---

# Lessons Learned

*Record improvements discovered while implementing.*

---

# New Wishes

*Record newly discovered wishes without implementing them.*

Future wishes belong in Discovery.

The current implementation remains focused on EKPP-W001.

---

# Completion Criteria

Project Foundation is complete when the implementation environment is ready for the next engineering activity.

This phase establishes places.

Future Build Guides will gradually bring those places to life.

---

# Closing Thought

Project Foundation prepares the environment.

It does not attempt to predict the future.

Establish the places.

Preserve a single source of truth.

Allow future implementation—and future discovery—to determine how those places evolve.
