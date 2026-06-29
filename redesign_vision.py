import re

with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Define the glass HTML grid and items for all 3 languages
# Icons: 🛡️ (Honesty), 👷 (Safety), 💎 (Quality), 🎨 (Art), ⏱️ (Time)

glass_html_en = """<div class="vision-glass-grid">
    <div class="vision-glass-card card-honesty">
        <div class="glass-icon">🛡️</div>
        <div class="glass-text">1. Honesty, transparency, and sincerity</div>
    </div>
    <div class="vision-glass-card card-safety">
        <div class="glass-icon">👷</div>
        <div class="glass-text">2. Working with safety</div>
    </div>
    <div class="vision-glass-card card-quality">
        <div class="glass-icon">💎</div>
        <div class="glass-text">3. Paying attention to good quality</div>
    </div>
    <div class="vision-glass-card card-art">
        <div class="glass-icon">🎨</div>
        <div class="glass-text">4. Incorporating artistic beauty</div>
    </div>
    <div class="vision-glass-card card-time">
        <div class="glass-icon">⏱️</div>
        <div class="glass-text">5. Completing work on time</div>
    </div>
</div>"""

glass_html_la = """<div class="vision-glass-grid">
    <div class="vision-glass-card card-honesty">
        <div class="glass-icon">🛡️</div>
        <div class="glass-text">1. ມີຄວາມສັດຊື່ ໂປ່ງໃສ ແລະ ຈິງໃຈ</div>
    </div>
    <div class="vision-glass-card card-safety">
        <div class="glass-icon">👷</div>
        <div class="glass-text">2. ເຮັດວຽກມີຄວາມປອດໄພ</div>
    </div>
    <div class="vision-glass-card card-quality">
        <div class="glass-icon">💎</div>
        <div class="glass-text">3. ໃສ່ໃຈຄຸນນະພາບທີ່ດີ</div>
    </div>
    <div class="vision-glass-card card-art">
        <div class="glass-icon">🎨</div>
        <div class="glass-text">4. ມີສິນລະປະຄວາມສວຍງາມ</div>
    </div>
    <div class="vision-glass-card card-time">
        <div class="glass-icon">⏱️</div>
        <div class="glass-text">5. ວຽກສຳເລັດຕາມກຳນົດເວລາ</div>
    </div>
</div>"""

glass_html_zh = """<div class="vision-glass-grid">
    <div class="vision-glass-card card-honesty">
        <div class="glass-icon">🛡️</div>
        <div class="glass-text">1. 诚实、透明和真诚</div>
    </div>
    <div class="vision-glass-card card-safety">
        <div class="glass-icon">👷</div>
        <div class="glass-text">2. 安全工作</div>
    </div>
    <div class="vision-glass-card card-quality">
        <div class="glass-icon">💎</div>
        <div class="glass-text">3. 注重优良品质</div>
    </div>
    <div class="vision-glass-card card-art">
        <div class="glass-icon">🎨</div>
        <div class="glass-text">4. 融入艺术美感</div>
    </div>
    <div class="vision-glass-card card-time">
        <div class="glass-icon">⏱️</div>
        <div class="glass-text">5. 按时完成工作</div>
    </div>
</div>"""

new_vision_list = f"""        visionList: {{
            en: `{glass_html_en}`,
            la: `{glass_html_la}`,
            zh: `{glass_html_zh}`
        }},"""

js = re.sub(r'visionList:\s*\{.*?\},', new_vision_list, js, flags=re.DOTALL)

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js)

# Now for the CSS
css = """
/* ==========================================================================
   Vision Glassmorphism Cards
   ========================================================================== */
.vision-glass-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
    gap: 1.5rem;
    margin-top: 2rem;
    width: 100%;
}

.vision-glass-card {
    background: rgba(255, 255, 255, 0.05);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border-radius: 16px;
    padding: 1.5rem;
    display: flex;
    align-items: center;
    gap: 1rem;
    box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.1);
    transition: all 0.3s ease;
    border: 1px solid rgba(255, 255, 255, 0.1);
    position: relative;
    overflow: hidden;
}

[data-theme="light"] .vision-glass-card {
    background: rgba(255, 255, 255, 0.4);
    box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.07);
    border: 1px solid rgba(255, 255, 255, 0.4);
}

.vision-glass-card:hover {
    transform: translateY(-5px);
}

.glass-icon {
    font-size: 2rem;
    filter: drop-shadow(0 2px 4px rgba(0,0,0,0.2));
}

.glass-text {
    font-size: 1rem;
    font-weight: 500;
    color: var(--text-color);
    line-height: 1.4;
    z-index: 2;
}

/* Color Matching Glows */
.vision-glass-card::before {
    content: '';
    position: absolute;
    top: -50%;
    left: -50%;
    width: 200%;
    height: 200%;
    background: radial-gradient(circle, var(--glow-color) 0%, transparent 60%);
    opacity: 0.15;
    z-index: 0;
    pointer-events: none;
    transition: opacity 0.3s ease;
}

.vision-glass-card:hover::before {
    opacity: 0.3;
}

.card-honesty { --glow-color: #3b82f6; border-bottom: 3px solid #3b82f6; } /* Blue for honesty/trust */
.card-safety { --glow-color: #f59e0b; border-bottom: 3px solid #f59e0b; } /* Orange for safety/caution */
.card-quality { --glow-color: #8b5cf6; border-bottom: 3px solid #8b5cf6; } /* Purple for premium quality */
.card-art { --glow-color: #ec4899; border-bottom: 3px solid #ec4899; } /* Pink for art/beauty */
.card-time { --glow-color: #10b981; border-bottom: 3px solid #10b981; } /* Green for on time/success */
"""

with open('style.css', 'a', encoding='utf-8') as f:
    f.write(css)

print("Redesign complete!")
