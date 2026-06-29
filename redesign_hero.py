import re

# 1. Update index.html
with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Replace the hero intro to include the vision-list
old_hero_intro = """                <div class="hero-intro">
                    <h1 class="hero-title animate-text">
                        <span class="lao-text">ກຸ່ມບໍລິສັດ PSL</span>
                        <span class="en-text">PSL Group</span>
                        <span class="zh-text">PSL 集团</span>
                    </h1>
                    <p class="hero-description animate-text-delay" id="hero-desc">
                        <!-- Content injected by JavaScript based on active language -->
                    </p>
                </div>"""

new_hero_intro = """                <div class="hero-intro">
                    <h1 class="hero-title animate-text">
                        <span class="lao-text">ກຸ່ມບໍລິສັດ PSL</span>
                        <span class="en-text">PSL Group</span>
                        <span class="zh-text">PSL 集团</span>
                    </h1>
                    <p class="hero-description animate-text-delay" id="hero-desc">
                        <!-- Content injected by JavaScript based on active language -->
                    </p>
                    <div class="hero-pillars-row animate-text-delay" id="vision-list">
                        <!-- Content injected by JS -->
                    </div>
                </div>"""
html = html.replace(old_hero_intro, new_hero_intro)

# Remove the orbit philosophy content
orbit_pattern = re.compile(r'\s*<div class="philosophy-content">.*?</div>\s*</div>\s*</div>\s*</section>', re.DOTALL)
html = orbit_pattern.sub('\n            </div>\n        </section>', html)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

# 2. Update style.css
with open("style.css", "r", encoding="utf-8") as f:
    css = f.read()

# Update hero-grid and hero-meta
old_hero_grid = """.hero-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 4rem;
    align-items: center;
    max-width: 1400px;
    margin: 0 auto;
}"""
new_hero_grid = """.hero-grid {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    gap: 4rem;
    max-width: 1400px;
    margin: 0 auto;
}

.hero-intro {
    width: 65%;
}

.hero-pillars-row {
    display: flex;
    flex-direction: row;
    gap: 1.5rem;
    margin-top: 3rem;
}

.hero-pillars-row .glass-orb {
    position: static;
    width: 130px;
    height: 160px; /* Make it more of an oval/card for horizontal row */
    border-radius: 65px;
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
css = css.replace(old_hero_grid, new_hero_grid)

# Update hero-meta directly
meta_pattern = re.compile(r'\.hero-meta\s*{.*?}\s*\.hero-meta:hover\s*{.*?}\s*\[data-theme="dark"\] \.hero-meta\s*{.*?}\s*\[data-theme="dark"\] \.hero-meta:hover\s*{.*?}', re.DOTALL)

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

css = meta_pattern.sub(compact_meta, css)

# Fix mobile layout for hero
mobile_hero_pattern = re.compile(r'@media \(max-width: 900px\)\s*{.*?(?=\s*@media)', re.DOTALL)
# It's better to just append a specific mobile override for these new classes
mobile_overrides = """
@media (max-width: 900px) {
    .hero-grid {
        flex-direction: column;
        gap: 3rem;
    }
    .hero-intro {
        width: 100%;
    }
    .hero-meta {
        width: 100%;
        max-width: 100%;
        margin-top: 1rem;
    }
    .hero-pillars-row {
        width: 100vw;
        margin-left: -2rem; /* Pull out of padding */
        padding: 1rem 2rem;
        overflow-x: auto;
        scroll-snap-type: x mandatory;
        scrollbar-width: none;
    }
    .hero-pillars-row::-webkit-scrollbar {
        display: none;
    }
    .hero-pillars-row .glass-orb {
        flex: 0 0 auto;
        scroll-snap-align: center;
    }
}
"""
css += mobile_overrides

with open("style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Updated HTML and CSS for Hero section")
