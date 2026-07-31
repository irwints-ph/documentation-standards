# 📄 Current Project Template

---

# Purpose

This document captures the **current engineering state** of a repository at the conclusion of **Journey 1 — Discovery**.

Its purpose is to establish an engineering baseline by documenting **what currently exists**, without proposing improvements or implementation changes.

This document should describe the repository exactly as discovered.

---

# Repository Overview

## Repository Name

> `<repository-name>`

## Repository Purpose

Briefly describe the purpose of the repository.

Focus on:

* what it does
* why it exists
* its primary engineering responsibility

Avoid implementation details.

---

# Discovery Summary

Summarize the overall repository.

Include:

* repository maturity
* engineering scope
* major responsibilities
* overall engineering confidence

---

# Repository Structure

Provide a high-level engineering view of the repository.

Example:

```text id="v4l1k3"
Repository

├── CLI
├── Builder
├── Infrastructure
├── Processing
├── Models
└── Tests
```

Avoid documenting every folder.

Only include engineering-relevant structure.

---

# Major Engineering Responsibilities

Identify the major engineering subsystems.

| Subsystem      | Responsibility |
| -------------- | -------------- |
| CLI            |                |
| Models         |                |
| Infrastructure |                |
| Processing     |                |
| ...            |                |

Focus on engineering responsibility rather than implementation.

---

# Repository Inventory

Summarize important repository assets.

| Area          | Present | Notes |
| ------------- | ------- | ----- |
| Source Code   |         |       |
| Documentation |         |       |
| Tests         |         |       |
| Configuration |         |       |
| Assets        |         |       |
| Build Scripts |         |       |

---

# Primary Entry Points

Document the primary engineering entry points.

Examples:

* CLI
* Main executable
* API bootstrap
* Application startup

If multiple entry points exist, describe each.

---

# Repository Health

Provide a high-level engineering assessment.

| Area            | Status |
| --------------- | ------ |
| Architecture    |        |
| Modularity      |        |
| Maintainability |        |
| Discoverability |        |
| Documentation   |        |

Avoid recommendations.

Only summarize current observations.

---

# Engineering Confidence

Summarize the current confidence level.

Possible values:

* High
* Moderate
* Low

Explain the reasoning briefly.

---

# Repository Boundaries

Describe what is inside the repository and what appears to belong elsewhere.

This section helps establish engineering context.

---

# Related Discovery Documents

Reference other Journey 1 outputs.

Typical examples:

```text id="gk0pcq"
02-<project>-validation.md

03-code-architecture.md

code-execution-flow/

    main-flow.md
```

---

# Discovery Notes

Capture any important repository observations that do not naturally fit elsewhere.

Do not include recommendations.

Those belong in the Validation document.

---

## Metadata

| Field    | Value                     |
| -------- | ------------------------- |
| Document | `01-current-<project>.md` |
| Scope    | Current Repository        |
| Category | Discovery                 |
| Type     | Current Project           |
| Status   | Reviewed                  |
| Journey  | Journey 1 — Discovery     |
| As Of    | `<date>`                  |
