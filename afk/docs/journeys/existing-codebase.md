# 🌱 Journey — Improve and Document an Existing Codebase

---

## Metadata

| Field | Value |
|--------|-------|
| Journey | Existing Codebase |
| Audience | Human + AI Collaborator |
| Category | Guided Journey |
| Status | 🚧 Growing |
| Version | 1.0 |

---

## Welcome

Welcome to the Engineering Knowledge Repository.

This journey introduces the **Assisted Flow of Knowledge (AFK)** by guiding you through your first engineering collaboration.

You do not need prior knowledge of AFK.

By the end of this journey, you will have:

* started an engineering project,
* collaborated with an AI Engineer,
* completed Discovery,
* and produced your first preserved engineering knowledge.

---

# What You Will Learn

During this journey you will learn how to:

* initialize a project,
* collaborate with an AI Engineer,
* perform engineering discovery,
* preserve engineering knowledge,
* establish project continuity,
* and continue engineering incrementally.

---

# Prerequisites

You will need:

* Git
* A Markdown editor (or any text editor)
* ChatGPT (or another AI Collaborator)
* The Engineering Knowledge Repository

---

# Journey Overview

```text id="ukr5z9"
Create Project

↓

Start Collaboration

↓

Discovery

↓

Review

↓

Build Planning

↓

WWAN

↓

Continue Engineering
```

---

# Step 1 — Initialize a Project

Initialize a new Engineering Project using the [AFK Bootstrap Tool](../../../tools/afk-init.cmd)

Example:

```bash id="96p00u"
afk-init demo "My First Engineering Project"
```

This creates the Project Foundation.

---

# Step 2 — Open the Project

Open the newly created project.

You should see something similar to:

```text id="ut9z7x"
README.md
roadmap.md
wwan.md
scratch.md

docs/

    discovery/

    registry/
```

---

# Step 3 — Define the First Wish

Open:

```text id="juzbuj"
docs/discovery/001-<project>-wish-list.md
```

Record your first engineering wish.

Keep it small.

Example:

> I wish I could better understand this existing codebase.

---

# Step 4 — Start an AI Collaboration

Open ChatGPT (or another AI Collaborator).

Use the [Collaboration Prompt provided by AFK.](../../templates/01-boot-prompt-template.md)

The prompt introduces the collaborator to AFK before introducing the project.

---

# Step 5 — Begin Discovery

Discovery is the first collaborative engineering activity.

The objective is **not** to solve the problem immediately.

The objective is to establish a shared understanding between the Human Collaborator and the AI Collaborator.

---

## Provide Project Context

Begin by describing the project at a high level.

Example:

```text id="k5ow7t"
This project is an internal frontend application used to manage customer transactions.

It has been under development for several years.

The goal is to understand the existing implementation before making architectural improvements.
```

---

## Provide Existing Source Material

Share the engineering artifacts that best represent the current system.

Examples include:

* source code,
* folder structures,
* architecture diagrams,
* documentation,
* configuration files,
* API contracts,
* or database schemas.

Do not worry about uploading everything at once.

Discovery is incremental.

---

## Provide Your First Wish

State what you hope to accomplish.

Keep the wish focused.

Examples:

> I wish I could better understand this codebase.

> I wish this project had complete engineering documentation.

> I wish we could modernize the architecture without losing existing functionality.

---

## Allow Discovery to Begin

Once sufficient context has been provided, authorize the AI Collaborator to begin Discovery.

Typical authorization:

```text id="6d3axh"
You now have sufficient context.

Please begin the Discovery phase.
```

The AI Collaborator should then begin analyzing the project and gradually produce Discovery artifacts.

---

## During Discovery

Discovery is collaborative.

Continue answering questions.

Clarify assumptions.

Correct misunderstandings.

Provide additional source material when requested.

Discovery is complete only when both Human and AI share the same engineering understanding.

---

## Expected Outputs

Discovery typically produces:

* Current State
* Validation Notes
* Observations
* Gap Analysis
* Grant Strategy
* Initial Architecture
* Build Plan

The exact outputs depend on the project.

---

## Reminder

Discovery is not implementation.

Resist the temptation to immediately solve problems.

The better the shared understanding, the easier every engineering decision becomes afterward.

---

# Step 6 — Collaborate

Discovery is collaborative.

Review the generated output.

Ask questions.

Correct assumptions.

Improve understanding.

The goal is **shared engineering understanding**, not perfect documentation.

---

# Step 7 — Complete Discovery

Discovery is complete when both the Human Collaborator and the AI Collaborator share the same engineering understanding.

At this point, authorize the AI Collaborator to complete the Discovery phase by producing the remaining engineering artifacts.

Typical Discovery outputs include:

* Grant Strategy
* Initial Architecture
* Build Plan

Review these outputs collaboratively.

Ask questions.

Clarify assumptions.

Refine the engineering direction until both collaborators agree that the proposed approach accurately represents the project.

---

## Transition to Build

Once the Discovery outputs have been accepted, authorize the AI Collaborator to begin the initial implementation.

Typical authorization:

```text
Discovery has been completed and accepted.

Please proceed with the initial implementation based on the approved Build Plan.
```

---

## Initial Implementation

The AI Collaborator should generate the engineering artifacts defined by the Build Plan.

Depending on the project, these may include:

* source code,
* documentation,
* scripts,
* templates,
* configuration files,
* website assets,
* automation,
* or other implementation deliverables.

These artifacts represent the **first implementation**, not the final solution.

---

## Human Collaboration

The Human Collaborator now becomes the primary reviewer.

Typical activities include:

* implementing or applying the generated artifacts,
* executing scripts,
* testing the output,
* validating assumptions,
* identifying issues,
* suggesting improvements,
* and collaborating with the AI throughout the implementation.

Implementation is collaborative and iterative.

The objective is continuous improvement—not immediate perfection.

---

## Prepare for Observation

Once the initial implementation has been completed, pause before beginning the next engineering task.

Observe the results together.

Questions to consider include:

* Did the implementation satisfy the original wish?
* What worked well?
* What feels incomplete?
* What unexpected discoveries were made?
* What engineering knowledge should be preserved?

The observations made here become the foundation for the next stage of the AFK lifecycle.

---

## Reminder

Discovery is **not** implementation.

Implementation begins only after Discovery has been collaboratively reviewed and accepted.

Resist the temptation to build before understanding.

Shared understanding remains the strongest foundation for sustainable engineering.

---

# Step 8 — Create WWAN

Once Discovery has stabilized, create the initial WWAN.

The WWAN becomes the operational snapshot for future collaboration.

If this is your first collaboration, ask the AI Collaborator to help establish the initial WWAN using [Understanding WWAN](../collaboration/001-understanding-wwan.md).

---

# Step 9 — Continue Engineering

The project is now ready to continue its engineering journey.

AFK is iterative.

Every completed implementation increases engineering understanding, creating the foundation for the next wish.

Future collaboration follows this lifecycle:

```text
Wish

↓

Discovery

↓

Build Planning

↓

Build Implementation

↓

Human Review

↓

Observation

↓

Grant

↓

Next Wish
```

Each completed cycle preserves engineering knowledge before beginning the next.

---

## Continuous Improvement

Every engineering cycle should leave the project in a better state than it was before.

Typical improvements include:

* increased understanding,
* improved documentation,
* cleaner architecture,
* better implementation,
* stronger automation,
* or refined engineering workflows.

No cycle is expected to be perfect.

Each cycle contributes another layer of preserved engineering knowledge.

---

## Engineering Never Truly Ends

AFK is designed around continuous engineering rather than one-time delivery.

Every granted wish naturally reveals new opportunities for improvement.

The next wish may come from:

* Human observation,
* AI observation,
* user feedback,
* testing,
* implementation experience,
* or newly discovered engineering knowledge.

Each wish begins another collaborative engineering cycle.

---

## Closing Thought

Engineering is not the act of writing code.

Engineering is the continuous preservation and refinement of understanding.

Code, documentation, architecture, automation, and knowledge all evolve together through repeated collaboration.

---

# What You Have Accomplished

Congratulations.

You have completed your first AFK collaboration.

You now understand:

* how AFK begins,
* how engineering understanding is preserved,
* how Human and AI collaboration works,
* and how future engineering work continues naturally.
* how engineering continuity is preserved.

---

# Continue your learning

* [Learn AFK Collaboration](../afk/README.md)
* Explore the Engineering Documentation System [EDS](../eds/README.md)
* Explore the Engineering Knowledge System [EKS](../eks/README.md)

Or begin your next engineering wish.

---

# Closing Thought

Your first project is not about building software.

It is about learning how to preserve understanding.

Once understanding is preserved, engineering becomes easier to continue—for yourself, for your teammates, and for future AI collaborators.
