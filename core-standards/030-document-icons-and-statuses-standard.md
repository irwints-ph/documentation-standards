# 📘 Document Icons and Statuses Standard

---

## Metadata

| Field | Value |
|--------|-------|
| Document | `030-document-icons-and-statuses-standard.md` |
| Category | Core Standards |
| Type | Canonical Standard |
| Status | ✅ Accepted |
| Companion | `030r-document-icons-and-statuses-standard.md` |
| Version | 1.1 |

---

# Purpose

Define the standardized document icons and lifecycle status icons used throughout the Engineering Documentation System (EDS).

The visual language improves recognition, navigation, and consistency while remaining simple enough to be reused across projects, repositories, and engineering disciplines.

---

# Standard

## One Primary Document Icon

Every document shall have **one primary document icon**.

The icon identifies the document's primary engineering purpose.

Example

```markdown
# 📘 Document Template Standard
```

---

## One Lifecycle Status

Every document shall contain **one lifecycle status**.

The lifecycle status communicates the document's current engineering maturity.

Example

```markdown
## Metadata

| Field | Value |
|--------|-------|
| Status | ✅ Accepted |
```

Lifecycle definitions are maintained by:

```text
015-document-status-lifecycle.md
```

---

## Placement

Document icons shall appear in the document title.

Lifecycle status shall appear within the Metadata table.

| Element | Standard |
|----------|----------|
| Document Title | Primary Document Icon |
| Metadata | Lifecycle Status |
| Tables | Optional where helpful |
| Body Text | Optional where helpful |

---

## Icon Categories

The Engineering Documentation System defines two categories of icons.

### Document Icons

Document icons identify the primary purpose of a document.

Examples include:

- README
- Standard
- Reference
- WWAN
- Roadmap
- Procedure
- Discovery
- Architecture Finding

---

### Lifecycle Status Icons

Lifecycle status icons communicate document maturity.

Examples include:

- Planning
- In Progress
- Under Review
- Experimental
- Accepted
- Official
- Archived

---

## Standardized Icon Set

Only standardized document icons and lifecycle status icons shall be used.

The complete reference is maintained in:

```text
030a-document-icons-and-statuses-cheatsheet.md
```

---

# Principles

Engineering documentation shall follow these principles.

- One primary document icon per document.
- One lifecycle status per document.
- Icons communicate purpose—not decoration.
- Icons improve recognition and navigation.
- Do not combine multiple primary document icons.
- Do not invent project-specific icons.
- Maintain consistent icon usage across EDS, EKS, AFK, and all discovery projects.

---

# Related Documents

## Prerequisites

- [020-document-template-standard.md](./020-document-template-standard.md)
- [015-document-status-lifecycle.md](./015-document-status-lifecycle.md)

## Related

- [001-documentation-system-overview.md](./001-documentation-system-overview.md)

## Companion

- [030a-document-icons-and-statuses-cheatsheet.md](./030a-document-icons-and-statuses-cheatsheet.md)
- [030r-document-icons-and-statuses-standard.md](./030r-document-icons-and-statuses-standard.md)