# 📄 Session Reactivation Playbook

> **Resume engineering through documented state rather than conversational memory.**

---

# Metadata

| Field    | Value                                  |
| -------- | -------------------------------------- |
| Document | `005-session-reactivation-playbook.md` |
| Category | AFK Collaboration                      |
| Type     | Operational Playbook                   |
| Status   | 🚧 Draft                               |
| Owner    | Engineering                            |
| Version  | 0.1                                    |

---

# Purpose

The Session Reactivation Playbook defines the standard procedure for resuming an engineering collaboration after a pause.

Whether the interruption lasts minutes, days, weeks, or months, engineering work should resume from documented engineering state rather than reconstructed memory.

This playbook minimizes onboarding effort while maximizing engineering continuity.

---

# Guiding Principle

> **Reconstruct the engineering state before continuing the engineering work.**

The AI collaborator should understand the current engineering state before contributing new analysis, recommendations, or implementation.

---

# Reactivation Workflow

```text
Project
      ↓
Boot Prompt
      ↓
Engineering Replay
      ↓
Where We Are Now (WWAN)
      ↓
Build Plan
      ↓
Additional Context
      ↓
Clarification
      ↓
Resume Engineering
```

---

# Required Inputs

| Step | Artifact                         | Required | Replace Before Use |
| ---- | -------------------------------- | :------: | :----------------: |
| 1    | Boot Prompt                      |     ✅    |         No         |
| 2    | Engineering Replay               |     ✅    |         Yes        |
| 3    | Where We Are Now (WWAN)          |     ✅    |         Yes        |
| 4    | Build Plan & Future Improvements |     ✅    |         Yes        |
| 5    | Additional Context               | Optional |         Yes        |

---

# Step 1 — Boot Prompt

## Purpose

Establish the collaboration.

The Boot Prompt defines:

* project context,
* engineering collaboration rules,
* documentation framework,
* AI operating assumptions.

## Reference

Replace with the project's Boot Prompt.

Example:

```text
_collaboration/prompts/00-boot-prompt.md
```

---

# Step 2 — Engineering Replay

## Purpose

Understand how the current engineering state emerged.

Replay answers:

* What changed?
* Why did it change?
* What engineering understanding already exists?

Replay restores engineering continuity.

## Reference

Replace with the latest Engineering Replay.

Example:

```text
docs/replay/001-engineering-replay.md
```

---

# Step 3 — Where We Are Now (WWAN)

## Purpose

Synchronize the current engineering state.

WWAN answers:

* Where are we now?
* What has been completed?
* What is currently in progress?
* What comes next?

WWAN restores operational alignment.

## Reference

Replace with the current WWAN.

Example:

```text
docs/where-we-are-now.md
```

---

# Step 4 — Build Plan & Future Improvements

## Purpose

Understand the engineering roadmap.

The Build Plan answers:

* What should be built next?
* Why?
* In what order?
* What engineering wishes are currently active?

This restores engineering direction.

## Reference

Replace with the current Build Plan.

Example:

```text
docs/build-plan.md
```

---

# Step 5 — Additional Context (Optional)

## Purpose

Provide any information that has changed since the latest Replay or WWAN.

Examples include:

* new discoveries,
* updated assumptions,
* revised engineering wishes,
* stakeholder decisions,
* new constraints,
* validation results,
* external feedback.

If no additional context exists, this step may be skipped.

---

# Step 6 — Clarification

Before resuming engineering work, the AI collaborator should identify any ambiguity.

Examples:

* conflicting milestones,
* missing assumptions,
* unclear priorities,
* inconsistent engineering wishes,
* incomplete documentation.

Clarification questions should be concise and engineering-focused.

The AI collaborator should never invent engineering state.

---

# Step 7 — Resume Engineering

Once the engineering state has been reconstructed and clarified, normal engineering collaboration resumes.

At this point the AI collaborator should behave as though the engineering session had never been interrupted.

---

# Operational Checklist

Before continuing engineering work, verify:

* ☐ Boot Prompt reviewed
* ☐ Engineering Replay reviewed
* ☐ Current WWAN reviewed
* ☐ Current Build Plan reviewed
* ☐ Additional context supplied (if applicable)
* ☐ Clarifications resolved
* ☐ Engineering state understood

---

# Benefits

Following this playbook:

* reduces onboarding effort,
* preserves engineering continuity,
* minimizes repeated explanations,
* enables long-running engineering initiatives,
* supports multiple human collaborators,
* produces predictable AI collaboration,
* maintains evidence-driven engineering.

---

# Relationship to AFK

Within the Assisted Flow of Knowledge (AFK), this playbook serves as the standard operating procedure for re-establishing engineering context before new work begins.

Rather than depending on conversational memory, collaborators rebuild engineering state from documented evidence.

---

# Future Enhancements

Potential future improvements include:

* automated document discovery,
* document freshness validation,
* replay completeness checks,
* engineering state verification,
* multi-human collaboration support,
* voice-assisted collaboration workflows.

---

# Current Assessment

The Session Reactivation Playbook is proposed as the standard procedure for resuming Human–AI engineering collaboration.

Validation across multiple projects is recommended before promotion into an accepted AFK collaboration standard.

---

# Guiding Principles

> **Engineering state should be reconstructed from evidence, not memory.**

> **Replay explains the past. WWAN synchronizes the present. Build Plan engineers the future.**

> **A resumed engineering session should require alignment, not rediscovery.**
