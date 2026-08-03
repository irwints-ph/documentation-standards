# 📄 Replay Document Creation Guide

---

# Metadata

| Field    | Value                               |
| -------- | ----------------------------------- |
| Document | `replay-document-creation-guide.md` |
| Category | AFK Replay Framework                |
| Type     | Engineering Playbook                |
| Status   | 🟢 Active                           |
| Version  | 2.0                                 |
| As Of    | 2026-08-04                          |

---

# Purpose

This guide defines the standard process for creating the **Replay Framework** for any AFK-based project.

The Replay Framework enables a new AI collaborator to reconstruct the current engineering state without relying on previous conversation history.

It is created **once**, immediately after the project's Purpose, Context, and Collaboration have been established.

---

# When to Create

Create the Replay Framework after completing:

```text
Generic Boot Prompt

↓

Purpose

↓

Context

↓

Collaboration

↓

Initialize Replay Framework
```

The Replay Framework should **not** be created before the project's engineering philosophy has been established.

---

# Replay Framework Components

The Replay Framework consists of the following project documents.

```text
replay-docs/

000-project-boot-prompt.md

010-purpose.md

020-session-framework.md

021-where-we-are-now.md

022-required-context-map.md

030-session-handoff.md
```

---

# Document Responsibilities

## 000 — Project Boot Prompt

Purpose

Entry point for every future engineering session.

Responsibilities

* identify the project,
* instruct the AI to read the AFK Collaboration Principles,
* define the replay sequence,
* instruct the AI to reconstruct engineering state,
* wait for required context before implementation.

Update Frequency

Rarely.

Usually only if the replay process changes.

---

## 010 — Purpose

Purpose

Explains the mission and scope of the project.

Contains

* project vision,
* engineering philosophy,
* success criteria,
* architectural intent.

Update Frequency

Rarely.

Only when the project's mission changes.

---

## 020 — Session Framework

Purpose

Defines how engineering collaboration occurs.

Contains

* repository structure,
* engineering workflow,
* canonical architecture,
* engineering principles,
* collaboration rules.

Update Frequency

Occasionally.

Only when the engineering workflow evolves.

---

## 021 — Where We Are Now (WWAN)

Purpose

Canonical runtime state of the project.

Contains

* current milestone,
* pipeline progress,
* completed artifacts,
* current engineering activity,
* next tasks,
* active experiment status.

Update Frequency

Every engineering session.

---

## 022 — Required Context Map

Purpose

Defines the minimum documents required for each engineering activity.

Contains

Task → Required Upload Context mappings.

Examples

* Resume generation
* Portfolio mapping
* Cover letter generation
* Application package generation

Update Frequency

Only when new engineering activities are introduced.

---

## 030 — Session Handoff

Purpose

Summarizes the completed engineering session.

Contains

* work completed,
* decisions made,
* artifacts created,
* observations,
* recommended starting point for the next session.

Update Frequency

Every engineering session.

---

# Session Lifecycle

Once the Replay Framework exists, future engineering sessions follow this sequence.

```text
Generic Boot Prompt

↓

AFK Collaboration Principles

↓

Project Boot Prompt

↓

Replay Documents

↓

Determine Required Context

↓

Upload Context

↓

Engineering Work

↓

Update WWAN

↓

Generate Session Handoff

↓

End Session
```

---

# Update Rules

| Document                 | Frequency     |
| ------------------------ | ------------- |
| 000 Project Boot Prompt  | Rare          |
| 010 Purpose              | Rare          |
| 020 Session Framework    | Occasional    |
| 021 WWAN                 | Every Session |
| 022 Required Context Map | Rare          |
| 030 Session Handoff      | Every Session |

---

# Engineering Principle

The Replay Framework separates:

* **stable project knowledge**,
* **current engineering state**,
* **session history**.

Only the runtime state and session history should change during normal engineering work.

---

# Guiding Principle

> **Every AFK project should be restartable from its Replay Framework, allowing a new AI collaborator to resume engineering work consistently without relying on conversational memory.**

---

# Revision History

| Version | Date       | Description                                                                                                                                                            |
| ------- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1.0     | 2026-08-03 | Initial replay document creation guide.                                                                                                                                |
| 2.0     | 2026-08-04 | Updated to reflect Replay Framework architecture, AFK Collaboration Principles, Project Boot Prompt, WWAN as runtime state, Required Context Map, and Session Handoff. |

This updated guide aligns with the architecture we've evolved:

* **AFK Collaboration Principles** establish *how* to collaborate.
* **Project Boot Prompt** establishes *what project* is being resumed.
* **Replay Documents** establish *where the project currently is*.
* **WWAN** and **Session Handoff** become the only documents that normally change from session to session.
