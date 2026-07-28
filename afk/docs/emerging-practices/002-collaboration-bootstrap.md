# 🤝 Collaboration Bootstrap

---

## Metadata

**Document:** `002-collaboration-bootstrap.md`

**Category:** Emerging Practice

**Status:** 🚧 Under Operational Validation

**Parent:** Assisted Flow of Knowledge (AFK)

**Version:** 0.1

---

# Purpose

This document captures an emerging AFK practice observed during operational validation.

Rather than beginning collaboration with a task-oriented prompt, AFK begins by establishing a shared operational context between collaborators.

The objective is not to tell the AI collaborator what to produce.

The objective is to help the collaborators understand where they currently are before deciding what should happen next.

---

# Observation

During the implementation of the Engineering Knowledge Publishing Portal (EKPP), a Build Bootstrap document was provided to a fresh AI session before any implementation request was made.

The AI collaborator was instructed only to:

* become the AI collaborator,
* understand the current project state,
* review the operational context,
* preserve existing decisions,
* and continue from the current understanding.

The AI then:

* reconstructed the project's operational state,
* identified the current Build phase,
* requested confirmation before proceeding,
* and produced the expected first implementation.

The implementation request itself contained very little instruction.

Most of the collaboration quality came from the preserved context.

---

# The Practice

Before asking an AI collaborator to perform engineering work:

1. Establish the collaborator's role.
2. Provide operational context.
3. Identify the current wish.
4. Point to the existing source of truth.
5. Explain how collaboration should occur.
6. Only then begin implementation.

The bootstrap prepares the collaboration.

The implementation becomes a natural continuation rather than an isolated prompt.

---

# AFK Flow

```text
Collaboration Bootstrap

↓

Operational Context

↓

Shared Understanding

↓

Implementation

↓

Observation

↓

Validation

↓

Learning
```

---

# Philosophy

AFK treats collaboration as something that should be prepared.

Not merely prompted.

A collaborator who understands the project requires fewer assumptions.

Fewer assumptions produce better engineering conversations.

---

# Why It Matters

Traditional prompting often begins with:

> "Build this."

AFK instead begins with:

> "Understand where we are."

The task remains important.

Understanding becomes the prerequisite.

---

# Relationship to Session Bootstrap

The Session Bootstrap establishes the collaboration.

The Collaboration Bootstrap establishes the operational context for the current phase of work.

They complement one another.

```text
Session Bootstrap

↓

Project WWAN

↓

Phase Bootstrap

↓

Implementation
```

---

# Current Validation

This practice has currently been observed during:

| Project                                        | Status                           |
| ---------------------------------------------- | -------------------------------- |
| Engineering Knowledge Publishing Portal (EKPP) | ✅ Initial Operational Validation |

Additional operational evidence is required before this practice can become AFK Methodology.

---

# Emerging Insight

The Build Bootstrap produced an unexpected result.

The quality of collaboration appeared to improve more from the preserved operational context than from the implementation request itself.

This suggests that successful AI collaboration may depend less on increasingly sophisticated prompts and more on increasingly complete shared context.

This observation remains under validation.

---

# Promotion Criteria

This Emerging Practice may become AFK Methodology if repeated operational experience demonstrates that collaboration bootstraps consistently:

* reduce unnecessary assumptions,
* improve continuity between sessions,
* produce implementations more closely aligned with existing project knowledge,
* and improve collaboration across multiple projects and domains.

---

# Notes

AFK intentionally avoids concluding that this practice is universally applicable after a single successful observation.

The purpose of this document is to preserve the discovery until additional operational evidence either strengthens or challenges it.

---

# Closing Thought

The first step in collaboration is not assigning work.

It is establishing shared understanding.

When collaborators begin from the same context, implementation becomes a continuation of understanding rather than an exercise in reconstruction.

As always:

> **Understand first. Collaborate second. Build together.**
