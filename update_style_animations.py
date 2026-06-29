import re

with open("style.css", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update .header-container for sticky/scrolled
old_header = """.header-container {
    max-width: 1400px;
    margin: 0 auto;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1.25rem 2rem;
}"""
new_header = """.header-container {
    max-width: 1400px;
    margin: 0 auto;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1.25rem 2rem;
    position: sticky;
    top: 0;
    z-index: 1000;
    background: transparent;
    transition: background-color 0.4s ease, backdrop-filter 0.4s ease, box-shadow 0.4s ease, padding 0.4s ease;
}
.header-container.scrolled {
    background: rgba(250, 250, 250, 0.85);
    backdrop-filter: blur(15px);
    -webkit-backdrop-filter: blur(15px);
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05);
    padding: 0.75rem 2rem; /* Shrink slightly on scroll */
    border-radius: 0 0 16px 16px;
}
[data-theme="dark"] .header-container.scrolled {
    background: rgba(15, 15, 20, 0.85);
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.4);
}"""
content = content.replace(old_header, new_header)


# 2. Append animation classes at the end of the file
animation_css = """
/* ==========================================================================
   Premium Animations & Interactions
   ========================================================================== */

/* Scroll Reveal */
.animate-on-scroll {
    opacity: 0;
    transform: translateY(20px);
    transition: opacity 0.6s cubic-bezier(0.215, 0.610, 0.355, 1.000), transform 0.6s cubic-bezier(0.215, 0.610, 0.355, 1.000);
    will-change: opacity, transform;
}

.animate-on-scroll.appear,
.animate-on-scroll.animated {
    opacity: 1;
    transform: translateY(0);
}

/* Enhanced Hover Interactions */
.contact-card, .project-entry {
    transition: transform 0.3s cubic-bezier(0.25, 0.8, 0.25, 1), box-shadow 0.3s cubic-bezier(0.25, 0.8, 0.25, 1) !important;
}

.contact-card:hover, .project-entry:hover, .vision-glass-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 15px 35px rgba(0, 0, 0, 0.1) !important;
}

[data-theme="dark"] .contact-card:hover, [data-theme="dark"] .project-entry:hover, [data-theme="dark"] .vision-glass-card:hover {
    box-shadow: 0 15px 35px rgba(0, 0, 0, 0.5) !important;
}

/* Ken Burns / Parallax Zoom */
@keyframes kenBurns {
    0% { transform: scale(1); }
    50% { transform: scale(1.05); }
    100% { transform: scale(1); }
}

.project-card-img {
    animation: kenBurns 20s ease-in-out infinite alternate;
}
.project-entry:hover .project-card-img {
    /* Stop infinite animation and force slightly larger scale on hover */
    animation-play-state: paused;
    transform: scale(1.08) !important;
}
"""

if "Premium Animations & Interactions" not in content:
    content += "\n" + animation_css

with open("style.css", "w", encoding="utf-8") as f:
    f.write(content)

print("Updated style.css with animations, sticky header, and Ken Burns effect.")
