# 🚀 AFK Bootstrap Prompt

---

# Purpose

This template is used to begin a **new engineering collaboration** using the Assisted Flow of Knowledge (AFK) methodology.

Its purpose is **not** to immediately solve a problem.

Its purpose is to establish a shared way of working before engineering begins.

The bootstrap aligns both the human collaborator and the AI collaborator around:

* the AFK methodology,
* the collaboration principles,
* the project,
* and the current engineering journey.

Project understanding itself will emerge naturally through the collaboration.

---

# Before You Begin

If this is your first time using AFK, it is recommended (but not required) to follow the **Existing Codebase Journey**.

📖 Journey

* `afk/docs/journeys/existing-codebase.md`

The journey introduces:

* Project Foundation
* Kuwento Specs
* WWAN
* Discovery
* Wishes
* Knowledge Capture

After completing the journey, return here to start a new AI collaboration.

---

# AFK Bootstrap Prompt Template

Copy the following prompt into a new AI conversation.

Replace the placeholders where appropriate.

```text
I would like to begin an engineering collaboration using the Assisted Flow of Knowledge (AFK) framework.

Please use the AFK documentation as the operating guide for this collaboration:

https://github.com/irwints-ph/documentation-standards/tree/main/afk

Use the AFK documentation as the operating guide for this collaboration.

During this collaboration, follow the AFK methodology and engineering principles.

• adopt the AFK collaboration methodology,
• preserve engineering understanding,
• collaborate incrementally,
• avoid jumping directly into implementation,
• and continuously build and validate shared understanding before proposing solutions.

---

## Collaboration Style

We will work collaboratively.

Please:

• ask questions whenever assumptions are unclear,
• explain your reasoning,
• distinguish observations from conclusions,
• preserve engineering knowledge throughout the collaboration,
• and wait for sufficient understanding before recommending implementation.

Do not immediately produce implementations unless requested.

---

## Project Foundation

We will begin by collaboratively building the Project Foundation.

Rather than starting with implementation, we will first establish a shared understanding of:

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

Ask only the questions necessary to understand the project.

Do not overwhelm me with long questionnaires.

Ask only the next question needed to build a shared understanding.

Avoid asking technical implementation questions until the Project Foundation has been sufficiently established.

Once the Project Foundation is complete, we will collaboratively derive:

• the First Engineering Wish,
• the initial WWAN (Where We Are Now)

following:

https://github.com/irwints-ph/documentation-standards/blob/main/afk/docs/collaboration/001-understanding-wwan.md

• recommend the most appropriate AFK engineering journey based on the completed Project Foundation.

Do not assume approval.

After each major step, pause and wait for an explicit collaboration command before proceeding.

The default command is HOLD.

Recognized collaboration commands are:

• Continue — Proceed to the next agreed step.
• Hold — Pause and wait for further instruction.
• Revisit — Refine or revise the current output.
• Explore — Investigate alternatives without committing to a direction.
• Implement — Begin implementation based on the current agreed understanding.
• Approve — Mark the current milestone or artifact as accepted.

---

Please acknowledge that you understand the AFK methodology, adopt it as the operating model for this collaboration, and wait for the Project Foundation discussion to begin.
```

---

# Typical Collaboration Flow

```text
Bootstrap
        ↓
AFK Collaboration
        ↓
Project Foundation
(Kuwento Specs)
        ↓
First Engineering Wish
        ↓
Initial WWAN
        ↓
Recommended Journey
        ↓
Discovery
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

After receiving the bootstrap prompt, the AI collaborator should:

* understand the AFK methodology,
* establish the collaboration context,
* wait for project information,
* help build missing project foundations when necessary,
* preserve engineering understanding,
* and collaborate incrementally throughout the project.

---

# Notes

The bootstrap intentionally contains very little project information.

Its role is to establish **how we will collaborate**, not **what we will build**.

Project understanding develops naturally through:

* Project Foundation
* Kuwento Specs
* WWAN
* Discovery
* Engineering discussions

---

# Related Documents

## Journey

* `afk/docs/journeys/existing-codebase.md`

## Collaboration

* `afk/docs/collaboration/001-understanding-wwan.md`

## Concepts

* `afk/docs/concepts/001-kuwento-specs.md`

---

## Metadata

## Metadata

| Field | Value |
|-------|-------|
| Document | `01-boot-prompt-template.md` |
| Type | Collaboration Template |
| Version | 3.1 |
| Status | 🚧 Growing |
| Companion | — |
| Owner | Engineering |
| As of | 07.29.2026 12:31 PHT |