# 📄 AFK Discovery Artifact Creation Guide

---

# Metadata

| Field | Value |
| --- | --- |
| Document | `060-discovery-and-finding-creation-guide.md` |
| Category | AFK Framework |
| Type | Discovery Standard |
| Status | 🟢 Active |
| Version | 2.0 |
| As Of | 2026-08-03 |

---

# Purpose

This document defines how engineering discovery artifacts are created, classified, migrated, and maintained within the Assisted Flow of Knowledge (AFK) framework.

Its purpose is to ensure that engineering understanding is captured from evidence rather than assumptions.

AFK Discovery answers:

> **"What is currently true about the engineering system?"**

before answering:

> **"What should change?"**

---

# What is Discovery?

Discovery is the engineering process of understanding an existing system.

Discovery captures:

- implementation reality,
- architectural patterns,
- runtime behavior,
- component responsibilities,
- relationships between systems,
- engineering observations.

Discovery does not:

- implement changes,
- redesign architecture,
- enforce intended structure,
- replace engineering decisions.

---

# Discovery Philosophy

AFK separates:

```text
Current Reality

from

Intended Architecture

from

Future Improvement
````

A discovery artifact must clearly identify which category information belongs to.

---

# Discovery Principles

## 1. Evidence Before Interpretation

All discovery begins with evidence.

Example:

Evidence:

```
client/src/main.tsx renders App.
```

Observation:

```
main.tsx is the frontend entry point.
```

Interpretation:

```
The application uses a centralized application composition root.
```

These must remain distinguishable.

---

# 2. Discovery Is Not Implementation

A discovery artifact may identify:

* architectural drift,
* missing boundaries,
* duplicated responsibilities,
* improvement opportunities.

However:

Discovery does not automatically create implementation tasks.

Example:

Observation:

```
Pages are not grouped under a domain namespace.
```

Correct:

```
The current structure differs from the intended namespace design.
```

Incorrect:

```
Move all pages immediately.
```

---

# 3. Historical Documents Are Evidence

Existing documentation should not be discarded.

Historical discoveries should be:

* preserved,
* reviewed,
* classified,
* migrated when appropriate.

Old documentation is evidence of previous engineering understanding.

It is not automatically the current truth.

---

# Discovery Artifact Categories

AFK Discovery artifacts are classified by purpose.

---

# 1. Architecture Findings

Purpose:

Capture architectural observations and patterns.

Examples:

```
001-domain-namespace.md
002-composition-root.md
003-responsibility-pattern.md
```

Location:

```
01-discovery/

client/

architecture/
```

---

## Finding Template

```markdown
# Discovery Finding: <Title>

---

## Status

🚧 Discovery

---

## Summary

Short description of the observation.

---

## Historical Context

(Optional)

Previous architectural intent or related documentation.

---

## Observation

What was directly observed.

---

## Evidence

Files, folders, configurations,
or runtime behavior supporting the observation.

---

## Validation

How the observation was confirmed.

---

## Engineering Interpretation

Possible meaning of the observation.

---

## Impact

Potential engineering implications.

---

## Recommendation

Possible future consideration.

Not an implementation instruction.

---

## Related Documents

References.
```

---

# 2. Component Registry Discovery

Purpose:

Document existing components and their responsibilities.

Examples:

```
api-client.md
auth-context.md
route-utils.md
```

Location:

```
01-discovery/

client/

registry/
```

---

## Registry Template

```markdown
# Component Registry: <Component>

---

## Status

🚧 Discovery

---

## Location

Source location.

---

## Purpose

Observed responsibility.

---

## Evidence

Files inspected.

---

## Dependencies

Known dependencies.

---

## Consumers

Known consumers.

---

## Runtime Role

Where this component participates.

---

## Related Components

References.
```

---

# 3. Structure Discovery

Purpose:

Document physical organization.

Examples:

```
001-current-api-folder.md
001-current-routing-folder.md
```

Captures:

* folders,
* modules,
* packages,
* boundaries.

---

Example:

```text
01-discovery/

client/

structure/

001-folder-structure.md
```

---

# 4. Runtime Flow Discovery

Purpose:

Document execution behavior.

Examples:

* application startup,
* authentication flow,
* request flow,
* initialization sequence.

Example:

```
runtime/

001-frontend-startup-flow.md
001-api-startup-flow.md
```

---

# 5. Configuration Discovery

Purpose:

Document configuration behavior.

Examples:

* environment variables,
* application configuration,
* build configuration,
* deployment settings.

Example:

```
configuration/

001-environment.md
002-vite-config.md
```

---

# 6. UI / Feature Discovery

Purpose:

Document UI structures and responsibilities.

Examples:

* layouts,
* pages,
* components,
* workflows.

Example:

```
components/

layout/

header.md
sidebar.md
```

---

# Historical Discovery Migration

When migrating an existing discovery system into AFK:

Do not copy documents directly.

Instead:

```text
Historical Document

↓

Identify Knowledge Type

↓

Apply AFK Artifact Template

↓

Create New Discovery Artifact

↓

Preserve Historical Reference
```

---

# Historical Document Classification

| Existing Document Type | AFK Artifact             |
| ---------------------- | ------------------------ |
| Architecture findings  | Discovery Findings       |
| Folder validation      | Structure Discovery      |
| API documentation      | Component Registry       |
| Configuration notes    | Configuration Discovery  |
| Startup notes          | Runtime Discovery        |
| UI documentation       | UI / Feature Discovery   |
| Recommendations        | Engineering Observations |

---

# Discovery Folder Convention

Recommended structure:

```text
afk-docs/

01-discovery/

    api/

        architecture/

        registry/

        runtime/

        configuration/


    client/

        architecture/

        registry/

        runtime/

        configuration/

        components/
```

---

# Discovery Relationship With Replay

Discovery answers:

> What do we know about the system?

Replay answers:

> What context is required to continue collaboration?

Relationship:

```text
Discovery

↓

Engineering Context

↓

Replay Documents

↓

New Session
```

---

# AI Collaborator Rules During Discovery

The AI collaborator should:

* inspect before concluding,
* cite evidence,
* preserve previous knowledge,
* classify discoveries correctly,
* separate facts from interpretation,
* identify uncertainty.

The AI collaborator should not:

* refactor during discovery,
* assume intended architecture is current architecture,
* convert observations into tasks automatically,
* remove historical documentation.

---

# Discovery Completion Criteria

Discovery is complete when:

* relevant areas have been inspected,
* evidence is recorded,
* artifacts are classified,
* assumptions are identified,
* open questions are preserved,
* future improvements are separated from current reality.

---

# Guiding Principle

> **Discovery creates engineering understanding. Implementation creates engineering change. AFK requires understanding before change.**

---

# Revision History

| Version | Date       | Description                                                                                                                                     |
| ------- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| 1.0     | 2026-08-03 | Initial discovery finding guide.                                                                                                                |
| 2.0     | 2026-08-03 | Expanded into AFK Discovery Artifact Creation Guide covering findings, registries, runtime, structure, configuration, and historical migration. |
