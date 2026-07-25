# 📖 Documentation Level Standard (Reference)

---

## Metadata

**Document:** 005r-documentation-level-standard.md

**Type:** 📖 Reference

**Companion Standard:** 005-documentation-level-standard.md

**Owner:** Engineering

**Version:** 1.0

---

## Status

**As of:** 07.25.2026 06:55 PHT

✅ Accepted

---

# Purpose

Explain the reasoning behind the documentation levels used throughout the Engineering Documentation System.

This document describes why the documentation is divided into Official and Reference levels, the problems this solves, and the principles that guide their use.

---

# Why Documentation Levels Exist

Engineering documentation serves multiple audiences.

An engineer returning after several months usually needs only a quick reminder of the current standard.

A new team member may need historical background, design rationale, examples, and implementation guidance.

AI assistants perform best when provided with concise, focused context rather than lengthy discussions.

Attempting to satisfy all of these audiences with a single document often results in documentation that is too long for quick reference and too brief for effective learning.

To address this, the Engineering Documentation System separates documentation into two complementary levels.

---

# Official Documents

Official documents define engineering standards.

They are intended to answer one question:

> **"What is the current engineering standard?"**

Official documents intentionally avoid unnecessary explanation.

Instead, they focus on the information required to correctly implement or follow the standard.

Typical contents include:

* Purpose
* Rules
* Required structure
* Naming conventions
* Short examples
* Related documents

Official documents should remain concise enough to be reviewed quickly and should generally fit within one or two pages.

Because of their size and structure, they are also suitable for use as AI project context.

---

# Reference Documents

Reference documents explain the engineering standard.

They answer questions such as:

* Why was this standard created?
* What problems does it solve?
* How has it evolved?
* What alternatives were considered?
* What lessons have been learned?

Reference documents intentionally have no practical length limit.

Their goal is preservation of engineering knowledge rather than quick implementation.

Typical contents include:

* Design rationale
* Historical evolution
* Migration guidance
* Frequently asked questions
* Extended examples
* Best practices
* Lessons learned

---

# Relationship Between Levels

The two documentation levels are complementary.

The Official document defines the standard.

The Reference document explains the standard.

The Reference document must never replace or contradict the Official document.

If additional explanation becomes necessary, it belongs in the Reference document rather than expanding the Official document unnecessarily.

---

# When a Reference Document Is Needed

Not every Official document requires a companion Reference.

A Reference document should be created when the topic benefits from additional explanation that is expected to remain valuable over time.

Examples include:

* Complex engineering standards
* Architectural decisions
* Design philosophies
* Migration strategies
* Frequently misunderstood concepts

Short or self-explanatory standards may not require a companion Reference document.

---

# Benefits of Two Documentation Levels

## Faster Navigation

Experienced engineers can quickly locate the current standard without reading historical discussion.

---

## Better AI Context

Official documents are intentionally optimized for AI-assisted engineering by minimizing unnecessary context.

---

## Easier Maintenance

Most engineering changes affect only the Official document.

Supporting rationale remains stable within the Reference document.

---

## Historical Preservation

Engineering knowledge, discussions, and lessons learned remain available without cluttering the current standard.

---

## Consistency Across Repositories

Using the same documentation levels across all repositories creates a predictable documentation experience for engineers regardless of project size or technology.

---

# Common Misunderstandings

### Is an Official document a summary?

No.

An Official document is the complete engineering standard.

It is concise because unnecessary explanation has been moved to the companion Reference document.

---

### Is a Reference document optional?

Yes.

Reference documents should be created only when they provide long-term value.

Many simple standards can be fully documented using only an Official document.

---

### Can engineers update only the Reference document?

Yes, provided the engineering standard itself does not change.

Historical notes, examples, FAQs, and implementation guidance may evolve independently of the Official document.

If the engineering standard changes, the Official document must be updated first.

---

### Which document takes precedence?

The Official document always represents the current engineering standard.

If a conflict exists between the two documents, the Official document is considered authoritative.

---

# Design Principles

The documentation level model follows several guiding principles.

* Standards should be easy to find.
* Standards should be easy to read.
* Historical knowledge should never be lost.
* AI context should remain concise.
* Documentation should grow without becoming difficult to maintain.
* The documentation system should remain consistent across all engineering repositories.

---

# Related Documents

## Prerequisite

* 001-documentation-system-overview.md
* 005-documentation-level-standard.md

## Related

* 010-document-numbering-standard.md
* 020-document-status-lifecycle.md
* 030-document-template-standard.md
* 040-document-naming-standard.md
* 045-terminology-standard.md

## Companion

* 005-documentation-level-standard.md

---

# Revision Notes

This Reference document explains the philosophy behind the two-level documentation model.

Future revisions should preserve the underlying design principles while allowing the companion Official document to remain concise, implementation-focused, and suitable for use as AI project context.
