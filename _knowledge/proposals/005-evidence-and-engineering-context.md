# 📄 Proposal — Evidence and Engineering Context

---

## Status

🚧 Proposal

---

# Purpose

This proposal introduces a foundational distinction within the Assisted Flow of Knowledge (AFK) methodology:

**Engineering Context is not Engineering Evidence.**

Although both contribute to engineering understanding, they serve fundamentally different purposes during collaboration.

Clearly separating these concepts allows AFK to reconstruct engineering state objectively, avoid assumption drift, and support long-running engineering collaborations.

---

# Problem

Traditional engineering discussions frequently mix:

* objectives,
* assumptions,
* observations,
* previous decisions,
* and validated facts.

As a result:

* assumptions are mistaken as facts,
* previous conversations become difficult to reconstruct,
* AI collaborators may incorrectly inherit unsupported conclusions,
* engineering decisions become difficult to validate.

AFK requires a clearer separation.

---

# Proposed Principle

> **Engineering Context describes the current engineering hypothesis. Engineering Evidence provides the information required to validate or refine that hypothesis.**

Context guides engineering.

Evidence validates engineering.

Neither replaces the other.

---

# Definitions

## Engineering Context

Engineering Context represents the current shared understanding of the engineering activity.

It describes:

* the current wish,
* objectives,
* constraints,
* known information,
* assumptions,
* intended outcomes.

Engineering Context answers:

> **"What do we currently believe we are trying to accomplish?"**

Engineering Context is intentionally lightweight and may evolve throughout the collaboration.

It should never be considered absolute truth.

---

## Engineering Evidence

Engineering Evidence consists of artifacts that can be inspected, assessed, and validated.

Examples include:

### Software

* Repository Tree
* Source Code
* Architecture Documents
* Execution Flow
* Test Results
* Logs
* Screenshots

### Career

* Resume
* Portfolio
* GitHub
* LinkedIn
* Certifications
* Job Descriptions

### Business

* Financial Reports
* Customer Interviews
* Analytics
* Operational Metrics

Engineering Evidence answers:

> **"What information can we objectively assess?"**

---

# Relationship

```text
Engineering Context
(Current Working Hypothesis)

            ↓

Collect Engineering Evidence

            ↓

Engineering Assessment

            ↓

Engineering Understanding

            ↓

Engineering Decision

            ↓

Implementation

            ↓

Validation
```

---

# Context is a Working Hypothesis

An Engineering Context should always be treated as the current engineering hypothesis.

Even when it references:

* previous research,
* architecture documents,
* historical decisions,
* conversations,
* or external sources,

those references remain hypotheses until their supporting evidence has been assessed.

Example:

```text
Context

According to previous research,
Bootstrap causes the mobile rendering issue.
```

Without the referenced research artifact, this remains a hypothesis.

Only after reviewing the research document does the statement become evidence-backed engineering knowledge.

---

# Evidence Availability Principle

> **Any engineering statement, regardless of its source, remains a working hypothesis until its supporting evidence becomes available for assessment.**

Sources include:

* Human memory
* Previous conversations
* Existing documentation
* AI responses
* Internet resources

Evidence, not origin, establishes confidence.

---

# Engineering State

Engineering State represents validated engineering knowledge accumulated throughout collaboration.

Engineering State is produced from:

* assessed evidence,
* validated findings,
* accepted decisions,
* implemented changes,
* operational observations.

Engineering State is **not** the conversation.

Engineering State is what survives the conversation.

---

# Context Across AFK Journeys

## Journey 1

Engineering Context primarily originates from the human collaborator.

It represents assumptions and desired outcomes.

Confidence is initially low.

Evidence collection validates or refines the context.

---

## Journey 2+

Engineering Context increasingly references validated artifacts produced by previous journeys.

Examples:

* Architecture Assessment
* Execution Flow
* Dependency Analysis
* WWAN
* Knowledge Capture

Although supported by previous evidence, the new Engineering Context still represents a working hypothesis for the current activity until validated by the next journey.

---

# Engineering Confidence

Confidence should be proportional to available evidence.

Example:

| Situation                                    | Confidence |
| -------------------------------------------- | ---------: |
| Human assumption                             |        Low |
| Previous conversation only                   |        Low |
| Existing documentation without evidence      |     Medium |
| Documentation supported by assessed evidence |       High |
| Operationally validated                      |  Very High |

---

# Example

## Software

Engineering Context

```text
Wish

Improve DataTable responsiveness.

Known Information

Bootstrap may be responsible.
```

Evidence

* Source Code
* CSS
* Mobile Screenshots
* Execution Flow

Assessment

Bootstrap contributes to only a portion of the issue.

Primary issue is hardcoded table layout.

Result

Engineering Context evolves.

---

## Career

Engineering Context

```text
Wish

Obtain a sustainable second source of income.

Known Information

React is believed to be the strongest opportunity.
```

Evidence

* Resume
* GitHub
* Portfolio
* Market Assessment

Assessment

Documentation systems and engineering methodology provide stronger market differentiation than React alone.

Result

Engineering Context evolves before implementation begins.

---

# Benefits

Separating Context from Evidence enables AFK to:

* reconstruct engineering state instead of conversations,
* reduce assumption drift,
* improve replay quality,
* support multiple AI collaborators,
* preserve objective engineering reasoning,
* maintain evidence-backed engineering decisions.

---

# Proposed AFK Principle

> **Engineering Context guides engineering. Engineering Evidence validates engineering. Engineering State preserves validated engineering knowledge.**

---

## Status

This proposal requires validation through additional AFK collaboration experiments before acceptance into the AFK core concepts.

---

## Metadata

| Field    | Value                                     |
| -------- | ----------------------------------------- |
| Document | `005-evidence-and-engineering-context.md` |
| Type     | Knowledge Proposal                        |
| Status   | 🚧 Proposal                               |
| Version  | 0.1                                       |
| Owner    | AFK                                       |
| As of    | 07.31.2026                                |
