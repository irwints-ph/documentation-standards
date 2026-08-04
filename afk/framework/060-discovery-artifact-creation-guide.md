# Proposed Additions to `060-discovery-artifact-creation-guide.md`

## New Section — Discovery vs Migration

### Discovery

Discovery inspects the current system and produces new engineering knowledge.

Discovery activities include:

* inspecting source code,
* observing runtime behavior,
* identifying architectural patterns,
* documenting engineering findings.

### Migration

Migration does **not** create new engineering knowledge.

Migration converts historical discovery documents into AFK Discovery Artifacts while preserving their meaning.

Migration activities include:

* preserving historical identity,
* normalizing document structure,
* improving traceability,
* improving navigation,
* preserving engineering intent.

Migration must never reinterpret the historical discovery.

---

# New Section — Migration Source of Truth

When performing a migration:

The historical discovery documents are the authoritative source.

Example:

```text
client/_discovery/
```

The current implementation may only be consulted:

* to validate an existing historical observation,
* to verify links,
* to confirm file locations.

The current implementation must never replace or rewrite historical engineering understanding.

---

# New Section — Migration Rules

During migration the AI shall:

* preserve document identity,
* preserve document subject,
* preserve engineering intent,
* preserve historical traceability,
* normalize formatting,
* improve navigation,
* improve references.

The AI shall **not**:

* invent new discoveries,
* rename findings because they "sound better",
* merge unrelated discovery artifacts,
* create implementation tasks,
* reinterpret historical findings,
* replace historical conclusions with newly inferred ones.

---

# New Section — Historical Identity

Historical document identity must remain recognizable.

Example:

Historical

```text
F001-domain-namespace.md
```

AFK

```text
001-domain-namespace.md
```

The number may change to AFK numbering.

The engineering subject shall not.

---

# New Section — Historical Traceability

Every migrated artifact shall include:

## Historical Source

Original document path.

## Migration Context

Example:

> Normalized from historical discovery documentation into the AFK Discovery Artifact format.

---

# New Section — Artifact Generation Policy

Migration shall only produce one of the following:

* migrated historical artifacts,
* navigation documents (README),
* migration summary.

Navigation documents must clearly identify themselves as AFK-generated indexes.

They are not discovery artifacts.

---

# New Section — Migration Completion Checklist

Before completing a migration, verify:

* historical documents preserved,
* migrated artifacts created,
* historical traceability included,
* navigation updated,
* links validated,
* remaining historical documents listed,
* remaining discovery gaps identified,
* no implementation tasks created,
* no undocumented discoveries invented.

---

# Revision History

| Version | Date       | Description                                                                                                                                                                                                                                                                         |
| ------- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 3.0     | 2026-08-04 | Added explicit separation between Discovery and Migration, established historical documents as the migration source of truth, defined migration rules, historical identity preservation, traceability requirements, artifact generation policy, and migration completion checklist. |
