# 020 — Engineering Context Prompt Guide

---

# Status

**Accepted**

---

# Purpose

This guide defines how to create an **Engineering Context Prompt**.

An Engineering Context Prompt establishes the **shared engineering understanding** between the Human Collaborator (HC) and the AI Collaborator (AC) before any engineering activity begins.

The objective is **not** to document the entire system.

The objective is to provide **just enough context** for the AI Collaborator to safely perform work on a specific Engineering Unit.

---

# Scope

This guide applies whenever work is performed on an existing software system.

Examples include:

* Engineering Unit Discovery
* Engineering Design
* Implementation
* Validation
* Knowledge Capture
* Continuation of previous engineering work

---

# Guiding Principles

An Engineering Context Prompt should always be:

* Minimal
* Accurate
* Engineering-focused
* Current
* Repository-specific
* Wish-specific
* Easy for both humans and AI to understand

It should avoid unnecessary implementation details.

---

# Engineering Context is NOT

An Engineering Context Prompt is **not**:

❌ Repository Discovery

❌ Architecture Documentation

❌ Engineering Design

❌ Build Script

❌ Implementation Instructions

❌ Validation Report

It exists only to establish a shared understanding before engineering begins.

---

# When to Create One

Create an Engineering Context Prompt whenever:

* a new Engineering Unit will be explored;
* work resumes after a long period;
* a new AI Collaborator joins the project;
* an engineering wish is selected.

---

# Relationship to AFK Journeys

The Engineering Context Prompt belongs **before** the engineering lifecycle.

```text
System Discovery
        │
        ▼
Engineering Context Prompt
        │
        ▼
Engineering Unit Lifecycle

    • Discovery
    • Design
    • Implementation
    • Validation
    • Knowledge Capture
```

It is **not** exclusive to Journey 2.

It is the entry point for all engineering work performed on a specific Engineering Unit.

---

# Recommended Structure

An Engineering Context Prompt should contain the following sections.

## 1. Purpose

Briefly describe the project.

Example:

> This project is an existing React frontend application. The objective is incremental engineering improvement while preserving production behavior.

---

## 2. Current State

Describe the current engineering reality.

Examples:

* current architecture maturity
* existing implementation
* known limitations
* current modernization effort

Avoid assumptions.

---

## 3. Discovery Strategy

Explain how engineering work will be performed.

Example:

> The system will be discovered incrementally, one Engineering Unit at a time. Documentation and architecture will evolve alongside implementation.

---

## 4. Current Engineering Unit

Identify the Engineering Unit.

Example:

```text
Engineering Unit

Dialog Module
```

Include a short description of its responsibility.

---

## 5. Current Wish

Describe the engineering objective.

Describe **what** will change.

Do **not** describe **how** it should be implemented.

Example:

> Enable mobile Card View while preserving desktop table behavior.

---

## 6. Additional Objectives

List secondary goals.

Examples:

* document execution flow
* capture architecture
* improve maintainability
* preserve compatibility

---

## 7. AI Collaboration Rules

Explicitly define collaboration expectations.

Typical rules include:

* Understand only the current Engineering Unit.
* Do not redesign unrelated components.
* Preserve existing behavior.
* Avoid assumptions.
* Produce only the requested artifact.
* HOLD after completing each requested artifact.

---

# Validation Checklist

Before using the prompt, verify the following.

## Project

* [ ] Project purpose is clear.

## Engineering Unit

* [ ] Engineering Unit is identified.
* [ ] Responsibility is described.

## Wish

* [ ] Current wish is clearly stated.
* [ ] Scope is limited.

## Collaboration

* [ ] AI responsibilities are defined.
* [ ] AI limitations are defined.
* [ ] HOLD behavior is defined.

If all items are satisfied, the Engineering Context Prompt is considered ready.

---

# Best Practices

Prefer:

* concise descriptions;
* engineering terminology;
* repository-specific information;
* current facts.

Avoid:

* implementation details;
* speculative architecture;
* future redesign discussions;
* unrelated engineering units.

---

# Typical Flow

```text
Human Collaborator

↓

Creates Engineering Context Prompt

↓

AI Collaborator

↓

Reads Engineering Context

↓

Produces Understanding Summary

↓

HOLD

↓

Engineering begins only after Human approval.
```

---

# Future Extensions

Companion documents may later include:

* 021 — Engineering Context Template
* 022 — Engineering Context Checklist
* 023 — Engineering Context Examples

This guide defines the engineering standard used to create those documents.
