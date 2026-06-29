import re

# 1. UPDATE APP.JS VISION TEXT
with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

new_vision_text = """        visionText: {
            en: "Committed to being a leader in comprehensive construction conglomerates through strategic partnerships with domestic and international partners to elevate construction technology to be modern and outstanding. We focus on building trust and meeting customer needs with international standard quality and impressive service, driven by 5 key success factors:",
            la: "ມຸ່ງໝັ້ນສູ່ການເປັນຜູ້ນຳດ້ານກຸ່ມບໍລິສັດກໍ່ສ້າງຄົບວົງຈອນ ໂດຍການຮ່ວມມືຍຸດທະສາດກັບຄູ່ຄ້າທັງພາຍໃນ ແລະ ຕ່າງປະເທດ ເພື່ອຍົກລະດັບເຕັກໂນໂລຊີການກໍ່ສ້າງໃຫ້ທັນສະໄໝ ແລະ ໂດດເດັ່ນ. ພວກເຮົາມຸ່ງເນັ້ນການສ້າງຄວາມເຊື່ອໝັ້ນ, ຕອບສະໜອງຄວາມຕ້ອງການຂອງລູກຄ້າດ້ວຍຄຸນນະພາບມາດຕະຖານສາກົນ ແລະ ການບໍລິການທີ່ປະທັບໃຈ ພາຍໃຕ້ການຂັບເຄື່ອນຂອງ 5 ປັດໄຈຫຼັກສູ່ຄວາມສຳເລັດ",
            zh: "致力于通过与国内外合作伙伴的战略合作，成为综合性建筑企业集团的领导者，提升现代卓越的建筑技术。我们注重建立信任，以国际标准的质量和令人印象深刻的服务满足客户需求，受5个关键成功因素的驱动："
        },"""

js = re.sub(r'visionText:\s*\{.*?\},', new_vision_text, js, flags=re.DOTALL)

# Since we are making circles, the text inside the circles should be shorter if possible, but the user didn't ask to change the list text.
# The glass-text might overflow a perfect circle if the text is too long, so I will ensure the text is small and wraps nicely.

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js)

# 2. UPDATE STYLE.CSS FOR CIRCULAR PREMIUM GLASS
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

old_bento_css = r"""/\* Asymmetrical Modern "Scattered" Bento Grid \*/.*?(?=/\* Activity Feed Styling \*/|/\* ==========================================================================
   Tab Navigation System)"""

new_circular_css = """/* Premium Circular Glassmorphism */
.vision-glass-grid {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 2.5rem;
    margin-top: 4rem;
    width: 100%;
    padding-bottom: 2rem;
}

.vision-glass-card {
    background: linear-gradient(135deg, rgba(255, 255, 255, 0.12) 0%, rgba(255, 255, 255, 0.02) 100%);
    backdrop-filter: blur(40px);
    -webkit-backdrop-filter: blur(40px);
    border-radius: 50%; /* Perfect Circle */
    width: 220px;
    height: 220px;
    padding: 1.5rem;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    gap: 0.8rem;
    box-shadow: 
        0 25px 45px rgba(0, 0, 0, 0.2), 
        inset 0 1px 0 rgba(255, 255, 255, 0.3),
        inset 0 -1px 0 rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(255, 255, 255, 0.08);
    position: relative;
    overflow: hidden;
    z-index: 1;
    /* Removed hover transform transitions to fulfill user request */
}

[data-theme="light"] .vision-glass-card {
    background: linear-gradient(135deg, rgba(255, 255, 255, 0.8) 0%, rgba(255, 255, 255, 0.4) 100%);
    box-shadow: 
        0 25px 45px rgba(31, 38, 135, 0.1),
        inset 0 2px 0 rgba(255, 255, 255, 0.8),
        inset 0 -1px 0 rgba(255, 255, 255, 0.3);
    border: 1px solid rgba(255, 255, 255, 0.5);
}

/* Color Matching Glows inside the circle */
.vision-glass-card::before {
    content: '';
    position: absolute;
    top: -50%;
    left: -50%;
    width: 200%;
    height: 200%;
    background: radial-gradient(circle, var(--glow-color) 0%, transparent 60%);
    opacity: 0.2;
    z-index: 0;
    pointer-events: none;
}

.card-honesty { --glow-color: #3b82f6; border-bottom: 2px solid #3b82f6; } 
.card-safety { --glow-color: #f59e0b; border-bottom: 2px solid #f59e0b; } 
.card-quality { --glow-color: #8b5cf6; border-bottom: 2px solid #8b5cf6; } 
.card-art { --glow-color: #ec4899; border-bottom: 2px solid #ec4899; } 
.card-time { --glow-color: #10b981; border-bottom: 2px solid #10b981; } 

.glass-icon {
    font-size: 2.2rem;
    filter: drop-shadow(0 2px 4px rgba(0,0,0,0.2));
    z-index: 2;
    margin-bottom: 0.2rem;
}

.glass-text {
    font-size: 0.95rem; /* Slightly smaller to fit circle */
    font-weight: 600;
    color: var(--text-color);
    line-height: 1.4;
    z-index: 2;
}

@media (max-width: 600px) {
    .vision-glass-card {
        width: 180px;
        height: 180px;
        padding: 1rem;
    }
    .glass-icon { font-size: 1.8rem; }
    .glass-text { font-size: 0.85rem; }
}
"""

# I need to use re.sub very carefully. The previous CSS block started with /* Asymmetrical Modern "Scattered" Bento Grid */.
# However, I also appended /* Ultra-Premium Glassmorphism */ recently.
# Let's search for the old grid and card CSS from the end of the file.

# Instead of regex, since I appended this code sequentially in previous steps, 
# I can split the CSS file and replace everything after a certain point, or use a more precise regex.
