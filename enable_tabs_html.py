import re

# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# We need to wrap specific sections in tab-content divs.
# Tab Home: hero-section, chronology-section, org-section, philosophy-section
# Tab Projects: showcase-section
# Tab Activity: activity-section
# Tab Contact: contact-section

# To do this safely, we will replace the section opening and closing tags.
# First, wrap the entire <main> contents.

# Find the start of main
main_start = html.find('<main class="main-content">') + len('<main class="main-content">')
main_end = html.rfind('</main>')

main_content = html[main_start:main_end]

# It's easier to inject opening wrappers before the first section, and closing wrappers after the specific sections.
# We will just write a custom replacer.

new_main = main_content

# Wrap Home
new_main = new_main.replace('<section class="hero-section">', '<div class="tab-content active" id="tab-home">\n        <section class="hero-section">')
# Close Home after philosophy
new_main = new_main.replace('</section>\n\n        <!-- Contact Section -->', '</section>\n        </div>\n\n        <!-- Contact Section -->')

# Wrap Projects
new_main = new_main.replace('<section class="showcase-section" id="projects">', '<div class="tab-content" id="tab-projects">\n        <section class="showcase-section" id="projects">')
new_main = new_main.replace('</section>\n\n        <!-- Chronology', '</section>\n        </div>\n\n        <!-- Chronology')

# Note: The activity section was injected above the footer, outside of <main>! Wait, let me check where activity is.
pass

# Let's write the file back safely by just replacing the section strings directly.
html = html.replace('<section class="hero-section">', '<div class="tab-content active" id="tab-home">\n        <section class="hero-section">')
# showcase is next
html = html.replace('<section class="showcase-section" id="projects">', '</div>\n\n        <div class="tab-content" id="tab-projects">\n        <section class="showcase-section" id="projects">')
# chronology is next (belongs to home, so close projects, open home again... wait, it's better to just put showcase-section somewhere else, or rearrange the HTML)

# Rearranging HTML for Tab layout:
# Tab Home: hero, chronology, org, philosophy
# Tab Projects: showcase
# Tab Activity: activity
# Tab Contact: contact

# Since this is complex in python, I'll use a regex to extract sections and rebuild <main>
sections = {
    'hero': re.search(r'<section class="hero-section">.*?</section>', html, re.DOTALL).group(0),
    'showcase': re.search(r'<section class="showcase-section" id="projects">.*?</section>', html, re.DOTALL).group(0),
    'chronology': re.search(r'<section class="chronology-section" id="timeline">.*?</section>', html, re.DOTALL).group(0),
    'org': re.search(r'<section class="org-section" id="organization">.*?</section>', html, re.DOTALL).group(0),
    'philosophy': re.search(r'<section class="philosophy-section">.*?</section>', html, re.DOTALL).group(0),
    'contact': re.search(r'<section class="contact-section" id="contact">.*?</section>', html, re.DOTALL).group(0)
}

# The activity section was appended before footer.
activity_match = re.search(r'<!-- Company Activity / News Section -->.*?</section>', html, re.DOTALL)
activity_sec = activity_match.group(0) if activity_match else ""

# Remove old sections from HTML
html = re.sub(r'<main class="main-content">.*?</main>', '<main class="main-content">\n<!-- CONTENT REPLACED -->\n</main>', html, flags=re.DOTALL)
if activity_sec:
    html = html.replace(activity_sec, '')

# Build new main content
rebuilt_main = f"""
    <main class="main-content">
        <!-- TAB: HOME -->
        <div class="tab-content active" id="tab-home">
            {sections['hero']}
            {sections['chronology']}
            {sections['org']}
            {sections['philosophy']}
        </div>

        <!-- TAB: PROJECTS -->
        <div class="tab-content" id="tab-projects">
            {sections['showcase']}
        </div>

        <!-- TAB: ACTIVITY -->
        <div class="tab-content" id="tab-activity">
            {activity_sec}
        </div>

        <!-- TAB: CONTACT -->
        <div class="tab-content" id="tab-contact">
            {sections['contact']}
        </div>
    </main>
"""

html = html.replace('<main class="main-content">\n<!-- CONTENT REPLACED -->\n</main>', rebuilt_main)

# Update Dock items to match tabs
dock_old = """                <ul class="dock-nav">
                    <li class="dock-item active" data-filter="all" id="dock-all">
                        <span class="dock-label">
                            <span class="en-text">All Projects</span>
                            <span class="lao-text">ໂຄງການທັງໝົດ</span>
                            <span class="zh-text">所有项目</span>
                        </span>
                    </li>
                    <li class="dock-item" data-filter="construction" id="dock-construction">
                        <span class="dock-label">
                            <span class="en-text">Construction</span>
                            <span class="lao-text">ກໍ່ສ້າງ</span>
                            <span class="zh-text">建筑</span>
                        </span>
                    </li>
                    <li class="dock-item" data-filter="service" id="dock-service">
                        <span class="dock-label">
                            <span class="en-text">Service</span>
                            <span class="lao-text">ບໍລິການ</span>
                            <span class="zh-text">服务</span>
                        </span>
                    </li>
                    <li class="dock-item" data-filter="activity" id="dock-activity">
                        <span class="dock-label">
                            <span class="en-text">News</span>
                            <span class="lao-text">ຂ່າວສານ</span>
                            <span class="zh-text">新闻</span>
                        </span>
                    </li>
                    <li class="dock-item" data-filter="contact" id="dock-contact">
                        <span class="dock-label">
                            <span class="en-text">Contact</span>
                            <span class="lao-text">ຕິດຕໍ່ພົວພັນ</span>
                            <span class="zh-text">联系</span>
                        </span>
                    </li>
                </ul>"""

dock_new = """                <ul class="dock-nav">
                    <li class="dock-item active" data-tab="tab-home">
                        <span class="dock-label">
                            <span class="en-text">Home</span>
                            <span class="lao-text">ໜ້າຫຼັກ</span>
                            <span class="zh-text">首页</span>
                        </span>
                    </li>
                    <li class="dock-item" data-tab="tab-projects">
                        <span class="dock-label">
                            <span class="en-text">Projects</span>
                            <span class="lao-text">ໂຄງການ</span>
                            <span class="zh-text">项目</span>
                        </span>
                    </li>
                    <li class="dock-item" data-tab="tab-activity">
                        <span class="dock-label">
                            <span class="en-text">News</span>
                            <span class="lao-text">ຂ່າວສານ</span>
                            <span class="zh-text">新闻</span>
                        </span>
                    </li>
                    <li class="dock-item" data-tab="tab-contact">
                        <span class="dock-label">
                            <span class="en-text">Contact</span>
                            <span class="lao-text">ຕິດຕໍ່ພົວພັນ</span>
                            <span class="zh-text">联系</span>
                        </span>
                    </li>
                </ul>"""

# If the old dock doesn't perfectly match (because of spacing), we can replace using regex
html = re.sub(r'<ul class="dock-nav">.*?</ul>', dock_new, html, flags=re.DOTALL)


with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("index.html refactored for tabs.")
