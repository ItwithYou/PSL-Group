import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Add Sub-headings
replacements = [
    (
        '<h2 class="section-title animate-on-scroll" data-en="About PSL Group"',
        '<span class="sub-heading animate-on-scroll" data-en="OUR COMPANY" data-la="ບໍລິສັດຂອງພວກເຮົາ" data-zh="我们的公司">OUR COMPANY</span>\n                <h2 class="section-title animate-on-scroll" data-en="About PSL Group"'
    ),
    (
        '<h2 class="section-title animate-on-scroll" data-en="Corporate Roadmap"',
        '<span class="sub-heading animate-on-scroll" data-en="OUR JOURNEY" data-la="ການເດີນທາງຂອງພວກເຮົາ" data-zh="我们的旅程">OUR JOURNEY</span>\n                <h2 class="section-title animate-on-scroll" data-en="Corporate Roadmap"'
    ),
    (
        '<h2 class="section-title animate-on-scroll" data-en="Organization Structure"',
        '<span class="sub-heading animate-on-scroll" data-en="LEADERSHIP" data-la="ການນໍາພາ" data-zh="领导层">LEADERSHIP</span>\n                <h2 class="section-title animate-on-scroll" data-en="Organization Structure"'
    ),
    (
        '<h2 class="section-title animate-on-scroll" data-en="Corporate Portfolio"',
        '<span class="sub-heading animate-on-scroll" data-en="OUR WORK" data-la="ຜົນງານຂອງພວກເຮົາ" data-zh="我们的工作">OUR WORK</span>\n        <h2 class="section-title animate-on-scroll" data-en="Corporate Portfolio"'
    ),
    (
        '<h2 class="section-title animate-on-scroll" data-en="Company Activity"',
        '<span class="sub-heading animate-on-scroll" data-en="NEWS & UPDATES" data-la="ຂ່າວສານ ແລະ ການເຄື່ອນໄຫວ" data-zh="新闻与动态">NEWS & UPDATES</span>\n                <h2 class="section-title animate-on-scroll" data-en="Company Activity"'
    )
]

for old, new in replacements:
    if new not in content:
        content = content.replace(old, new)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Added sub-headings to index.html.")
