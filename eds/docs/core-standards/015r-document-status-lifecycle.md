# 📑 Document Status Lifecycle — Reference

> **Quick guide for assigning and interpreting document lifecycle statuses.**

---

# Purpose

Provide a concise operational reference for applying document lifecycle statuses within the Engineering Documentation System (EDS).

For the complete explanation, rationale, and lifecycle philosophy, see:

**`015-document-status-lifecycle.md`**

---

# Lifecycle Summary

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

Historical states:

```text
📦 Official

      │

      ├── 🔄 Superseded

      ├── 🗃️ Archived

      └── ❌ Cancelled
```

---

# Status Reference

| Status | Use When |
|--------|----------|
| 📝 Planning | Work has been identified but has not started. |
| 🚧 In Progress | The document is actively being written or revised. |
| 👀 Under Review | Ready for engineering review and feedback. |
| ✅ Accepted | Approved baseline ready for project adoption and validation. |
| 📦 Official | Mature, validated engineering guidance. |
| 🧪 Experimental | Exploring an idea that is not yet validated. |
| ⚠️ Blocked | Progress depends on an external dependency. |
| ⏸️ On Hold | Work has been intentionally paused. |
| 🔄 Superseded | Replaced by a newer standard. |
| ❌ Cancelled | Work has been abandoned. |
| 🗃️ Archived | Retained for historical reference only. |

---

# Accepted vs Official

| Accepted | Official |
|----------|----------|
| Engineering review completed | Proven through real-world engineering use |
| Ready for adoption | Mature engineering standard |
| May still evolve | Considered stable guidance |

---

# Status Checklist

Before changing a document status:

- ☐ Has the document reached a new engineering maturity level?
- ☐ Is the status based on engineering evidence rather than repository activity?
- ☐ Has the **As Of** date been updated?
- ☐ Does the new status accurately reflect current engineering confidence?

---

# Status Placement

Every Engineering Standard should include its current status near the end of the document metadata.

Example:

```text
Status

✅ Accepted

As Of

07.29.2026
```

---

# Relationship to Git

Remember:

```text
Git

↓

Version History

Document Status

↓

Engineering Maturity
```

Git tracks revisions.

Status communicates engineering confidence.

They serve different purposes.

---

# Related Standards

Core Standards

- `001` Documentation System Overview
- `005` Documentation Levels
- `020` Document Template
- `030` Document Icons & Status
- `040` Document References

---

# Companion Standard

For the complete lifecycle explanation and philosophy, see:

**`015-document-status-lifecycle.md`**

---

## Metadata

| Field | Value |
|------|------|
| Document | `015r-document-status-lifecycle.md` |
| Category | Engineering Documentation System |
| Type | 📑 Reference |
| Companion | `015-document-status-lifecycle.md` |
| Version | 2.0 |
| Status | ✅ Accepted |
| As Of | 07.29.2026 |
| Owner | Engineering |