# 📘 Document Status Lifecycle

---

## Metadata

**Document:** `015-document-status-lifecycle.md`

**Type:** 📘 Canonical Standard

**Companion Reference:** [015r-document-status-lifecycle.md](./015r-document-status-lifecycle.md)

**Owner:** Engineering

**Version:** 1.0

---

## Status

**As of:** 07.26.2026 HH:MM PHT

✅ Accepted

---

# Purpose

Define the standard lifecycle for engineering documentation.

A document's status indicates its current maturity level and helps readers determine whether the document is being developed, reviewed, accepted, officially adopted, replaced, or archived.

---

# Standard

Every engineering document shall include a **Status** section immediately after the metadata section.

Example:

```markdown
## Status

**As of:** MM.DD.YYYY HH:MM TZ

🚧 In Progress
```

The status should represent the current maturity and lifecycle stage of the document.

The status does not represent Git history.

A document committed to a repository is not automatically considered Official.

---

# Status Lifecycle

Documents generally progress through the following lifecycle.

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
      ▼
📦 Official
```

Not every document must pass through every stage.

The lifecycle represents the normal maturity path for engineering standards.

---

# Standard Statuses

| Status          | Meaning                                                                                        |
| --------------- | ---------------------------------------------------------------------------------------------- |
| 📝 Planning     | Document has been proposed but work has not started.                                           |
| 🚧 In Progress  | Document is actively being developed or revised.                                               |
| 👀 Under Review | Document is complete enough for engineering review and feedback.                               |
| ✅ Accepted      | Document has been approved as a valid baseline and is ready for adoption and validation.       |
| 📦 Official     | Document has matured through validation and is the current authoritative engineering standard. |
| 🔄 Superseded   | Document has been replaced by a newer standard or version.                                     |
| ⏸️ On Hold      | Work has been temporarily paused.                                                              |
| ⚠️ Blocked      | Progress depends on an external issue or decision.                                             |
| 🧪 Experimental | Document describes a prototype or exploratory approach.                                        |
| ❌ Cancelled     | Work has been abandoned and will not continue.                                                 |
| 🗃️ Archived    | Historical document retained for reference only.                                               |

---

# Status Definitions

## Working Statuses

These indicate documents that are still evolving.

* 📝 Planning
* 🚧 In Progress
* 👀 Under Review
* 🧪 Experimental
* ⚠️ Blocked
* ⏸️ On Hold

---

## Adoption Statuses

These indicate approved engineering guidance.

### ✅ Accepted

An Accepted document:

* has completed review,
* represents an approved baseline,
* is ready to be used by projects,
* may still evolve based on real-world feedback.

Accepted documents are candidates for future Official status.

---

### 📦 Official

An Official document:

* has been validated through usage,
* represents mature engineering guidance,
* is the current authoritative standard.

Official status indicates adoption maturity, not simply approval.

---

## Historical Statuses

These indicate documents that are no longer active.

* 🔄 Superseded
* ❌ Cancelled
* 🗃️ Archived

---

# Accepted vs Official

Accepted and Official represent different maturity levels.

```text
Accepted

Approved baseline

      │

      │ Real project usage
      │ Feedback
      │ Refinement

      ▼

Official

Validated engineering standard
```

A document should not become Official only because:

* it has been committed to Git,
* it exists in the repository,
* it has been reviewed once.

Official status represents maturity gained through practical validation.

---

# Git Relationship

Git records document history.

Document status records document maturity.

These are related but separate concepts.

Example:

```text
Git Commit

"docs: establish documentation foundation v1"

        │

        ▼

Repository history

        +

Document Status

        ▼

✅ Accepted
```

The commit creates a historical checkpoint.

The lifecycle determines whether the guidance has reached Official maturity.

---

# Official Documents

Documents with the **📦 Official** status define mature engineering standards.

Documents with the **✅ Accepted** status define approved baseline standards that may be adopted while undergoing validation.

If multiple documents conflict:

1. 📦 Official takes precedence.
2. ✅ Accepted takes precedence over drafts.
3. Older or superseded documents should not override current standards.

---

# Status Registry

The current status of engineering standards should be tracked through:

```text
registry/current-standards.md
```

The registry provides a summary view.

Individual documents remain the source of truth for their own status.

---

# Status Changes

Document status should be updated whenever the document reaches a new lifecycle stage.

The **As of** timestamp should also be updated whenever the status changes.

Status changes should represent meaningful maturity changes, not routine edits.

---

# Related Documents

## Prerequisites

* 001-documentation-system-overview.md
* 005-documentation-level-standard.md

## Related

* 010-document-numbering-standard.md
* 020-document-template-standard.md
* 030-document-icons-and-statuses-standard.md
* 040-document-reference-standard.md

## Companion

* 015r-document-status-lifecycle.md