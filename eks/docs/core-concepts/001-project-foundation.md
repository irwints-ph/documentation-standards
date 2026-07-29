# 📄 Project Foundation

> **Every engineering project needs a shared understanding before technical understanding.**

---

# Purpose

The Project Foundation establishes the long-lived engineering context for a project.

It explains **what the project is**, **why it exists**, and **the environment in which engineering work takes place**.

Unlike discovery documents, the Project Foundation changes infrequently and serves as the baseline understanding for all future collaboration.

---

# Objective

Provide a stable, high-level understanding of the project that can be shared by:

- Engineers
- AI collaborators
- New team members
- Future maintainers

The Project Foundation minimizes repeated explanations and gives every engineering session a common starting point.

---

# What a Project Foundation Contains

A Project Foundation typically describes:

- Project overview
- Business purpose
- Primary users
- Technology stack
- Known constraints
- Engineering objectives

It should remain concise and avoid implementation details.

---

# What It Does Not Contain

The Project Foundation is not intended to replace:

- Architecture documentation
- Discovery documents
- API documentation
- Folder registries
- WWAN
- Knowledge packages

Those documents evolve independently as engineering work progresses.

---

# Relationship to Other Artifacts

Each artifact answers a different question.

| Artifact | Primary Question |
|----------|------------------|
| Kuwento Specs | What is the story of this project? |
| Project Foundation | What kind of project is this? |
| Discovery | How is it implemented? |
| WWAN | Where are we now? |
| Knowledge Package | What reusable knowledge should be preserved? |

Together they create a complete engineering context.

---

# Lifecycle

The Project Foundation is usually created during the first engineering session.

Afterward it evolves only when significant project understanding changes.

Examples include:

- major business changes
- technology migrations
- architectural direction changes
- significant scope changes

Routine implementation work should not require Project Foundation updates.

---

# Benefits

Maintaining a Project Foundation provides several advantages:

- Faster onboarding
- Better AI collaboration
- Reduced context reconstruction
- Shared project vocabulary
- Consistent engineering understanding

---

# Engineering Philosophy

Projects evolve.

Implementations evolve.

Conversations evolve.

The Project Foundation exists to preserve the parts that should remain stable.

It provides a shared understanding that survives individual engineering sessions.

---

# Relationship to AFK

Within Assisted Flow of Knowledge (AFK), the Project Foundation is one of the foundational engineering artifacts.

Typical flow:

```text
Kuwento Specs
        ↓
Project Foundation
        ↓
Discovery
        ↓
WWAN
        ↓
Knowledge
```

The Project Foundation captures the enduring context that supports all later engineering activities.

---

# Related Documents

## Related

- `../concepts/001-kuwento-specs.md` *(Draft)*
- `../collaboration/010-project-foundation.md`
- `../collaboration/001-understanding-wwan.md`
- `../methodology/020-afk-discovery.md`

---

# Guiding Principle

> **Build shared understanding before building shared solutions.**

---

## Metadata

| Field | Value |
|-------|-------|
| Document | `001-project-foundation.md` |
| Type | Foundation |
| Version | 1.0 |
| Status | 🚧 Draft |
| As of | 07.29.2026 |