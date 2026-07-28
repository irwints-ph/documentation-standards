---
marp: true
theme: default
paginate: true
---

# Part 2: Basic Slides & Markdown Syntax

---

## Slide Separation

Marp uses horizontal rules (`---`) to separate individual slides.

```markdown
# Slide 1
Content for slide 1.

---

# Slide 2
Content for slide 2.

```

---

## Standard Markdown Support

You can use all standard Markdown features:

* **Bold** and *Italic* text
* [Links](https://marp.app)
* Inline code like `marp --pdf presentation.md`

> Blockquotes are also fully supported and styled nicely by default themes.

---

## Lists and Tables

### Ordered vs Unordered

1. First item
2. Second item
* Sub-bullet A
* Sub-bullet B



### Simple Table

| Command | Description |
| --- | --- |
| `marp` | Run CLI compiler |
| `-p` | Preview mode |
