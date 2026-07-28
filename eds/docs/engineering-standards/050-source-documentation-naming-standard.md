# 📄 050 — Source Documentation Naming Standard

---

## Metadata

| Field | Value |
|--------|-------|
| As of | 07.26.2026 23:00 PHT |
| Document | `050-source-documentation-naming-standard.md` |
| Category | Engineering Standards |
| Type | Canonical Standard |
| Status | ✅ Accepted |
| Companion | `050r-source-documentation-naming-standard.md` |
| Version | 1.0 |

---

# Purpose

This standard defines the naming convention for documentation describing individual source files.

The objective is to establish a predictable one-to-one relationship between implementation artifacts and their corresponding discovery documentation.

The convention simplifies navigation, enables automation, improves maintainability, and ensures consistency across engineering repositories.

---

# Scope

This standard applies to documentation that describes individual implementation files.

Examples include:

* Source code
* Configuration files
* Scripts
* Stylesheets
* SQL files
* Markup files

This standard does **not** apply to:

* Folder registry documents
* Architecture Findings
* Standards
* Knowledge Base articles
* Procedures
* Design documentation

---

# Standard

Documentation describing a source file shall use the complete source filename with the `.md` extension appended.

```
<source filename>.md
```

The original filename shall remain unchanged.

Only the Markdown extension is appended.

---

# Examples

| Source File        | Documentation         |
| ------------------ | --------------------- |
| `Icon.tsx`         | `Icon.tsx.md`         |
| `apiClient.ts`     | `apiClient.ts.md`     |
| `DialogService.ts` | `DialogService.ts.md` |
| `Main.cpp`         | `Main.cpp.md`         |
| `Program.cs`       | `Program.cs.md`       |
| `routes.py`        | `routes.py.md`        |
| `index.html`       | `index.html.md`       |
| `styles.css`       | `styles.css.md`       |
| `database.sql`     | `database.sql.md`     |

---

# Directory Organization

Documentation should mirror the source directory structure whenever practical.

Example:

```
Source

src/
└── components/
    └── icons/
        ├── Icon.tsx
        ├── IconSvg.tsx
        └── IconMaps.ts

↓

Discovery Documentation

docs/
└── ui/
    └── icons/
        ├── Icon.tsx.md
        ├── IconSvg.tsx.md
        └── IconMaps.ts.md
```

Maintaining a similar hierarchy simplifies navigation between implementation and documentation.

---

# Rationale

Using the complete source filename provides several advantages.

## One-to-One Mapping

Each implementation file has exactly one corresponding documentation file.

```
Icon.tsx

↓

Icon.tsx.md
```

No translation or lookup table is required.

---

## Predictable Navigation

Developers can immediately locate the documentation associated with a source file.

Likewise, documentation readers can immediately identify the implementation being described.

---

## Automation Friendly

Tooling can derive documentation filenames directly from source filenames without maintaining additional metadata.

Example workflow:

```
Source File

↓

Append ".md"

↓

Documentation File
```

This convention supports future automation, validation tools, and documentation generators.

---

## Search Friendly

Searching for the implementation filename also locates its documentation.

Example:

```
Search

Icon.tsx

Results

Icon.tsx
Icon.tsx.md
```

---

## Refactoring Friendly

When source files are renamed, their documentation naturally follows the same rename.

```
Old

Icon.tsx
Icon.tsx.md

↓

Rename

IconRenderer.tsx
IconRenderer.tsx.md
```

This minimizes broken references and improves long-term maintainability.

---

## Language Independent

The convention applies consistently across programming languages and technologies.

Examples include:

* TypeScript
* JavaScript
* C#
* Java
* C++
* Python
* HTML
* CSS
* SQL
* Shell scripts

The naming rule remains identical regardless of implementation language.

---

# Benefits

This standard provides:

* Predictable naming
* One-to-one implementation mapping
* Simple navigation
* Reduced ambiguity
* Easier maintenance
* Automation readiness
* Human-friendly organization
* AI-friendly organization

---

# Related Standards

This standard complements:

* 025 — Document Naming Standard
* 040 — Document Reference Standard

Together, these standards define how engineering documentation is consistently named and referenced.

---

# Notes

This standard establishes the naming convention for implementation-level documentation.

It forms part of the Engineering Standards collection, which defines how software systems are documented, discovered, and understood.

Folder registries, architecture findings, validation reports, and other higher-level engineering documents follow their respective standards.
