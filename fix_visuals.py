import re

with open("style.css", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Redesign .hero-meta (Executive Contact Card)
old_meta = """.hero-meta {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 2.5rem;
}

.meta-item {
    border-top: 1px solid var(--border-color);
    padding-top: 1rem;
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
}"""

new_meta = """.hero-meta {
    background-color: var(--card-bg);
    border: 1px solid var(--border-color);
    border-top: 4px solid var(--accent-color);
    border-radius: 16px;
    padding: 3rem;
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.05);
    display: flex;
    flex-direction: column;
    gap: 2rem;
    transition: transform 0.4s cubic-bezier(0.25, 0.8, 0.25, 1), box-shadow 0.4s ease;
}

.hero-meta:hover {
    transform: translateY(-8px);
    box-shadow: 0 25px 50px rgba(0, 0, 0, 0.1);
}

.meta-item {
    border-top: none;
    border-bottom: 1px solid var(--border-light);
    padding-bottom: 2rem;
    padding-top: 0;
    display: flex;
    flex-direction: column;
    gap: 0.75rem;
}

.meta-item:last-child {
    border-bottom: none;
    padding-bottom: 0;
}"""
content = content.replace(old_meta, new_meta)

# Update the media query for hero-meta since it's no longer a grid
content = content.replace("""    .hero-meta {
        grid-template-columns: repeat(4, 1fr);
        gap: 1.5rem;
    }""", """    .hero-meta {
        flex-direction: row;
        gap: 1.5rem;
        flex-wrap: wrap;
    }
    .meta-item { border: none; padding: 0; }""")
content = content.replace("""    .hero-meta {
        grid-template-columns: repeat(2, 1fr);
        gap: 1.5rem;
    }""", """    .hero-meta {
        flex-direction: row;
        gap: 1.5rem;
        flex-wrap: wrap;
    }""")
content = content.replace("""    .hero-meta {
        grid-template-columns: 1fr;
    }""", """    .hero-meta {
        flex-direction: column;
        padding: 2rem;
    }""")

# 2. Fix the 5 Things (vision-glass-grid) wrapping issue
old_glass_grid = """.vision-glass-grid {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 2.5rem;
    margin-top: 4rem;
    width: 100%;
    padding-bottom: 2rem;
}"""
new_glass_grid = """.vision-glass-grid {
    display: flex;
    flex-wrap: nowrap;
    justify-content: space-between;
    align-items: center;
    gap: 1.5rem;
    margin-top: 2rem;
    width: 100%;
    padding-bottom: 2rem;
    overflow-x: auto; /* Prevent layout breakage on extremely small screens */
}"""
content = content.replace(old_glass_grid, new_glass_grid)


with open("style.css", "w", encoding="utf-8") as f:
    f.write(content)

print("Updated style.css to fix contact card and 5-things wrapping.")
