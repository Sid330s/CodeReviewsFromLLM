import os
from pathlib import Path
import html

SOLUTION_DIR = 'solution'
LEETCODE_FILE = 'leetcode.txt'
OUTPUT_DIR = 'site'
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Load problem URLs
with open(LEETCODE_FILE, 'r') as f:
    urls = [line.strip() for line in f if line.strip()]

# Parse problem slugs
problems = []
for url in urls:
    slug = url.rstrip('/').split('/')[-1]
    problems.append((slug, url))

# Prism.js CDN + minimal CSS
HEADER = '''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>{title}</title>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism-tomorrow.min.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
  <style>
    body {{
      font-family: 'Segoe UI', sans-serif;
      margin: 40px auto;
      max-width: 800px;
      background: #1e1e1e;
      color: #fff;
      padding: 0 20px;
    }}
    a {{
      color: #4FC3F7;
      text-decoration: none;
    }}
    a:hover {{
      text-decoration: underline;
    }}
    pre {{
      border-radius: 8px;
      overflow: auto;
    }}
    .card {{
      background: #2d2d2d;
      padding: 15px;
      border-radius: 10px;
      margin: 10px 0;
      box-shadow: 0 4px 6px rgba(0,0,0,0.3);
    }}
    .title {{
      font-size: 1.2em;
      font-weight: bold;
    }}
    .card-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 8px;
    }
    .icon {
      font-size: 1.2em;
    }
    .icon.ok {
      color: #4CAF50;
    }
    .icon.bad {
      color: #f44336;
    }
  </style>
</head>
<body>
<h1>{header}</h1>
'''

FOOTER = '''
<script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-cpp.min.js"></script>
</body>
</html>
'''

# Generate index.html
with open(os.path.join(OUTPUT_DIR, 'index.html'), 'w') as f:
  f.write(HEADER.format(title="LeetCode Solutions", header="📘 LeetCode Problem List"))
  for slug, url in problems:
      cpp_path = os.path.join(SOLUTION_DIR, f"{slug}.cpp")
      has_solution = os.path.exists(cpp_path) and sum(1 for _ in open(cpp_path)) > 5
      icon_class = "fa-circle-check ok" if has_solution else "fa-circle-xmark bad"
      f.write(f'''
      <div class="card">
          <div class="card-header">
              <div class="title">{slug.replace('-', ' ').title()}</div>
              <div class="icon"><i class="fa-solid {icon_class}"></i></div>
          </div>
          <a href="{url}" target="_blank">LeetCode Problem</a> |
          <a href="{slug}.html">View Solution</a>
      </div>
      ''')
  f.write(FOOTER)

# Generate individual solution pages
for slug, _ in problems:
    cpp_path = os.path.join(SOLUTION_DIR, f"{slug}.cpp")
    if os.path.exists(cpp_path):
        with open(cpp_path, 'r') as cpp_file:
            code = html.escape(cpp_file.read())

        html_path = os.path.join(OUTPUT_DIR, f"{slug}.html")
        with open(html_path, 'w') as sol_file:
            sol_file.write(HEADER.format(title=slug, header=f"💡 Solution: {slug.replace('-', ' ').title()}"))
            sol_file.write(f'<pre><code class="language-cpp">{code}</code></pre>')
            sol_file.write('<p><a href="index.html">⬅ Back to index</a></p>')
            sol_file.write(FOOTER)

print("✅ Site generated in the 'site/' folder.")
