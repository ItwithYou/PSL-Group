import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Extract existing sections safely
sections = {}
for sec_class in ['hero-section', 'chronology-section', 'org-section', 'philosophy-section', 'showcase-section', 'contact-section']:
    match = re.search(f'<section class="{sec_class}".*?</section>', html, re.DOTALL)
    if match:
        sections[sec_class] = match.group(0)
    else:
        print(f"CRITICAL: {sec_class} not found!")

# 2. Re-create the Activity Section since it was deleted
activity_section = """        <section class="activity-section" id="activity" style="padding: 5rem 2rem; max-width: 1200px; margin: 0 auto; position: relative; z-index: 10;">
            <div class="org-header">
                <h2 class="section-title" data-en="Company Activity" data-la="ການເຄື່ອນໄຫວຂອງບໍລິສັດ" data-zh="公司活动">Company Activity</h2>
                <div class="section-divider"></div>
            </div>
            
            <div id="activity-feed" class="activity-feed-grid">
                <!-- Activities will be injected here by app.js -->
                <div class="loading-state" data-en="Loading latest news..." data-la="ກຳລັງໂຫຼດຂ່າວໃໝ່ລ່າສຸດ..." data-zh="正在加载最新新闻...">Loading latest news...</div>
            </div>
        </section>"""
sections['activity-section'] = activity_section

# 3. Build perfect tabs
rebuilt_main = f"""    <main class="main-content">
        <!-- TAB: HOME -->
        <div class="tab-content active" id="tab-home">
{sections['hero-section']}
{sections['philosophy-section']}
        </div>

        <!-- TAB: ABOUT US -->
        <div class="tab-content" id="tab-about">
{sections['chronology-section']}
{sections['org-section']}
        </div>

        <!-- TAB: PROJECTS -->
        <div class="tab-content" id="tab-projects">
{sections['showcase-section']}
        </div>

        <!-- TAB: ACTIVITY -->
        <div class="tab-content" id="tab-activity">
{sections['activity-section']}
        </div>

        <!-- TAB: CONTACT -->
        <div class="tab-content" id="tab-contact">
{sections['contact-section']}
        </div>
    </main>"""

# 4. Replace <main> block
html = re.sub(r'<main class="main-content">.*?</main>', rebuilt_main, html, flags=re.DOTALL)

# 5. Fix the Dock to exactly match these 5 tabs, perfectly aligned
dock_new = """<nav class="floating-dock">
            <ul class="dock-list" style="display: flex; gap: 10px; padding: 0; margin: 0; list-style: none;">
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
print("index.html perfectly rebuilt!")
