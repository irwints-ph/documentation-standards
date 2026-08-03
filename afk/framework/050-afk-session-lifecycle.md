Yes. Since you've promoted the Session Lifecycle into the Framework, `050-afk-session-lifecycle.md` should become the canonical workflow that everything else references.

I would update it so it reflects the current AFK architecture, where **Project Foundation is standardized**, **Replay Documents are the continuity mechanism**, and **Project Boot Prompt** becomes the bridge between the generic AFK bootstrap and the project.

I recommend this structure:

---

# 📄 AFK Session Lifecycle

## Purpose

Defines the canonical lifecycle of an AFK engineering collaboration session.

Every AFK project should follow this lifecycle to ensure engineering knowledge is reconstructed, preserved, and handed over consistently.

Unlike project-specific replay documents, this standard describes the generic collaboration workflow.

---

# Guiding Principle

> Engineering sessions are temporary. Engineering state is persistent.

Every session should improve the engineering state while remaining resumable by another collaborator.

---

# Canonical Session Lifecycle

```text
New Session
      │
      ▼
Generic Boot Prompt
      │
      ▼
AFK Collaboration Principles
      │
      ▼
Project Boot Prompt
      │
      ▼
Replay Documents
      │
      ▼
Engineering State Reconstruction
      │
      ▼
Determine Required Context
      │
      ▼
Context Upload
      │
      ▼
Engineering Collaboration
      │
      ▼
Update WWAN
      │
      ▼
Generate Session Handoff
      │
      ▼
End Session
```

---

# Phase 1 — Session Initialization

### Generic Boot Prompt

Loads the AFK collaboration methodology.

Objective:

* establish collaboration style
* load AFK principles
* wait for project instructions

---

### AFK Collaboration Principles

Defines:

* engineering philosophy
* collaboration rules
* engineering roles
* decision principles

Reference:

```
000-afk-collaboration-principles.md
```

---

### Project Boot Prompt

Project-specific bootstrap.

Responsible for:

* identifying the project
* loading replay documents
* defining replay sequence
* selecting the next engineering activity

---

# Phase 2 — Engineering State Reconstruction

Replay Documents reconstruct project knowledge.

Typical replay sequence:

```
010-purpose.md
↓

020-session-framework.md

↓

021-session-runtime.md

↓

022-required-context-map.md

↓

030-session-handoff.md (previous session)
```

At the end of reconstruction, the AI collaborator should understand:

* project mission
* current engineering state
* current milestone
* next engineering task

---

# Phase 3 — Context Loading

Using the Required Context Map:

Determine which engineering artifacts must be uploaded for the current task.

Only load what is required.

Avoid unnecessary context consumption.

---

# Phase 4 — Engineering Collaboration

Engineering work begins.

Typical activities:

* Discovery
* Design
* Documentation
* Validation
* Implementation
* Review

Throughout collaboration:

* preserve canonical knowledge
* distinguish observation from conclusion
* ask before assuming
* pause at engineering milestones

---

# Phase 5 — Session Preservation

Before ending the session:

Update:

* WWAN (Session Runtime)

Generate:

* Session Handoff

The session should leave enough engineering state that another collaborator can continue without reading conversation history.

---

# Relationship to Other Standards

| Standard | Responsibility           |
| -------- | ------------------------ |
| 000      | Collaboration principles |
| 010      | Project Foundation       |
| 020      | Session Framework        |
| 021      | Session Runtime (WWAN)   |
| 022      | Required Context Map     |
| 030      | Session Handoff          |

---

# Lifecycle Characteristics

The lifecycle intentionally separates:

* collaboration methodology
* project identity
* operational state
* context requirements
* engineering work
* session preservation

This allows every AFK project to reuse the same collaboration workflow while maintaining project-specific replay documents.

---

# Guiding Principle

> AFK sessions should be resumable, predictable, and independent of conversational memory.

---

I also recommend renumbering it from `003-afk-session-lifecycle.md` to `050-afk-session-lifecycle.md` (or whatever number you've standardized on) so it sits naturally in the Framework sequence:

```text
framework/
000-afk-collaboration-principles.md
010-project-foundation-standard.md
020-session-framework.md
021-session-runtime-standard.md
022-required-context-map-standard.md
030-session-handoff-standard.md
050-afk-session-lifecycle.md
100-replay-document-creation-guide.md
```

This ordering mirrors the lifecycle itself and makes the framework much easier to navigate.
