# Engineering Knowledge Presentation Methodology (Draft)

---

## Status

🚧 Draft

---

# Purpose

Explore how engineering knowledge can be presented to different audiences without duplicating or fragmenting the underlying source of knowledge.

This draft investigates the use of Markdown-based presentations as an extension of the Engineering Knowledge System and the Assisted Flow of Knowledge (AFK).

The long-term objective is to make presentations another representation of engineering knowledge rather than a separate artifact.

---

# Problem Statement

Traditional presentations often become disconnected from the engineering knowledge they are intended to communicate.

Typical workflow:

```text
Documentation
        │
        ▼
Copy into PowerPoint
        │
        ▼
Presentation
        │
        ▼
Presentation becomes outdated
```

This creates multiple problems:

* Duplicate maintenance
* Knowledge drift
* Version inconsistency
* Difficult collaboration
* Limited AI accessibility

---

# Proposed Direction

Treat presentations as another **knowledge view**.

Instead of maintaining separate content, presentations should derive from the same engineering knowledge base.

```text
Engineering Knowledge

        │

        ├── Documentation

        ├── Standards

        ├── Discovery

        ├── Architecture

        ├── Presentation

        └── Training
```

Each view serves a different audience while sharing the same underlying knowledge.

---

# Candidate Technology

Current recommendation:

## Marp

Reasons:

* Markdown native
* Git friendly
* AI friendly
* Human readable
* Easy review through pull requests
* Supports diagrams
* Simple navigation
* Export capability when required

Presentation files remain ordinary Markdown documents.

---

# Relationship to AFK

The Assisted Flow of Knowledge encourages preserving engineering context as reusable artifacts.

Presentations become part of that flow.

```text
Engineering Knowledge
        │
        ▼
Presentation
        │
        ▼
Discussion
        │
        ▼
Feedback
        │
        ▼
Improved Knowledge
```

Rather than ending with the presentation, the knowledge returns to the repository.

---

# Proposed Knowledge Views

Current knowledge representations under consideration:

| Knowledge View | Primary Audience       |
| -------------- | ---------------------- |
| Standard       | Engineers              |
| Reference      | Engineers              |
| Discovery      | Engineers              |
| Architecture   | Engineers / Architects |
| Presentation   | Teams / Leadership     |
| Tutorial       | Learners               |
| Workshop       | Interactive sessions   |
| Playbook       | Operational teams      |
| Checklist      | Daily engineering work |

Each representation communicates the same knowledge at different levels of detail.

---

# Architecture Diagrams

Architecture remains best represented using dedicated diagram tools.

Current recommendation:

```text
Draw.io

↓

SVG

↓

Referenced by Markdown
```

Example:

```markdown
# API Architecture

![API Architecture](architecture.svg)
```

The diagram remains independently editable while becoming part of the presentation.

---

# Knowledge Representation Pipeline

```text
Engineering Knowledge
            │
            ▼
Knowledge Views
            │
            ├── Documentation
            ├── Standards
            ├── Architecture
            ├── Presentations
            ├── Tutorials
            └── Workshops
```

Knowledge is authored once and represented multiple ways.

---

# Candidate Workflow

```text
Discovery
        │
        ▼
Documentation
        │
        ▼
Validated Knowledge
        │
        ▼
Presentation
        │
        ▼
Discussion
        │
        ▼
Feedback
        │
        ▼
Knowledge Updated
```

Every presentation becomes another validation activity.

---

# Potential Repository Organization

```text
knowledge/

    standards/

    references/

    discovery/

    architecture/

    presentations/

    tutorials/

    playbooks/

    workshops/
```

Each folder contains a different representation of engineering knowledge rather than a separate body of knowledge.

---

# Initial Presentation Structure

Candidate structure for engineering presentations:

```text
Title

Problem

Current Situation

Observation

Discovery

Evidence

Solution

Methodology

Benefits

Roadmap

Questions
```

This structure aligns naturally with engineering storytelling.

---

# Future Exploration

Potential research topics include:

* Presentation metadata standards
* Presentation lifecycle
* Knowledge-to-presentation automation
* Embedded architecture diagrams
* Interactive engineering workshops
* AI-assisted presentation generation
* Presentation validation workflows

---

# Relationship to the Engineering Knowledge System

This draft extends the Engineering Knowledge System by proposing presentations as reusable engineering artifacts.

It supports the broader objective of AFK:

> Preserve engineering knowledge in forms that are useful to both humans and AI while minimizing duplication.

---

# Open Questions

* Should presentations become a formal Knowledge View within the EKS?
* Can presentation decks be generated automatically from validated engineering knowledge?
* Should presentations follow their own metadata standard?
* How should presentations reference standards, architecture, and discovery artifacts?
* Can presentation feedback become part of the knowledge validation process?

---

## My favorite idea in this draft

One sentence stood out as a potential guiding principle for the future EKS:

> **A presentation is not a deliverable—it is a temporary view of validated engineering knowledge for a specific audience.**

That single principle ties together AFK, EKS, Marp, and your documentation framework. Instead of creating slides as isolated assets, you're simply exposing the same knowledge in the form most appropriate for the moment. I can easily imagine this becoming one of the foundational ideas of the Engineering Knowledge System.
