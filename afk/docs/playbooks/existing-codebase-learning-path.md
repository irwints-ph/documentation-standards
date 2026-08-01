# 📚 Existing Codebase Learning Path

> **Learn the AFK methodology for understanding an existing software project before making changes.**

---

## Purpose

This Learning Path guides engineers through the complete AFK discovery process for an existing software project.

Unlike the Playbook, this document focuses on **learning the methodology**.

If you already know the AFK workflow, use:

➡️ `existing-codebase-playbook.md`

---

# Learning Outcomes

After completing this Learning Path, you should be able to:

- Understand an unfamiliar codebase systematically
- Collaborate effectively with an AI engineering companion
- Produce high-quality Discovery documentation
- Separate understanding from implementation
- Create reusable engineering knowledge
- Transition confidently from Discovery into Build

---

# Learning Path

---

## □ Step 1 — Prepare the Session

**Objective**

Establish the collaboration mindset before beginning engineering work.

📖 Read:

- [`../methodology/000-afk-session-bootstrap.md`](../methodology/000-afk-session-bootstrap.md)

Learn:

- AFK mindset
- Working agreements
- Session expectations
- Human and AI responsibilities

---

## □ Step 2 — Define the Wish

**Objective**

Clearly identify what you want to accomplish before exploring the system.

📖 Read:

- [`../future-concepts/001-wish-engineering.md`](../future-concepts/001-wish-engineering.md)

Learn:

- What a Wish is
- Why engineering begins with intent
- How Wishes guide Discovery

Deliverable:

- Initial Wish

---

## □ Step 3 — Understand the Current Context

**Objective**

Describe the project before investigating its implementation.

Topics include:

- project purpose
- business context
- technology stack
- current challenges
- desired outcome

Reference:

- Boot Prompt Template
- WWAN (if available)

Deliverable:

- Project Context

---

## □ Step 4 — Gather Existing Source Material

**Objective**

Provide the AI collaborator with the information needed to begin Discovery.

Typical inputs include:

- folder structure
- README
- architecture documents
- source files
- configuration
- build scripts
- existing documentation

Remember:

Do **not** explain everything.

Discovery should reveal the system naturally.

Deliverable:

- Source Material

---

## □ Step 5 — Begin Discovery

**Objective**

Allow the AI collaborator to understand the system before suggesting improvements.

📖 Read:

- `../methodology/020-afk-discovery.md`

Discovery should identify:

- components
- responsibilities
- dependencies
- architecture
- unknowns
- questions

Deliverable:

- Discovery Documentation

---

## □ Step 6 — Validate Discovery

**Objective**

Confirm that Discovery accurately represents the current system.

Review:

- component responsibilities
- architectural relationships
- assumptions
- unknowns

If Discovery is incomplete:

Return to Discovery.

Deliverable:

- Validated Discovery

---

## □ Step 7 — Complete Discovery

**Objective**

Transform understanding into engineering planning.

Produce:

- Grant Strategy
- Initial Architecture
- Build Plan

Reminder:

Planning only.

No implementation yet.

Deliverables:

- Grant Strategy
- Initial Architecture
- Build Plan

---

## □ Step 8 — Review Before Building

**Objective**

Verify that planning accurately reflects the intended work.

Review:

- Discovery
- Grant Strategy
- Initial Architecture
- Build Plan

If necessary:

Return to Discovery.

Deliverable:

- Approved Build Plan

---

## □ Step 9 — Begin Build

**Objective**

Implement according to the approved Build Plan.

Implementation should follow Discovery.

Unexpected findings should trigger:

Discovery → Grant → Build

not direct implementation.

Deliverable:

- Working implementation

---

## □ Step 10 — Observe

**Objective**

Capture engineering learning before ending the session.

Record:

- what worked
- what changed
- what surprised you
- new discoveries
- reusable knowledge

Update:

- WWAN
- Session Record

Deliverables:

- Observation
- Updated WWAN
- Session Record

---

## □ Step 11 — Capture the Next Wish

Engineering never truly ends.

Document:

- follow-up improvements
- unanswered questions
- future investigations
- modernization opportunities

These become the starting point for the next AFK session.

Deliverable:

- Next Wish

---

# Expected Session Outputs

A completed Existing Codebase Learning Path should produce:

- ✅ Wish
- ✅ Project Context
- ✅ Discovery Documentation
- ✅ Grant Strategy
- ✅ Initial Architecture
- ✅ Build Plan
- ✅ Implementation
- ✅ Observation
- ✅ Updated WWAN
- ✅ Session Record
- ✅ Next Wish

---

# Progression

```text
Wish
    ↓
Project Context
    ↓
Discovery
    ↓
Grant
    ↓
Build
    ↓
Observation
    ↓
Next Wish
```

---

# Continue Learning

After completing this Learning Path, continue with:

- `existing-codebase-playbook.md`

The Playbook condenses this learning into an operational checklist suitable for day-to-day engineering work.

---

> **Understand first. Build second. Learn always.**