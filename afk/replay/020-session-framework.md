# 📄 Session Framework

---

# Metadata

| Field    | Value                      |
| -------- | -------------------------- |
| Document | `020-session-framework.md` |
| Category | AFK Replay                 |
| Type     | Collaboration Framework    |
| Status   | 🟢 Active                  |
| Version  | 1.0                        |
| As Of    | 2026-08-04                 |

---

# Purpose

This document defines the expected engineering collaboration model for this project.

It provides stable guidance describing **how engineering sessions should operate** independently of the current implementation state.

Unlike the WWAN, this document changes only when the collaboration process itself evolves.

---

# Collaboration Methodology

This project follows the **Assisted Flow of Knowledge (AFK)** framework.

Engineering collaboration is based on the following principles:

* Engineering State before Conversation
* Documentation First
* Evidence before Interpretation
* Incremental Engineering
* Canonical Knowledge Preservation
* Replay-driven Context Reconstruction

The AFK framework documentation remains the authoritative source for collaboration standards.

---

# Collaboration Sequence

Every engineering session should follow the same high-level flow.

```text
AFK Collaboration Boot

↓

Project Boot

↓

Engineering State Reconstruction

↓

Discovery / Review

↓

Implementation (if appropriate)

↓

Replay Update

↓

Session Handoff
```

Implementation should begin only after sufficient engineering understanding has been established.

---

# Engineering Philosophy

The project follows a **Discovery Before Change** philosophy.

Engineering work progresses through:

1. Understand
2. Discover
3. Validate
4. Improve
5. Implement

Whenever evidence is insufficient, additional discovery should be performed before recommendations are made.

---

# AI Collaborator Expectations

AI collaborators are expected to:

* reconstruct engineering state before implementation,
* distinguish observations from conclusions,
* distinguish evidence from assumptions,
* preserve engineering traceability,
* avoid undocumented assumptions,
* explain reasoning when appropriate,
* pause at engineering milestones.

AI collaborators should not:

* invent project requirements,
* overwrite canonical knowledge,
* infer architecture without evidence,
* optimize before understanding.

---

# Repository Interaction

The collaboration mode depends on the available environment.

## Workspace Mode

When the AI has direct access to the repository:

* inspect the repository directly,
* treat implementation as the primary source of truth,
* validate documentation against the implementation,
* create or update discovery artifacts from observed evidence.

Repository navigation snapshots become optional.

---

## Document Mode

When the AI cannot access the repository:

* reconstruct engineering state from replay artifacts,
* use the Repository Navigation Snapshot as an initial navigation aid,
* avoid assumptions about undocumented implementation details,
* request additional evidence whenever required.

---

# Discovery Standards

Discovery should follow the AFK Discovery Artifact Creation Guide.

Engineering observations should be separated into:

* Observation
* Evidence
* Engineering Interpretation
* Impact
* Recommendation

Discovery artifacts should never become implementation tasks automatically.

---

# Engineering Milestones

Engineering sessions should pause after completing meaningful work.

Typical milestones include:

* Discovery completed
* Review completed
* Architecture validated
* Replay updated
* Documentation accepted

At each milestone the collaborator should:

* summarize outcomes,
* identify remaining gaps,
* preserve engineering state,
* HOLD until instructed to continue.

---

# Replay Responsibilities

At the conclusion of a session the collaborator should update the replay documents as appropriate.

Typical replay artifacts include:

* `021-wwan.md`
* `022-required-context.md`
* `030-session-handoff.md`

Replay artifacts should reflect the current engineering state without duplicating canonical documentation.

---

# Relationship to Other Replay Documents

This document describes **how collaboration operates**.

The remaining replay documents describe the current engineering state.

| Document                   | Responsibility                        |
| -------------------------- | ------------------------------------- |
| `010-purpose.md`           | Why the project exists                |
| `020-session-framework.md` | How collaboration operates            |
| `021-wwan.md`              | Current operational engineering state |
| `022-required-context.md`  | Required engineering context          |
| `030-session-handoff.md`   | End-of-session continuation point     |

---

# Maintenance Rules

This document should only change when the project's collaboration process changes.

Routine engineering work should not modify this document.

Examples of valid updates include:

* introducing new collaborator roles,
* changing the AFK workflow,
* modifying replay sequencing,
* adding new collaboration modes.

---

# Guiding Principle

> **Purpose explains why the project exists. The Session Framework explains how engineering collaboration should occur. Together they provide the stable foundation from which every engineering session begins.**

---

# Revision History

| Version | Date       | Description                                                                                                                                   |
| ------- | ---------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| 1.0     | 2026-08-04 | Initial Session Framework defining the project's engineering collaboration model, workflow, collaboration modes, and replay responsibilities. |
