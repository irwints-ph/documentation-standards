# 📄 Session Record Template

---

## Metadata

| Field    | Value                        |
| -------- | ---------------------------- |
| Document | `session-record-template.md` |
| Scope    | Human + AI Collaboration     |
| Category | Collaboration Framework      |
| Type     | Template                     |
| Status   | Active                       |

---

# Purpose

The Session Record preserves the outcome of a completed engineering collaboration.

Unlike the **WWAN**, which represents the project's current operational state and continues to evolve, a Session Record captures a permanent snapshot of one collaboration cycle.

Its purpose is to preserve:

* what the collaboration set out to accomplish,
* what work was performed,
* what decisions were made,
* what artifacts were produced,
* how the WWAN changed,
* and where the next collaborator should continue.

Once completed, a Session Record should **never be modified** except to correct factual errors.

---

# Relationship to WWAN

```text
Start Collaboration

        │

        ▼

Current WWAN

        │

        ▼

Engineering Work

        │

        ▼

Session Record

        │

        ▼

Updated WWAN

        │

        ▼

Next Collaboration
```

---

# Session Metadata

| Field                | Value |
| -------------------- | ----- |
| Session              |       |
| Project              |       |
| Repository           |       |
| Human Collaborator   |       |
| AI Collaborator      |       |
| Started              |       |
| Completed            |       |
| Duration             |       |
| WWAN Version (Start) |       |
| WWAN Version (End)   |       |

---

# Session Objective

Describe the objective of this collaboration.

Example:

> Build the initial project foundation and establish the repository architecture.

---

# Starting Context

Describe the state of the project before work began.

Include:

* Active milestone
* Current wish
* Existing architecture
* Important constraints
* Relevant WWAN summary

---

# Activities Performed

List the major activities completed during the session.

Example:

* Reviewed repository architecture
* Completed Discovery
* Designed project folder structure
* Created engineering standards
* Updated WWAN

---

# Engineering Decisions

Document the important decisions made.

For each decision record:

| Decision | Reason |
| -------- | ------ |
|          |        |

This section is intended to preserve engineering reasoning for future collaborators.

---

# Artifacts Produced

List every document, script, configuration, or implementation produced.

Example:

| Artifact | Description |
| -------- | ----------- |
|          |             |

---

# Wishes Addressed

List wishes worked on during this session.

| Wish | Result                                 |
| ---- | -------------------------------------- |
|      | Granted / Partially Granted / Deferred |

---

# Observations

Record important discoveries.

Examples include:

* architectural findings,
* technical debt,
* unexpected behaviour,
* opportunities for future improvement.

---

# WWAN Changes

Summarize how the WWAN changed during this collaboration.

Include:

* milestone progress,
* active wish updates,
* completed work,
* newly discovered work.

---

# Outstanding Work

Document work intentionally left unfinished.

Include sufficient context so another collaborator can continue without reconstructing previous discussions.

---

# Recommended Next Collaboration

Describe the logical next engineering step.

Example:

> Begin Discovery for Wish 002 and prepare the initial Grant Strategy.

---

# References

List documents relevant to this session.

Examples:

* WWAN
* Discovery documents
* Build Plans
* Standards
* Procedures

---

# Closing Notes

This Session Record permanently preserves one engineering collaboration.

Future collaborators should begin by reading:

1. Current WWAN
2. Relevant Session Records
3. Current active wish

before continuing engineering work.
