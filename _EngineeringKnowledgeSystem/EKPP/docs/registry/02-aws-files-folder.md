# 📄 AWS Files Folder

---

## Purpose

This document explains the purpose of the `aws-files/` folder.

---

## Folder Purpose

The `aws-files/` folder contains the current production website deployed to AWS.

These files are preserved to provide a stable reference throughout EKPP development.

They are **not** the active implementation.

---

## Current Role

The folder serves as:

* the current production baseline,
* a comparison point during implementation,
* and a deployment reference while EKPP is under development.

---

## Relationship to Other Folders

### `aws-files/`

Current production website.

### `website/`

Current implementation being developed.

### `implementation/evidence/`

Historical snapshots of completed implementation stages.

---

## Why Preserve These Files?

Preserving the current production website allows future collaborators to compare:

* the existing experience,
* the evolving implementation,
* and the improvements introduced by each Build cycle.

This supports AFK's principle of engineering through observation rather than assumption.

---

## Future

Once EKPP is capable of publishing engineering knowledge automatically, the contents of the `website/` folder are expected to become the new production website, replacing the current AWS-hosted implementation.

Until that point, the `aws-files/` folder remains the production reference.
