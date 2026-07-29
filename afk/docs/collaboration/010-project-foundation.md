# 🤝 Project Foundation

> **Every engineering session begins by understanding the project before understanding the code.**

---

# Purpose

The Project Foundation establishes a shared understanding of the project between engineers and AI collaborators.

Before reading source code, both collaborators should understand:

- why the project exists,
- who it serves,
- what it currently does,
- what it is trying to achieve.

This creates a common engineering context that makes later discovery significantly more effective.

---

# Objective

Capture the minimum information required to begin collaborating on an existing project.

The goal is **shared understanding**, not complete documentation.

---

# What to Capture

## Project Overview

Describe the project at a high level.

Examples:

- Internal business application
- Customer-facing website
- API service
- Shared component library
- Mobile application

---

## Purpose

Why does this project exist?

What business problem does it solve?

---

## Users

Who uses the system?

Examples:

- Customers
- Internal users
- Administrators
- Engineers
- External systems

---

## Current Objective

What is the current engineering objective?

Examples:

- Understand the existing implementation
- Validate architecture
- Fix production issues
- Prepare for migration
- Add new functionality

---

## Technology Stack

Record only the technologies that are immediately relevant.

Examples:

- React
- Angular
- Vue
- .NET
- Java
- Node.js
- PostgreSQL

Detailed technical discovery happens later.

---

## Known Constraints

Capture important information already known.

Examples:

- Legacy system
- Production application
- Active users
- Tight deadlines
- Regulatory requirements

---

# Example

```markdown
## Project Overview

Internal frontend application used to manage customer transactions.

---

## Purpose

Provide operational staff with a unified interface for managing customer workflows.

---

## Users

- Operations Team
- Customer Support
- Administrators

---

## Current Objective

Understand the existing implementation before proposing architectural improvements.

---

## Technology Stack

- React
- TypeScript
- OIDC
- REST APIs

---

## Known Constraints

- Large existing codebase
- Production system
- Active development
```

---

# Engineering Notes

Keep this document concise.

Avoid documenting:

- implementation details
- architecture
- APIs
- folder structures
- components

Those belong to discovery.

The Project Foundation answers one question:

> **"What kind of project are we about to explore?"**

---

# Relationship to Other Documents

After completing the Project Foundation:

➡ Read the project's WWAN (if available)

Then continue with:

- Existing Codebase Playbook
- Existing Codebase Learning Path
- Discovery Methodology

---

# Guiding Principle

> **Understand the project before understanding the implementation.**

A shared understanding of the project creates better engineering conversations and better AI collaboration.

---

## Metadata

| Field | Value |
|-------|-------|
| Document | `010-project-foundation.md` |
| Type | Collaboration |
| Version | 2.0 |
| Status | ✅ Active |
| As of | 07.29.2026 |