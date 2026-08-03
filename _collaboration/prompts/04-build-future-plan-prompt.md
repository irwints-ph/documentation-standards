# 📄 Build Plan & Future Improvements Request Prompt

> **Template Document**
>
> This is a reusable collaboration prompt.
>
> Before use, replace the **Runtime Input** sections with the current session context.
>
> Do **not** submit this document unchanged.

---

# Purpose

Generate an engineering implementation roadmap for the next phase of the project.

Unlike WWAN or Engineering Replay, this document focuses on:

* what should be built,
* why it should be built,
* how it should be implemented,
* and in what order implementation should occur.

The objective is to transform engineering wishes into a structured implementation roadmap.

---

# Runtime Input

## Engineering Wish

Replace this section with the **current engineering wishes** for this session.

Engineering Wishes represent ideas, goals, or desired outcomes rather than implementation requirements.

The AI collaborator should:

* analyze them,
* organize them,
* identify dependencies,
* recommend implementation order,
* engineer them into a phased roadmap.

### Example Only

```text
Engineering Wish

- Implement Light Mode
- Improve page readability
- Move project list into JSON
- Introduce theme management
- Improve accessibility
```

The AI collaborator may:

* merge related wishes,
* split large wishes into smaller engineering phases,
* recommend supporting work,
* recommend a better implementation sequence.

Do **not** invent unrelated features.

---

# Instructions

Generate the Build Plan using engineering thinking rather than feature listing.

The roadmap should:

* transform wishes into engineering work,
* preserve architectural consistency,
* remain implementation-oriented,
* support incremental delivery,
* minimize unnecessary complexity.

Each proposed phase should include:

* Purpose
* Objectives
* Engineering Rationale
* High-Level Technical Approach
* Expected Impact
* Estimated Complexity

---

# Engineering Principles

The Build Plan should:

* build upon the current engineering architecture,
* preserve architectural consistency,
* prioritize maintainability,
* encourage reuse,
* minimize technical debt,
* identify dependencies between phases,
* encourage incremental delivery,
* remain technology-agnostic where practical.

---

# Clarification Rule

Before generating the roadmap, verify that the intended direction is clear.

If any Engineering Wish appears ambiguous, pause and ask concise clarification questions.

Do **not** infer or invent:

* implementation priorities,
* product direction,
* architectural constraints,
* scope boundaries,
* hidden objectives.

Clarify first.

---

# Engineering Constraints

Do **not** produce:

* brainstorming lists,
* unordered feature wishlists,
* generic software advice,
* marketing language,
* implementation without rationale.

Instead, produce a structured engineering roadmap.

---

# Recommended Structure

```text
Purpose
        ↓
Current Engineering State
        ↓
Engineering Principles
        ↓
Engineering Wish
        ↓
Implementation Roadmap

    Phase 1

    Phase 2

    Phase 3

        ↓
Dependencies
        ↓
Risks
        ↓
Future Considerations
        ↓
Execution Summary
```

---

# Phase Structure

Each implementation phase should contain:

## Objective

What is being achieved?

---

## Engineering Rationale

Why should this phase exist?

Why is it in this order?

---

## Technical Approach

High-level engineering approach.

Avoid low-level implementation unless requested.

---

## Implementation Steps

Ordered engineering activities.

---

## Expected Outcome

What engineering capability will exist after completion?

---

## Estimated Complexity

Suggested values:

* Low
* Low–Medium
* Medium
* Medium–High
* High

---

# Roadmap Principles

Favor:

* incremental implementation,
* independently deliverable phases,
* reversible decisions where practical,
* measurable outcomes,
* clear engineering milestones.

Large architectural changes should be decomposed into smaller executable phases.

---

# Pre-Submission Checklist

Before producing the final Build Plan, verify:

* ☐ Runtime Engineering Wish has been replaced with the current session input.
* ☐ Example content has **not** been included in the final document.
* ☐ Session context has been understood.
* ☐ Clarifications have been requested if necessary.
* ☐ Roadmap follows engineering principles.
* ☐ Output is implementation-oriented rather than aspirational.

---

# Output

Produce a complete **Build Plan & Future Improvements** document suitable for direct inclusion into the project documentation repository.

The document should be:

* concise,
* engineering-focused,
* reusable,
* versionable,
* human-friendly,
* AI-friendly.
