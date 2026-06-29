import re

with open("style.css", "r", encoding="utf-8") as f:
    css = f.read()

# 1. Fix hero grid layout
old_grid = """.hero-grid {
    display: grid;
    grid-template-columns: 1.5fr 1fr;
    gap: 4rem;
    align-items: flex-start;
}"""
new_grid = """.hero-grid {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    gap: 4rem;
    max-width: 1400px;
    margin: 0 auto;
}

.hero-intro {
    width: 65%;
}"""
if ".hero-grid {" in css:
    css = css.replace(old_grid, new_grid)

# 2. Fix the pillars row
# Currently, the hero-pillars-row is defined in a media query at the bottom, and some parts might be missing for desktop.
# Let's add the core desktop CSS for hero-pillars-row right after hero-intro
desktop_pillars = """
.hero-pillars-row {
    display: flex;
    flex-direction: row;
    gap: 1.5rem;
    margin-top: 3rem;
    flex-wrap: nowrap;
}

.hero-pillars-row .glass-orb {
    position: static;
    width: 140px;
    height: 140px;
    border-radius: 50%;
    transform: none;
    background: rgba(255, 255, 255, 0.4);
    box-shadow: 0 10px 20px rgba(0,0,0,0.02);
    padding: 1.5rem 1rem;
    cursor: default;
}
.hero-pillars-row .glass-orb:hover {
    transform: translateY(-5px) !important;
}
.hero-pillars-row .orb-text {
    opacity: 1;
    transform: none;
    position: relative;
    bottom: 0;
    margin-top: 1rem;
    font-size: 0.75rem;
}
.hero-pillars-row .orb-icon {
    font-size: 2rem;
    margin-bottom: 0;
    transform: none !important;
}
"""

if ".hero-pillars-row {" not in css.split("@media (max-width: 900px)")[0]:
    css = css.replace(".hero-intro {\n    width: 65%;\n}", ".hero-intro {\n    width: 65%;\n}\n" + desktop_pillars)


# 3. Ensure contact card is actually compact on desktop
# We already added the compact styling at the bottom, but the original hero-meta styling might be overriding it.
# Let's remove the original hero-meta styling.
original_meta_pattern = re.compile(r'\.hero-meta\s*{\s*background:\s*rgba\(255, 255, 255, 0\.45\);.*?\[data-theme="dark"\] \.hero-meta:hover\s*{.*?}', re.DOTALL)
css = original_meta_pattern.sub('', css)


# Now ensure our compact meta is in there
if "width: 30%;\n    min-width: 280px;" not in css:
    compact_meta = """.hero-meta {
    width: 30%;
    min-width: 280px;
    max-width: 350px;
    background: rgba(255, 255, 255, 0.5);
    backdrop-filter: blur(15px);
    -webkit-backdrop-filter: blur(15px);
    border: 1px solid rgba(255, 255, 255, 0.8);
    border-top: 3px solid var(--accent-color);
    border-radius: 12px;
    padding: 2rem 1.5rem;
    box-shadow: 0 15px 30px rgba(0, 0, 0, 0.03);
    display: flex;
    flex-direction: column;
    gap: 1.5rem;
    transition: transform 0.3s ease;
}

.hero-meta:hover {
    transform: translateY(-5px);
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.05);
}

[data-theme="dark"] .hero-meta {
    background: rgba(10, 37, 64, 0.5);
    border: 1px solid rgba(255, 255, 255, 0.1);
    box-shadow: 0 15px 30px rgba(0, 0, 0, 0.2);
}"""
    css += "\n" + compact_meta

with open("style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Fixed hero pillar and card CSS")
