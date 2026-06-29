import re

with open("style.css", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update CSS Variables (Colors and Fonts)
old_vars = """    /* Color Palette - Light Theme (Sophisticated Warm Minimal) */
    --bg-color: #f7f6f2;
    --text-color: #151515;
    --text-muted: #6f6f6f;
    --border-color: #d1cfc9;
    --border-light: #e5e3dd;
    --accent-color: #bfa15f;
    --accent-dark: #8c7340;
    --card-bg: #ffffff;
    --dock-bg: rgba(255, 255, 255, 0.7);
    --dock-border: rgba(21, 21, 21, 0.08);
    --dock-text: #151515;
    --dock-indicator: #151515;
    --modal-bg: #f7f6f2;
    --success-bg: #e8f5e9;
    --success-text: #2e7d32;
    
    /* Typography & Spacing */
    --font-primary: 'Outfit', 'Noto Sans Lao', sans-serif;"""

new_vars = """    /* Color Palette - Light Theme (Phongsupthavy Corporate) */
    --bg-color: #F8F9FA;
    --text-color: #0A2540; /* Conglomerate Navy */
    --text-muted: #4a5568;
    --border-color: #e2e8f0;
    --border-light: #edf2f7;
    --accent-color: #C5A059; /* Royal Gold */
    --accent-dark: #A38241;
    --card-bg: #ffffff;
    --dock-bg: rgba(255, 255, 255, 0.75);
    --dock-border: rgba(10, 37, 64, 0.08);
    --dock-text: #0A2540;
    --dock-indicator: #0A2540;
    --modal-bg: #F8F9FA;
    --success-bg: #e8f5e9;
    --success-text: #2e7d32;
    
    /* Typography & Spacing */
    --font-primary: 'Inter', 'Montserrat', 'Noto Sans Lao', sans-serif;"""

content = content.replace(old_vars, new_vars)

# Update Dark Theme Variables for good measure
old_dark = """[data-theme="dark"] {
    --bg-color: #1a1a1a;
    --text-color: #f7f6f2;
    --text-muted: #9f9f9f;
    --border-color: #333333;
    --border-light: #2a2a2a;
    --accent-color: #d4b872;
    --accent-dark: #bfa15f;
    --card-bg: #222222;
    --dock-bg: rgba(30, 30, 30, 0.7);
    --dock-border: rgba(255, 255, 255, 0.08);
    --dock-text: #f7f6f2;
    --dock-indicator: #f7f6f2;
    --modal-bg: #1a1a1a;
}"""
new_dark = """[data-theme="dark"] {
    --bg-color: #051322; /* Darker Navy */
    --text-color: #F8F9FA;
    --text-muted: #a0aec0;
    --border-color: #1a365d;
    --border-light: #2a4365;
    --accent-color: #C5A059;
    --accent-dark: #A38241;
    --card-bg: #0A2540;
    --dock-bg: rgba(10, 37, 64, 0.75);
    --dock-border: rgba(255, 255, 255, 0.08);
    --dock-text: #F8F9FA;
    --dock-indicator: #F8F9FA;
    --modal-bg: #051322;
}"""
content = content.replace(old_dark, new_dark)


# 2. Add Sub-heading Utility Class
sub_heading_css = """
.sub-heading {
    text-transform: uppercase;
    letter-spacing: 2px;
    color: var(--accent-color);
    font-size: 0.85rem;
    font-weight: 700;
    margin-bottom: 0.5rem;
    display: block;
}
"""
if ".sub-heading {" not in content:
    content = content.replace("/* Typography Base */", "/* Typography Base */\n" + sub_heading_css)


# 3. Rewrite Project Layout
old_projects = """.project-entries {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
    gap: 2rem;
}

.project-entry {
    position: relative;
    background-color: var(--card-bg);
    border: 1px solid var(--border-color);
    border-radius: 14px;
    padding: 1.5rem 1.5rem 1.5rem 1.75rem;
    overflow: hidden;
    transition: var(--transition-quick);
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.02);
    display: flex;
    flex-direction: column;
    gap: 1.25rem;
}

.project-img-wrap {
    margin: -1.5rem -1.5rem 1.25rem -1.75rem;
    border-radius: 14px 14px 0 0;
    overflow: hidden;
}

.project-card-img {
    width: 100%;
    height: 240px;
    object-fit: cover;
    display: block;
    transition: transform 0.5s ease;
    animation: kenBurns 20s ease-in-out infinite alternate;
}"""

new_projects = """.project-entries {
    display: flex;
    flex-direction: column;
    gap: 6rem;
}

.project-entry {
    position: relative;
    display: flex;
    flex-direction: row;
    align-items: center;
    transition: transform 0.4s cubic-bezier(0.25, 0.8, 0.25, 1);
}

.project-entry:nth-child(even) {
    flex-direction: row-reverse;
}

.project-img-wrap {
    width: 60%;
    height: 400px;
    position: relative;
    z-index: 1;
    border-radius: 8px;
    overflow: hidden;
    box-shadow: 0 20px 40px rgba(0,0,0,0.15);
}

.project-card-img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    display: block;
    transition: transform 0.5s ease;
    animation: kenBurns 20s ease-in-out infinite alternate;
}

.project-info-container {
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
}

.project-entry:nth-child(even) .project-info-container {
    margin-left: 0;
    margin-right: -10%;
}

@media (max-width: 900px) {
    .project-entries {
        gap: 4rem;
    }
    .project-entry, .project-entry:nth-child(even) {
        flex-direction: column;
    }
    .project-img-wrap {
        width: 100%;
        height: 300px;
    }
    .project-info-container {
        width: 90%;
        margin-left: 0;
        margin-right: 0;
        margin-top: -3rem;
        padding: 2rem;
    }
    .project-entry:nth-child(even) .project-info-container {
        margin-left: 0;
        margin-right: 0;
    }
}"""

content = content.replace(old_projects, new_projects)

# 4. Remove flex-grow from old detail (it was for equal heights, not needed in asymmetric layout)
old_detail = """.project-entry-detail {
    font-size: 0.9rem;
    line-height: 1.6;
    color: var(--text-muted);
    font-weight: 300;
    margin: 0 0 1.1rem 0;
    flex-grow: 1;
}"""
new_detail = """.project-entry-detail {
    font-size: 1rem;
    line-height: 1.6;
    color: var(--text-muted);
    font-weight: 400;
    margin: 0 0 1.5rem 0;
}"""
content = content.replace(old_detail, new_detail)

with open("style.css", "w", encoding="utf-8") as f:
    f.write(content)

print("Updated style.css for Phongsupthavy Corporate style.")
