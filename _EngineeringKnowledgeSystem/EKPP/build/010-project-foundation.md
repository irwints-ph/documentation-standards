# 🛠️ Project Foundation

---

## Metadata

**Document:** `010-project-foundation.md`

**Type:** 🛠️ Build Guide

**Project:** Engineering Knowledge Publishing Portal (EKPP)

**Sprint:** Sprint 0 — Grant EKPP-W001

**Version:** 1.0

---

## Status

🚧 Ready to Build

---

# Purpose

This Build Guide establishes the minimum project foundation required to begin implementing the Engineering Knowledge Publishing Portal (EKPP).

The objective is not to build features.

The objective is to create a clean, understandable project structure that supports granting the current active wish.

---

# Related Documents

Discovery

* 03 — EKPP Wish List
* 04 — EKPP Grant Strategy
* 05 — EKPP Initial Architecture
* 06 — EKPP Build Plan

Build

* 001 — Build Task List

---

# Current Active Wish

## 💭 EKPP-W001

> **I wish I could see the initial output of EKPP.**

Everything created during this phase should directly contribute toward granting this wish.

---

# Objective

At the completion of this guide, the project should have:

* A clear repository structure.
* A location for engineering knowledge.
* A location for implementation artifacts.
* A location for the publishable website.
* A location for generated output.

No user-facing functionality is expected during this phase.

---

# Deliverables

The following project structure should exist.

```text
EKPP/
│
├── README.md
│
├── docs/
│   ├── discovery/
│   ├── registry/
│   └── where-we-are-now.md
│
├── build/
│   ├── 001-build-task-list.md
│   └── 010-project-foundation.md
│
├── website/
│   ├── assets/
│   │   ├── css/
│   │   └── js/
│   │
│   ├── afk/
│   └── index.html
│
└── output/
```

This structure intentionally contains only what Sprint 0 requires.

---

# Build Convention

## Rule 001

Everything inside the **website** folder is considered deployable.

The deployment process should be as simple as:

```text
website/

↓

Upload

↓

Published
```

No framework, build pipeline, or code generation is required for Sprint 0.

---

# Implementation Checklist

## Repository

* [ ] Create EKPP project folder.
* [ ] Verify repository structure.
* [ ] Confirm documentation location.

---

## Documentation

* [ ] Discovery documents available.
* [ ] Registry available.
* [ ] WWAN reflects "Ready to Build".
* [ ] Build folder created.

---

## Website

* [ ] Create website folder.
* [ ] Create assets folder.
* [ ] Create CSS folder.
* [ ] Create JavaScript folder.
* [ ] Create AFK content folder.
* [ ] Create placeholder `index.html`.

---

## Output

* [ ] Create output folder for generated artifacts.

---

# Validation

Project Foundation is complete when:

* Repository structure matches the intended architecture.
* Build documents are accessible.
* Website folder exists.
* No unnecessary folders have been introduced.
* The project is ready to begin building the Website Shell.

---

# Observations

*Record implementation observations here.*

---

# Lessons Learned

*Record improvements discovered while performing this build.*

---

# New Wishes

*Record any newly emerged wishes without implementing them during this phase.*

---

# Completion Criteria

This Build Guide is complete when the project is prepared for:

**020 — Website Shell**

No additional implementation should occur until this guide has been validated.

---

# Closing Thought

A good foundation is rarely noticed once a project is complete.

Its value lies in making everything that follows easier to understand.

Build only what the current wish needs.

Leave tomorrow's wishes for tomorrow's discovery.
