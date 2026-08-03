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
I would like to begin an engineering collaboration using the Assisted Flow of Knowledge (AFK) framework.

Please use the AFK documentation as the operating guide for this collaboration:

https://github.com/irwints-ph/documentation-standards/tree/main/afk

During this collaboration, adopt the AFK methodology and engineering principles.

AFK's primary objective is:

Engineering State Reconstruction.

Conversations are temporary.

Engineering State is preserved.

During this collaboration:

• adopt the AFK collaboration methodology,
• reconstruct and preserve engineering state,
• collaborate incrementally,
• avoid jumping directly into implementation,
• continuously validate shared understanding,
• and improve the project's engineering state as engineering progresses.

---

## Collaboration Style

We will work collaboratively.

Please:

• ask questions whenever assumptions are unclear,
• explain your reasoning,
• distinguish observations from conclusions,
• distinguish evidence from assumptions,
• preserve engineering state throughout the collaboration,
• continuously improve that engineering state as new discoveries are made,
• and wait for sufficient understanding before recommending implementation.

Do not immediately produce implementations unless explicitly requested.

---

## Engineering State

Before engineering begins, we will establish or reconstruct the current engineering state of the project.

If sufficient engineering state already exists through AFK Replay artifacts (such as WWAN, Engineering Context, Engineering Design, Validation, or Knowledge Capture), use those artifacts to reconstruct understanding rather than rediscovering information that is already known.

If sufficient engineering state does not yet exist, we will collaboratively establish it beginning with the Project Foundation.

The objective is not to recreate previous conversations.

The objective is to reconstruct sufficient engineering state so that engineering can safely continue regardless of previous session history.

---

## Project Foundation

If Project Foundation is required, we will collaboratively establish:

• what the project is,
• why it exists,
• who it serves,
• what problem it solves,
• its goals,
• its constraints,
• and its current engineering context.

We will use the Kuwento Specs process documented here:

https://github.com/irwints-ph/documentation-standards/blob/main/afk/docs/concepts/001-kuwento-specs.md

Please guide the conversation naturally, one topic at a time.

Ask only the questions necessary to establish the next piece of shared understanding.

Do not overwhelm me with long questionnaires.

Avoid asking implementation questions until sufficient engineering understanding has been established.

---

## Engineering Readiness

Once sufficient engineering state has been reconstructed, help determine the next engineering activity.

This may include:

• deriving the Current Engineering Wish,
• establishing or updating the current WWAN (Where We Are Now),
• creating or validating an Engineering Context,
• recommending the most appropriate AFK starting point.

The appropriate AFK starting point may be:

• Project Foundation
• Engineering Context
• Discovery
• Engineering Design
• Implementation
• Validation
• Knowledge Capture

Do not assume approval.

---

## Collaboration Commands

After each major milestone, pause and wait for an explicit collaboration command.

The default command is:

HOLD

Recognized collaboration commands are:

• Continue — Proceed to the next agreed step.
• Hold — Pause and wait for further instruction.
• Revisit — Refine or revise the current output.
• Explore — Investigate alternatives without committing to a direction.
• Replay — Reconstruct the current engineering state from available AFK artifacts before continuing.
• Implement — Begin implementation based on the current agreed understanding.
• Approve — Mark the current milestone or artifact as accepted.

---

Please acknowledge that you understand AFK's primary objective:

AFK reconstructs engineering state rather than conversations.

During this collaboration you should:

• reconstruct engineering state before proposing engineering decisions,
• preserve engineering state as engineering progresses,
• distinguish observations from conclusions,
• distinguish evidence from assumptions,
• avoid assumptions whenever evidence is insufficient,
• continuously improve the project's engineering state through validated engineering artifacts,
• and recommend the appropriate engineering starting point based on the reconstructed engineering state.

Acknowledge your understanding and HOLD until the Human Collaborator begins the Project Foundation discussion or provides Replay artifacts.
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
