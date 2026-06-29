import re
import os

HTML_FILE = "index.html"
CSS_FILE = "style.css"
JS_FILE = "app.js"

def update_html():
    with open(HTML_FILE, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Convert tab-content divs to section tags
    html = re.sub(
        r'<div class="tab-content active" id="tab-home">',
        r'<section class="page-section" id="home">',
        html
    )
    html = re.sub(
        r'<div class="tab-content" id="tab-([^"]+)">',
        r'<section class="page-section" id="\1">',
        html
    )

    # 2. Fix closing tags for those sections
    html = re.sub(
        r'</div>(\s*<!-- TAB:)',
        r'</section>\1',
        html
    )
    # the last one might be right before </main>
    html = re.sub(
        r'</div>(\s*</main>)',
        r'</section>\1',
        html
    )

    # 3. Update dock items to be links instead of li
    html = re.sub(
        r'<li class="dock-item(\s+active)?" data-tab="tab-([^"]+)" id="dock-[^"]+">',
        r'<a href="#\2" class="dock-item\1" id="dock-\2">',
        html
    )
    html = re.sub(
        r'</li>(\s*<!--|(?s:\s*<li)|(?s:\s*</ul))',
        r'</a>\1',
        html
    )
    
    # Change <ul class="dock-list"> to <nav class="dock-list">
    html = html.replace('<ul class="dock-list"', '<nav class="dock-list"')
    html = html.replace('</ul>', '</nav>')

    # Add background mesh div right inside body
    mesh_html = """
    <!-- Ambient Background Mesh -->
    <div class="premium-mesh-bg"></div>
    """
    if "premium-mesh-bg" not in html:
        html = html.replace('<body>', f'<body>\n{mesh_html}')

    with open(HTML_FILE, 'w', encoding='utf-8') as f:
        f.write(html)
    print("HTML updated.")


def update_css():
    with open(CSS_FILE, 'r', encoding='utf-8') as f:
        css = f.read()

    # Premium CSS Additions
    premium_css = """

/* ==========================================================================
   Premium Single-Page Additions
   ========================================================================== */

html {
    scroll-behavior: smooth;
}

body {
    position: relative;
    background-color: var(--bg-primary);
}

.premium-mesh-bg {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    z-index: -1;
    background: radial-gradient(circle at 15% 50%, rgba(27, 117, 187, 0.05), transparent 40%),
                radial-gradient(circle at 85% 30%, rgba(58, 170, 53, 0.05), transparent 40%),
                radial-gradient(circle at 50% 80%, rgba(227, 36, 43, 0.03), transparent 50%);
    pointer-events: none;
}

[data-theme="dark"] .premium-mesh-bg {
    background: radial-gradient(circle at 15% 50%, rgba(27, 117, 187, 0.08), transparent 40%),
                radial-gradient(circle at 85% 30%, rgba(58, 170, 53, 0.08), transparent 40%),
                radial-gradient(circle at 50% 80%, rgba(227, 36, 43, 0.05), transparent 50%);
}

.page-section {
    padding: 120px 0;
    min-height: 100vh; /* Ensure each section takes up good space */
    display: flex;
    flex-direction: column;
    justify-content: center;
}

/* Adjust the first section (home) to account for header */
#home {
    padding-top: 160px;
}

/* Redefine dock as flex nav */
nav.dock-list {
    display: flex;
    gap: 8px;
    padding: 0;
    margin: 0;
}

a.dock-item {
    text-decoration: none;
    color: inherit;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 4px;
    padding: 10px 16px;
    border-radius: 14px;
    cursor: pointer;
    transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    background: transparent;
}
"""
    if "Premium Single-Page Additions" not in css:
        css += premium_css

    with open(CSS_FILE, 'w', encoding='utf-8') as f:
        f.write(css)
    print("CSS updated.")


def update_js():
    with open(JS_FILE, 'r', encoding='utf-8') as f:
        js = f.read()

    # Remove old tab logic
    js = re.sub(
        r'// Handle Dock Navigation clicks.*?// Mobile Menu Toggle',
        r'// Scroll Spy Navigation Logic (Added below)\\n\\n    // Mobile Menu Toggle',
        js,
        flags=re.DOTALL
    )

    scroll_spy_js = """
    // ==========================================================================
    // Scroll Spy & Premium Reveal Animations
    // ==========================================================================

    const sections = document.querySelectorAll('.page-section');
    const dockItems = document.querySelectorAll('.dock-item');

    // Scroll Spy to highlight dock icons
    const observerOptions = {
        root: null,
        rootMargin: '-30% 0px -70% 0px', // Trigger when section is in top 30% of viewport
        threshold: 0
    };

    const sectionObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                // Remove active from all
                dockItems.forEach(item => item.classList.remove('active'));
                
                // Add active to corresponding dock item
                const id = entry.target.getAttribute('id');
                const correspondingDock = document.querySelector(`.dock-item[href="#${id}"]`);
                if (correspondingDock) {
                    correspondingDock.classList.add('active');
                }
                
                // Trigger any animations inside this section
                const animatedElements = entry.target.querySelectorAll('.animate-on-scroll:not(.animated)');
                animatedElements.forEach((el, index) => {
                    setTimeout(() => {
                        el.style.opacity = '1';
                        el.style.transform = 'translateY(0) scale(1)';
                        el.classList.add('animated');
                    }, index * 100);
                });
            }
        });
    }, observerOptions);

    sections.forEach(section => {
        sectionObserver.observe(section);
    });

    // Smooth scroll for dock items
    dockItems.forEach(item => {
        item.addEventListener('click', (e) => {
            e.preventDefault();
            const targetId = item.getAttribute('href');
            const targetSection = document.querySelector(targetId);
            if (targetSection) {
                targetSection.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });
"""
    if "Scroll Spy & Premium Reveal" not in js:
        js += scroll_spy_js

    with open(JS_FILE, 'w', encoding='utf-8') as f:
        f.write(js)
    print("JS updated.")

if __name__ == "__main__":
    update_html()
    update_css()
    update_js()
