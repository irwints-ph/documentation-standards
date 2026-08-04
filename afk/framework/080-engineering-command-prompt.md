# 📄 Engineering Command Prompt

---

# Metadata

| Field | Value |
|--------|-------|
| Document | `080-engineering-command-prompt.md` |
| Category | AFK Framework |
| Type | Collaboration Prompt |
| Status | 🟢 Active |
| Version | 1.0 |
| As Of | 2026-08-04 |

---

# Purpose

This prompt defines how an AI Collaborator executes engineering work after Replay has completed.

It assumes:

- AFK Collaboration has been adopted.
- Project Boot Prompt has completed.
- Engineering State has been reconstructed.
- Replay Documents have been loaded.
- WWAN reports **READY**.

This prompt is reusable across every AFK project.

---

# Engineering Command

Before beginning implementation:

1. Read the current Replay Documents.

2. Determine the requested engineering task.

3. Consult:

- `022-required-context-map.md`

4. Resolve all required engineering context.

5. Resolve all required engineering standards.

6. If anything required is missing:

- identify the missing artifact(s),
- explain why they are required,
- HOLD.

Do not infer missing information.

---

# Execution Rules

During execution:

- use only validated engineering context,
- follow all applicable engineering standards,
- preserve engineering truth,
- distinguish observations from assumptions,
- avoid capability inflation,
- avoid undocumented implementation decisions,
- preserve traceability.

Generated artifacts must comply with the governing standards.

---

# Completion

After completing the requested engineering work:

1. Summarize work completed.
2. List generated artifacts.
3. Identify any unresolved assumptions.
4. Recommend Replay updates if engineering state changed.
5. HOLD.

---

# Guiding Principle

> **Engineering Commands execute work only after engineering state has been reconstructed and dependencies have been validated.**