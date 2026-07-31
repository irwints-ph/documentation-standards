# 💡 Proposal — Document Metadata Placement

> **Place metadata where it best serves the document's primary purpose.**

---

# Metadata

| Field | Value |
|------|------|
| Document | `004-document-metadata-placement.md` |
| Category | Emerging Engineering Concepts |
| Type | Proposal |
| Status | 🚧 Draft |
| Owner | Engineering |
| Version | 0.1 |
| As Of | 2026-07-30 |

---

# Purpose

This proposal introduces a context-aware approach for placing document metadata.

Rather than enforcing a single metadata location across all documentation, metadata should be positioned according to the document's primary consumption pattern.

The objective is to improve readability, reduce interruptions, and optimize both human and AI consumption.

---

# Background

During the development of the Engineering Documentation System, multiple document categories emerged.

Examples include:

- Standards
- Proposals
- Discovery documents
- Architecture documents
- Operational Playbooks
- Knowledge Base articles
- Procedures
- Replay documents
- WWAN dashboards

It became apparent that a single metadata placement strategy does not equally benefit every document type.

---

# Observation

Different documents are consumed differently.

Some documents are intended to be read from beginning to end.

Others are intended to be executed immediately.

Others serve primarily as reference material.

Metadata placement should support these different reading behaviors.

---

# Proposed Principle

Metadata should be positioned where it provides the greatest value without interrupting the primary purpose of the document.

---

# Candidate Placement Guidelines

## Top Metadata

Recommended for documents where identity and status should be immediately visible before reading.

Examples:

- Standards
- Proposals
- Discovery documents
- Architecture documents
- Replay documents
- WWAN

Reasoning:

These documents are primarily informational and often referenced individually. Knowing their identity, version, and status before reading helps establish context.

---

## Bottom Metadata

Recommended for documents whose primary objective is execution rather than reading.

Examples:

- Playbooks
- Procedures
- Operational Runbooks
- Installation Guides
- Step-by-step Instructions

Reasoning:

Readers typically want to begin execution immediately. Metadata can be consulted after completing or reviewing the procedure.

---

## Flexible Metadata

Some document categories may allow either placement depending on context.

Examples:

- Knowledge Base articles
- Tutorials
- Design notes

These should be evaluated individually.

---

# Expected Benefits

A context-aware placement strategy may provide several benefits.

## Improved Readability

Readers encounter the document's primary content immediately.

---

## Better User Experience

Operational documents become easier to execute.

Reference documents become easier to identify.

---

## Improved AI Context

AI systems still receive metadata while maintaining a document structure that aligns with the document's purpose.

---

## Consistency Through Intent

Instead of enforcing identical formatting, the documentation framework remains consistent by applying a consistent decision rule.

---

# Examples

## Standard

```text
Metadata
↓

Purpose
↓

Standard
↓

References
```

---

## Proposal

```text
Metadata
↓

Purpose
↓

Proposal
↓

Assessment
```

---

## Discovery

```text
Metadata
↓

Purpose
↓

Current State
↓

Observations
↓

Assessment
```

---

## Playbook

```text
Purpose
↓

Steps

↓

Verification

↓

Metadata
```

The operational content remains uninterrupted.

---

# Relationship to Replay

Replay documents are primarily narrative and architectural.

Metadata is expected to remain at the beginning.

---

# Relationship to WWAN

WWAN functions as the operational dashboard for current engineering work.

Metadata should remain at the beginning to immediately communicate current status.

---

# Relationship to AFK

AFK emphasizes reducing cognitive overhead during engineering collaboration.

Metadata placement based on document purpose aligns with this objective.

---

# Open Questions

The following require validation.

- Should Knowledge Base articles always place metadata at the bottom?
- Should tutorials follow Playbook conventions?
- Should generated documents automatically choose placement?
- Should templates expose metadata placement as a configurable option?

---

# Validation Plan

Validate this proposal across multiple documentation categories.

Suggested validation projects include:

- Engineering Documentation System
- Video Engine
- Frontend Architecture Audit

Feedback should evaluate:

- readability
- usability
- navigation speed
- AI consumption quality

---

# Current Assessment

Early observations suggest that purpose-driven metadata placement improves document usability while preserving consistency across the documentation framework.

Additional validation is recommended before standardizing this behavior.

---

# Guiding Principle

> **Metadata should support the document—not interrupt it.**