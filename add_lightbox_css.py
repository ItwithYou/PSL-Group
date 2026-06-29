import re

with open("style.css", "r", encoding="utf-8") as f:
    css = f.read()

# 1. Polish project boxes (project-info-container)
old_info = """.project-info-container {
    width: 50%;
    background-color: var(--card-bg);
    padding: 3.5rem;
    position: relative;
    z-index: 2;
    margin-left: -10%;
    border-radius: 8px;
    border: 1px solid var(--border-color);
    box-shadow: 0 15px 35px rgba(0,0,0,0.05);
    display: flex;
    flex-direction: column;
    justify-content: center;
    transition: all 0.4s cubic-bezier(0.25, 0.8, 0.25, 1);
}"""

new_info = """.project-info-container {
    width: 50%;
    background: rgba(255, 255, 255, 0.95);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    padding: 3.5rem;
    position: relative;
    z-index: 2;
    margin-left: -10%;
    border-radius: 16px;
    border: 1px solid rgba(255, 255, 255, 0.6);
    box-shadow: 0 25px 50px rgba(10, 37, 64, 0.08), inset 0 0 0 1px rgba(255, 255, 255, 0.5);
    display: flex;
    flex-direction: column;
    justify-content: center;
    transition: all 0.4s cubic-bezier(0.25, 0.8, 0.25, 1);
}

[data-theme="dark"] .project-info-container {
    background: rgba(10, 37, 64, 0.95);
    border-color: rgba(255, 255, 255, 0.1);
    box-shadow: 0 25px 50px rgba(0, 0, 0, 0.4), inset 0 0 0 1px rgba(255, 255, 255, 0.05);
}"""
css = css.replace(old_info, new_info)

# Upgrade project-img-wrap to rounded corners
old_wrap = """.project-img-wrap {
    width: 60%;
    height: 400px;
    position: relative;
    z-index: 1;
    border-radius: 8px;
    overflow: hidden;
    box-shadow: 0 20px 40px rgba(0,0,0,0.15);
}"""
new_wrap = """.project-img-wrap {
    width: 60%;
    height: 420px;
    position: relative;
    z-index: 1;
    border-radius: 16px;
    overflow: hidden;
    box-shadow: 0 30px 60px rgba(0,0,0,0.15);
    cursor: zoom-in;
}"""
css = css.replace(old_wrap, new_wrap)


# 2. Add Lightbox CSS
lightbox_css = """
/* ==========================================================================
   Image Lightbox
   ========================================================================== */
.lightbox {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background: rgba(10, 37, 64, 0.95);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    z-index: 9999;
    display: flex;
    align-items: center;
    justify-content: center;
    opacity: 0;
    pointer-events: none;
    transition: opacity 0.4s ease;
}

.lightbox.active {
    opacity: 1;
    pointer-events: all;
}

.lightbox-img {
    max-width: 90vw;
    max-height: 90vh;
    border-radius: 8px;
    box-shadow: 0 25px 50px rgba(0, 0, 0, 0.5);
    transform: scale(0.9);
    transition: transform 0.4s cubic-bezier(0.25, 0.8, 0.25, 1);
}

.lightbox.active .lightbox-img {
    transform: scale(1);
}

.lightbox-close {
    position: absolute;
    top: 2rem;
    right: 2rem;
    color: #ffffff;
    font-size: 2.5rem;
    cursor: pointer;
    line-height: 1;
    transition: color 0.3s ease;
}

.lightbox-close:hover {
    color: var(--accent-color);
}
"""

if "Image Lightbox" not in css:
    css += "\n" + lightbox_css

with open("style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Updated style.css with polished projects and lightbox.")
