# 📄 AFK Collaboration Protocol (Draft)

---

## Status

🚧 Draft

---

# Purpose

Define the lightweight conversation protocol used during AFK collaborations.

The protocol reduces ambiguity between the human collaborator and the AI collaborator.

---

# Guiding Principle

Unless explicitly instructed otherwise:

The AI should never assume approval.

---

# Default Behavior

After completing a major milestone:

• pause

• summarize

• wait

The AI should not automatically continue into the next engineering stage.

---

# Suggested Commands

| Command | Meaning |
|----------|---------|
| Continue | Continue from the current point. |
| Approved | The previous milestone is accepted. |
| Next | Move to the next planned stage. |
| Pause | Stop here until resumed. |
| Resume | Continue from the last confirmed state. |
| Revisit | Return to the previous topic. |
| Explore | Brainstorm without making decisions. |
| Decide | Enter decision mode. |
| Draft | Produce an initial draft. |
| Finalize | Produce a polished version. |

---

# Example

AI

✓ Project Foundation completed.

Summary...

Waiting for your instruction.

Human

Approved

AI

Proceeding to First Engineering Wish.

---

# Notes

These commands are conveniences.

Natural language remains fully supported.

For example:

"Looks good, let's continue."

is equivalent to

Approved
Continue

---

This protocol may evolve as AFK matures.