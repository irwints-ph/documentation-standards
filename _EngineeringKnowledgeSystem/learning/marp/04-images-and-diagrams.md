---
marp: true
theme: default
paginate: true
---

# Part 4: Images & Diagrams

---

## Local and Remote Images

Standard Markdown image syntax works out of the box:

```markdown
![bg left:40%](https://picsum.photos/600/800)

# Split Screen Image
Using `bg left` places the image as a background element on the left side of the slide while keeping text on the right.

```

---

## Advanced Image Scaling

Control image sizing easily using width and height parameters:

```markdown
![width:400px](logo.png)
![height:200px](banner.jpg)

```

---

## Mermaid.js Diagrams

Marp natively supports Mermaid diagrams via code blocks if enabled or rendered through extensions:

```mermaid
graph TD
    A [Markdown Source] -->|Marp CLI| B(HTML Output);
    A -->|VS Code Extension| C(Live Preview);
    B --> D[PDF / PPTX Export];

``