# 🧠 Build Knowledge Package

---

## Metadata

**Document:** `001-build-knowledge-package.md`

**Category:** Build

**Status:** 🚧 Growing

**Parent:** Engineering Knowledge Publishing Portal (EKPP)

**Version:** 0.1

---

# Purpose

This document provides the minimum body of knowledge required before beginning a Build session.

Unlike the Build Bootstrap, which establishes how collaborators should work together, the Build Knowledge Package establishes what collaborators should understand before implementation begins.

Its objective is to reduce assumptions by making existing engineering knowledge available before implementation.

---

# Philosophy

Implementation should emerge from understanding.

A collaborator can only synthesize knowledge that has been shared.

The Build Knowledge Package exists to provide that shared understanding.

---

# Build Preparation

Before implementing, the collaborator should understand the project from four perspectives.

## 1. Project Purpose

Understand why the project exists.

Recommended reading:

* EKPP Purpose
* Project README

Questions to answer:

* What problem is EKPP solving?
* What is the project's overall objective?
* What should never change?

---

## 2. Current Operational State

Understand where the project currently is.

Recommended reading:

* 📍 Where We Are Now (WWAN)

Questions to answer:

* What phase are we currently in?
* What is the active wish?
* What work has already been completed?
* What work comes next?

---

## 3. Discovery

Understand the engineering decisions that led to the current Build phase.

Recommended reading:

* Current Discovery
* Wish List
* Grant Strategy
* Initial Architecture
* Build Plan

Questions to answer:

* Why was this architecture chosen?
* What alternatives were considered?
* Which decisions have already been validated?
* Which discoveries remain experimental?

---

## 4. Current Build

Understand the current implementation objective.

Recommended reading:

* Current Build Guide
* Current Implementation Guide

Questions to answer:

* What are we building?
* Why are we building it now?
* What is the smallest useful implementation?
* What observation are we trying to create?

---

# Source of Truth

Before generating new content, determine whether the required knowledge already exists.

Preferred workflow:

```text id="2lvuhc"
Read

↓

Understand

↓

Synthesize

↓

Implement
```

Avoid:

```text id="xn95yx"
Generate

↓

Assume

↓

Duplicate
```

Implementation should extend existing understanding rather than replace it.

---

# Knowledge Completeness Check

Before implementation begins, confirm that enough knowledge has been provided to answer the following questions.

## Project

* What is this project?
* Why does it exist?

## Current State

* Where are we?
* What has already been completed?

## Current Wish

* What are we trying to grant?

## Architecture

* What engineering decisions have already been made?

## Build

* What is the next smallest useful implementation?

If any answer is unclear, collaboration should pause until sufficient context has been provided.

---

# AI Collaborator Guidance

If referenced documents have not been provided:

* do not assume their contents,
* do not recreate missing knowledge,
* ask for the missing context,
* continue only after sufficient understanding has been established.

Understanding should always precede implementation.

---

# Emerging Observation

Operational validation of EKPP revealed that the quality of implementation depended heavily upon the completeness of the shared knowledge.

The Build Bootstrap successfully established collaboration.

The Build Knowledge Package enables informed implementation.

Together they reduce the need for assumptions.

---

# Relationship to Build Bootstrap

The Build Bootstrap prepares the collaboration.

The Build Knowledge Package prepares the understanding.

Together they form the beginning of every Build session.

```text id="wxg2sb"
Session Bootstrap

↓

Build Bootstrap

↓

Build Knowledge Package

↓

WWAN

↓

Implementation

↓

Observation

↓

Validation

↓

Learning
```

---

# Success Criteria

The Build Knowledge Package is considered successful if collaborators can begin implementation without needing to reconstruct prior engineering decisions.

Implementation should feel like a continuation of understanding rather than the beginning of discovery.

---

# Closing Thought

A Build session should never begin with missing knowledge.

The better the shared understanding, the fewer the assumptions.

The fewer the assumptions, the stronger the collaboration.

As always:

> **Understand first. Share knowledge. Build together.**
