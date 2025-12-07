#!/usr/bin/env python3

import nbformat
from nbconvert import HTMLExporter
from pathlib import Path
from datetime import datetime

# Directories
ROOT = Path(__file__).parent
POSTS_DIR = ROOT / "posts"
OUTPUT_DIR = ROOT / "blog"
TEMPLATES_DIR = ROOT / "templates"
OUTPUT_DIR.mkdir(exist_ok=True)

# HTML Exporter with our nbconvert template
exporter = HTMLExporter(template_file=f"{TEMPLATES_DIR}/blog.tpl")
exporter.exclude_input = True  # Hide code inputs, optional

# Collect posts metadata
posts = []
# Resources passed to template (for navigation, footer year)
resources = {
    'post_list': posts,
    'build_year': datetime.now().year
}
for nb_path in POSTS_DIR.glob("*.ipynb"):
    nb = nbformat.read(nb_path, as_version=4)
    body, _ = exporter.from_notebook_node(nb, resources={**resources, "current_filename": nb_path.stem + ".html"})
    out_file = OUTPUT_DIR / f"{nb_path.stem}.html"
    out_file.write_text(body, encoding='utf-8')
    print(f"Converted {out_file}")

# Copy style.css if exists
style_src = TEMPLATES_DIR / 'style.css'
style_dst = OUTPUT_DIR / 'style.css'
if style_src.exists():
    import shutil
    shutil.copy(style_src, style_dst)

print("Blog built successfully. All notebooks converted with navigation and styling.")

