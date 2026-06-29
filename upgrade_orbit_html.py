import re

# 1. Update index.html
with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

old_phil_content = """                <div class="philosophy-content">
                    <h2 class="section-tag animate-on-scroll" data-en="COMPANY VISION" data-la="ວິໄສທັດຂອງບໍລິສັດ" data-zh="公司愿景">COMPANY VISION</h2>
                    <p class="philosophy-text animate-on-scroll" id="vision-text">
                        <!-- Content injected by JS -->
                    </p>
                    <ul class="vision-list" id="vision-list">
                        <!-- Content injected by JS -->
                    </nav>
                </div>"""

new_phil_content = """                <div class="philosophy-content">
                    <div class="orbit-container">
                        <div class="orbit-center animate-on-scroll">
                            <h2 class="section-tag" data-en="COMPANY VISION" data-la="ວິໄສທັດຂອງບໍລິສັດ" data-zh="公司愿景">COMPANY VISION</h2>
                            <p class="philosophy-text" id="vision-text">
                                <!-- Content injected by JS -->
                            </p>
                        </div>
                        <div id="vision-list">
                            <!-- Orbit orbs injected by JS -->
                        </div>
                    </div>
                </div>"""

html = html.replace(old_phil_content, new_phil_content)
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

# 2. Update app.js
with open("app.js", "r", encoding="utf-8") as f:
    js = f.read()

# Replace visionList en
old_en = """            en: `<div class="vision-glass-grid">
    <div class="vision-glass-card animate-on-scroll card-honesty">
        <div class="glass-icon">🤝</div>
        <div class="glass-text">1. Honesty, transparency, and sincerity</div>
    </div>
    <div class="vision-glass-card animate-on-scroll card-safety">
        <div class="glass-icon">👷‍♂️</div>
        <div class="glass-text">2. Working with safety</div>
    </div>
    <div class="vision-glass-card animate-on-scroll card-quality">
        <div class="glass-icon">💎</div>
        <div class="glass-text">3. Paying attention to good quality</div>
    </div>
    <div class="vision-glass-card animate-on-scroll card-art">
        <div class="glass-icon">🎨</div>
        <div class="glass-text">4. Incorporating artistic beauty</div>
    </div>
    <div class="vision-glass-card animate-on-scroll card-time">
        <div class="glass-icon">⏱️</div>
        <div class="glass-text">5. Completing work on time</div>
    </div>
</div>`"""
new_en = """            en: `
    <div class="glass-orb animate-on-scroll orb-honesty orb-1">
        <div class="orb-icon">🤝</div>
        <div class="orb-text">1. Honesty & Transparency</div>
    </div>
    <div class="glass-orb animate-on-scroll orb-safety orb-2">
        <div class="orb-icon">👷‍♂️</div>
        <div class="orb-text">2. Superior Safety</div>
    </div>
    <div class="glass-orb animate-on-scroll orb-quality orb-3">
        <div class="orb-icon">💎</div>
        <div class="orb-text">3. Unmatched Quality</div>
    </div>
    <div class="glass-orb animate-on-scroll orb-art orb-4">
        <div class="orb-icon">🎨</div>
        <div class="orb-text">4. Artistic Beauty</div>
    </div>
    <div class="glass-orb animate-on-scroll orb-time orb-5">
        <div class="orb-icon">⏱️</div>
        <div class="orb-text">5. On-Time Delivery</div>
    </div>`"""
js = js.replace(old_en, new_en)

# Replace visionList la
old_la = """            la: `<div class="vision-glass-grid">
    <div class="vision-glass-card animate-on-scroll card-honesty">
        <div class="glass-icon">🤝</div>
        <div class="glass-text">1. ມີຄວາມຊື່ສັດ ໂປ່ງໃສ ແລະ ຈິງໃຈ</div>
    </div>
    <div class="vision-glass-card animate-on-scroll card-safety">
        <div class="glass-icon">👷‍♂️</div>
        <div class="glass-text">2. ເຮັດວຽກມີຄວາມປອດໄພ</div>
    </div>
    <div class="vision-glass-card animate-on-scroll card-quality">
        <div class="glass-icon">💎</div>
        <div class="glass-text">3. ໃສ່ໃຈຄຸນນະພາບທີ່ດີ</div>
    </div>
    <div class="vision-glass-card animate-on-scroll card-art">
        <div class="glass-icon">🎨</div>
        <div class="glass-text">4. ມີສິລະປະຄວາມສວຍງາມ</div>
    </div>
    <div class="vision-glass-card animate-on-scroll card-time">
        <div class="glass-icon">⏱️</div>
        <div class="glass-text">5. ວຽກສຳເລັດຕາມກຳນົດເວລາ</div>
    </div>
</div>`"""
new_la = """            la: `
    <div class="glass-orb animate-on-scroll orb-honesty orb-1">
        <div class="orb-icon">🤝</div>
        <div class="orb-text">1. ມີຄວາມຊື່ສັດ ໂປ່ງໃສ ແລະ ຈິງໃຈ</div>
    </div>
    <div class="glass-orb animate-on-scroll orb-safety orb-2">
        <div class="orb-icon">👷‍♂️</div>
        <div class="orb-text">2. ເຮັດວຽກມີຄວາມປອດໄພ</div>
    </div>
    <div class="glass-orb animate-on-scroll orb-quality orb-3">
        <div class="orb-icon">💎</div>
        <div class="orb-text">3. ໃສ່ໃຈຄຸນນະພາບທີ່ດີ</div>
    </div>
    <div class="glass-orb animate-on-scroll orb-art orb-4">
        <div class="orb-icon">🎨</div>
        <div class="orb-text">4. ມີສິລະປະຄວາມສວຍງາມ</div>
    </div>
    <div class="glass-orb animate-on-scroll orb-time orb-5">
        <div class="orb-icon">⏱️</div>
        <div class="orb-text">5. ວຽກສຳເລັດຕາມກຳນົດເວລາ</div>
    </div>`"""
js = js.replace(old_la, new_la)

# Replace visionList zh
old_zh = """            zh: `<div class="vision-glass-grid">
    <div class="vision-glass-card animate-on-scroll card-honesty">
        <div class="glass-icon">🤝</div>
        <div class="glass-text">1. 诚实、透明和真诚</div>
    </div>
    <div class="vision-glass-card animate-on-scroll card-safety">
        <div class="glass-icon">👷‍♂️</div>
        <div class="glass-text">2. 安全工作</div>
    </div>
    <div class="vision-glass-card animate-on-scroll card-quality">
        <div class="glass-icon">💎</div>
        <div class="glass-text">3. 关注优良品质</div>
    </div>
    <div class="vision-glass-card animate-on-scroll card-art">
        <div class="glass-icon">🎨</div>
        <div class="glass-text">4. 融入艺术美感</div>
    </div>
    <div class="vision-glass-card animate-on-scroll card-time">
        <div class="glass-icon">⏱️</div>
        <div class="glass-text">5. 按时完成工作</div>
    </div>
</div>`"""
new_zh = """            zh: `
    <div class="glass-orb animate-on-scroll orb-honesty orb-1">
        <div class="orb-icon">🤝</div>
        <div class="orb-text">1. 诚实、透明和真诚</div>
    </div>
    <div class="glass-orb animate-on-scroll orb-safety orb-2">
        <div class="orb-icon">👷‍♂️</div>
        <div class="orb-text">2. 安全工作</div>
    </div>
    <div class="glass-orb animate-on-scroll orb-quality orb-3">
        <div class="orb-icon">💎</div>
        <div class="orb-text">3. 关注优良品质</div>
    </div>
    <div class="glass-orb animate-on-scroll orb-art orb-4">
        <div class="orb-icon">🎨</div>
        <div class="orb-text">4. 融入艺术美感</div>
    </div>
    <div class="glass-orb animate-on-scroll orb-time orb-5">
        <div class="orb-icon">⏱️</div>
        <div class="orb-text">5. 按时完成工作</div>
    </div>`"""
js = js.replace(old_zh, new_zh)

with open("app.js", "w", encoding="utf-8") as f:
    f.write(js)

print("Updated html and js")
