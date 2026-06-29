import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove Agriculture and Energy Cards
card_ag_regex = r'<!-- Card 3: PSL Agriculture -->.*?</div>\s*</div>'
content = re.sub(card_ag_regex, '', content, flags=re.DOTALL)

card_en_regex = r'<!-- Card 4: PSL Energy -->.*?</div>\s*</div>'
content = re.sub(card_en_regex, '', content, flags=re.DOTALL)

# 2. Remove Agriculture and Energy from Dock
dock_ag_regex = r'<li class="dock-item" data-filter="agriculture" id="dock-agriculture">.*?</li>'
content = re.sub(dock_ag_regex, '', content, flags=re.DOTALL)

dock_en_regex = r'<li class="dock-item" data-filter="energy" id="dock-energy">.*?</li>'
content = re.sub(dock_en_regex, '', content, flags=re.DOTALL)

# 3. Remove from Contact Form Sector Options
form_ag_regex = r'<option value="agriculture".*?</option>'
content = re.sub(form_ag_regex, '', content, flags=re.DOTALL)

form_en_regex = r'<option value="energy".*?</option>'
content = re.sub(form_en_regex, '', content, flags=re.DOTALL)

# 4. Remove timeline events for 2021 (Agriculture) and 2024 (Energy)
time_ag_regex = r'<div class="timeline-step" data-year="2021">.*?</div>\s*</div>'
content = re.sub(time_ag_regex, '', content, flags=re.DOTALL)

time_en_regex = r'<div class="timeline-step" data-year="2024">.*?</div>\s*</div>'
content = re.sub(time_en_regex, '', content, flags=re.DOTALL)

# 5. Add Organization Structure Section before Philosophy Section
org_structure_html = """
        <!-- Organization Structure Section -->
        <section class="org-section" id="organization">
            <div class="org-header">
                <h2 class="section-title" data-en="Organization Structure" data-la="ໂຄງປະກອບການຈັດຕັ້ງ" data-zh="组织结构">Organization Structure</h2>
                <div class="section-divider"></div>
            </div>
            
            <div class="org-tree-container">
                <!-- Top Level: Board / Managing Director -->
                <div class="org-node top-level">
                    <div class="org-card primary-card">
                        <div class="org-icon">
                            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>
                        </div>
                        <h3 data-en="Managing Director" data-la="ຜູ້ອຳນວຍການ" data-zh="总经理">Managing Director</h3>
                        <p data-en="Board of Directors" data-la="ສະພາບໍລິຫານ" data-zh="董事会">Board of Directors</p>
                    </div>
                </div>

                <!-- Second Level: Divisions -->
                <div class="org-level-branches">
                    <div class="org-branch">
                        <div class="org-card secondary-card">
                            <div class="org-icon">
                                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/></svg>
                            </div>
                            <h4 data-en="Administrative & Finance" data-la="ພະແນກບໍລິຫານ ແລະ ການເງິນ" data-zh="行政与财务部">Administrative & Finance</h4>
                        </div>
                    </div>
                    
                    <div class="org-branch">
                        <div class="org-card secondary-card">
                            <div class="org-icon">
                                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 2 7 12 12 22 7 12 2"/><polyline points="2 17 12 22 22 17"/><polyline points="2 12 12 17 22 12"/></svg>
                            </div>
                            <h4 data-en="Engineering & Technical" data-la="ພະແນກວິສະວະກຳ ແລະ ເຕັກນິກ" data-zh="工程与技术部">Engineering & Technical</h4>
                        </div>
                    </div>

                    <div class="org-branch">
                        <div class="org-card secondary-card">
                            <div class="org-icon">
                                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
                            </div>
                            <h4 data-en="Project Management (PMO)" data-la="ຫ້ອງການຄຸ້ມຄອງໂຄງການ" data-zh="项目管理办公室">Project Management (PMO)</h4>
                        </div>
                    </div>

                    <div class="org-branch">
                        <div class="org-card secondary-card">
                            <div class="org-icon">
                                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="16" height="16" x="4" y="4" rx="2" ry="2"/><rect width="6" height="6" x="9" y="9" rx="1" ry="1"/><path d="M9 15v2"/><path d="M9 7v2"/><path d="M15 9h2"/><path d="M7 9h2"/><path d="M15 15h2"/><path d="M7 15h2"/></svg>
                            </div>
                            <h4 data-en="Procurement & Logistics" data-la="ພະແນກຈັດຊື້ ແລະ ໂລຈິດສະຕິກ" data-zh="采购与物流部">Procurement & Logistics</h4>
                        </div>
                    </div>
                </div>
            </div>
        </section>
"""

# Inject before philosophy section
content = content.replace('<!-- Philosophy Section (The Through-Line) -->', org_structure_html + '\n        <!-- Philosophy Section (The Through-Line) -->')

# Update Hero Intro Text (removing agriculture/energy from HTML description fallback if any)
content = content.replace('Spanning across infrastructure, construction, logistics services, sustainable agriculture, and renewable energy.', 'Specializing in major infrastructure, public works, and enterprise logistics services.')


with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("index.html refactored successfully.")
