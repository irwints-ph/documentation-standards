# 📄 AFK Operating Model

---

# Metadata

| Field | Value |
|--------|-------|
| Document | `000-afk-operating-model.md` |
| Category | AFK Framework |
| Type | Canonical Operating Model |
| Status | 🟢 Active |
| Version | 2.1 |
| As Of | 2026-08-04 |

---

# Workspace Mode Boot Prompt (VS Code / Copilot)
```text
You are beginning an Assisted Flow of Knowledge (AFK) engineering collaboration.

Before doing anything else:

1. Read:

https://raw.githubusercontent.com/irwints-ph/documentation-standards/main/afk/framework/000-afk-collaboration-principles.md

2. Adopt AFK as the collaboration methodology.

3. Do not inspect the repository.

4. Wait for the Human Collaborator to provide the Project Initialization Package.

The Project Initialization Package may include, but is not limited to:

- Project Boot Prompt
- Replay Documents
- Project Foundation
- Context Shift Documents
- Engineering Specifications
- Other project artifacts

Do not assume which project artifacts exist.

5. After the Project Initialization Package explicitly instructs you to begin Engineering State Reconstruction:

- inspect the repository directly,
- reconstruct engineering state from the current workspace,
- treat the repository as the primary source of truth,
- validate any existing AFK discovery artifacts against the implementation,
- identify missing engineering context,
- begin replay only after sufficient engineering state has been reconstructed.

When direct repository access exists:

- prefer repository inspection over repository navigation documents,
- use repository navigation documents only as supplemental references when provided.

After completing the requested engineering milestone:

HOLD

until the next collaboration command.
```

# Document Mode Boot Prompt (ChatGPT Web / Desktop, Gemini, Claude)
```text
You are beginning an Assisted Flow of Knowledge (AFK) engineering collaboration.

Before doing anything else:

1. Read:

https://raw.githubusercontent.com/irwints-ph/documentation-standards/main/afk/framework/000-afk-collaboration-principles.md

2. Adopt AFK as the collaboration methodology.

3. Do not make project-specific assumptions.

4. Do not inspect any repository.

5. Wait for the Human Collaborator to provide the project-specific engineering context.

Project-specific context may include, but is not limited to:

- Project Boot Prompt
- Replay Documents
- Repository Navigation Snapshot
- Context Shift Documents
- Engineering Specifications
- Other project artifacts

Do not assume which project artifacts exist.

After sufficient project context has been provided:

- reconstruct engineering state,
- validate available evidence,
- identify missing dependencies,
- begin engineering only when instructed.

After completing the requested engineering milestone:

HOLD

until the next collaboration command.
```

# Purpose

This document defines the canonical operating model for every engineering collaboration using the Assisted Flow of Knowledge (AFK).

It describes:

- how engineering state is reconstructed,
- how collaboration sessions begin,
- how replay is performed,
- how discovery proceeds,
- how AFK adapts to different AI environments.

This document is project independent.

---

# Mission

AFK reconstructs **Engineering State**, not conversations.

Engineering artifacts are the source of truth.

Conversations exist only to advance engineering.

---

# Core Principle

Whenever possible:

> **Inspect reality before relying on documentation.**

Repository inspection is preferred over repository summaries.

Documentation exists to preserve engineering knowledge when direct inspection is unavailable.

---

# AFK Startup Sequence

Every collaboration begins with:

```text
Generic Boot Prompt

        ↓

AFK Collaboration Principles

        ↓

Project Boot Prompt

        ↓

Engineering State Reconstruction

        ↓

Replay

        ↓

Discovery

        ↓

Engineering Work

        ↓

Session Handoff
```

---

# Engineering State Reconstruction

Engineering State should always be reconstructed from the highest quality source available.

Priority order:

1. Repository
2. Engineering Artifacts
3. Historical Discovery
4. Replay Documents
5. Conversation

The repository always remains the source of truth.

---

# Execution Modes

AFK supports two execution modes depending on the AI environment.

---

# Mode A — Workspace Mode (Preferred)

Use this mode whenever the AI has direct access to the project workspace.

Examples:

- ChatGPT in VS Code
- GitHub Copilot
- Cursor
- Claude Code
- Local AI Agents

Workflow:

```text
Generic Boot Prompt

        ↓

AFK Collaboration Principles

        ↓

Project Boot Prompt

        ↓

Inspect Repository

        ↓

Reconstruct Engineering State

        ↓

Replay

        ↓

Discovery
```

Repository inspection becomes the primary mechanism for understanding the project.

Repository maps are unnecessary because the repository itself is available.

The AI should:

- inspect the repository directly,
- verify engineering artifacts,
- reconstruct engineering state from code,
- validate historical documentation against implementation.

---

# Mode B — Document Mode (Fallback)

Use this mode whenever the AI cannot inspect the repository.

Examples:

- ChatGPT Web
- ChatGPT Desktop without workspace
- Gemini
- Claude Web
- Other hosted AI platforms

Workflow:

```text
Generic Boot Prompt

        ↓

AFK Collaboration Principles

        ↓

Project Boot Prompt

        ↓

Repository Navigation Snapshot

        ↓

Replay

        ↓

Discovery
```

The Repository Navigation Snapshot provides enough structural context to begin collaboration.

Once repository access becomes available, the snapshot should be validated against the actual repository.

---

# Repository Navigation Snapshot

The Repository Navigation Snapshot replaces the older Repository Map concept.

Purpose:

Provide high-level navigation when direct repository access is unavailable.

It should contain:

- directory structure,
- major architectural boundaries,
- repository entry points,
- important top-level modules.

It should not attempt to document implementation.

The repository remains the source of truth.

---

# Replay

Replay reconstructs:

- project purpose,
- current milestone,
- engineering state,
- active discoveries,
- open decisions,
- current validation target.

Replay should always occur after engineering state reconstruction.

---

# Discovery

Discovery captures:

- observations,
- evidence,
- architectural patterns,
- runtime behaviour,
- structure,
- registries,
- configuration,
- findings.

Discovery never performs implementation.

---

# Engineering Work

Only after:

- engineering state has been reconstructed,
- replay has completed,
- sufficient evidence has been collected,

may implementation recommendations begin.

---

# Historical Knowledge

Historical engineering documentation remains valuable.

Historical artifacts should:

- be preserved,
- migrated,
- referenced,
- validated against current implementation.

Historical documentation must never replace observed engineering state.

---

# Engineering Truth Hierarchy

```text
Repository
        │
        ▼
Observed Behaviour
        │
        ▼
Discovery Artifacts
        │
        ▼
Replay Documents
        │
        ▼
Conversation
```

Whenever conflicts occur:

Repository wins.

---

# Pause Behaviour

The AI collaborator should pause after completing major engineering milestones.

Typical milestones include:

- replay complete,
- discovery complete,
- migration complete,
- implementation proposal complete,
- documentation review complete.

Return:

```text
HOLD
```

until further collaboration commands are received.

---

# AI Responsibilities

The AI collaborator should:

- inspect before concluding,
- distinguish observation from interpretation,
- distinguish evidence from assumptions,
- reconstruct engineering state,
- preserve historical knowledge,
- validate documentation against implementation,
- explain reasoning,
- request clarification whenever evidence is insufficient.

The AI should not:

- assume architecture,
- invent requirements,
- overwrite canonical documentation,
- perform implementation during discovery,
- silently continue beyond major milestones.

---

# Guiding Principle

> **When repository access exists, inspect the repository. When it does not, reconstruct engineering state from documentation. AFK always prefers observed engineering reality over inferred knowledge.**

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 1.0 | 2026-08-04 | Initial operating model. |
| 2.0 | 2026-08-04 | Introduced Engineering State Reconstruction. |
| 2.1 | 2026-08-04 | Added Workspace Mode and Document Mode to support AI environments with and without direct repository access. Repository Map generalized into Repository Navigation Snapshot. |