import os

with open("style.css", "r", encoding="utf-8") as f:
    content = f.read()

# Fix 1: Project Cards
old_project = """.project-entry {
    position: relative;
    background-color: var(--card-bg);
    border: 1px solid var(--border-color);
    border-radius: 14px;
    padding: 1.5rem 1.5rem 1.5rem 1.75rem;
    overflow: hidden;
    transition: var(--transition-quick);
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.02);
    display: flex;
    flex-direction: column;
    gap: 1.25rem;
}"""

new_project = """.project-entry {
    position: relative;
    background-color: var(--card-bg);
    border: 1px solid var(--border-color);
    border-radius: 14px;
    padding: 1.5rem 1.5rem 1.5rem 1.75rem;
    overflow: hidden;
    transition: var(--transition-quick);
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.02);
    display: flex;
    flex-direction: column;
    gap: 1.25rem;
}

.project-img-wrap {
    margin: -1.5rem -1.5rem 1.25rem -1.75rem;
    border-radius: 14px 14px 0 0;
    overflow: hidden;
}

.project-card-img {
    width: 100%;
    height: 240px;
    object-fit: cover;
    display: block;
    transition: transform 0.5s ease;
}

.project-entry:hover .project-card-img {
    transform: scale(1.05);
}"""

content = content.replace(old_project, new_project)

old_detail = """.project-entry-detail {
    font-size: 0.9rem;
    line-height: 1.6;
    color: var(--text-muted);
    font-weight: 300;
    margin: 0 0 1.1rem 0;
}"""
new_detail = """.project-entry-detail {
    font-size: 0.9rem;
    line-height: 1.6;
    color: var(--text-muted);
    font-weight: 300;
    margin: 0 0 1.1rem 0;
    flex-grow: 1;
}"""

content = content.replace(old_detail, new_detail)

# Fix 2: 5 things on one line
old_grid = """.philosophy-grid {
    max-width: 900px;
    margin: 0 auto;
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 2rem;
}"""
new_grid = """.philosophy-grid {
    max-width: 1400px;
    margin: 0 auto;
    display: flex;
    flex-wrap: nowrap;
    justify-content: space-between;
    align-items: stretch;
    gap: 1.5rem;
    width: 100%;
}
.philosophy-grid .vision-item {
    flex: 1;
    min-width: 0;
}"""
content = content.replace(old_grid, new_grid)

# Fix 3: Reduce vertical heights so they all fit on one screen
content = content.replace("min-height: 80vh;", "min-height: 60vh;")
content = content.replace("padding: 2rem 4% 6rem 4%;", "padding: 1rem 4% 2rem 4%;")
content = content.replace("margin-top: 10rem;", "margin-top: 3rem;")
content = content.replace("padding: 4rem 2rem;", "padding: 2rem;")


with open("style.css", "w", encoding="utf-8") as f:
    f.write(content)
print("Project cards, grid, and padding fixed.")
