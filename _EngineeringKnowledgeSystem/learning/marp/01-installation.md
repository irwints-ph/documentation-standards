---
marp: true
theme: default
paginate: true
---

# Part 1: Installation & Setup

Welcome to **Marp** (Markdown Presentation Ecosystem). This guide will get your environment running in minutes.

---

## Prerequisites

To use Marp effectively, you need:
1. **VS Code** (Visual Studio Code) installed on your machine.
2. A basic understanding of Markdown (`#`, `*`, `-`, etc.).

---

## Step 1: Install the Marp Extension

1. Open VS Code.
2. Go to the **Extensions** view (`Ctrl+Shift+X` or `Cmd+Shift+X`).
3. Search for **Marp for VS Code** (by marp-team).
4. Click **Install**.

---

## Step 2: Create Your First Presentation

Create a new file named `index.md` and add the frontmatter directives at the top:

```markdown
---
marp: true
---

# Hello Marp!
This is my first slide.

```

---

## Step 3: Previewing and Exporting

* **Toggle Preview:** Press `Ctrl+K V` (Windows/Linux) or `Cmd+K V` (Mac) to open the live preview pane.
* **Export Slides:** Click the Marp icon in the top-right corner of the editor or use the Command Palette (`Ctrl+Shift+P` / `Cmd+Shift+P`) and type `Marp: Export Slide Deck`.
* **Formats supported:** PDF, HTML, and PPTX.
