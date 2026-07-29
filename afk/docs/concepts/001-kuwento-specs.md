# 📘 Kuwento Specs

> **Every engineering project has a story. Tell the story before exploring the code.**

---

## Purpose

Kuwento Specs defines how project context should be communicated between humans and AI collaborators.

Rather than beginning with architecture, source code, or implementation details, the collaboration begins by understanding the project's story.

The objective is not to document every detail, but to establish enough shared understanding for productive engineering work to begin.

Kuwento Specs serves as the collaborative process used to build the **Project Foundation**.

---

# Guiding Principles

A good Kuwento should:

* Begin with the business problem.
* Explain the project before the implementation.
* Capture today's engineering context.
* Be conversational rather than technical.
* Grow naturally as understanding improves.
* End with a shared understanding of the first engineering wish.

---

# Typical Flow

A Kuwento naturally explores the project one topic at a time.

## 1. The Story

What is this project?

Why does it exist?

Who benefits from it?

What problem is it trying to solve?

---

## 2. The Current Situation

Where is the project today?

What already exists?

What is currently known?

---

## 3. Constraints

What limitations exist?

Examples:

* business constraints
* technical constraints
* time
* architecture
* external dependencies

---

## 4. Success Criteria

At the end of today's collaboration:

What would make the session successful?

---

## 5. First Engineering Wish

Once enough shared understanding has been established, derive the **First Engineering Wish**.

The wish should represent the smallest meaningful engineering objective that naturally follows from the story.

Examples:

> I wish I could better understand this existing codebase.

> I wish I could document the authentication flow.

> I wish I could identify the API boundaries.

The wish is **not** the first question.

It is the outcome of understanding the project.

---

# Engineering Notes

The AI collaborator should guide the conversation naturally.

Questions should adapt to the project rather than following a rigid questionnaire.

Only ask the next question needed to improve shared understanding.

Avoid long interviews.

If information is unknown, continue and discover it later during engineering discovery.

---

# Output

A completed Kuwento should provide enough understanding to create or update:

* Project Foundation
* First Engineering Wish
* Initial WWAN (Where We Are Now)
* Discovery Plan
* Session Objective

Kuwento does not replace technical discovery.

It prepares the collaboration for discovery.

---

# Relationship to AFK

Within AFK, Kuwento Specs is the first collaborative activity after the collaboration bootstrap.

```text
Bootstrap
      ↓
Kuwento Specs
      ↓
Project Foundation
      ↓
First Engineering Wish
      ↓
Initial WWAN
      ↓
Engineering Journey
      ↓
Discovery
```

---

# Guiding Principle

> **Understand the story before understanding the system.**

The first engineering wish should emerge naturally from the story—not precede it.

---

## Metadata

| Field    | Value                  |
| -------- | ---------------------- |
| Document | `001-kuwento-specs.md` |
| Type     | Collaboration Concept  |
| Version  | 0.2                    |
| Status   | 🚧 Draft               |
