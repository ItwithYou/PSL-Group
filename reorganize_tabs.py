import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Extract sections
sections = {
    'hero': re.search(r'<section class="hero-section">.*?</section>', html, re.DOTALL).group(0),
    'showcase': re.search(r'<section class="showcase-section" id="projects">.*?</section>', html, re.DOTALL).group(0),
    'chronology': re.search(r'<section class="chronology-section" id="timeline">.*?</section>', html, re.DOTALL).group(0),
    'org': re.search(r'<section class="org-section" id="organization">.*?</section>', html, re.DOTALL).group(0),
    'philosophy': re.search(r'<section class="philosophy-section">.*?</section>', html, re.DOTALL).group(0),
    'activity': re.search(r'<section class="activity-section" id="activity".*?</section>', html, re.DOTALL).group(0),
    'contact': re.search(r'<section class="contact-section" id="contact">.*?</section>', html, re.DOTALL).group(0)
}

# Remove old main content
html = re.sub(r'<main class="main-content">.*?</main>', '<main class="main-content">\n<!-- REPLACED -->\n</main>', html, flags=re.DOTALL)

# Rebuild main content
rebuilt_main = f"""    <main class="main-content">
        <!-- TAB: HOME -->
        <div class="tab-content active" id="tab-home">
            {sections['hero']}
            {sections['philosophy']}
        </div>

        <!-- TAB: ABOUT US -->
        <div class="tab-content" id="tab-about">
            {sections['chronology']}
            {sections['org']}
        </div>

        <!-- TAB: PROJECTS -->
        <div class="tab-content" id="tab-projects">
            {sections['showcase']}
        </div>

        <!-- TAB: ACTIVITY -->
        <div class="tab-content" id="tab-activity">
            {sections['activity']}
        </div>

        <!-- TAB: CONTACT -->
        <div class="tab-content" id="tab-contact">
            {sections['contact']}
        </div>
    </main>"""

html = html.replace('<main class="main-content">\n<!-- REPLACED -->\n</main>', rebuilt_main)

# Update Dock
dock_new = """<nav class="floating-dock">
            <ul class="dock-list">
                <li class="dock-item active" data-tab="tab-home" id="dock-home">
                    <span class="dock-label">
                        <span class="en-text">Home</span>
                        <span class="lao-text">ໜ້າຫຼັກ</span>
                        <span class="zh-text">首页</span>
                    </span>
                </li>
                <li class="dock-item" data-tab="tab-about" id="dock-about">
                    <span class="dock-label">
                        <span class="en-text">About</span>
                        <span class="lao-text">ກ່ຽວກັບພວກເຮົາ</span>
                        <span class="zh-text">关于我们</span>
                    </span>
                </li>
                <li class="dock-item" data-tab="tab-projects" id="dock-projects">
                    <span class="dock-label">
                        <span class="en-text">Projects</span>
                        <span class="lao-text">ໂຄງການ</span>
                        <span class="zh-text">项目</span>
                    </span>
                </li>
                <li class="dock-item" data-tab="tab-activity" id="dock-activity">
                    <span class="dock-label">
                        <span class="en-text">News</span>
                        <span class="lao-text">ຂ່າວສານ</span>
                        <span class="zh-text">新闻</span>
                    </span>
                </li>
                <li class="dock-item" data-tab="tab-contact" id="dock-contact">
                    <span class="dock-label">
                        <span class="en-text">Contact</span>
                        <span class="lao-text">ຕິດຕໍ່ພົວພັນ</span>
                        <span class="zh-text">联系</span>
                    </span>
                </li>
            </ul>
        </nav>"""

html = re.sub(r'<nav class="floating-dock">.*?</nav>', dock_new, html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("index.html completely reorganized!")
