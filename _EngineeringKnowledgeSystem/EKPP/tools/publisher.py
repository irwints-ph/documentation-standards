import os
from pathlib import Path

# Configuration: Distinct source directories mapped to their respective output folders
SOURCE_MAPPINGS = {
    "afk": {
        "source": Path("source/afk"),
        "output": Path("website/output/afk")
    },
    "eks": {
        "source": Path("source/eks"),
        "output": Path("website/output/eks")
    },
    "eds": {
        "source": Path("source/eds"),
        "output": Path("website/output/eds")
    },
    "ekpp": {
        "source": Path("source/ekpp"),
        "output": Path("website/output/ekpp")
    }
}

def parse_markdown_to_html(md_content):
    """
    Lightweight Markdown-to-HTML converter for EKPP foundational output.
    """
    lines = md_content.splitlines()
    html_lines = []
    in_code_block = False

    for line in lines:
        if line.startswith("```"):
            if in_code_block:
                html_lines.append("</code></pre>")
                in_code_block = False
            else:
                html_lines.append("<pre><code>")
                in_code_block = True
            continue

        if in_code_block:
            html_lines.append(line.replace("<", "&lt;").replace(">", "&gt;"))
            continue

        if line.startswith("# "):
            html_lines.append(f"<h1>{line[2:]}</h1>")
        elif line.startswith("## "):
            html_lines.append(f"<h2>{line[3:]}</h2>")
        elif line.startswith("### "):
            html_lines.append(f"<h3>{line[4:]}</h3>")
        elif line.startswith("* ") or line.startswith("- "):
            html_lines.append(f"<li>{line[2:]}</li>")
        elif not line.strip():
            html_lines.append("<br>")
        else:
            html_lines.append(f"<p>{line}</p>")

    return "\n".join(html_lines)

def wrap_html_template(title, content):
    """Wraps parsed content in the EKPP output layout template."""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} — EKPP Published Output</title>
    <link rel="stylesheet" href="../../assets/css/style.css">
</head>
<body>
    <header class="site-header">
        <div class="container">
            <h1>{title}</h1>
            <p class="tagline">Published Engineering Knowledge</p>
        </div>
    </header>
    <main class="main-content">
        <div class="container">
            <article class="doc-content">
                {content}
            </article>
            <div style="margin-top: 2rem;">
                <a href="../../index.html" class="output-link">&larr; Back to Portal Home</a>
            </div>
        </div>
    </main>
    <footer class="site-footer">
        <div class="container">
            <p>&copy; 2026 Engineering Knowledge Publishing Portal.</p>
        </div>
    </footer>
</body>
</html>
"""

def publish_docs():
    print("🚀 Starting EKPP Publisher with distinct source paths...")
    
    for category, paths in SOURCE_MAPPINGS.items():
        src_dir = paths["source"]
        out_dir = paths["output"]
        
        # Ensure output directory exists
        out_dir.mkdir(parents=True, exist_ok=True)
        
        if not src_dir.exists():
            print(f"⚠️ Source directory [{src_dir}] does not exist yet. Skipping {category.upper()}.")
            continue
            
        print(f"📂 Processing category [{category.upper()}] from {src_dir} -> {out_dir}")
        
        # Process markdown files in the specific source directory
        for md_file in src_dir.glob("*.md"):
            print(f"  └─ Compiling: {md_file.name}")
            md_content = md_file.read_text(encoding="utf-8")
            
            # Extract title from first H1 or filename
            title_match = next((line[2:] for line in md_content.splitlines() if line.startswith("# ")), md_file.stem)
            
            html_body = parse_markdown_to_html(md_content)
            final_html = wrap_html_template(title_match, html_body)
            
            output_file = out_dir / f"{md_file.stem}.html"
            output_file.write_text(final_html, encoding="utf-8")
            
    print("✨ EKPP Publishing complete.")

if __name__ == "__main__":
    publish_docs()