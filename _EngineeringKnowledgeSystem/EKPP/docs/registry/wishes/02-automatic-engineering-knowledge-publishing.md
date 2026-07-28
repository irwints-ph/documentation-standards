# 🌟 EKPP-W002 — Automatic Engineering Knowledge Publishing

---

## Metadata

| Field         | Value                                   |
| ------------- | --------------------------------------- |
| Wish          | `EKPP-W002`                             |
| As of         | 07.28.2026 06:30 PHT                    |
| Document | `02-automatic-engineering-knowledge-publishing.md` |
| Category      | Engineering Knowledge Publishing Portal |
| Type          | Engineering Wish                        |
| Status        | 🚧 Discovery                            |
| Previous Wish | `EKPP-W001 — Initial Website Output`    |
| Version       | 0.1                                     |

---

# Original Wish

> **I wish EKPP could automatically publish engineering knowledge.**

---

# Purpose

The purpose of this wish is to transform EKPP from a manually maintained website into an automated Engineering Knowledge Publisher.

Rather than manually creating HTML pages, EKPP should publish engineering knowledge directly from its maintained source documentation.

The published website should always reflect the current engineering knowledge while preserving the single source of truth.

---

# Desired Outcome

EKPP should be capable of transforming engineering documentation into a published website.

Conceptually:

```text
Engineering Knowledge

↓

Markdown Source Documents

↓

EKPP Publisher

↓

Generated HTML

↓

Website

↓

Reader
```

The publishing process should minimize manual effort while preserving engineering intent.

---

# Success Criteria

This wish will be considered granted when EKPP can:

* publish engineering documentation from Markdown sources,
* generate consistent HTML pages,
* preserve document structure and relationships,
* support incremental publication,
* produce a navigable website,
* and eliminate manual page maintenance for published engineering documents.

---

# Current Inputs

This wish builds upon knowledge produced during EKPP-W001.

Important inputs include:

* Website Shell
* Reader Journey
* Engineering Documentation System (EDS)
* Engineering Knowledge System (EKS)
* Assisted Flow of Knowledge (AFK)

---

# Discovery Questions

Current Discovery should answer questions including:

## Publishing Source

* Which Markdown files become publishable?
* How are documents selected?

## Rendering

* How should Markdown become HTML?
* Which Markdown features are supported?
* How are diagrams, tables, and code blocks rendered?

## Navigation

* Should navigation be generated automatically?
* How are document relationships represented?
* How are registries published?

## Assets

* How are images handled?
* How are downloadable files published?
* How are relative links rewritten?

## Metadata

* How are document icons displayed?
* How are document statuses rendered?
* How are document references preserved?

## Incremental Publishing

* Can EKPP publish a single document?
* Can only modified pages be rebuilt?
* When is a full rebuild required?

---

# Initial Architecture Direction

The current conceptual publishing pipeline is:

```text
Markdown

↓

Read

↓

Parse

↓

Transform

↓

Apply Templates

↓

Generate HTML

↓

Publish Website
```

This architecture remains subject to discovery and validation.

---

# Non-Objectives

This wish does not currently include:

* search,
* authentication,
* analytics,
* editing within EKPP,
* document authoring,
* content ownership.

EKPP remains a publishing platform rather than a knowledge management system.

---

# Relationship to Previous Wish

EKPP-W001 answered:

> *Can we see EKPP?*

EKPP-W002 asks:

> *Can EKPP automatically publish engineering knowledge?*

The Website Shell produced during W001 becomes the visual destination for the publishing engine developed during this wish.

---

# Expected Deliverables

Discovery should produce:

* Publishing Architecture
* Publisher Design
* Build Strategy
* Publishing Workflow
* Implementation Plan

Implementation is expected to produce:

* EKPP Publisher
* First generated engineering pages
* Published documentation using real engineering content

---

# Current Status

Current activity:

🚧 Discovery

Focus:

Understand the publishing problem before implementing the publisher.

---

# Closing Thought

The Website Shell demonstrated that EKPP could exist.

This wish explores whether EKPP can become a true Engineering Knowledge Publisher.

Rather than maintaining websites by hand, engineering knowledge itself should become the source from which the website is continuously generated.
