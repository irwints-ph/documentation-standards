# 📘 Document Naming Standard

---

## Metadata

**Document:** `025-document-naming-standard.md`

**Type:** 📘 Official Standard

**Companion Reference:** [025r-document-naming-standard.md](./025r-document-naming-standard.md)

**Owner:** Engineering

**Version:** 1.0

---

## Status

**As of:** 07.25.2026 06:40 PHT

✅ Accepted

---

# Purpose

Define the standard naming convention for engineering documentation.

Consistent document names improve discoverability, readability, cross-referencing, automation, and long-term maintenance across engineering repositories.

---

# Standard

All engineering documents shall follow a consistent file naming convention.

General format:

```text
NNN-document-name.md
```

Reference companion:

```text
NNNr-document-name.md
```

Where:

- `NNN` is the document sequence number.
- `r` identifies the companion Reference document.
- `document-name` is a short descriptive name.
- `.md` is the Markdown file extension.

---

# Naming Rules

Document names shall:

- Use lowercase letters.
- Use hyphens (`-`) to separate words.
- Use descriptive names.
- Be stable once published.
- Match the document purpose.

---

## Characters

Use:

```text
a-z
0-9
-
```

Avoid:

- Spaces
- Underscores (`_`)
- CamelCase
- PascalCase
- Special characters
- Punctuation (except hyphens)

---

## Number Prefix

Every Official document begins with a three-digit sequence.

Example:

```text
001-documentation-system-overview.md
005-documentation-level-standard.md
010-document-numbering-standard.md
025-document-naming-standard.md
```

---

## Reference Documents

Reference documents append an `r` immediately after the document number.

Example:

```text
001r-documentation-system-overview.md
015r-document-status-lifecycle.md
025r-document-naming-standard.md
```

The `r` indicates the file is the Reference companion to the corresponding Official document.

---

## Templates

Templates follow the standard naming convention.

Example:

```text
000-template-where-we-are-now.md
020-template-engineering-standard.md
```

---

## Snapshot Documents

Working dashboard documents use descriptive names.

Example:

```text
000-where-we-are-now.md
```

---

## Folder Names

Documentation folders shall follow the same convention.

Use:

```text
engineering-history/
git/
templates/
roadmaps/
knowledge-base/
```

Do not use:

```text
Engineering History/
EngineeringHistory/
engineering_history/
```

---

# File Extensions

Documentation files use:

```text
.md
```

Supporting assets retain their native extensions.

Examples:

```text
png
svg
pdf
csv
xlsx
```

---

# Related Documents

## Prerequisites

- [001-documentation-system-overview.md](./001-documentation-system-overview.md)
- [005-documentation-level-standard.md](./005-documentation-level-standard.md)
- [010-document-numbering-standard.md](./010-document-numbering-standard.md)

## Related

- [020-document-template-standard.md](./020-document-template-standard.md)
- [035-terminology-standard.md](./035-terminology-standard.md)

## Companion

- [025r-document-naming-standard.md](./025r-document-naming-standard.md)