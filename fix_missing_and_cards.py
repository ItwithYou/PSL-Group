import re

# 1. FIX INDEX.HTML (Restore vision text & ensure lightbox HTML exists)
with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Add the vision message back
hero_desc_pattern = r'(<p class="hero-description animate-text-delay" id="hero-desc">\s*<!-- Content injected by JavaScript based on active language -->\s*</p>)'
if 'id="vision-text"' not in html:
    new_desc = r'\1\n                    <p class="vision-paragraph animate-text-delay" id="vision-text"></p>'
    html = re.sub(hero_desc_pattern, new_desc, html)

# Add lightbox container at the end of the body if it doesn't exist
if 'id="lightbox"' not in html:
    lightbox_html = """
    <!-- Lightbox -->
    <div id="lightbox" class="lightbox">
        <span class="lightbox-close">&times;</span>
        <img class="lightbox-content" id="lightbox-img">
    </div>
</body>"""
    html = html.replace("</body>", lightbox_html)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)


# 2. FIX STYLE.CSS (Project cards, Lightbox, Vision paragraph)
with open("style.css", "r", encoding="utf-8") as f:
    css = f.read()

# Vision paragraph styling
if '.vision-paragraph' not in css:
    vision_css = """
.vision-paragraph {
    font-size: 1rem;
    line-height: 1.6;
    color: var(--text-muted);
    margin-top: 1.5rem;
    margin-bottom: 2rem;
    padding-left: 1.5rem;
    border-left: 3px solid var(--accent-color);
}
"""
    css = css.replace('.hero-intro {\n    width: 65%;\n}', '.hero-intro {\n    width: 65%;\n}\n' + vision_css)

# Project Card styling
# Remove old .project-entry styles
css = re.sub(r'\.project-entry\s*{[^}]*}\s*\.project-entry::before\s*{[^}]*}\s*\.project-entry:hover\s*{[^}]*}\s*\.project-entry:hover::before\s*{[^}]*}', '', css)

# Insert clean card styling
new_card_css = """
.project-entry {
    background-color: var(--card-bg);
    border: 1px solid var(--border-color);
    border-radius: 12px;
    overflow: hidden;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    display: flex;
    flex-direction: column;
    height: 100%;
    cursor: pointer;
}
.project-entry:hover {
    transform: translateY(-5px);
    box-shadow: 0 15px 30px rgba(0,0,0,0.1);
    border-color: var(--accent-color);
}
[data-theme="dark"] .project-entry:hover {
    box-shadow: 0 15px 30px rgba(0,0,0,0.5);
}
.project-img-wrap {
    width: 100%;
    height: 220px;
    overflow: hidden;
    position: relative;
}
.project-card-img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.5s ease;
}
.project-entry:hover .project-card-img {
    transform: scale(1.08);
}
.project-info-container {
    padding: 1.5rem;
    display: flex;
    flex-direction: column;
    flex-grow: 1;
}
.spec-chips {
    margin-top: auto; /* push chips to bottom */
}
"""
# inject new card css
if '.project-img-wrap' not in css:
    css = css.replace('.project-entry-name {', new_card_css + '\n.project-entry-name {')

# Lightbox CSS
if '.lightbox' not in css:
    lightbox_css = """
/* Lightbox Styles */
.lightbox {
    display: none; 
    position: fixed; 
    z-index: 9999; 
    left: 0;
    top: 0;
    width: 100%; 
    height: 100%; 
    background-color: rgba(0,0,0,0.9);
    backdrop-filter: blur(5px);
}
.lightbox-content {
    margin: auto;
    display: block;
    max-width: 90%;
    max-height: 90vh;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    box-shadow: 0 0 30px rgba(0,0,0,0.5);
    border: 2px solid white;
    border-radius: 4px;
}
.lightbox-close {
    position: absolute;
    top: 20px;
    right: 35px;
    color: #f1f1f1;
    font-size: 40px;
    font-weight: bold;
    cursor: pointer;
    transition: 0.3s;
    z-index: 10000;
}
.lightbox-close:hover,
.lightbox-close:focus {
    color: var(--accent-color);
    text-decoration: none;
    cursor: pointer;
}
"""
    css += '\n' + lightbox_css

with open("style.css", "w", encoding="utf-8") as f:
    f.write(css)


# 3. FIX APP.JS (Add lightbox event listeners)
with open("app.js", "r", encoding="utf-8") as f:
    js = f.read()

if "lightbox" not in js:
    lightbox_js = """
// Lightbox Logic
document.addEventListener('DOMContentLoaded', () => {
    const lightbox = document.getElementById('lightbox');
    if (!lightbox) return;
    const lightboxImg = document.getElementById('lightbox-img');
    const closeBtn = document.querySelector('.lightbox-close');

    // Add click to all project images
    document.querySelectorAll('.project-card-img').forEach(img => {
        img.style.cursor = 'pointer';
        // Add click listener to the whole card for better UX, or just image
        img.addEventListener('click', (e) => {
            e.stopPropagation(); // prevent card click if we had one
            lightbox.style.display = 'block';
            lightboxImg.src = img.src;
        });
    });

    // Close logic
    closeBtn.addEventListener('click', () => {
        lightbox.style.display = 'none';
    });
    lightbox.addEventListener('click', (e) => {
        if (e.target !== lightboxImg) {
            lightbox.style.display = 'none';
        }
    });
});
"""
    js += '\n' + lightbox_js

with open("app.js", "w", encoding="utf-8") as f:
    f.write(js)

print("Fixed missing vision text, styled project cards perfectly, and added lightbox.")
