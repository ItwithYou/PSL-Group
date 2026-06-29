import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

new_org_html = """        <section class="org-section" id="organization">
            <div class="org-header">
                <h2 class="section-title" data-en="Organization Structure" data-la="ໂຄງປະກອບການຈັດຕັ້ງ" data-zh="组织结构">Organization Structure</h2>
                <div class="section-divider"></div>
            </div>
            
            <div class="org-template-wrapper">
                
                <!-- Central Top Chain -->
                <div class="org-center-chain">
                    <div class="org-capsule solid-gold">
                        <h4 data-en="President" data-la="ປະທານ ບໍລິສັດ" data-zh="总裁">President</h4>
                        <p data-en="Mrs. Thepphalak Khavisorn" data-la="ທ່ານ ນາງ ເທບພະລັກ ຄາວີສອນ" data-zh="Thepphalak Khavisorn 女士">Mrs. Thepphalak Khavisorn</p>
                    </div>
                    
                    <div class="org-v-line center"></div>
                    
                    <div class="org-capsule outline-gold">
                        <h4 data-en="Vice President" data-la="ຮອງປະທານ ບໍລິສັດ" data-zh="副总裁">Vice President</h4>
                        <p data-en="Mrs. Sudaman Phengdala" data-la="ທ່ານ ນາງ ສຸດາມັນ ແພງດາລາ" data-zh="Sudaman Phengdala 女士">Mrs. Sudaman Phengdala</p>
                    </div>
                    
                    <div class="org-v-line center"></div>
                </div>

                <!-- Horizontal Split -->
                <div class="org-h-split"></div>
                
                <!-- 3 Columns -->
                <div class="org-columns-container">
                    
                    <!-- Column 1: Advisor (Staff) -->
                    <div class="org-column">
                        <div class="org-v-line center short"></div>
                        <div class="org-capsule outline-gold column-header">
                            <h4 data-en="Advisor" data-la="ທີ່ປຶກສາ ບໍລິສັດ" data-zh="顾问">Advisor</h4>
                            <p data-en="Mr. Viengsavath" data-la="ທ່ານ ວຽງສະຫວັດ" data-zh="Viengsavath 先生">Mr. Viengsavath</p>
                        </div>
                    </div>

                    <!-- Column 2: Engineering -->
                    <div class="org-column">
                        <div class="org-v-line center short"></div>
                        <div class="org-capsule outline-gold column-header">
                            <h4 data-en="Engineering Manager" data-la="ຜູ້ຈັດການຝ່າຍວິສະວະກຳ" data-zh="工程经理">Engineering Manager</h4>
                            <p data-en="Mr. Bounpheng Souliyaong" data-la="ທ່ານ ບຸນເພັງ ສຸລິຍະວົງ" data-zh="Bounpheng Souliyaong 先生">Mr. Bounpheng Souliyaong</p>
                        </div>
                        
                        <!-- Vertical Left-Aligned List -->
                        <div class="org-left-tree">
                            <div class="org-left-line"></div>
                            
                            <div class="org-list-item">
                                <div class="org-h-connector"></div>
                                <div class="org-card-modern">
                                    <h4 data-en="Construction Engineering" data-la="ໜ່ວຍງານ ວິສະວະກຳກໍ່ສ້າງ" data-zh="建筑工程组">Construction Engineering</h4>
                                </div>
                            </div>
                            
                            <div class="org-list-item">
                                <div class="org-h-connector"></div>
                                <div class="org-card-modern">
                                    <h4 data-en="Inspection & Repair" data-la="ໜ່ວຍງານ ກວດກາ ແລະ ສ້ອມແປງ" data-zh="检查与维修组">Inspection & Repair</h4>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- Column 3: Project & Admin -->
                    <div class="org-column">
                        <div class="org-v-line center short"></div>
                        <div class="org-capsule outline-gold column-header">
                            <h4 data-en="Project Manager" data-la="ຜູ້ຈັດການ ໂຄງການ" data-zh="项目经理">Project Manager</h4>
                            <p data-en="Mr. Kornvilay Sihanath" data-la="ທ່ານ ກ້ອນວິໄລ ສີຫານາດ" data-zh="Kornvilay Sihanath 先生">Mr. Kornvilay Sihanath</p>
                        </div>
                        
                        <!-- Vertical Left-Aligned List -->
                        <div class="org-left-tree">
                            <div class="org-left-line"></div>
                            
                            <div class="org-list-item">
                                <div class="org-h-connector"></div>
                                <div class="org-card-modern">
                                    <h4 data-en="Environment & Safety" data-la="ໜ່ວຍງານ ສິ່ງແວດລ້ອມ ແລະ ຄວາມປອດໄພ" data-zh="环境与安全组">Environment & Safety</h4>
                                </div>
                            </div>
                            
                            <div class="org-list-item">
                                <div class="org-h-connector"></div>
                                <div class="org-card-modern">
                                    <h4 data-en="Admin & HR" data-la="ໜ່ວຍງານ ບໍລິຫານ ແລະ ບຸກຄະລາກອນ" data-zh="行政与人力资源组">Admin & HR</h4>
                                </div>
                            </div>
                            
                            <div class="org-list-item">
                                <div class="org-h-connector"></div>
                                <div class="org-card-modern">
                                    <h4 data-en="Procurement & Finance" data-la="ໜ່ວຍງານ ຈັດຊື້ ແລະ ບັນຊີ-ການເງິນ" data-zh="采购与财务组">Procurement & Finance</h4>
                                </div>
                            </div>
                        </div>
                    </div>

                </div>
            </div>
        </section>"""

pattern = r'<section class="org-section" id="organization">.*?</section>'
html = re.sub(pattern, new_org_html, html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("HTML updated for template org chart")
