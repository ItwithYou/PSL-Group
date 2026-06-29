import re

# 1. Add Lightbox HTML to index.html
with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

lightbox_html = """
    <!-- Image Lightbox -->
    <div id="image-lightbox" class="lightbox">
        <span class="lightbox-close">&times;</span>
        <img src="" alt="Fullscreen Image" class="lightbox-img" id="lightbox-img">
    </div>
"""

if "id=\"image-lightbox\"" not in html:
    html = html.replace("</body>", lightbox_html + "\n</body>")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)


# 2. Add Lightbox JS to app.js
with open("app.js", "r", encoding="utf-8") as f:
    js = f.read()

lightbox_js = """
    // -----------------------------------------------------------------------------
    // Image Lightbox Logic
    // -----------------------------------------------------------------------------
    const lightbox = document.getElementById('image-lightbox');
    const lightboxImg = document.getElementById('lightbox-img');
    const lightboxClose = document.querySelector('.lightbox-close');

    if (lightbox && lightboxImg && lightboxClose) {
        // Find all project images
        const projectImages = document.querySelectorAll('.project-card-img, .news-img');
        
        projectImages.forEach(img => {
            img.parentElement.style.cursor = 'zoom-in'; // Ensure wrap has cursor
            img.parentElement.addEventListener('click', (e) => {
                e.preventDefault();
                lightboxImg.src = img.src;
                lightbox.classList.add('active');
            });
        });

        // Close on X click
        lightboxClose.addEventListener('click', () => {
            lightbox.classList.remove('active');
            setTimeout(() => lightboxImg.src = '', 400); // Clear after animation
        });

        // Close on background click
        lightbox.addEventListener('click', (e) => {
            if (e.target === lightbox) {
                lightbox.classList.remove('active');
                setTimeout(() => lightboxImg.src = '', 400);
            }
        });

        // Close on Escape key
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape' && lightbox.classList.contains('active')) {
                lightbox.classList.remove('active');
                setTimeout(() => lightboxImg.src = '', 400);
            }
        });
    }
"""

if "Image Lightbox Logic" not in js:
    # Insert at the end of DOMContentLoaded
    js = js.replace("}); // End DOMContentLoaded", lightbox_js + "\n}); // End DOMContentLoaded")

with open("app.js", "w", encoding="utf-8") as f:
    f.write(js)

print("Added lightbox logic to HTML and JS.")
