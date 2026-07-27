# 📖 Document Template Standard (Reference)

---

## Metadata

| Field            | Value                                |
| ---------------- | ------------------------------------ |
| As of            | 07.26.2026 23:30 PHT                 |
| Document         | `020r-document-template-standard.md` |
| Category         | Core Standards                       |
| Type             | Companion Reference                  |
| Status           | ✅ Accepted                          |
| Related Standard | `020-document-template-standard.md`  |
| Version          | 2.0                                  |

---

# Purpose

Provide supporting information, rationale, examples, and implementation guidance for the Document Template Standard.

The companion standard defines **what** the documentation standard is.

This reference explains **why** the standard exists, **how** it should be applied, and **how it evolves** across different engineering artifacts.

This document is intended as the learning guide for engineers adopting the Engineering Documentation System.

---

# Background

Engineering documentation rarely becomes inconsistent intentionally.

It usually evolves over time as different engineers document different problems using different styles.

Typical symptoms include:

* Different section names
* Missing metadata
* Duplicate information
* Inconsistent document layouts
* Difficulty locating information
* Poor cross-document navigation
* Increased effort for AI-assisted engineering

Although each document may be technically correct, the collection gradually becomes difficult to maintain.

The Engineering Documentation System standardizes document structure to eliminate this problem.

---

# Why Standardize Document Structure?

Documentation serves two audiences simultaneously:

* Engineers
* AI systems

Both benefit from consistency.

Engineers quickly learn where information belongs.

AI systems can reliably identify:

* purpose
* ownership
* authority
* relationships
* lifecycle
* engineering rules

Without a consistent structure, every document becomes a unique interpretation.

With a standard, every document becomes immediately recognizable.

---

# The Philosophy Behind the Template

The template is intentionally simple.

Rather than forcing every document into an identical layout, it defines a **common starting point**.

Every document begins with:

```text
Title

Metadata

Purpose
```

From that point forward, the remaining sections depend on the artifact being documented.

This provides consistency without sacrificing flexibility.

---

# Metadata Philosophy

Metadata identifies the engineering artifact.

It should answer the question:

> "What am I looking at?"

before the reader begins reading the content.

Metadata is designed to be:

* concise
* structured
* machine-readable
* human-readable
* stable

Metadata is not intended to explain the artifact.

That is the responsibility of the document itself.

---

# Why a Metadata Table?

Earlier revisions used individual fields:

```markdown
Document:
Type:
Version:
Owner:
```

While readable, this format became difficult to extend as additional document types were introduced.

A table provides several advantages.

## Consistency

Every document begins with the same visual structure.

## Extensibility

Different document types may introduce additional fields without changing the overall format.

## Automation

Structured tables are significantly easier to parse for documentation tooling.

## AI Readability

AI systems can quickly identify metadata fields without interpreting prose.

---

# Standard Metadata Fields

The Engineering Documentation System defines a common set of metadata fields.

Individual document types use only those applicable to the artifact.

| Field            | Purpose                             |
| ---------------- | ----------------------------------- |
| As of            | Current revision timestamp          |
| Document         | Documentation filename              |
| File             | Source implementation filename      |
| Scope            | Folder or subsystem                 |
| Category         | Documentation family                |
| Component        | Logical subsystem                   |
| Type             | Artifact classification             |
| Status           | Lifecycle status                    |
| Companion        | Associated companion document       |
| Related Standard | Standard supported by this document |
| Version          | Document revision                   |

Not every document requires every field.

The objective is consistency, not completeness.

---

# Document Categories

The documentation system currently recognizes several categories of engineering documents.

Examples include:

* Core Standards
* Engineering Standards
* Discovery
* Architecture
* Registry
* UI
* API
* Configuration
* Knowledge Base
* Procedures

Additional categories may be introduced without changing the metadata model.

---

# Document Types

Document type describes the role of the artifact.

Examples include:

* Canonical Standard
* Companion Reference
* Folder Registry
* Source Documentation
* Architecture Finding
* Framework
* Component
* Registry
* Procedure
* Knowledge Base

The document type determines the remainder of the document structure.

---

# Canonical Standards

Canonical Standards answer a single question:

> "What is the current engineering rule?"

Characteristics:

* concise
* authoritative
* implementation focused
* current
* repository independent

Canonical Standards intentionally avoid extensive explanation.

---

# Companion References

Companion References answer:

> "Why does this rule exist?"

They provide:

* background
* rationale
* examples
* migration guidance
* implementation advice
* historical context

Companion References never introduce new engineering rules.

They explain existing ones.

---

# Discovery Documents

Discovery documents record observations about an existing implementation.

They are implementation-specific.

They should describe:

* current implementation
* responsibilities
* dependencies
* observations
* assessments

Discovery documents intentionally avoid recommending redesigns.

---

# Folder Registries

Folder Registries describe the contents of a folder.

Their objectives include:

* ownership
* organization
* classification
* documentation tracking

Registries provide an inventory.

They are not intended to document implementation details.

---

# Source Documentation

Source Documentation records the responsibility of an individual implementation artifact.

Typical subjects include:

* source files
* components
* services
* utilities
* frameworks

The objective is understanding.

Not code review.

---

# Architecture Findings

Architecture Findings record validated architectural observations.

They should be evidence-based.

Findings should not become recommendations.

Recommendations belong in future engineering discussions or standards.

---

# Template Examples

## Canonical Standard

```markdown
# Title

## Metadata

Purpose

Standard

Related Documents
```

---

## Companion Reference

```markdown
# Title

## Metadata

Purpose

Background

Examples

Guidance

Related Documents
```

---

## Folder Registry

```markdown
# Title

## Metadata

Purpose

Folder Responsibility

Current Contents

Assessment
```

---

## Source Documentation

```markdown
# Title

## Metadata

Purpose

Responsibilities

Dependencies

Assessment
```

---

## Architecture Finding

```markdown
# Title

## Metadata

Observation

Evidence

Assessment
```

---

# Why Templates Vary

Not every engineering artifact communicates the same information.

Attempting to force every document into an identical layout creates unnecessary sections.

Instead, the Engineering Documentation System standardizes:

* beginning structure
* metadata
* terminology
* navigation

while allowing later sections to adapt to the artifact.

---

# AI Considerations

The documentation framework has been intentionally designed to support AI-assisted engineering.

Consistent metadata enables AI systems to identify:

* document authority
* lifecycle
* engineering domain
* ownership
* relationships

Predictable document layouts reduce ambiguity and improve retrieval quality.

---

# Automation Considerations

Structured metadata enables future tooling such as:

* documentation validation
* registry generation
* cross-reference validation
* document indexing
* engineering dashboards
* dependency analysis

The template was intentionally designed to remain simple while supporting these future capabilities.

---

# Common Mistakes

## Mixing Rules with Explanations

Canonical Standards should define rules.

References should explain them.

---

## Mixing Discovery with Recommendations

Discovery records observations.

Recommendations belong elsewhere.

---

## Overusing Metadata

Only include metadata applicable to the artifact.

More metadata does not necessarily improve documentation.

---

## Treating Templates as Rigid

Templates provide consistency.

They should not prevent clear communication.

Additional sections may be introduced where appropriate provided they do not violate established standards.

---

# Evolution of the Standard

Version 1 established a common document layout.

Version 2 introduces a metadata-driven documentation model capable of supporting multiple engineering artifact types while maintaining a consistent user experience.

Future revisions may introduce:

* documentation validation tooling
* automated template generation
* engineering dashboards
* metadata extraction
* repository-wide document analysis

The overall philosophy, however, is expected to remain stable.

---

# Relationship to Other Standards

This document supports:

* 001 Documentation System Overview
* 005 Documentation Level Standard
* 010 Document Numbering Standard
* 015 Document Status Lifecycle
* 020 Document Template Standard
* 025 Document Naming Standard
* 040 Document Reference Standard
* 050 Source Documentation Naming Standard

---

# Notes

The Engineering Documentation System is intended to evolve alongside engineering practice.

Templates should improve documentation without becoming burdensome.

The objective is to create documentation that engineers naturally maintain because it is useful, rather than because it is required.

Consistency should always improve clarity.

Clarity should always take precedence over complexity.
