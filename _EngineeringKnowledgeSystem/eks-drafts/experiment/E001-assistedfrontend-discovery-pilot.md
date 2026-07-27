# AFK Experiment #001

## AFK Assisted Frontend Discovery Pilot

---

# Objective

Validate whether a junior developer can perform structured discovery of an unfamiliar subsystem using the AFK methodology and ChatGPT assistance.

The primary goal is **not** to validate the Dialog module.

The primary goal is to validate the AFK methodology.

---

# Scope

Subsystem

* Dialog Module

Current Phase

* Discovery
* Documentation
* Assessment

Future phases such as extraction, portability, and reuse are intentionally outside the scope of this experiment.

---

# Participants

## Senior Engineer

**Role**

Mentor and Architectural Reviewer

**Responsibilities**

* Explain the purpose of the discovery.
* Introduce the AFK methodology.
* Define the discovery objective.
* Explain expected deliverables.
* Validate architectural conclusions.
* Review end-of-day assessment.
* Mentor when engineering judgment is required.

---

## Junior Developer

**Role**

Discovery Engineer

**Responsibilities**

* Perform subsystem discovery.
* Use ChatGPT as an engineering assistant.
* Maintain `roadmap.md`.
* Maintain `where-we-are-now.md`.
* Document implementation.
* Record observations.
* Record unanswered questions.
* Record assumptions separately from facts.
* Ask for help when discovery becomes blocked.

---

## AFK (Current Implementation)

**Role**

AI-Assisted Discovery Facilitator

Current implementation consists of:

* ChatGPT
* AFK Methodology
* Engineering Documentation Framework

**Responsibilities**

* Explain the discovery process.
* Assist documentation.
* Help analyze unfamiliar code.
* Organize engineering knowledge.
* Suggest architectural observations.
* Challenge assumptions where appropriate.
* Review discovery outputs.
* Recommend learning opportunities.
* Capture improvements to the AFK methodology.

---

# Day 0 — Discovery Kickoff

## Participants

* Senior Engineer
* Junior Developer
* AFK (ChatGPT)

---

## Objective

Prepare the junior developer to begin independent discovery using the AFK methodology.

The purpose of Day 0 is **orientation**, not technical training.

---

## Agenda

### 1. Project Background

The Senior Engineer explains:

* Why the project is being documented.
* Why subsystem discovery is important.
* Why the Dialog module was selected.
* Expected scope of the discovery.

---

### 2. Introduction to AFK

AFK introduces:

* Discovery philosophy.
* Evidence-based documentation.
* Difference between Observation, Discovery, and Finding.
* How ChatGPT should be used.
* Importance of documenting uncertainty.
* Why engineering judgment remains with the developer.

---

### 3. Review of Core Documents

The team reviews the minimum document set required for discovery.

* `roadmap.md`
* `where-we-are-now.md`
* Documentation Standard
* Existing discovery examples (optional)

The objective is familiarity, not mastery.

---

### 4. Define the Discovery Objective

Together the team agrees on:

* Scope
* Deliverables
* Success criteria
* Out-of-scope activities

---

### 5. Questions and Expectations

The Junior Developer may ask questions regarding:

* Discovery methodology
* Documentation expectations
* ChatGPT usage
* Escalation process
* End-of-day review

---

### 6. Assignment

The Senior Engineer officially assigns the discovery.

Example:

> Discover the Dialog subsystem well enough that another engineer could understand and maintain it without repeating the same investigation.

---

# Day 1

## Independent Discovery

The Junior Developer begins independent investigation.

AFK provides assistance only when requested.

The Senior Engineer intentionally minimizes intervention unless architectural or business clarification is required.

---

# End-of-Day Assessment

Participants:

* Junior Developer
* Senior Engineer
* AFK (ChatGPT)

The assessment evaluates:

### Discovery Output

* Documentation produced
* Roadmap updates
* Where-we-are updates
* Observations
* Questions
* Findings (if any)

---

### Junior Growth

Evidence-based review of:

* Progress
* Strengths
* Growth areas
* Recommended learning
* Readiness to continue

---

### AFK Methodology

Review of the methodology itself:

* Were the documents sufficient?
* Was onboarding clear?
* Were expectations realistic?
* What guidance was missing?
* What should be improved before the next discovery?

---

# Expected Outcomes

## Junior Developer

* Improved discovery skills
* Better understanding of unfamiliar code
* Evidence-based learning recommendations
* Increased engineering confidence

---

## Senior Engineer

* Reduced onboarding effort
* Better visibility into learning progress
* Higher-quality architectural discussions
* Reusable discovery artifacts

---

## AFK

* Validate the methodology
* Identify missing guidance
* Improve onboarding
* Improve templates
* Improve discovery workflow
* Build evidence for future evolution

---

I would make one small addition that I think will become a signature of AFK.

At the very beginning of the kickoff, before anyone talks about code, I'd have the Senior Engineer say something like:

> **Today's objective is not to finish the Dialog module.**
>
> **Today's objective is to learn how to discover an unfamiliar system using AFK.**
>
> If, at the end of this experiment, we improve both the Dialog documentation and the AFK methodology, then the experiment is a success.

I think that perfectly sets the expectation. The junior isn't just contributing to the frontend project—they're also helping validate and improve the methodology itself. That makes them a participant in the experiment, not just someone completing an assigned task.
