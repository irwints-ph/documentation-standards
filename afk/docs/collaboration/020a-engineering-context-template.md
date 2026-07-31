# 020a — Engineering Context Template

---

# Status

Template

---

# Purpose

This template is used to create an **Engineering Context Prompt** for a specific Engineering Unit.

It should be completed by the Human Collaborator before requesting engineering work from the AI Collaborator.

For guidance on completing each section, refer to:

**Reference**

* `020-engineering-context-prompt-guide.md`

---

# Engineering Context

## Purpose

> Briefly describe the project and the objective of the collaboration.

Example

```text
This project is an existing ____________________________.

The objective of this collaboration is incremental engineering improvement while preserving existing production behavior.
```

---

## Current State

> Describe the current engineering reality.

Include only information relevant to the current Engineering Unit.

Example

```text
The overall architecture is not yet fully documented.

Engineering understanding currently comes from:

• Existing source code
• Repository structure
• Previous discovery work
• Engineering observations

Architecture documentation will evolve as engineering units are discovered and improved.
```

---

## Discovery Strategy

> Explain how engineering work will be performed.

Example

```text
Engineering work will be performed incrementally.

Each Engineering Unit will be:

• Discovered
• Documented
• Improved
• Validated
• Incorporated into the overall system architecture

The objective is to evolve both the software and its documentation together.
```

---

## Current Engineering Unit

Engineering Unit

```text
<Engineering Unit Name>
```

Purpose

```text
Describe the responsibility of this Engineering Unit.
```

Typical Responsibilities

* Responsibility 1
* Responsibility 2
* Responsibility 3

---

## Current Wish

Wish Identifier

```text
WL-XXX
```

Wish

```text
Describe WHAT should change.

Do not describe HOW it should be implemented.
```

---

## Additional Objectives

List any secondary objectives.

Examples

* Capture execution flow.
* Document architecture.
* Improve maintainability.
* Preserve compatibility.
* Capture engineering decisions.

---

## Constraints

List engineering constraints.

Examples

* Preserve existing behavior.
* Preserve existing public API.
* Avoid unrelated refactoring.
* Minimize breaking changes.
* Maintain compatibility with existing consumers.

---

## Known Information

Document any engineering knowledge already available.

Examples

* Existing implementation
* Known dependencies
* Known limitations
* Existing engineering observations

---

## AI Collaboration Rules

The AI Collaborator should:

* Understand only the current Engineering Unit.
* Do not redesign unrelated components.
* Preserve existing behavior whenever possible.
* Avoid assumptions.
* Produce only the requested engineering artifact.
* HOLD after completing each requested artifact.

---

# Engineering Readiness Checklist

Before beginning engineering, verify the following.

## Project

* [ ] Project purpose is clear.

## Engineering Unit

* [ ] Engineering Unit is identified.
* [ ] Engineering Unit responsibility is described.

## Wish

* [ ] Current wish is clearly defined.
* [ ] Engineering scope is limited.

## Constraints

* [ ] Constraints are documented.

## Collaboration

* [ ] AI responsibilities are defined.
* [ ] AI limitations are defined.
* [ ] HOLD behavior is defined.

If all items are satisfied, the Engineering Context Prompt is ready for review by the AI Collaborator.

---

# Related Documents

## Guide

* `020-engineering-context-prompt-guide.md`

## Example

* `020e-engineering-context-example-datatable.md`

---

# Final Engineering Context

Once completed, this template becomes a project-specific Engineering Context document.

Example destination:

```text
docs/03-engineering/<Journey>/<Wish>/engineering-context.md
```

This document will then serve as the engineering handoff artifact before Discovery, Design, Implementation, Validation, or Knowledge Capture begins.
