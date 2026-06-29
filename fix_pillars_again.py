import re

with open("style.css", "r", encoding="utf-8") as f:
    css = f.read()

# Fix the hero pillars row to use compact pill shapes
old_pillars = """
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

new_pillars = """
.hero-pillars-row {
    display: flex;
    flex-direction: row;
    gap: 1rem;
    margin-top: 2rem;
    flex-wrap: wrap; /* allow wrapping if needed */
}

.hero-pillars-row .glass-orb {
    position: static;
    width: auto;
    height: auto;
    border-radius: 50px; /* Pill shape */
    flex-direction: row;
    align-items: center;
    justify-content: flex-start;
    transform: none;
    background: rgba(255, 255, 255, 0.5);
    backdrop-filter: blur(15px);
    -webkit-backdrop-filter: blur(15px);
    border: 1px solid rgba(255, 255, 255, 0.8);
    box-shadow: 0 10px 20px rgba(0,0,0,0.03);
    padding: 0.5rem 1rem;
    cursor: default;
    gap: 0.75rem;
}
.hero-pillars-row .glass-orb:hover {
    transform: translateY(-3px) !important;
    background: rgba(255, 255, 255, 0.8);
}
.hero-pillars-row .orb-text {
    opacity: 1;
    transform: none;
    position: static;
    margin-top: 0;
    font-size: 0.85rem;
    font-weight: 600;
    color: var(--text-color);
}
.hero-pillars-row .orb-icon {
    font-size: 1.5rem;
    margin-bottom: 0;
    transform: none !important;
}
"""

if ".hero-pillars-row {" in css:
    css = css.replace(old_pillars, new_pillars)

# Also fix the mobile override for it so it scrolls correctly
old_mobile = """.hero-pillars-row {
        width: 100vw;
        margin-left: -2rem; /* Pull out of padding */
        padding: 1rem 2rem;
        overflow-x: auto;
        scroll-snap-type: x mandatory;
        scrollbar-width: none;
    }"""
new_mobile = """.hero-pillars-row {
        width: 100vw;
        margin-left: -2rem;
        padding: 1rem 2rem;
        overflow-x: auto;
        flex-wrap: nowrap;
        scroll-snap-type: x mandatory;
        scrollbar-width: none;
    }"""
css = css.replace(old_mobile, new_mobile)

with open("style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Updated hero pillars to pill layout")
