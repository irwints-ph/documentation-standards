---
marp: true
theme: default
paginate: true
---

# Part 5: Speaker Notes

---

## Adding Notes to Slides

Speaker notes are added using HTML comment syntax (`<!-- Note: ... -->` or `<!-- notes: ... -->`) directly inside your slide content.

```markdown
# Slide Heading
Visible slide content goes here.

<!--
Speaker Notes:
- Remember to introduce the core concept first.
- Transition into the live demo after this slide.
-->

```

---

## Viewing Speaker Notes

* **During Presentation:** Use the Marp CLI or supported presentation modes (like Marp CLI's built-in preview server) to view notes in real-time.
* **Exporting:** When exporting to HTML or PDF, notes remain hidden from the audience view but can be accessed through specific presentation interfaces.
