# 🗺️ Journey 1 — Understand an Existing Codebase

> **Understand before changing.**
>
> This journey helps engineers and AI collaborators quickly understand an existing codebase before making architectural or implementation changes.

---

# Objective

Develop enough understanding of an existing project to safely begin engineering work.

The outcome of this journey is **understanding**, not implementation.

This journey establishes the engineering baseline that all future improvements build upon.
---

# Journey Overview

```text
Initialize
    ↓
Start AI Collaboration
    ↓
Kuwento Specs
    ↓
Project Foundation
    ↓
Discovery
    ↓
WWAN
    ↓
Continue Engineering
```

---

# 🚀 Quick Start

These are the minimum steps required to begin using AFK.

---

## □ Step 1 — Initialize the Engineering Project

Prepare the collaboration workspace.

📖 Read:

* [`../procedures/010-initialize-engineering-project.md`](../procedures/010-initialize-engineering-project.md)

---

## □ Step 2 — Start AI Collaboration

Open ChatGPT (or another AI collaborator).

Use:

* [`../../../_collaboration/01-boot-prompt-template.md`](../../../_collaboration/01-boot-prompt-template.md)

The boot prompt introduces the collaborator to AFK before introducing the project.

---

## □ Step 3 — Create the Kuwento Specs

Begin by telling the story of the project.

📖 Read:

* [`../concepts/001-kuwento-specs.md`](../concepts/001-kuwento-specs.md) *(Draft)*

The AI collaborator should guide the conversation naturally.

The Kuwento should capture:

* The project story
* Why the project exists
* The current situation
* Today's engineering wish
* Success criteria

The goal is **shared understanding**, not complete documentation.

---

## □ Step 4 — Create the Project Foundation

Using the Kuwento, create a concise Project Foundation document.

📖 Read:

* [`../collaboration/010-project-foundation.md`](../collaboration/010-project-foundation.md)

The Project Foundation becomes the shared engineering context for future sessions.

---

## □ Step 5 — Follow the Existing Codebase Playbook

Use the playbook while performing discovery.

📖 Read:

* [`../playbooks/existing-codebase-playbook.md`](../playbooks/existing-codebase-playbook.md)

---

## □ Step 6 — Perform Discovery

Execute discovery using the AFK methodology.

📖 Read:

* [`../methodology/020-afk-discovery.md`](../methodology/020-afk-discovery.md)

Typical activities include:

* Repository discovery
* Folder registry
* Architecture observations
* Validation
* Knowledge capture

---

## □ Step 7 — Capture Engineering Knowledge

Preserve discoveries as reusable engineering knowledge.

Typical outputs include:

* Discovery documents
* Architecture findings
* Knowledge packages (when appropriate)

---

## □ Step 8 — Create or Update WWAN

At the end of the session, create or update the project's WWAN.

📖 Read:

* [`../collaboration/001-understanding-wwan.md`](../collaboration/001-understanding-wwan.md)

The WWAN preserves the operational state of the project and becomes the starting point for the next engineering session.

---

---

# 🤝 Journey Handoff
Congratulations.

You have completed Journey 1 — Understand an Existing Codebase.

The project now contains sufficient engineering context to begin planning improvements.

The following artifacts become the primary inputs for the next journey:

- ✅ Project Foundation
- ✅ Discovery Documents
- ✅ Architecture Findings
- ✅ Validation Results
- ✅ Current WWAN

These documents establish the engineering baseline from which future improvements will be planned.

---

# Next Journey
Continue with:

> 🗺️ Journey 2 — Improve an Existing Codebase
Journey 2 transforms engineering understanding into validated implementation.

Typical activities include:

- Review the current WWAN
- Consolidate Replay Findings
- Perform a Production Readiness Assessment
- Classify Release Gates
- Build the Implementation Plan
- Execute approved changes
- Validate implementation
- Prepare the Engineering Replay

The output of Journey 2 becomes the primary input for Journey 3 — Release an Existing Codebase.

---

# 📚 Learn More (Optional)

Once you've completed your first session, these documents provide deeper understanding of AFK.

## Repository

* [`../../../README.md`](../../../README.md)

Understand the Engineering Knowledge Repository ecosystem.

---

## AFK Overview

* [`../README.md`](../README.md)

Understand the philosophy behind Assisted Flow of Knowledge.

---

## Existing Codebase Learning Path

* [`../playbooks/existing-codebase-learning-path.md`](../playbooks/existing-codebase-learning-path.md)

Recommended order for studying an existing system.

---

## Engineering Discovery Methodology

* [`../methodology/020-afk-discovery.md`](../methodology/020-afk-discovery.md)

Complete discovery methodology and engineering rationale.

---

# Deliverables

At the end of this journey, the project should have:

* ✅ Kuwento Specs
* ✅ Project Foundation
* ✅ Folder Registry
* ✅ Discovery Notes
* ✅ Architecture Findings
* ✅ Validation Results
* ✅ Current WWAN
* ✅ Knowledge captured for future sessions

These deliverables establish the engineering baseline for all future work.
---

# Related Documents

## Concepts

* `../concepts/001-kuwento-specs.md`

## Collaboration

* [`../collaboration/010-project-foundation.md`](../collaboration/010-project-foundation.md)
* [`../collaboration/001-understanding-wwan.md`](../collaboration/001-understanding-wwan.md)

## Playbooks

* [`../playbooks/existing-codebase-playbook.md`](../playbooks/existing-codebase-playbook.md)
* [`../playbooks/existing-codebase-learning-path.md`](../playbooks/existing-codebase-learning-path.md)

## Procedures

* [`../procedures/010-initialize-engineering-project.md`](../procedures/010-initialize-engineering-project.md)

## Methodology

* [`../methodology/020-afk-discovery.md`](../methodology/020-afk-discovery.md)

---

# Guiding Principle

> **Every engineering project has a story. Tell the story before exploring the code.**

Understanding the project creates better discovery.

Discovery creates better engineering.

Engineering creates reusable knowledge.

---
# Lifecycle Position

```text
Journey 1
Understand
        ↓
Journey 2
Improve
        ↓
Journey 3
Release
        ↓
Project Stable
        ↓
Waiting for the next
Journey 2
```
Journey 1 is typically performed once per codebase.

Future engineering work normally begins at Journey 2, using the latest WWAN and Engineering Replay as the starting point.

Journey 1 is revisited only when a major architectural reset, platform migration, or new codebase requires establishing a new engineering baseline.

---
## Metadata

| Field    | Value                                        |
| -------- | -------------------------------------------- |
| Document | `journey-01-understand-existing-codebase.md` |
| Type     | Journey                                      |
| Version  | 4.0                                          |
| Status   | 🚧 Draft                                     |
| As of    | 07.30.2026 08:10 PHT                         |
