import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add "Company Activity" tab to bottom dock
dock_contact_regex = r'<li class="dock-item" data-filter="contact" id="dock-contact">.*?</li>'

dock_new = """
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
"""
content = re.sub(dock_contact_regex, dock_new, content, flags=re.DOTALL)

# 2. Add Activity Section HTML above the Footer
activity_section = """
        <!-- Company Activity / News Section -->
        <section class="activity-section" id="activity" style="padding: 8rem 2rem; max-width: 1200px; margin: 0 auto; position: relative; z-index: 10;">
            <div class="org-header">
                <h2 class="section-title" data-en="Company Activity" data-la="ການເຄື່ອນໄຫວຂອງບໍລິສັດ" data-zh="公司活动">Company Activity</h2>
                <div class="section-divider"></div>
            </div>
            
            <div id="activity-feed" class="activity-feed-grid">
                <!-- Activities will be injected here by app.js -->
                <div class="loading-state" data-en="Loading latest news..." data-la="ກຳລັງໂຫຼດຂ່າວໃໝ່ລ່າສຸດ..." data-zh="正在加载最新新闻...">Loading latest news...</div>
            </div>
        </section>

"""

content = content.replace('<!-- Footer Section -->', activity_section + '        <!-- Footer Section -->')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Injected activity section to index.html successfully.")
