import re

with open("style.css", "r", encoding="utf-8") as f:
    css = f.read()

# FIX 1: Make the 5 pillars (vision-glass-card) into small pills always!
old_glass_grid = re.compile(r'\.vision-glass-grid\s*{[^}]*}')
new_glass_grid = """.vision-glass-grid {
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    gap: 1rem;
    margin-top: 2rem;
    width: 100%;
}"""
css = old_glass_grid.sub(new_glass_grid, css)

# Fix the vision-glass-card to be a small horizontal pill
old_glass_card = re.compile(r'\.vision-glass-card\s*{[^}]*}')
new_glass_card = """.vision-glass-card {
    display: flex;
    flex-direction: row;
    align-items: center;
    gap: 0.75rem;
    width: auto !important; /* Override 220px */
    height: auto !important; /* Override 220px */
    border-radius: 50px !important; /* Pill shape */
    padding: 0.5rem 1.2rem !important; /* Small padding */
    background: rgba(255, 255, 255, 0.1) !important;
    backdrop-filter: blur(15px);
    -webkit-backdrop-filter: blur(15px);
    border: 1px solid rgba(255, 255, 255, 0.2) !important;
    box-shadow: 0 4px 15px rgba(0,0,0,0.05) !important;
    transition: transform 0.3s ease, background 0.3s ease !important;
}
.vision-glass-card:hover {
    transform: translateY(-3px) !important;
    background: rgba(255, 255, 255, 0.2) !important;
}
[data-theme="light"] .vision-glass-card {
    background: rgba(255, 255, 255, 0.8) !important;
    border: 1px solid rgba(0, 0, 0, 0.05) !important;
    box-shadow: 0 4px 15px rgba(0,0,0,0.05) !important;
}
[data-theme="light"] .vision-glass-card:hover {
    background: rgba(255, 255, 255, 1) !important;
}"""
css = old_glass_card.sub(new_glass_card, css)

# Make the text and icon inline
old_glass_icon = re.compile(r'\.glass-icon\s*{[^}]*}')
new_glass_icon = """.glass-icon {
    font-size: 1.5rem !important;
    margin-bottom: 0 !important;
}"""
css = old_glass_icon.sub(new_glass_icon, css)

old_glass_text = re.compile(r'\.glass-text\s*{[^}]*}')
new_glass_text = """.glass-text {
    font-size: 0.85rem !important;
    font-weight: 600 !important;
    color: var(--text-color) !important;
    text-align: left !important;
    opacity: 1 !important;
}"""
css = old_glass_text.sub(new_glass_text, css)

# Remove the massive glowing gradients that were bleeding everywhere
glow_pattern = re.compile(r'\.vision-glass-card::before\s*{[^}]*}\s*\.card-honesty::before\s*{[^}]*}\s*\.card-safety::before\s*{[^}]*}\s*\.card-quality::before\s*{[^}]*}\s*\.card-art::before\s*{[^}]*}\s*\.card-time::before\s*{[^}]*}')
css = glow_pattern.sub('', css)


# FIX 2: Redesign .hero-meta to be "minimal and premium classic"
# Remove old .hero-meta
meta_pattern = re.compile(r'\.hero-meta\s*{[^}]*}\s*\.hero-meta:hover\s*{[^}]*}\s*\[data-theme="dark"\] \.hero-meta\s*{[^}]*}')

minimal_classic_meta = """.hero-meta {
    width: 30%;
    min-width: 280px;
    max-width: 350px;
    background: var(--card-bg); /* Use theme card bg instead of transparent blur */
    border: 1px solid var(--border-color);
    border-top: 3px solid var(--accent-color); /* Classic premium gold top line */
    border-radius: 8px; /* Slightly sharper edges for a classic look */
    padding: 2rem 1.5rem;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.05); /* Very soft shadow */
    display: flex;
    flex-direction: column;
    gap: 1.5rem;
}

[data-theme="dark"] .hero-meta {
    background: #111820; /* Very deep, classic dark grey/navy */
    border: 1px solid rgba(255, 255, 255, 0.05);
    border-top: 3px solid var(--accent-color);
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
}

.hero-meta .meta-item {
    padding-bottom: 1rem;
    border-bottom: 1px solid var(--border-light);
}
.hero-meta .meta-item:last-child {
    padding-bottom: 0;
    border-bottom: none;
}
"""
css = meta_pattern.sub(minimal_classic_meta, css)

with open("style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Fixed CSS")
