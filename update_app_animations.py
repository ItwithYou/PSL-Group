import os

with open("app.js", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Add animate-on-scroll to vision-glass-card
content = content.replace('class="vision-glass-card', 'class="vision-glass-card animate-on-scroll')

# 2. Add sticky header logic
sticky_code = """
    // -----------------------------------------------------------------------------
    // Sticky Header Morphing
    // -----------------------------------------------------------------------------
    const header = document.querySelector('.header-container');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }
    });
"""

# Check if it already has sticky_code, if not insert at end of DOMContentLoaded
if "Sticky Header Morphing" not in content:
    content = content.replace("initScrollAnimations();", "initScrollAnimations();\n" + sticky_code)


with open("app.js", "w", encoding="utf-8") as f:
    f.write(content)

print("Updated app.js with animate-on-scroll classes and sticky header.")
