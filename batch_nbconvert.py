import os
import nbformat
from nbconvert import HTMLExporter
from datetime import datetime

POSTS_DIR = "posts"
BLOG_DIR = "blog"
ASSETS_DIR = "templates"

os.makedirs(BLOG_DIR, exist_ok=True)

# ------------------------------------------------------------
# Extract title/date/tags
# ------------------------------------------------------------
def parse_meta(nb_node):
    for cell in nb_node.cells:
        if cell.cell_type == "markdown":
            lines = cell.source.splitlines()
            if not lines: 
                continue
            title = lines[0].strip("# ").strip()
            date, tags = "", ""
            for ln in lines[1:]:
                if ln.lower().startswith("date:"):
                    date = ln.split(":",1)[1].strip()
                if ln.lower().startswith("tags:"):
                    tags = ln.split(":",1)[1].strip()
            return title, date, tags
    return "Untitled", "", ""

# ------------------------------------------------------------
# Load notebooks and gather metadata
# ------------------------------------------------------------
posts = []
for fn in sorted(os.listdir(POSTS_DIR)):
    if not fn.endswith(".ipynb"):
        continue
    path = os.path.join(POSTS_DIR, fn)
    nb = nbformat.read(path, as_version=4)
    title, date, tags = parse_meta(nb)
    html_file = fn.replace(".ipynb", ".html")
    posts.append({
        "file": fn,
        "html": html_file,
        "title": title,
        "date": date or "1900-01-01",
        "tags": tags
    })

# Sort by date descending
posts.sort(key=lambda p: datetime.strptime(p["date"], "%Y-%m-%d"), reverse=True)

# Make HTML exporter
exporter = HTMLExporter(template_name="basic")

# ------------------------------------------------------------
# Create global navigation sidebar HTML
# ------------------------------------------------------------
post_links_html = "\n".join(
    f'<li><a href="{p["html"]}">{p["title"]}</a></li>'
    for p in posts
)

# ------------------------------------------------------------
# Page template
# ------------------------------------------------------------
PAGE_TEMPLATE = """
<html>
<head>
  <link rel="stylesheet" href="style.css">
  <title>{title}</title>
</head>
<body>

<header>
  <h1><a href="index.html">My Blog</a></h1>
</header>

<div id="layout">
  <aside>
    <h3>All Posts</h3>
    <ul>
      {links}
    </ul>
  </aside>

  <main>
    {content}
  </main>
</div>

</body>
</html>
"""

# ------------------------------------------------------------
# Convert each notebook to styled, wrapped HTML
# ------------------------------------------------------------
for post in posts:
    nb_path = os.path.join(POSTS_DIR, post["file"])
    nb_node = nbformat.read(nb_path, as_version=4)
    body, _ = exporter.from_notebook_node(nb_node)

    wrapped = PAGE_TEMPLATE.format(
        title=post["title"],
        links=post_links_html,
        content=body
    )

    outpath = os.path.join(BLOG_DIR, post["html"])
    with open(outpath, "w", encoding="utf-8") as f:
        f.write(wrapped)

# ------------------------------------------------------------
# Generate index.html using the same template
# ------------------------------------------------------------
index_content = "<h2>Posts</h2><ul>"
for p in posts:
    index_content += f'<li><a href="{p["html"]}">{p["title"]}</a> ({p["date"]})</li>'
index_content += "</ul>"

index_html = PAGE_TEMPLATE.format(
    title="Index",
    links=post_links_html,
    content=index_content
)

with open(os.path.join(BLOG_DIR, "index.html"), "w", encoding="utf-8") as f:
    f.write(index_html)

print("All pages generated with full navigation and consistent layout.")

