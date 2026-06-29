import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Add Google Fonts for Inter and Montserrat
fonts_link = """    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Montserrat:wght@400;500;600;700&family=Noto+Sans+Lao:wght@300;400;500;600&display=swap" rel="stylesheet">"""

if "family=Inter" not in content:
    content = content.replace("<title>", fonts_link + "\n    <title>")

# 2. Wrap project info in project-info-container
# Find all project-entry blocks
pattern = re.compile(
    r'(<article class="project-entry animate-on-scroll">.*?</div>\s*)(<h5 class="project-entry-name".*?</article>)', 
    re.DOTALL
)

def replace_entry(match):
    part1 = match.group(1) # Contains <article> and <div class="project-img-wrap">...</div>
    part2 = match.group(2) # Contains <h5...>...<div class="spec-chips">...</div>\n</article>
    
    # Wrap part2 (excluding the closing </article>) in project-info-container
    part2_inner = part2.rsplit('</article>', 1)[0]
    
    new_part2 = f'                    <div class="project-info-container">\n    {part2_inner}                </div>\n                </article>'
    return part1 + new_part2

# Keep applying until no more changes (since there are multiple)
new_content = pattern.sub(replace_entry, content)
content = new_content

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Updated index.html with new project structure and fonts.")
