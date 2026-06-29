import re

# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

vision_html = """            <section class="philosophy-section">
            <div class="philosophy-grid">
                <div class="philosophy-content">
                    <h2 class="section-tag" data-en="COMPANY VISION" data-la="ວິໄສທັດຂອງບໍລິສັດ" data-zh="公司愿景">COMPANY VISION</h2>
                    <p class="philosophy-text" id="vision-text">
                        <!-- Content injected by JS -->
                    </p>
                    <ul class="vision-list" id="vision-list">
                        <!-- Content injected by JS -->
                    </ul>
                </div>
            </div>
        </section>"""

# Replace the existing philosophy section
html = re.sub(r'<section class="philosophy-section">.*?</section>', vision_html, html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

# 2. Update app.js
with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

vision_translations = """        visionText: {
            en: "We have a vision to develop the company into a comprehensive construction conglomerate through cooperation with domestic and international companies. By utilizing advanced construction technologies, we aim to achieve outstanding success, build confidence and trust with project owners, and create maximum satisfaction to meet customer needs with excellent quality and impressive services under 5 key factors:",
            la: "ພວກເຮົາມີວິໄສທັດທີ່ຈະພັດທະນາບໍລິສັດ ໃຫ້ເປັນກຸ່ມບໍລິສັດກໍ່ສ້າງຄົບວົງຈອນ ໂດຍການຮ່ວມມືກັບບັນດາບໍລິສັດພາຍໃນ ແລະ ບໍລິສັດຕ່າງປະເທດ ເພື່ອນຳໃຊ້ເຕັກໂນໂລຊີກໍ່ສ້າງຕ່າງໆ ໃຫ້ມີຜົນສຳເລັດທີ່ໂດດເດັ່ນ, ສ້າງຄວາມເຊື່ອໝັ້ນ ແລະ ໄວ້ວາງໃຈ ຂອງເຈົ້າຂອງໂຄງການ ແລະ ສ້າງຄວາມເພິ່ງພໍໃຈ ເພື່ອຕອບສະໜອງຄວາມຕ້ອງການຂອງລູກຄ້າດ້ວຍຄຸນນະພາບທີ່ດີເລີດ ແລະ ການບໍລິການທີ່ປະທັບໃຈ ພາຍໃຕ້ການປະຕິບັດ 5 ປັດໃຈສຳຄັນ ຄື:",
            zh: "我们的愿景是通过与国内外公司合作，将公司发展成为一家综合性建筑企业集团。利用先进的建筑技术，我们旨在取得卓越的成就，建立项目业主的信心和信任，并以卓越的质量和令人印象深刻的服务创造最大的满意度，以满足客户的需求。我们的行动基于5个关键因素："
        },
        visionList: {
            en: "<li>1. Honesty, transparency, and sincerity;</li><li>2. Working with safety;</li><li>3. Paying attention to good quality;</li><li>4. Incorporating artistic beauty;</li><li>5. Completing work on time;</li>",
            la: "<li>1. ມີຄວາມສັດຊື່ ໂປ່ງໃສ ແລະ ຈິງໃຈ;</li><li>2. ເຮັດວຽກມີຄວາມປອດໄພ;</li><li>3. ໃສ່ໃຈຄຸນນະພາບທີ່ດີ;</li><li>4. ມີສິນລະປະຄວາມສວຍງາມ;</li><li>5. ວຽກສຳເລັດຕາມກຳນົດເວລາ;</li>",
            zh: "<li>1. 诚实、透明和真诚；</li><li>2. 安全工作；</li><li>3. 注重优良品质；</li><li>4. 融入艺术美感；</li><li>5. 按时完成工作；</li>"
        },
"""

# Replace philosophyText1 and philosophyText2 with visionText and visionList
js = re.sub(r'philosophyText1:\s*\{.*?\},', vision_translations, js, flags=re.DOTALL)
js = re.sub(r'philosophyText2:\s*\{.*?\},', '', js, flags=re.DOTALL)

# Update the injection logic in updateLanguageUI
js_injection = """    // Update dynamic fields from JavaScript database
    const heroDesc = document.getElementById('hero-desc');
    if (heroDesc) heroDesc.textContent = translations.heroDesc[currentLang];

    const visText = document.getElementById('vision-text');
    if (visText) visText.textContent = translations.visionText[currentLang];

    const visList = document.getElementById('vision-list');
    if (visList) visList.innerHTML = translations.visionList[currentLang];"""

js = re.sub(r'// Update dynamic fields from JavaScript database\s*document.getElementById\(\'hero-desc\'\).*?document.getElementById\(\'phil-text-2\'\).textContent = translations.philosophyText2\[currentLang\];', js_injection, js, flags=re.DOTALL)

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Vision text updated successfully.")
