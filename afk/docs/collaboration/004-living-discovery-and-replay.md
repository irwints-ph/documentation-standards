# 📚 Living Discovery and Historical Replay

---

# Purpose

This document defines how engineering understanding evolves throughout an AFK collaboration.

AFK distinguishes between **current engineering understanding** and **historical engineering understanding**.

This distinction allows projects to remain accurately documented while preserving the ability to replay any engineering journey.

---

# Core Principle

Discovery documents represent the **current state** of the project.

Replay documents preserve the **historical state** of the project.

These two purposes must never be mixed.

---

# Living Discovery

Discovery documents are **living documents**.

They should always describe the repository **as it currently exists**.

Examples:

```text
docs/
└── 01-discovery/
    ├── 01-current-project.md
    ├── 02-code-validation.md
    ├── 03-code-architecture.md
    └── code-execution-flow/
        └── main-flow.md
```

Whenever an engineering wish is successfully granted, any affected Discovery documents should be updated to reflect the new implementation.

Discovery should always answer:

> "If I cloned this repository today, how does it currently work?"

---

# Historical Replay

Replay documents preserve engineering history.

They capture the state of the repository **at the completion of a journey**.

Example:

```text
docs/
└── 02-replay/
    ├── Journey1/
    ├── Journey2/
    └── Journey3/
```

Replay should answer:

> "How did the repository work at this point in time?"

Replay documents are never modified after they have been accepted.

---

# Journey Closure

An engineering journey is not considered complete simply because code has been written.

A journey is complete only after engineering understanding has been preserved.

The recommended closure sequence is:

```text
Wish
        │
        ▼
Engineering Design
        │
        ▼
Implementation
        │
        ▼
Validation
        │
        ▼
Knowledge Capture
        │
        ▼
Update Discovery Documents
        │
        ▼
Create Replay Snapshot
        │
        ▼
Update WWAN
        │
        ▼
Journey Closed
```

---

# Discovery Update Rules

After a wish has been fully granted:

* Update affected Discovery documents.
* Do not update unrelated Discovery documents.
* Preserve consistency across all Discovery documentation.

Typical updates may include:

* Current Project
* Code Architecture
* Code Execution Flow
* Validation
* Engineering diagrams

---

# Replay Rules

Replay snapshots:

* are immutable,
* preserve historical engineering understanding,
* provide reproducibility,
* support onboarding,
* and allow engineering evolution to be reviewed over time.

Replay documents should never be edited after acceptance.

If corrections are required, they should be documented in a later journey rather than modifying historical artifacts.

---

# Living vs Historical

| Document Type      | Purpose                              | Mutable          |
| ------------------ | ------------------------------------ | ---------------- |
| Discovery          | Current engineering understanding    | ✅ Yes            |
| Replay             | Historical engineering understanding | ❌ No             |
| WWAN               | Current project status               | ✅ Yes            |
| Engineering Design | Journey-specific design decisions    | ✅ During journey |
| Knowledge Capture  | Engineering lessons learned          | ✅ During journey |

---

# Relationship to AFK

This distinction supports one of AFK's guiding principles:

> Preserve engineering understanding while allowing engineering to evolve.

By separating current documentation from historical snapshots, AFK enables both accurate documentation and complete engineering replay.

---

## Metadata

| Field    | Value                                           |
| -------- | ----------------------------------------------- |
| Document | `004-living-discovery-and-historical-replay.md` |
| Category | Collaboration                                   |
| Type     | Collaboration Standard                          |
| Status   | Proposed                                        |
| Version  | 1.0                                             |
| As Of    | 07.30.2026 18:47 PHT                                  |
