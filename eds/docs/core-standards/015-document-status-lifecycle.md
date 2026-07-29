# 📘 Document Status Lifecycle

> **Document status reflects engineering maturity—not repository history.**

---

# Purpose

Define the lifecycle used to communicate the maturity of Engineering Documentation System (EDS) documents.

A document's status helps readers understand whether the document is being developed, reviewed, validated, adopted, retired, or preserved for historical purposes.

The lifecycle communicates the engineering confidence behind a document, not simply its existence in version control.

---

# Lifecycle Philosophy

Engineering documentation evolves.

A document is rarely created in its final form.

Instead, it progresses through stages of discovery, refinement, validation, and long-term adoption.

```text
Idea

↓

Draft

↓

Review

↓

Accepted

↓

Official

↓

Historical
```

Each stage communicates the document's current level of engineering confidence.

---

# Lifecycle Stages

## 📝 Planning

The document has been proposed but development has not yet begun.

Typical activities include:

- identifying the need
- defining scope
- creating backlog items

---

## 🚧 In Progress

The document is actively being written or revised.

The content should not yet be considered stable.

---

## 👀 Under Review

The document is sufficiently complete for engineering review.

Feedback is actively being gathered.

Changes are expected.

---

## ✅ Accepted

The document has completed review and represents an approved engineering baseline.

Accepted documents:

- may be adopted by projects,
- are expected to receive real-world validation,
- may continue evolving through engineering experience.

Acceptance represents approval—not maturity.

---

## 📦 Official

The document has demonstrated long-term stability through practical engineering use.

Official documents:

- have been validated,
- represent mature engineering guidance,
- become the authoritative engineering standard.

Official status is earned through evidence, not simply approval.

---

## Historical States

Historical states indicate that a document is no longer actively maintained.

### 🔄 Superseded

A newer Engineering Standard replaces this document.

The document is retained for historical traceability.

---

### ❌ Cancelled

Work has been abandoned.

The document remains only as historical context.

---

### 🗃️ Archived

The document is preserved for historical or educational purposes.

No further development is expected.

---

# Supporting States

Additional operational states may be used when appropriate.

| Status | Meaning |
|--------|---------|
| 🧪 Experimental | Exploring an idea that has not yet been validated. |
| ⚠️ Blocked | Progress depends on an external dependency or decision. |
| ⏸️ On Hold | Work has been intentionally paused. |

---

# Accepted vs Official

These two states are intentionally different.

```text
Engineering Review

↓

✅ Accepted

↓

Real Project Usage

↓

Validation

↓

📦 Official
```

A document should **not** become Official simply because:

- it has been committed to Git,
- it exists in the repository,
- it has been reviewed once.

Official status reflects demonstrated engineering confidence.

---

# Relationship to Version Control

Version control records document history.

Document status records engineering maturity.

These concepts complement one another but should never be confused.

```text
Git

↓

Repository History

+

Document Status

↓

Engineering Confidence
```

---

# Updating Status

Document status should change only when the engineering maturity of the document changes.

Routine edits do not necessarily require a status change.

Whenever the status changes:

- update the **As Of** date,
- record the new lifecycle stage,
- ensure the status accurately reflects current engineering confidence.

---

# Relationship to Other Standards

This standard defines how document maturity is communicated throughout the Engineering Documentation System.

Related Standards include:

- Documentation Levels
- Document Template
- Document Icons & Status
- Document References

---

# Companion Reference

For quick lookup of lifecycle stages and usage guidance, see:

**`015r-document-status-lifecycle.md`**

---

## Metadata

| Field | Value |
|------|------|
| Document | `015-document-status-lifecycle.md` |
| Category | Engineering Documentation System |
| Type | 📘 Engineering Standard |
| Companion | `015r-document-status-lifecycle.md` |
| Version | 2.0 |
| Status | ✅ Accepted |
| As Of | 07.29.2026 |
| Owner | Engineering |