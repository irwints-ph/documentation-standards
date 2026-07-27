# 📘 Document Icons and Statuses Reference (Cheatsheet)

---

## Metadata

| Field | Value |
|--------|-------|
| Document | `030a-document-icons-and-statuses-cheatsheet.md` |
| Category | Core Standards |
| Type | Companion Guide |
| Status | ✅ Accepted |
| Companion | `030-document-icons-and-statuses-standard.md` |
| Version | 1.1 |

---

# Purpose

Provide a quick reference for the standardized document icons and lifecycle status icons used throughout the Engineering Documentation System (EDS).

This document complements the **Document Icons and Statuses Standard** by providing a practical copy-and-paste guide for everyday engineering documentation.

The goal is consistency—not decoration.

---

# Core Document Icons

These icons identify the primary purpose of a document.

Each document should have **one primary document icon**.

| Icon | Typical Document | Purpose |
|------|------------------|---------|
| 📄 | README | Repository or folder entry point |
| 📘 | Standard | Canonical engineering standard |
| 📖 | Reference | Companion explanation or supporting knowledge |
| 📍 | WWAN | Where We Are Now (operational status) |
| 🗺️ | Roadmap | Direction, milestones, future planning |
| 🛠️ | Procedure | Step-by-step operational guidance |

---

# Discovery Document Icons

These icons are commonly used during software discovery.

| Icon | Typical Document | Purpose |
|------|------------------|---------|
| 🔍 | Discovery | Discovery notes or investigation |
| 📂 | Folder Registry | Current folder inventory |
| 📊 | Folder Validation | Validation against engineering standards |
| 🧩 | Component | Component documentation |
| 🌐 | API | API documentation |
| ⚙️ | Configuration | Configuration documentation |
| 🏛️ | Architecture Finding | Validated architectural observation |

---

# Knowledge Document Icons

These documents capture reusable engineering knowledge.

| Icon | Typical Document | Purpose |
|------|------------------|---------|
| 💡 | Knowledge Package *(Draft)* | Reusable engineering knowledge |
| 🆘 | Knowledge Base | Troubleshooting and operational guidance |
| 📋 | Checklist | Repeatable engineering activities |

---

# Lifecycle Status Icons

Every document should contain **one lifecycle status**.

| Icon | Status | Meaning |
|------|--------|---------|
| 📝 | Planning | Work has not started |
| 🚧 | In Progress | Currently being developed |
| 👀 | Under Review | Awaiting engineering review |
| 🧪 | Experimental | Prototype, experiment, or research |
| ⏸️ | On Hold | Temporarily paused |
| ⚠️ | Blocked | Waiting on dependency |
| ✅ | Accepted | Engineering-approved document |
| 📦 | Official | Current authoritative engineering document |
| 🔄 | Superseded | Replaced by a newer document |
| ❌ | Cancelled | No longer proceeding |
| 🗃️ | Archived | Historical reference only |

---

# Example — Engineering Standard

```markdown
# 📘 Document Template Standard

---

## Metadata

| Field | Value |
|--------|-------|
| Document | `020-document-template-standard.md` |
| Category | Core Standards |
| Type | Canonical Standard |
| Status | ✅ Accepted |
| Companion | `020r-document-template-standard.md` |
| Version | 1.1 |
```

---

# Example — WWAN

```markdown
# 📍 WWAN — Frontend Discovery

---

## Metadata

| Field | Value |
|--------|-------|
| As of | 07.28.2026 00:45 PHT |
| Category | Frontend Discovery |
| Type | WWAN (Operational Status) |
| Status | 🚧 Discovery In Progress |
```

---

# Example — Architecture Finding

```markdown
# 🏛️ Architecture Finding — Domain Namespace

---

## Metadata

| Field | Value |
|--------|-------|
| Status | ✅ Accepted |
```

---

# Quick Rules

## Document Icons

✅ Use **one primary document icon**

✅ Place the icon in the document title

✅ Choose the icon that best represents the document's primary purpose

❌ Do not combine multiple document icons

❌ Do not invent project-specific icons

---

## Status Icons

✅ Use **one lifecycle status**

✅ Place the status inside the Metadata table

✅ Update the status as the document evolves

---

## General Principles

Icons should:

- Improve recognition
- Improve navigation
- Improve scanning
- Communicate purpose
- Remain consistent across repositories

Icons should **not** be used as decoration.

---

# Common Documents

| Document | Recommended Icon |
|----------|------------------|
| README | 📄 |
| Standard | 📘 |
| Reference | 📖 |
| WWAN | 📍 |
| Roadmap | 🗺️ |
| Procedure | 🛠️ |
| Discovery | 🔍 |
| Folder Registry | 📂 |
| Folder Validation | 📊 |
| Component Documentation | 🧩 |
| Configuration | ⚙️ |
| API Documentation | 🌐 |
| Architecture Finding | 🏛️ |
| Knowledge Package *(Draft)* | 💡 |
| Knowledge Base | 🆘 |
| Checklist | 📋 |

---

# Relationship to EDS

The Engineering Documentation System uses a consistent visual language to help engineers quickly recognize document purpose and lifecycle.

Icons should remain consistent across:

- Core Standards
- Engineering Standards
- Discovery Projects
- Engineering Knowledge System (EKS)
- Assisted Flow of Knowledge (AFK)

Consistency improves readability for both engineers and AI-assisted workflows.

---

# Related Documents

## Standard

- [030-document-icons-and-statuses-standard.md](./030-document-icons-and-statuses-standard.md)

## Reference

- [030r-document-icons-and-statuses-standard.md](./030r-document-icons-and-statuses-standard.md)

## Related

- [020-document-template-standard.md](./020-document-template-standard.md)
- [015-document-status-lifecycle.md](./015-document-status-lifecycle.md)