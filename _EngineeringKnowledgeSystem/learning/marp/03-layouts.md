---
marp: true
theme: default
paginate: true
---

# Part 3: Layouts & Directives

---

## Scoped Directives vs Global Directives

* **Global Directives** (at the top of the file) apply to the whole deck.
* **Scoped Directives** (`<!-- _directive: value -->`) apply **only** to the current slide. Notice the leading underscore!

---

## Directives: Background Colors

```markdown
---
marp: true
---

# Normal Slide

---
<!-- _backgroundColor: #1a1a1a -->
<!-- _color: #ffffff -->

# Dark Mode Slide
Custom background and text colors applied locally.

```

---

## Split Columns (Using HTML/CSS)

For multi-column layouts, use basic HTML structures supported by Marp:

### Column Left

* Bullet point one
* Bullet point two

### Column Right

* Feature A
* Feature B
