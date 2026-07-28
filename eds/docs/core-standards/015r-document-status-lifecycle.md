# 📖 Document Status Lifecycle (Reference)

---

## Metadata

**Document:** `015r-document-status-lifecycle.md`

**Type:** 📖 Reference Document

**Companion Standard:** [015-document-status-lifecycle.md](./015-document-status-lifecycle.md)

**Owner:** Engineering

**Version:** 1.0

---

## Status

**As of:** 07.26.2026 HH:MM PHT

✅ Accepted

---

# Purpose

Explain the philosophy, rationale, and recommended practices behind the Engineering Documentation Status Lifecycle.

This document supplements the companion standard by describing why document statuses exist, how they should be used throughout a document's lifecycle, and how they support collaboration, maintenance, and long-term knowledge preservation.

---

# Why Document Status Matters

Documentation is not static.

Like software, documents evolve through planning, drafting, review, adoption, revision, and retirement.

Without a clearly defined status, readers cannot easily determine whether a document is:

* an initial idea,
* a work in progress,
* an approved baseline,
* a mature engineering standard,
* or historical reference material.

The status lifecycle provides this context at a glance.

---

# Design Goals

The document status lifecycle was designed to:

* Communicate document maturity.
* Prevent unfinished work from being mistaken as engineering guidance.
* Separate approved standards from mature standards.
* Identify current authoritative documentation.
* Preserve historical decisions without cluttering active documentation.
* Support AI-assisted engineering workflows.
* Provide a consistent workflow across repositories.

---

# Lifecycle Philosophy

Documents mature over time.

Ideas become drafts.

Drafts become reviewed proposals.

Reviewed proposals become accepted engineering guidance.

Accepted guidance becomes official after practical validation and adoption.

Eventually, standards may be replaced or retired.

The documentation system records this progression through standardized status values.

This preserves engineering history while keeping current standards easy to identify.

---

# Standard Lifecycle

The normal progression is:

```text
📝 Planning
      │
      ▼
🚧 In Progress
      │
      ▼
👀 Under Review
      │
      ▼
✅ Accepted
      │
      │
      │ Real project usage
      │ Feedback
      │ Validation
      │
      ▼
📦 Official
```

After publication, a document may transition into historical states.

```text
📦 Official
      │
      ├──────────────► 🔄 Superseded
      │
      ├──────────────► 🗃️ Archived
      │
      └──────────────► ❌ Cancelled
```

Temporary statuses such as:

* ⚠️ Blocked
* ⏸️ On Hold
* 🧪 Experimental

may occur during development.

---

# Status Categories

## Working Statuses

These indicate active development.

* 📝 Planning
* 🚧 In Progress
* 👀 Under Review
* 🧪 Experimental
* ⚠️ Blocked
* ⏸️ On Hold

Documents in these states should not be considered approved standards.

---

## Adoption Statuses

These indicate approved engineering guidance.

## ✅ Accepted

The document has been reviewed and approved.

It represents an approved baseline that can be adopted by projects.

Accepted documents:

* have completed review,
* are considered valid guidance,
* may still receive improvements based on practical usage,
* are candidates for Official status.

---

## 📦 Official

The document is the mature, validated engineering standard.

Official documents:

* have been proven through practical usage,
* represent the current authoritative guidance,
* should be followed when applicable.

Official status represents adoption maturity, not simply approval.

---

# Git and Status Relationship

Git history and document lifecycle serve different purposes.

Git answers:

> When was a change recorded?

Document status answers:

> How mature and authoritative is this guidance?

Example:

```text
Git Commit

"docs: establish documentation foundation v1"

        │

        ▼

Repository history


Document Lifecycle

        │

        ▼

✅ Accepted
```

A Git commit does not automatically make a document Official.

---

# Status Change Philosophy

Status changes should represent meaningful maturity milestones.

Examples:

| Event                           | New Status      |
| ------------------------------- | --------------- |
| Idea identified                 | 📝 Planning     |
| Writing begins                  | 🚧 In Progress  |
| Ready for feedback              | 👀 Under Review |
| Review completed                | ✅ Accepted      |
| Validated through project usage | 📦 Official     |
| Replaced by newer guidance      | 🔄 Superseded   |
| Work paused                     | ⏸️ On Hold      |
| Dependency prevents progress    | ⚠️ Blocked      |
| Experimental investigation      | 🧪 Experimental |
| Work abandoned                  | ❌ Cancelled     |
| Historical retention only       | 🗃️ Archived    |

---

# Accepted vs Official

The documentation system intentionally separates Accepted and Official.

## Accepted

Accepted means:

> "This guidance has been reviewed and approved."

It does not necessarily mean:

* widely adopted,
* validated across projects,
* unchanged forever.

Examples:

* New engineering standards awaiting project validation.
* Framework improvements before broader adoption.
* Initial documentation foundations.

---

## Official

Official means:

> "This is the validated engineering standard."

Official documents are:

* mature,
* adopted,
* authoritative.

For a specific topic, there should normally be one Official standard.

---

# Why Preserve Historical Status?

Engineering documentation represents institutional knowledge.

Historical documents explain:

* why decisions were made,
* what alternatives were considered,
* how standards evolved.

Deleting outdated documents removes valuable context.

Instead, documents should transition to:

* 🔄 Superseded
* 🗃️ Archived

while remaining available for reference.

---

# Recommended Practices

To maintain consistency:

* Every document should include a Status section.
* Update the **As of** timestamp whenever status changes.
* Use only one lifecycle status at a time.
* Do not use Git commits as a replacement for document status.
* Do not mark documents Official without validation and adoption.
* Prefer Superseded over deleting obsolete standards.
* Track standard maturity through the standards registry.

---

# Common Questions

## Can a document move backward?

Yes.

A document under review may return to 🚧 In Progress if significant changes are required.

The lifecycle describes current maturity, not a strict one-way process.

---

## Can a document remain Accepted?

Yes.

Accepted is a valid state.

A document may remain Accepted while:

* being used for validation,
* waiting for broader adoption,
* awaiting related standards.

---

## Should historical documents be deleted?

No.

Historical documents preserve engineering knowledge.

They should normally transition to:

* 🔄 Superseded
* 🗃️ Archived

---

## Can multiple documents be Official?

Yes, if they define different topics.

For the same topic, there should normally be one authoritative Official document.

---

## Should session documents become Official?

No.

Session documents record development history.

They are historical engineering records, not standards.

---

# Future Evolution

The lifecycle may evolve to support:

* automated documentation validation,
* review workflows,
* publication pipelines,
* maturity dashboards,
* AI-assisted recommendations.

Future enhancements should extend the lifecycle without changing the meaning of existing statuses.

---

# Related Documents

## Prerequisites

* [001-documentation-system-overview.md](./001-documentation-system-overview.md)
* [005-documentation-level-standard.md](./005-documentation-level-standard.md)

## Related

* [010-document-numbering-standard.md](./010-document-numbering-standard.md)
* [020-document-template-standard.md](./020-document-template-standard.md)
* [030-document-icons-and-statuses-standard.md](./030-document-icons-and-statuses-standard.md)
* [040-document-reference-standard.md](./040-document-reference-standard.md)

## Registry

* [registry/core-standards.md](../registry/core-standards.md)

## Companion

* [015-document-status-lifecycle.md](./015-document-status-lifecycle.md)
