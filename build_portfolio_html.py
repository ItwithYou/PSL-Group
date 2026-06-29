import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update the About Us Text in index.html (the text under "Our Vision")
# Wait, the user wants the "About" text updated. Let's see how it's structured.
# The original text was hardcoded in HTML or translated via JS.
# Let's just create the massive new Projects HTML section.

new_projects_html = """<div class="tab-content" id="tab-projects">
<section class="portfolio-section" id="projects">
    <div class="portfolio-header">
        <h2 class="section-title" data-en="Corporate Portfolio" data-la="ຜົນງານ ແລະ ໂຄງການ" data-zh="企业项目组合">Corporate Portfolio</h2>
        <div class="section-divider"></div>
        <p class="portfolio-subtitle" data-en="A legacy of excellence with over 5,400 Billion LAK in strategic infrastructure projects." data-la="ຄວາມພາກພູມໃຈໃນຜົນງານການພັດທະນາໂຄງລ່າງພື້ນຖານມູນຄ່າຫຼາຍກວ່າ 5,400 ຕື້ກີບ." data-zh="超过 54,000 亿基普战略基础设施项目的卓越遗产。">A legacy of excellence with over 5,400 Billion LAK in strategic infrastructure projects.</p>
    </div>
    
    <!-- Tier 1: Priority Strategic Projects -->
    <div class="portfolio-tier">
        <div class="tier-header">
            <h3 data-en="Group I: Priority Strategic Projects" data-la="ກຸ່ມທີ I: ໂຄງການຍຸດທະສາດບູລິມະສິດ" data-zh="第一组：优先战略项目">Group I: Priority Strategic Projects</h3>
            <span class="tier-badge">> 5,400 Billion LAK</span>
        </div>
        
        <div class="tier-grid">
            <!-- Defense Projects -->
            <div class="portfolio-card highlight-card">
                <div class="card-glass-bg"></div>
                <div class="card-content">
                    <div class="card-icon">🛡️</div>
                    <h4 data-en="Ministry of Defense Strategic Projects" data-la="ໂຄງການຍຸດທະສາດຂອງ ກະຊວງປ້ອງກັນປະເທດ" data-zh="国防部战略项目">Ministry of Defense Strategic Projects</h4>
                    <p class="card-value">> 3,000 Billion LAK</p>
                    <ul class="card-list">
                        <li data-en="Military Equipment Procurement" data-la="ວຽກງານຈັດຊື້ອຸປະກອນຮັບໃຊ້ກອງທັບ" data-zh="军事装备采购">Military Equipment Procurement</li>
                        <li data-en="Medical & Pharmaceutical Tech Factory" data-la="ໂຮງງານພັດທະນາເຕັກໂນໂລຊີການຢາ-ການແພດ" data-zh="医疗和制药技术工厂">Medical & Pharmaceutical Tech Factory</li>
                        <li data-en="UAV (Drone) Development Factory" data-la="ໂຮງງານພັດທະນາຍານພາຫະນະບໍ່ມີຄົນຂັບ (Drone)" data-zh="无人机开发工厂">UAV (Drone) Development Factory</li>
                        <li data-en="Garment Industry Factory" data-la="ໂຮງງານພັດທະນາອຸດສະຫະກຳຕັດຫຍິບ" data-zh="服装工业工厂">Garment Industry Factory</li>
                        <li data-en="Huaphan Province Infrastructure" data-la="ໂຄງການພັດທະນາພື້ນຖານໂຄງລ່າງແຂວງຫົວພັນ" data-zh="华潘省基础设施">Huaphan Province Infrastructure</li>
                    </ul>
                </div>
            </div>

            <!-- Vientiane 10 Roads -->
            <div class="portfolio-card highlight-card">
                <div class="card-glass-bg"></div>
                <div class="card-content">
                    <div class="card-icon">🛣️</div>
                    <h4 data-en="Vientiane 10 Roads Project" data-la="ໂຄງການກໍ່ສ້າງເສັ້ນທາງ 10 ເສັ້ນ ຢູ່ນະຄອນຫຼວງວຽງຈັນ" data-zh="万象10条道路项目">Vientiane 10 Roads Project</h4>
                    <p class="card-value">> 2,000 Billion LAK</p>
                    <p class="card-desc" data-en="Extensive urban infrastructure improvement project across the capital city. Currently, over 1,000 Billion LAK has been successfully executed." data-la="ໂຄງການປັບປຸງໂຄງລ່າງພື້ນຖານໃນນະຄອນຫຼວງ. ປັດຈຸບັນປະຕິບັດສໍາເລັດແລ້ວປະມານ 1,000 ຕື້ກີບ." data-zh="首都广泛的城市基础设施改善项目。目前已成功执行超过 1 万亿基普。">Extensive urban infrastructure improvement project across the capital city. Currently, over 1,000 Billion LAK has been successfully executed.</p>
                </div>
            </div>

            <!-- Khammouane Riverbank -->
            <div class="portfolio-card highlight-card">
                <div class="card-glass-bg"></div>
                <div class="card-content">
                    <div class="card-icon">🌊</div>
                    <h4 data-en="Khammouane Riverbank Protection" data-la="ໂຄງການກໍ່ສ້າງປ້ອງກັນຕາຝັ່ງເຈື່ອນ ແຂວງຄໍາມ່ວນ" data-zh="甘蒙河岸保护">Khammouane Riverbank Protection</h4>
                    <p class="card-value">~ 2,400 Billion LAK</p>
                    <p class="card-desc" data-en="Construction of a 19-kilometer riverbank protection system spanning the Thakhek district to prevent erosion and secure infrastructure." data-la="ກໍ່ສ້າງປ້ອງກັນຕາຝັ່ງເຈື່ອນລວງຍາວ 19 ກິໂລແມັດ ຢູ່ຂອບເຂດເມືອງທ່າແຂກ." data-zh="在塔克区建设长达 19 公里的河岸保护系统，防止侵蚀并保护基础设施。">Construction of a 19-kilometer riverbank protection system spanning the Thakhek district to prevent erosion and secure infrastructure.</p>
                </div>
            </div>
        </div>
    </div>

    <!-- Tier 2: Highway Infrastructure -->
    <div class="portfolio-tier">
        <div class="tier-header">
            <h3 data-en="Group II: National Highway Projects" data-la="ກຸ່ມທີ II: ໂຄງການປັບປຸງເສັ້ນທາງຫຼວງແຫ່ງຊາດ" data-zh="第二组：国道项目">Group II: National Highway Projects</h3>
            <span class="tier-badge">313.6 km Total Length</span>
        </div>
        <p class="tier-subtitle" data-en="Survey, design, and construction projects under OPBRC and PRTC contracts for the Ministry of Public Works and Transport." data-la="ໂຄງການສຶກສາ, ອອກແບບ ແລະ ກໍ່ສ້າງ ໃນຮູບແບບສັນຍາ OPBRC ແລະ PRTC." data-zh="公共工程和运输部 OPBRC 和 PRTC 合同下的勘测、设计和建设项目。">Survey, design, and construction projects under OPBRC and PRTC contracts for the Ministry of Public Works and Transport.</p>
        
        <div class="highway-list">
            <div class="highway-item">
                <div class="hw-icon">🛣️</div>
                <div class="hw-details">
                    <h4 data-en="Route 13 North" data-la="ທາງເລກ 13 ເໜືອ" data-zh="13号公路北段">Route 13 North</h4>
                    <p data-en="Vang Vieng to Kasi (Luang Prabang Border)" data-la="ແຕ່ ເມືອງວັງວຽງ ຫາ ເມືອງກາສີ (ເຂດແດນແຂວງຫຼວງພະບາງ)" data-zh="万荣至卡西（琅勃拉邦边界）">Vang Vieng to Kasi (Luang Prabang Border)</p>
                </div>
                <div class="hw-length">84 km</div>
            </div>
            
            <div class="highway-item">
                <div class="hw-icon">🛣️</div>
                <div class="hw-details">
                    <h4 data-en="Route 21" data-la="ທາງເລກ 21" data-zh="21号公路">Route 21</h4>
                    <p data-en="Phou Pha Meuang to Tha Sy, Bolikhamxay" data-la="ແຕ່ ຕີນພູຜາເມືອງ ບ້ານໂພນມຸງຄຸນ ຫາ ບ້ານທ່າສີ, ແຂວງບໍລິຄໍາໄຊ" data-zh="富帕蒙至塔西，博利坎赛">Phou Pha Meuang to Tha Sy, Bolikhamxay</p>
                </div>
                <div class="hw-length">56 km</div>
            </div>
            
            <div class="highway-item">
                <div class="hw-icon">🛣️</div>
                <div class="hw-details">
                    <h4 data-en="Route 1D" data-la="ທາງເລກ 1D" data-zh="1D公路">Route 1D</h4>
                    <p data-en="Tha Sy to Xiengkhouang Border" data-la="ແຕ່ ບ້ານທ່າສີ ຫາ ເຂດແດນແຂວງຊຽງຂວາງ" data-zh="塔西至川圹边界">Tha Sy to Xiengkhouang Border</p>
                </div>
                <div class="hw-length">80.6 km</div>
            </div>

            <div class="highway-item">
                <div class="hw-icon">🛣️</div>
                <div class="hw-details">
                    <h4 data-en="Route 1C" data-la="ທາງເລກ 1C" data-zh="1C公路">Route 1C</h4>
                    <p data-en="Kham District Intersection to Phou Lau" data-la="ແຕ່ ສາມແຍກເມືອງຄໍາ ຫາ ພູເລົ້າ" data-zh="坎县路口至普劳">Kham District Intersection to Phou Lau</p>
                </div>
                <div class="hw-length">93 km</div>
            </div>
        </div>
    </div>

    <!-- Tier 3: Past Experience -->
    <div class="portfolio-tier">
        <div class="tier-header">
            <h3 data-en="Group III: Past Experience & Legacy" data-la="ກຸ່ມທີ III: ໂຄງການ ແລະ ຜົນງານໃນອະດີດທີ່ຜ່ານມາ" data-zh="第三组：过去经验与成就">Group III: Past Experience & Legacy</h3>
        </div>
        
        <div class="past-projects-container">
            <!-- Will inject the 13 projects here dynamically or statically -->
            <ul class="past-list">
                <li data-en="Road construction from Route 13 South (Nong Bua Thong) to Mak Hiao (11 km)" data-la="ທາງ ແຕ່ສາມແຍກທາງ 13 ໃຕ້ ບ້ານໜອງບົວທອງ - ບ້ານໝາກຮຽວ (11 ກມ)" data-zh="13号公路南段道路建设 (11 km)">Road construction from Route 13 South (Nong Bua Thong) to Mak Hiao (11 km)</li>
                <li data-en="Reinforced concrete road from Xok Noi intersection to 450 Year Road (3.01 km)" data-la="ທາງເບຕົງເສີມເຫຼັກ ຈາກສີ່ແຍກບ້ານໂຊກນ້ອຍ ຫາ ເຊື່ອມຕໍ່ຖະໜົນ 450 ປີ (3.01 ກມ)" data-zh="Xok Noi至450年大道的钢筋混凝土道路 (3.01 km)">Reinforced concrete road from Xok Noi intersection to 450 Year Road (3.01 km)</li>
                <li data-en="Access road to National Academy of Politics & Public Administration (2.45 km)" data-la="ທາງ ເຂົ້າສະຖາບັນການເມືອງ-ການປົກຄອງແຫ່ງຊາດ (2.45 ກມ)" data-zh="国家政治与公共行政学院通路 (2.45 km)">Access road to National Academy of Politics & Public Administration (2.45 km)</li>
                <li data-en="Concrete road from Na Khuay to Don Nok Khoum (450 Year Road)" data-la="ທາງເບຕົງເສີມເຫຼັກ ຈາກສາມແຍກບ້ານນາຄວາຍ ຫາ ຖະໜົນດອນນົກຂຸ້ມ" data-zh="Na Khuay至Don Nok Khoum的混凝土道路">Concrete road from Na Khuay to Don Nok Khoum (450 Year Road)</li>
                <li data-en="Concrete road from Sala Kham to Savang, Hatsayfong District (4.85 km)" data-la="ທາງເບຕົງເສີມເຫຼັກ ແຕ່ ບ້ານສາລາຄໍາ - ບ້ານສະຫວ່າງ (4.85 ກມ)" data-zh="Sala Kham至Savang混凝土道路 (4.85 km)">Concrete road from Sala Kham to Savang, Hatsayfong District (4.85 km)</li>
                <li data-en="Concrete road from Laos-China Railway to Non Sa-at (8 km)" data-la="ທາງເບຕົງເສີມເຫຼັກ ແຕ່ທາງລົດໄຟລາວຈີນ - ບ້ານໂນນສະອາດ (8 ກມ)" data-zh="老中铁路至Non Sa-at混凝土道路 (8 km)">Concrete road from Laos-China Railway to Non Sa-at (8 km)</li>
                <li data-en="Mekong riverside concrete road from Na Hai to Xayfong (9.38 km)" data-la="ທາງເບຕົງເສີມເຫຼັກ ເສັ້ນທາງແຄມຂອງ ຈາກບ້ານນາໄຮ ຫາ ບ້ານຊາຍຟອງ (9.38 ກມ)" data-zh="湄公河沿岸混凝土道路 (9.38 km)">Mekong riverside concrete road from Na Hai to Xayfong (9.38 km)</li>
                <li data-en="Concrete road from Na Tong to Sop Dung (Laos-Vietnam Border) (21.25 km)" data-la="ທາງເບຕົງເສີມເຫຼັກ ຈາກບ້ານນາຕອງ ຫາ ຊາຍແດນລາວ-ຫວຽດນາມ (21.25 ກມ)" data-zh="通往老越边境的混凝土道路 (21.25 km)">Concrete road from Na Tong to Sop Dung (Laos-Vietnam Border) (21.25 km)</li>
                <li data-en="Double-layer asphalt road in Xiengkhor municipality (12.5 km)" data-la="ທາງປູຢາງ 2 ຊັ້ນ ພາຍໃນເທດສະບານເມືອງຊຽງຄໍ້ (12.5 ກມ)" data-zh="香科市双层沥青道路 (12.5 km)">Double-layer asphalt road in Xiengkhor municipality (12.5 km)</li>
                <li data-en="Reinforced concrete bridge over Ma River, Xiengkhor (200m)" data-la="ຂົວເບຕົງເສີມເຫຼັກ ຂ້າມນໍ້າມ່າ ເມືອງຊຽງຄໍ້ (200 ແມັດ)" data-zh="跨马河钢筋混凝土桥 (200m)">Reinforced concrete bridge over Ma River, Xiengkhor (200m)</li>
                <li data-en="Construction and improvement of Plain of Jars Airport, Xiengkhouang (Ministry of Defense)" data-la="ໂຄງການກໍ່ສ້າງ ແລະ ປັບປຸງສະໜາມບິນທົ່ງໄຫຫີນ (ກະຊວງປ້ອງກັນປະເທດ)" data-zh="川圹平原机场建设与改善">Construction and improvement of Plain of Jars Airport, Xiengkhouang (Ministry of Defense)</li>
                <li data-en="Pharmaceutical and Medical Equipment Factory, Naxaithong" data-la="ໂຮງງານຜະລິດຢາ ແລະ ອຸປະກອນການແພດ ກະຊວງປ້ອງກັນປະເທດ" data-zh="制药与医疗设备工厂">Pharmaceutical and Medical Equipment Factory, Naxaithong</li>
                <li data-en="Garment Factory, Offices and Accommodation, Non Sa-at" data-la="ໂຮງງານຕັດຫຍິບ, ຫ້ອງການ ແລະ ທີ່ພັກ, ບ້ານໂນນສະອາດ" data-zh="服装厂及办公住宿设施">Garment Factory, Offices and Accommodation, Non Sa-at</li>
            </ul>
        </div>
    </div>
</section>
</div>"""

pattern = r'<div class="tab-content"\s+id="tab-projects">.*?<div class="tab-content"\s+id="tab-activity">'
new_html = re.sub(pattern, new_projects_html + '\n\n        <!-- TAB: ACTIVITY -->\n        <div class="tab-content" id="tab-activity">', html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Updated Projects section in index.html!")
