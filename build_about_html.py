import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# We will completely replace <div class="tab-content" id="tab-about"> ... </div>
new_tab_about = """<!-- TAB: ABOUT US -->
        <div class="tab-content" id="tab-about">
        
        <section class="roadmap-section" id="timeline">
            <div class="roadmap-header">
                <h2 class="section-title" data-en="Corporate Roadmap" data-la="ແຜນຜັງພັດທະນາອົງກອນ" data-zh="企业发展路线图">Corporate Roadmap</h2>
                <div class="section-divider"></div>
            </div>

            <!-- Hand-drawn style Roadmap -->
            <div class="roadmap-path-container">
                <div class="roadmap-stop left-stop">
                    <div class="roadmap-point"></div>
                    <div class="roadmap-card">
                        <span class="roadmap-year">2015</span>
                        <h4 data-en="Establishment & Foundations" data-la="ກໍ່ຕັ້ງກຸ່ມບໍລິສັດ" data-zh="成立与基础">Establishment & Foundations</h4>
                        <p data-en="Founded PSL Group with PSL Construction. Secured major infrastructure projects in Central Laos." data-la="ກໍ່ຕັ້ງກຸ່ມບໍລິສັດ PSL ໂດຍເລີ່ມຈາກທຸລະກິດກໍ່ສ້າງ ແລະ ໄດ້ຮັບໂຄງການພັດທະນາໂຄງລ່າງພື້ນຖານຂະໜາດໃຫຍ່." data-zh="与 PSL 建筑一起成立了 PSL 集团。在老挝中部获得了主要的基础设施项目。"></p>
                    </div>
                </div>

                <div class="roadmap-stop right-stop">
                    <div class="roadmap-point"></div>
                    <div class="roadmap-card">
                        <span class="roadmap-year">2018</span>
                        <h4 data-en="Expansion into Logistics" data-la="ຂະຫຍາຍສູ່ການບໍລິການໂລຈິດສະຕິກ" data-zh="扩展到物流">Expansion into Logistics</h4>
                        <p data-en="Launched PSL Service, establishing cold chain warehouses and cross-border transport corridors." data-la="ເປີດຕົວ ບໍລິສັດ ບໍລິການ PSL ເພື່ອສ້າງສາງເກັບຮັກສາຄວາມເຢັນ ແລະ ເສັ້ນທາງການຂົນສົ່ງສິນຄ້າຂ້າມແດນ." data-zh="推出了 PSL 服务，建立冷链仓库和跨境运输走廊。"></p>
                    </div>
                </div>

                <div class="roadmap-stop left-stop">
                    <div class="roadmap-point"></div>
                    <div class="roadmap-card">
                        <span class="roadmap-year">2026</span>
                        <h4 data-en="Strategic Integration" data-la="ການເຊື່ອມໂຍງຍຸດທະສາດ" data-zh="战略整合">Strategic Integration</h4>
                        <p data-en="Unified all subsidiaries under the modern PSL Group management system, advancing eco-friendly development." data-la="ຮວມທຸກບໍລິສັດໃນເຄືອພາຍໃຕ້ລະບົບການບໍລິຫານຈັດການແບບໃໝ່ ເພື່ອມຸ່ງເນັ້ນການພັດທະນາທີ່ເປັນມິດຕໍ່ສິ່ງແວດລ້ອມ." data-zh="在现代 PSL 集团管理系统下统一下属所有子公司，推进环保发展。"></p>
                    </div>
                </div>
            </div>
        </section>

        <section class="org-section" id="organization">
            <div class="org-header">
                <h2 class="section-title" data-en="Organization Structure" data-la="ໂຄງປະກອບການຈັດຕັ້ງ" data-zh="组织结构">Organization Structure</h2>
                <div class="section-divider"></div>
            </div>
            
            <div class="org-tree-wrapper">
                
                <!-- Level 1: President -->
                <div class="tree-level level-1">
                    <div class="tree-node president-node">
                        <h4 data-en="President" data-la="ປະທານ ບໍລິສັດ" data-zh="总裁">President</h4>
                        <p data-en="Mrs. Thepphalak Khavisorn" data-la="ທ່ານ ນາງ ເທບພະລັກ ຄາວີສອນ" data-zh="Thepphalak Khavisorn 女士">Mrs. Thepphalak Khavisorn</p>
                    </div>
                </div>
                
                <div class="tree-line vertical"></div>

                <!-- Level 2: Advisor & VP -->
                <div class="tree-level level-2">
                    <div class="tree-branch-horizontal wide"></div>
                    <div class="tree-nodes-row">
                        <div class="tree-node advisor-node">
                            <h4 data-en="Advisor" data-la="ທີ່ປຶກສາ ບໍລິສັດ" data-zh="顾问">Advisor</h4>
                            <p data-en="Mr. Viengsavath" data-la="ທ່ານ ວຽງສະຫວັດ" data-zh="Viengsavath 先生">Mr. Viengsavath</p>
                        </div>
                        <div class="tree-line vertical center-passthrough"></div>
                        <div class="tree-node vp-node">
                            <h4 data-en="Vice President" data-la="ຮອງປະທານ ບໍລິສັດ" data-zh="副总裁">Vice President</h4>
                            <p data-en="Mrs. Sudaman Phengdala" data-la="ທ່ານ ນາງ ສຸດາມັນ ແພງດາລາ" data-zh="Sudaman Phengdala 女士">Mrs. Sudaman Phengdala</p>
                        </div>
                    </div>
                </div>

                <div class="tree-line vertical"></div>

                <!-- Level 3: Engineering Manager -->
                <div class="tree-level level-3">
                    <div class="tree-node manager-node">
                        <h4 data-en="Engineering Manager" data-la="ຜູ້ຈັດການຝ່າຍວິສະວະກຳ" data-zh="工程经理">Engineering Manager</h4>
                        <p data-en="Mr. Bounpheng Souliyaong" data-la="ທ່ານ ບຸນເພັງ ສຸລິຍະວົງ" data-zh="Bounpheng Souliyaong 先生">Mr. Bounpheng Souliyaong</p>
                    </div>
                </div>

                <div class="tree-line vertical"></div>

                <!-- Level 4: Project Manager -->
                <div class="tree-level level-4">
                    <div class="tree-node manager-node">
                        <h4 data-en="Project Manager" data-la="ຜູ້ຈັດການ ໂຄງການ" data-zh="项目经理">Project Manager</h4>
                        <p data-en="Mr. Kornvilay Sihanath" data-la="ທ່ານ ກ້ອນວິໄລ ສີຫານາດ" data-zh="Kornvilay Sihanath 先生">Mr. Kornvilay Sihanath</p>
                    </div>
                </div>

                <div class="tree-line vertical"></div>

                <!-- Level 5: 5 Units -->
                <div class="tree-level level-5">
                    <div class="tree-branch-horizontal super-wide"></div>
                    <div class="tree-nodes-row five-cols">
                        
                        <div class="tree-node unit-node">
                            <h4 data-en="Environment & Safety Unit" data-la="ໜ່ວຍງານ ສິ່ງແວດລ້ອມ ແລະ ຄວາມປອດໄພ" data-zh="环境与安全组">Environment & Safety Unit</h4>
                        </div>
                        
                        <div class="tree-node unit-node">
                            <h4 data-en="Construction Engineering Unit" data-la="ໜ່ວຍງານ ວິສະວະກຳກໍ່ສ້າງ" data-zh="建筑工程组">Construction Engineering Unit</h4>
                        </div>
                        
                        <div class="tree-node unit-node">
                            <h4 data-en="Inspection & Repair Unit" data-la="ໜ່ວຍງານ ກວດກາ ແລະ ສ້ອມແປງ" data-zh="检查与维修组">Inspection & Repair Unit</h4>
                        </div>
                        
                        <div class="tree-node unit-node">
                            <h4 data-en="Admin & HR Unit" data-la="ໜ່ວຍງານ ບໍລິຫານ ແລະ ບຸກຄະລາກອນ" data-zh="行政与人力资源组">Admin & HR Unit</h4>
                        </div>
                        
                        <div class="tree-node unit-node">
                            <h4 data-en="Procurement & Finance Unit" data-la="ໜ່ວຍງານ ຈັດຊື້ ແລະ ບັນຊີ-ການເງິນ" data-zh="采购与财务组">Procurement & Finance Unit</h4>
                        </div>

                    </div>
                </div>

            </div>
        </section>
        </div>"""

# Replace the old tab-about block
pattern = r'<!-- TAB: ABOUT US -->.*?<div class="tab-content" id="tab-projects">'
html = re.sub(pattern, new_tab_about + '\n\n        <!-- TAB: PROJECTS -->\n        <div class="tab-content" id="tab-projects">', html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("HTML structure updated for Roadmap and Org Chart!")
