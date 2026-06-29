import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Fix the dock
dock_old_regex = r'<nav class="floating-dock">.*?</nav>'
dock_new = """<nav class="floating-dock">
            <ul class="dock-list">
                <li class="dock-item active" data-tab="tab-home" id="dock-home">
                    <span class="dock-label">
                        <span class="en-text">Home</span>
                        <span class="lao-text">ໜ້າຫຼັກ</span>
                        <span class="zh-text">首页</span>
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

html = re.sub(dock_old_regex, dock_new, html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("index.html dock fixed")
