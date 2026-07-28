---
marp: true
theme: uncover
paginate: true
---

# Part 8: Presentation Playbook

Best practices for building and delivering Marp decks.

---

## 1. Structure for Impact

* **One idea per slide:** Avoid cluttering your viewers' screens with dense blocks of text.
* **Use progressive disclosure:** Break complex lists into smaller chunks or use multiple slides.
* **Embrace whitespace:** Let your typography breathe.

---

## 2. Version Control (Git)

Because Marp presentations are plain text Markdown files:
* Track changes seamlessly using **Git**.
* Collaborate with teammates via Pull Requests.
* Review structural edits line-by-line in code reviews.

---

## 3. Automation & CI/CD

Automate PDF/HTML builds using GitHub Actions:

```yaml
name: Build Slides
on: [push]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Compile Marp Deck
        uses: marp-team/marp-action@v3
        with:
          pdf: true

```