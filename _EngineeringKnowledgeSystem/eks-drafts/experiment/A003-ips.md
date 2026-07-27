I think this is another excellent scenario, and it's actually different from Pilot 002.

Pilot 002 assumed:

> "The system is already dead."

This new scenario assumes:

> **"The system is alive... but no one wants to touch it."**

Those are very different engineering problems.

---

# AFK Pilot 003

## Legacy System Modernization Readiness Assessment

I would intentionally avoid calling it "migration."

At this point, we are **not migrating**.

We are determining whether we understand the system well enough to migrate it safely.

---

# Initial Conditions

The team receives:

✅ Running production system

✅ Source code

✅ Existing users

✅ Existing business processes

⚠️ Outdated technology

⚠️ Limited documentation

⚠️ Unknown architectural debt

⚠️ Workarounds accumulated over many years

⚠️ Original developers may no longer be available

---

# Problem Statement

The system continues to provide business value.

However:

* Bug fixes are becoming increasingly risky.
* Workarounds have replaced proper engineering solutions.
* The impact of changes is difficult to predict.
* The technology stack is approaching end of life.
* Organizational knowledge is gradually disappearing.

The organization needs confidence before investing in modernization.

---

# Primary Objective

Produce sufficient business and technical knowledge to determine whether the system can be safely modernized or replaced.

The goal is understanding.

Not rewriting.

---

# Phase 1 — Business Discovery

Before looking at technology, understand **why the system exists**.

Recover:

* Business goals
* Business processes
* User roles
* Operational workflows
* Critical business rules
* Regulatory requirements
* Success criteria

One of AFK's guiding principles here could be:

> **Business knowledge outlives technology.**

---

# Phase 2 — Technical Discovery

Recover:

* System architecture
* Module responsibilities
* Data flow
* Integration points
* Deployment model
* Security model
* Configuration
* External dependencies

---

# Phase 3 — Operational Discovery

This phase is unique to a running legacy system.

Document:

* Known bugs
* Existing workarounds
* Manual operational procedures
* Scheduled jobs
* Monitoring
* Recovery procedures
* Performance constraints
* Support processes

These often exist only in people's heads.

---

# Phase 4 — Technical Debt Assessment

Instead of immediately fixing problems, classify them.

For example:

### Architecture

* Tight coupling
* Hidden dependencies
* Circular references

### Technology

* Unsupported frameworks
* Unsupported libraries
* Obsolete tooling

### Code

* Duplicate logic
* Dead code
* Legacy patterns

### Operations

* Manual workarounds
* High-risk deployments
* Knowledge concentrated in a few individuals

---

# Phase 5 — Modernization Readiness

Now ask:

> **What must be understood before modernization can begin?**

For each module, assess:

* Business understanding
* Technical understanding
* Test coverage
* Documentation quality
* Dependency clarity
* Risk level

This becomes a readiness assessment rather than a migration plan.

---

# Phase 6 — Future Architecture Preparation

Only now begin separating:

Current Implementation

↓

Business Capability

↓

Future Implementation

For example:

```
Legacy Dialog

↓

User Confirmation Process

↓

React

Angular

Blazor

Flutter

Native

etc.
```

Notice that the business capability stays constant while the implementation changes.

---

# Deliverables

This pilot would produce a rich set of artifacts, such as:

## Business Documentation

* Business processes
* User journeys
* Business rules
* Operational procedures

## Technical Documentation

* Architecture
* Component registry
* Module responsibilities
* Integration catalog
* Data flow diagrams
* Configuration inventory

## Operational Documentation

* Workaround catalog
* Known issues
* Risk register
* Support procedures

## Assessment

* Technical debt assessment
* Modernization readiness report
* Risk analysis
* Recommended modernization sequence

---

# Success Criteria

This pilot succeeds if another engineering team can answer questions like:

* Why does this system exist?
* What business capabilities does it provide?
* Which modules are critical?
* Which workarounds are compensating for design issues?
* Which components can be modernized independently?
* Which components should remain unchanged?
* What risks exist before modernization?
* Can we estimate modernization effort with confidence?

Notice that **none** of these require writing a single line of new code. The value comes from reducing uncertainty.

---

# AFK Capability Map

At this point, I think AFK's pilots begin to form a progression:

| Pilot         | Capability Being Validated                                         |
| ------------- | ------------------------------------------------------------------ |
| **Pilot 001** | Discovery and onboarding of an active subsystem                    |
| **Pilot 002** | Recovery of engineering knowledge from a non-running legacy system |
| **Pilot 003** | Modernization readiness assessment for a running legacy system     |

Each pilot validates a different capability of the methodology.

---

## One observation that ties these together

Looking across all three pilots, I think AFK isn't really about "using AI."

It's about **reducing engineering uncertainty**.

* Pilot 001 reduces uncertainty about an unfamiliar subsystem.
* Pilot 002 reduces uncertainty when knowledge is disappearing.
* Pilot 003 reduces uncertainty before making expensive modernization decisions.

That suggests a broader mission statement for AFK:

> **AFK is a methodology for reducing engineering uncertainty through structured discovery, evidence-based documentation, and AI-assisted knowledge transfer.**

I like that because it's technology-agnostic. Whether the system is written in COBOL, Delphi, React, Java, .NET, or something that doesn't exist yet, the methodology remains focused on preserving and transferring knowledge so informed engineering decisions can be made.
