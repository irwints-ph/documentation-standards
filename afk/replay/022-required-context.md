# 📄 Required Context

---

# Metadata

| Field    | Value                     |
| -------- | ------------------------- |
| Document | `022-required-context.md` |
| Category | AFK Replay                |
| Type     | Context Reconstruction    |
| Status   | 🟢 Active                 |
| Version  | 1.0                       |
| As Of    | 2026-08-04                |

---

# Purpose

This document defines the minimum engineering context required before meaningful work can continue.

Its purpose is to reduce unnecessary repository exploration by identifying the documents and artifacts that should be reconstructed first.

Unlike the Project Boot Prompt, which starts a collaboration, this document identifies the engineering knowledge required to continue it.

---

# Context Loading Priority

Engineering context should be reconstructed in the following order.

---

## Level 1 — AFK Framework

Read the AFK framework first.

Required:

```text id="st79or"
000-afk-collaboration-principles.md
010-project-foundation-standard.md
020-replay-document-creation-guide.md
025-project-boot-prompt-creation-guide.md
030-understanding-wwan.md
040-understanding-session-handoff.md
050-afk-session-lifecycle.md
060-discovery-artifact-creation-guide.md
070-discovery-review-and-acceptance-guide.md
```

These documents define how collaboration operates.

---

## Level 2 — Replay

Read the replay documents.

Required:

```text id="5fwpj8"
010-purpose.md
020-session-framework.md
021-wwan.md
022-required-context.md
```

These documents reconstruct the project's current engineering state.

---

## Level 3 — Repository Context

Repository access depends on the collaboration mode.

### Workspace Mode

If direct repository access exists:

* inspect the repository,
* validate existing discovery artifacts,
* treat implementation as the primary source of truth.

Repository Navigation Snapshot is optional.

---

### Document Mode

If repository access is unavailable:

Read:

```text id="m67uuk"
000-repository-navigation-snapshot.md
```

Use it only as an initial navigation aid.

Do not infer undocumented implementation details.

---

## Level 4 — Context Shift

When switching engineering streams, load the appropriate context shift document.

Examples:

```text id="jdr7vf"
001-fe-context-shift.md
001-api-context-shift.md
```

Only one should be active for a given engineering session.

---

## Level 5 — Discovery

Reconstruct previously accepted discovery artifacts before creating new ones.

Priority order:

1. Architecture Findings
2. Structure Discovery
3. Runtime Discovery
4. Configuration Discovery
5. Component Registry
6. UI / Feature Discovery

Discovery should always be validated against the current implementation.

---

# Context Validation

After reconstruction, verify:

* engineering purpose,
* collaboration mode,
* current milestone,
* active implementation,
* discovery status.

If inconsistencies are found:

* identify them,
* request clarification,
* avoid assumptions.

---

# Optional Context

Load only when relevant.

Examples:

* historical discovery artifacts,
* architecture proposals,
* implementation plans,
* engineering discussions,
* previous validation reports.

These documents provide additional context but are not required for every session.

---

# Engineering Rules

During reconstruction:

* prefer evidence over assumptions,
* validate historical artifacts,
* preserve canonical documentation,
* distinguish observations from conclusions,
* do not begin implementation until sufficient engineering state has been reconstructed.

---

# Expected Completion

Context reconstruction is complete when the collaborator understands:

* why the project exists,
* how collaboration operates,
* the current engineering state,
* the active implementation,
* the current engineering objective.

Only then should engineering work continue.

---

# Related Documents

* `010-purpose.md`
* `020-session-framework.md`
* `021-wwan.md`
* `030-session-handoff.md`

---

# Maintenance Rules

Update this document whenever:

* required replay artifacts change,
* collaboration workflow changes,
* additional context becomes mandatory,
* repository reconstruction requirements evolve.

Routine engineering progress should not modify this document.

---

# Guiding Principle

> **Engineering should begin only after sufficient context has been reconstructed. This document identifies the minimum knowledge required to safely continue engineering without rediscovering the project from scratch.**

---

# Revision History

| Version | Date       | Description                                                                                                            |
| ------- | ---------- | ---------------------------------------------------------------------------------------------------------------------- |
| 1.0     | 2026-08-04 | Initial Required Context document defining the minimum engineering knowledge required before continuing collaboration. |
