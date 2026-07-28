# 📘 Current EKPP Platform

---

## Metadata

**Document:** `01-current-ekpp-platform.md`

**Type:** 📘 Current Platform

**Project:** Engineering Knowledge Publishing Portal (EKPP)

**Owner:** Engineering

**Version:** 1.0

---

## Status

**As of:** 07.28.2026 16:45 PHT

🚧 Discovery

---

# Purpose

This document describes the current implementation of the Engineering Knowledge Publishing Portal (EKPP).

It captures the platform as it exists today and serves as the baseline for future validation, improvement, and architectural evolution.

This document intentionally describes **what currently exists**, not future design decisions.

---

# Overview

The Engineering Knowledge Publishing Portal (EKPP) is a lightweight static publishing platform used to present engineering knowledge for collaborative review.

The platform currently publishes documentation for:

* Engineering Documentation System (EDS)
* Engineering Knowledge System (EKS)
* Assisted Flow of Knowledge (AFK)

The current implementation prioritizes simplicity, portability, and ease of publishing over advanced website functionality.

---

# Current Technology Stack

| Component       | Current Implementation   |
| --------------- | ------------------------ |
| Frontend        | Static HTML              |
| Styling         | Shared CSS               |
| Navigation      | Shared JavaScript        |
| Source Content  | Markdown                 |
| HTML Generation | Markdown Export          |
| Hosting         | Amazon S3 Static Website |
| Deployment      | AWS CLI                  |

---

# Current Publishing Workflow

```text
Markdown Documents

↓

HTML Export

↓

Local Review

↓

AWS CLI Upload

↓

Amazon S3 Static Website

↓

Collaborative Review
```

The publishing workflow is currently manual.

Each documentation update requires regeneration of the corresponding HTML pages followed by deployment to Amazon S3.

---

# Current Site Structure

Current published content consists primarily of:

```text
index.html

eks.html

afk.html

shared CSS

shared JavaScript

supporting assets
```

Navigation between pages is provided through a reusable sidebar component.

---

# Current Navigation

Navigation is implemented using a shared JavaScript module.

Current characteristics:

* Dynamically injects the navigation sidebar.
* Reuses a common navigation structure across pages.
* Supports responsive navigation using a collapsible sidebar.
* Keeps individual HTML pages independent of navigation implementation.

This approach reduces duplication while keeping deployment simple.

---

# Current Styling

Styling is divided into two responsibilities.

## Page Styling

Each generated document contains its own page styling derived from the Markdown export.

Examples include:

* typography
* spacing
* code blocks
* markdown presentation

---

## Shared Site Styling

A shared stylesheet provides site-wide behavior including:

* navigation drawer
* responsive layout
* menu button
* overall reading experience

This separation allows generated documentation to remain largely independent while sharing a consistent navigation experience.

---

# Current Hosting

The platform is currently hosted using:

Amazon S3 Static Website Hosting

Characteristics include:

* static hosting
* public read access
* low operational complexity
* inexpensive deployment
* AWS CLI publishing

CloudFront is intentionally not part of the current implementation.

---

# Current Strengths

Current implementation provides:

* Simple deployment.
* Minimal infrastructure.
* Low maintenance overhead.
* Fast page loading.
* Portable documentation.
* AI-readable source documents.
* Human-friendly presentation.

---

# Current Limitations

Current implementation also has several known limitations.

Examples include:

* Manual publishing workflow.
* Manual HTML generation.
* No version navigation.
* Limited search capabilities.
* Limited collaborative review features.
* No automated build pipeline.
* No publishing history.

These observations are intentionally descriptive rather than prescriptive.

Potential improvements will be evaluated during later validation phases.

---

# Current AFK Validation

EKPP represents another practical validation of the Assisted Flow of Knowledge methodology.

Unlike previous validation projects that focused on software discovery, EKPP validates how engineering knowledge itself can be published, shared, and collaboratively reviewed.

The platform therefore serves two purposes:

* Publish engineering knowledge.
* Validate the methodology that created that knowledge.

---

# Relationship to Other Projects

## Engineering Documentation System (EDS)

Provides the documentation standards used throughout the published content.

---

## Engineering Knowledge System (EKS)

Provides the broader knowledge framework within which EKPP operates.

---

## Assisted Flow of Knowledge (AFK)

Provides the methodology used to discover, document, and evolve both the published knowledge and the publishing platform itself.

---

# Current Assessment

The platform successfully demonstrates that engineering knowledge can be published using a lightweight static architecture.

Current implementation favors maintainability and simplicity over feature richness.

At this stage, the platform should be understood before significant architectural changes are proposed.

---

# Next Document

Following completion of the current platform snapshot, the next discovery artifact should be:

**02-ekpp-platform-validation.md**

This document will assess the current implementation, identify strengths and gaps, and recommend future improvements based on observed evidence.

---

# Closing Thought

The current platform is intentionally simple.

Its greatest value is not the technology it uses, but the engineering knowledge it helps preserve.

Just as AFK teaches us to understand systems before changing them, this document captures EKPP as it is today so that future improvements are grounded in evidence rather than assumptions.
