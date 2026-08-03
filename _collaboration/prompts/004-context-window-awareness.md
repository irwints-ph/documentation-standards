# 📄 Proposal

# 004 — Context Window Awareness

---

# Metadata

| Field    | Value                             |
| -------- | --------------------------------- |
| Document | `004-context-window-awareness.md` |
| Category | AFK Proposal                      |
| Type     | Collaboration Architecture        |
| Status   | 🟡 Proposal – Awaiting Validation |
| Version  | 0.1                               |
| As Of    | 2026-08-03                        |

---

# Purpose

Introduce **Context Window Awareness** as a first-class design principle within AFK.

The objective is to acknowledge that every collaborator—human or AI—operates within a finite working context and to design engineering workflows that reduce the impact of those limitations.

Rather than expecting perfect memory, AFK promotes important knowledge into persistent engineering artifacts.

---

# Background

During the development of the Resume Engineering System, an interesting pattern emerged.

Long engineering conversations naturally shifted from implementation toward architecture.

As discussions became richer, earlier implementation details gradually left the active working context.

The knowledge still existed within the repository, but no longer remained immediately available during collaborative reasoning.

This observation applies equally to:

* humans,
* AI,
* engineering teams.

---

# Engineering Observation

Every collaborator has limitations.

Good engineering systems minimize the impact of those limitations rather than expecting perfect behaviour.

---

# Problem Statement

Working context is finite.

Humans experience:

* memory decay,
* interruptions,
* context switching,
* fatigue,
* assumptions changing over time.

AI experiences:

* finite active context,
* incomplete visibility,
* prioritization of recent discussion,
* limited working memory.

Without deliberate mitigation:

* discoveries are repeated,
* decisions are forgotten,
* conversations restart,
* engineering effort is wasted.

---

# Engineering Principle

> **Do not rely on memory. Promote knowledge.**

If an engineering observation becomes valuable enough that losing it would slow future work, it should be promoted into the repository.

---

# Three Context Layers

## Layer 1 — Active Working Context

The information currently participating in reasoning.

Characteristics

* highest fidelity,
* immediately accessible,
* supports detailed discussion,
* temporary.

This answers:

> "What are we actively thinking about?"

---

## Layer 2 — Conversation Context

Historical discussion that still exists but no longer actively participates in reasoning.

Characteristics

* partially accessible,
* lower fidelity,
* useful for reference,
* may require rediscovery.

This answers:

> "What did we discuss earlier?"

---

## Layer 3 — Repository Knowledge

Persistent engineering knowledge stored within AFK.

Examples include:

* documentation,
* standards,
* proposals,
* architecture,
* replay documents,
* Master Resume,
* capability datasets.

Characteristics

* version controlled,
* canonical,
* reusable,
* durable.

This answers:

> "What do we know?"

---

# Context Promotion Workflow

```text
Conversation

↓

Interesting Observation

↓

Important Observation

↓

Repository Artifact

↓

Reduced Cognitive Load
```

Knowledge should move from temporary discussion into permanent engineering assets whenever appropriate.

---

# Relationship to Replay

Replay documents preserve the current working state.

Repository artifacts preserve engineering knowledge.

Together they allow AFK to reconstruct engineering state without relying on memory.

---

# Engineering Examples

Without Context Awareness

```text
Monday

↓

"What was I doing?"
```

With Context Awareness

```text
Replay

+

Repository

↓

Engineering State

↓

Continue
```

---

# Benefits

Context Window Awareness is expected to:

* reduce repeated discovery,
* improve collaboration,
* support AI continuity,
* improve onboarding,
* simplify knowledge transfer,
* reduce dependence on individual memory,
* increase engineering resilience.

---

# Design Philosophy

AFK assumes that no collaborator is perfect.

Instead of demanding better memory, AFK builds better systems.

Engineering is applied to human collaboration in the same way engineering is applied to software systems.

Limitations are acknowledged.

Mitigations are designed.

---

# Validation Plan

Evaluate this proposal during future AFK experiments.

Questions include:

* Did repository promotion reduce repeated discussions?
* Did replay documents reduce context rebuilding?
* Did collaborators resume work faster?
* Did important discoveries remain available over time?

---

# Mission Control Observation

One conversation produced the joke:

> **"Friday drink all you want all weekend. Monday open AFK docs and remember your Friday state."** 🍺

The joke revealed a genuine engineering problem.

People naturally forget.

AI naturally loses active context.

Neither is a defect.

They are system constraints.

Engineering does not eliminate constraints.

Engineering designs mitigations.

AFK therefore adopts a simple philosophy:

> **If it's worth remembering tomorrow, it's worth promoting today.**

Future You should spend less time remembering and more time building.

---

# Guiding Principle

> **Every collaborator has limitations. Good engineering systems reduce the impact of those limitations rather than expecting perfect behaviour.**

---

# Revision History

| Version | Date       | Description                                                                                                       |
| ------- | ---------- | ----------------------------------------------------------------------------------------------------------------- |
| 0.1     | 2026-08-03 | Initial proposal introducing Context Window Awareness and repository promotion as an AFK collaboration principle. |
