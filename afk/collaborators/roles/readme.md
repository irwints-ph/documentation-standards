Yes, and I'd start small and intentional rather than creating a dozen role documents immediately.

For the initial version, I'd create the **directory structure** and only the core role model plus the first role. The rest can grow naturally as we validate the workflow.

## Proposed structure

```text
afk/
└── collaborators/
    ├── README.md
    │
    └── roles/
        ├── 000-ai-collaborator-role-model.md
        ├── 010-ai-boot-collaborator.md
        ├── 020-ai-discovery-collaborator.md
        ├── 030-ai-documentation-collaborator.md
        ├── 040-ai-review-collaborator.md
        ├── 050-ai-replay-collaborator.md
        ├── 060-ai-implementation-collaborator.md
        └── 070-ai-architecture-collaborator.md
```

## Why these roles?

### 000 — AI Collaborator Role Model

The canonical document.

Defines:

* what an AI Collaborator is,
* how roles work,
* one role at a time,
* role transitions,
* inputs,
* outputs,
* completion criteria.

Everything else references this.

---

### 010 — Boot Collaborator

Responsible for:

* reading AFK principles,
* reading Project Boot Prompt,
* selecting Workspace vs Document mode,
* starting replay,
* stopping before discovery.

Produces:

* reconstructed engineering state.

---

### 020 — Discovery Collaborator

Responsible for:

* inspecting repositories,
* creating discovery artifacts,
* separating evidence from interpretation,
* stopping after discovery.

---

### 030 — Documentation Collaborator

Responsible for:

* documentation standards,
* migration,
* normalization,
* registries,
* references.

---

### 040 — Review Collaborator

Responsible for:

* validating artifacts,
* checking standards,
* checking consistency,
* identifying gaps.

Never implements.

---

### 050 — Replay Collaborator

Responsible for:

* WWAN,
* Session Handoff,
* replay updates,
* preserving engineering continuity.

---

### 060 — Implementation Collaborator

Responsible for:

* implementation,
* refactoring,
* testing,
* code generation.

Never starts without reconstructed engineering state.

---

### 070 — Architecture Collaborator

Responsible for:

* architecture reviews,
* boundary analysis,
* design evolution,
* long-term engineering consistency.

---

## Why number them?

Exactly like the rest of AFK.

Eventually you'll be able to say:

> Activate the **040 Review Collaborator**.

The AI immediately knows which document defines its responsibilities.

## One recommendation

I would **not** write all of these now.

I'd create the structure, then implement them in this order:

1. **000-ai-collaborator-role-model.md**
2. **010-ai-boot-collaborator.md**
3. **020-ai-discovery-collaborator.md**

After that, you'll already be able to use and validate the concept before expanding the remaining roles. That keeps the framework incremental and evidence-driven, consistent with AFK's philosophy.
