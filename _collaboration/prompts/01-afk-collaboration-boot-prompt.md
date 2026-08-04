# 🚀 AFK Bootstrap Prompt

---

# Purpose

This template is used to begin a **new engineering collaboration** using the Assisted Flow of Knowledge (AFK) methodology.

Its purpose is **not** to immediately solve an engineering problem.

Its purpose is to establish a shared way of working before engineering begins.

The bootstrap aligns both the Human Collaborator (HC) and the AI Collaborator (AC) around:

* the AFK methodology,
* the collaboration principles,
* the project's current engineering state,
* and the appropriate engineering starting point.

Project understanding will emerge naturally through the collaboration.

---

# Before You Begin

If this is your first time using AFK, it is recommended (but not required) to follow the **Existing Codebase Journey**.

📖 Journey

* `afk/docs/journeys/existing-codebase.md`

The journey introduces:

* Project Foundation
* Kuwento Specs
* WWAN
* Engineering Context
* Discovery
* Wishes
* Knowledge Capture

After completing the journey, return here to begin a new AI collaboration.

---

# AFK Bootstrap Prompt Template

Copy the following prompt into a new AI conversation.

Replace placeholders where appropriate.

```text
I would like to begin an engineering collaboration using the **Assisted Flow of Knowledge (AFK)** framework.

Before doing anything else, read and adopt the AFK Collaboration Principles:

https://github.com/irwints-ph/documentation-standards/blob/main/afk/framework/000-afk-collaboration-principles.md

After reading them:

* adopt AFK as the collaboration methodology,
* follow the collaboration principles throughout this session,
* preserve engineering context,
* do not assume any project-specific context.

The next document I will provide is the **Project Boot Prompt**.

The Project Boot Prompt defines:

* the project identity,
* the implementation under review (if applicable),
* the replay sequence,
* the current collaboration objective.

Until the Project Boot Prompt is provided:

* do not inspect the repository,
* do not infer project structure,
* do not make implementation recommendations.

After receiving the Project Boot Prompt:

* execute the replay sequence exactly as documented,
* reconstruct the engineering state incrementally,
* ask for clarification whenever evidence is insufficient,
* HOLD whenever instructed by the replay sequence or after completing the requested phase.
```

---

# Typical Collaboration Flow

```text
Bootstrap
        ↓
Engineering State Assessment
        ↓
Replay
        or
Project Foundation
        ↓
Engineering Context
        ↓
Engineering Unit
        ↓
Discovery
        ↓
Engineering Design
        ↓
Implementation
        ↓
Validation
        ↓
Knowledge Capture
        ↓
WWAN Update
```

---

# Expected AI Behavior

After receiving the bootstrap prompt, the AI Collaborator should:

* understand the AFK methodology;
* understand AFK's Engineering State Reconstruction objective;
* establish the collaboration context;
* determine whether Replay artifacts already exist;
* reconstruct existing engineering state whenever possible;
* help establish missing engineering understanding when necessary;
* recommend the correct engineering starting point;
* collaborate incrementally;
* preserve engineering state throughout the collaboration;
* and HOLD until the Human Collaborator explicitly continues.

---

# Notes

The bootstrap intentionally contains very little project-specific information.

Its role is to establish **how we will collaborate**, not **what we will build**.

Project understanding develops naturally through:

* Project Foundation
* Kuwento Specs
* WWAN
* Engineering Context
* Discovery
* Engineering discussions
* Engineering artifacts

---

# Related Documents

## Journey

* `afk/docs/journeys/existing-codebase.md`

## Collaboration

* `afk/docs/collaboration/001-understanding-wwan.md`
* `afk/docs/collaboration/020-engineering-context-prompt-guide.md`

## Concepts

* `afk/docs/concepts/001-kuwento-specs.md`

---

## Metadata

| Field     | Value                        |
| --------- | ---------------------------- |
| Document  | `01-boot-prompt-template.md` |
| Type      | Collaboration Template       |
| Version   | 4.0                          |
| Status    | 🚧 Growing                   |
| Companion | —                            |
| Owner     | Engineering                  |
| As of     | 07.30.2026                   |
