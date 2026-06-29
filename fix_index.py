import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove the orphaned Agriculture and Energy HTML blocks
orphaned_ag_en_regex = r'<div class="card-details">\s*<div class="card-header-row">\s*<h3 class="card-title">\s*<span class="en-text">PSL Smart Agriculture.*?</div>\s*</div>\s*<div class="card-details">\s*<div class="card-header-row">\s*<h3 class="card-title">\s*<span class="en-text">PSL Energy & Trading.*?</div>\s*</div>'

content = re.sub(orphaned_ag_en_regex, '', content, flags=re.DOTALL)


# 2. Update Hero Meta Section
meta_old = """                <div class="hero-meta">
                    <div class="meta-item">
                        <span class="meta-label" data-en="FIELD" data-la="ຂະແໜງການ" data-zh="领域">FIELD</span>
                        <span class="meta-value" data-en="Conglomerate" data-la="ກຸ່ມທຸລະກິດຮ່ວມ" data-zh="企业集团">Conglomerate</span>
                    </div>
                    <div class="meta-item">
                        <span class="meta-label" data-en="HEADQUARTERS" data-la="ສຳນັກງານໃຫຍ່" data-zh="总部">HEADQUARTERS</span>
                        <span class="meta-value" data-en="Vientiane, Laos" data-la="ວຽງຈັນ, ປະເທດລາວ" data-zh="老挝，万象">Vientiane, Laos</span>
                    </div>
                    <div class="meta-item">
                        <span class="meta-label" data-en="ACTIVE SINCE" data-la="ກໍ່ຕັ້ງແຕ່ປີ" data-zh="成立年份">ACTIVE SINCE</span>
                        <span class="meta-value">2018</span>
                    </div>
                    <div class="meta-item">
                        <span class="meta-label" data-en="STATUS" data-la="ສະຖານະ" data-zh="状态">STATUS</span>
                        <span class="meta-value" data-en="Practicing & Growing" data-la="ກຳລັງເຕີບໃຫຍ່ຂະຫຍາຍຕົວ" data-zh="发展中">Practicing & Growing</span>
                    </div>
                </div>"""

meta_new = """                <div class="hero-meta">
                    <div class="meta-item">
                        <span class="meta-label" data-en="CEO / PRESIDENT" data-la="ປະທານບໍລິສັດ" data-zh="总裁 / 首席执行官">CEO / PRESIDENT</span>
                        <span class="meta-value" data-en="Board of Directors" data-la="ສະພາບໍລິຫານ" data-zh="董事会">Board of Directors</span>
                    </div>
                    <div class="meta-item">
                        <span class="meta-label" data-en="ADDRESS" data-la="ທີ່ຢູ່" data-zh="地址">ADDRESS</span>
                        <span class="meta-value" data-en="Nongtha Tai Village, Chanthabouly District, Vientiane" data-la="ບ້ານໜອງທາໃຕ້, ເມືອງຈັນທະບູລີ, ນະຄອນຫຼວງວຽງຈັນ" data-zh="老挝万象市占塔布里县农塔泰村">Nongtha Tai Village, Chanthabouly District, Vientiane</span>
                    </div>
                    <div class="meta-item">
                        <span class="meta-label" data-en="CONTACT NUMBER" data-la="ເບີໂທລະສັບ" data-zh="联系电话">CONTACT NUMBER</span>
                        <span class="meta-value">+856 20 XX XXX XXX</span>
                    </div>
                    <div class="meta-item">
                        <span class="meta-label" data-en="COMPANY VISION" data-la="ວິໄສທັດຂອງບໍລິສັດ" data-zh="公司愿景">COMPANY VISION</span>
                        <span class="meta-value" data-en="Sustainable Development & Synergy" data-la="ການພັດທະນາແບບຍືນຍົງ ແລະ ການຮ່ວມມື" data-zh="可持续发展与协同">Sustainable Development & Synergy</span>
                    </div>
                </div>"""

content = content.replace(meta_old, meta_new)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("index.html fixed successfully.")
