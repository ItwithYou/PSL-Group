// JavaScript Logic for PSL Group Corporate Website

// Global State
let currentLang = localStorage.getItem('psl_lang') || 'la';
let currentTheme = localStorage.getItem('psl_theme') || 'light';

// Translations Database
const translations = {
    heroDesc: {
        en: "PSL Group is a 100% Lao-owned company founded in 2018. Restructured in 2025 with a registered capital of 50 Billion LAK, we specialize in major infrastructure development, government defense procurement, and advanced technological innovation.",
        la: "ບໍລິສັດ ພີເອັດສແອວ ກໍ່ສ້າງຄົບວົງຈອນ ຈຳກັດຜູ້ດຽວ (PSL) ແມ່ນບໍລິສັດຂອງຄົນລາວ 100% ທີ່ສ້າງຕັ້ງຂຶ້ນໃນປີ 2018 ແລະ ໄດ້ປ່ຽນແປງໂຄງຮ່າງໃນປີ 2025 ເປັນ ກຸ່ມບໍລິສັດ PSL Group ດ້ວຍທຶນຈົດທະບຽນ 50 ຕື້ກີບ. ພວກເຮົາມີຄວາມຊ່ຽວຊານໃນການພັດທະນາໂຄງລ່າງພື້ນຖານ, ການຈັດຊື້-ຈັດຈ້າງໃຫ້ພາກລັດ, ແລະ ການພັດທະນາເຕັກໂນໂລຊີອັນທັນສະໄໝ.",
        zh: "PSL集团是一家成立于2018年的100%老挝全资公司。我们在2025年进行了重组，注册资本为500亿基普。我们专注于重大基础设施开发、政府国防采购以及先进技术创新。"
    },
            visionText: {
            en: "We have a vision to develop the company into a comprehensive construction conglomerate through cooperation with domestic and international companies. By utilizing advanced construction technologies, we aim to achieve outstanding success, build confidence and trust with project owners, and create maximum satisfaction to meet customer needs with excellent quality and impressive services under 5 key factors:",
            la: "ພວກເຮົາມີວິໄສທັດທີ່ຈະພັດທະນາບໍລິສັດ ໃຫ້ເປັນກຸ່ມບໍລິສັດກໍ່ສ້າງຄົບວົງຈອນ ໂດຍການຮ່ວມມືກັບບັນດາບໍລິສັດພາຍໃນ ແລະ ບໍລິສັດຕ່າງປະເທດ ເພື່ອນຳໃຊ້ເຕັກໂນໂລຊີກໍ່ສ້າງຕ່າງໆ ໃຫ້ມີຜົນສຳເລັດທີ່ໂດດເດັ່ນ, ສ້າງຄວາມເຊື່ອໝັ້ນ ແລະ ໄວ້ວາງໃຈ ຂອງເຈົ້າຂອງໂຄງການ ແລະ ສ້າງຄວາມເພິ່ງພໍໃຈ ເພື່ອຕອບສະໜອງຄວາມຕ້ອງການຂອງລູກຄ້າດ້ວຍຄຸນນະພາບທີ່ດີເລີດ ແລະ ການບໍລິການທີ່ປະທັບໃຈ ພາຍໃຕ້ການປະຕິບັດ 5 ປັດໃຈສຳຄັນ ຄື:",
            zh: "我们的愿景是通过与国内外公司合作，将公司发展成为一家综合性建筑企业集团。利用先进的建筑技术，我们旨在取得卓越的成就，建立项目业主的信心和信任，并以卓越的质量和令人印象深刻的服务创造最大的满意度，以满足客户的需求。我们的行动基于5个关键因素："
        },
                visionList: {
            en: `<div class="vision-glass-grid">
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
</div>`,
            la: `<div class="vision-glass-grid">
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
</div>`,
            zh: `<div class="vision-glass-grid">
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
</div>`
        },

    
    projects: {
        construction: {
            title: { en: "PSL Construction Complete Sole Co., Ltd.", la: "ບໍລິສັດ ກໍ່ສ້າງຄົບວົງຈອນ ພີເອັສແອລ ຈຳກັດຜູ້ດຽວ", zh: "PSL 建筑独资有限公司" },
            tag: { en: "Construction & Infrastructure", la: "ການກໍ່ສ້າງ & ໂຄງລ່າງພື້ນຖານ", zh: "建筑与基础设施" },
            stats: {
                en: [
                    { label: "Sector", value: "Infrastructure Development" },
                    { label: "Completed Projects", value: "45+ Major Sites" },
                    { label: "Focus Areas", value: "Highways, Bridges, Commercial Properties" }
                ],
                la: [
                    { label: "ຂະແໜງການ", value: "ການພັດທະນາໂຄງລ່າງພື້ນຖານ" },
                    { label: "ໂຄງການທີ່ສຳເລັດ", value: "45+ ໂຄງການໃຫຍ່" },
                    { label: "ວຽກງານຫຼັກ", value: "ທາງດ່ວນ, ຂົວ, ອາຄານການຄ້າ" }
                ],
                zh: [
                    { label: "领域", value: "基础设施开发" },
                    { label: "已完成项目", value: "45+ 大型项目" },
                    { label: "重点领域", value: "高速公路、桥梁、商业地产" }
                ]
            },
            desc: {
                en: `<p>PSL Construction is the cornerstone division of PSL Group. Over the past decade, we have successfully delivered high-quality public and private sector projects across Laos. From regional highway networks to modern office towers, we maintain the highest standards of safety, durability, and eco-friendly design.</p>
                     <h4>Branches</h4>
                     <p>• <strong>Headquarters:</strong> Lane Xang Avenue, Hatsady, Chanthabouly, Vientiane<br>
                     • <strong>Southern Branch:</strong> Pakse, Champasak Province</p>
                     <h4>Key Projects</h4>
                     <ul>
                        <li><strong>Ministry of Defense Strategic Projects:</strong> Unmanned vehicle factory, medical technology factory, and specialized facilities in Vientiane & Houaphanh.</li>
                        <li><strong>National Highway Development:</strong> 313.6 km of road study, design, and construction, including Route 13 North, Route 21, 1D, and 1C.</li>
                        <li><strong>Vientiane Road Infrastructure:</strong> Construction and improvement of 10 major road networks within Vientiane Capital.</li>
                        <li><strong>Khammouane Riverbank Protection:</strong> 19 km of strategic riverbank erosion protection in Khammouane Province.</li>
                     </ul>`,
                la: `<p>ບໍລິສັດ ກໍ່ສ້າງ PSL ແມ່ນຮາກຖານຫຼັກຂອງກຸ່ມບໍລິສັດ PSL. ໃນທົດສະວັດທີ່ຜ່ານມາ, ພວກເຮົາໄດ້ຈັດຕັ້ງປະຕິບັດໂຄງການພາກລັດ ແລະ ເອກະຊົນທີ່ມີຄຸນນະພາບສູງໃນທົ່ວປະເທດລາວ. ເລີ່ມຈາກຕາໜ່າງທາງດ່ວນລະດັບພາກພື້ນ ຈົນເຖິງຕຶກອາຄານສໍານັກງານທີ່ທັນສະໄໝ, ພວກເຮົາຍຶດໝັ້ນໃນມາດຕະຖານຄວາມປອດໄພ, 精度 ແລະ ການອອກແບບທີ່ເປັນມິດຕໍ່ສິ່ງແວດລ້ອມ.</p>
                     <h4>ສາຂາ</h4>
                     <p>• <strong>ສຳນັກງານໃຫຍ່:</strong> ຖະໜົນລ້ານຊ້າງ, ບ້ານຫັດສະດີ, ເມືອງຈັນທະບູລີ, ນະຄອນຫຼວງວຽງຈັນ<br>
                     • <strong>ສາຂາພາກໃຕ້:</strong> ປາກເຊ, ແຂວງຈຳປາສັກ</p>
                     <h4>ໂຄງການທີ່ໂດດເດັ່ນ</h4>
                     <ul>
                        <li><strong>ໂຄງການຍຸດທະສາດບູລິມະສິດ ກະຊວງປ້ອງກັນປະເທດ:</strong> ໂຮງງານພັດທະນາເຕັກໂນໂລຊີການຢາ-ການແພດ, ໂຮງງານພັດທະນາຍານພາຫະນະບໍ່ມີຄົນຂັບ ຢູ່ນະຄອນຫຼວງວຽງຈັນ ແລະ ແຂວງຫົວພັນ.</li>
                        <li><strong>ໂຄງການພັດທະນາເສັ້ນທາງແຫ່ງຊາດ:</strong> ສຶກສາ, ອອກແບບ ແລະ ກໍ່ສ້າງເສັ້ນທາງ ລວມຄວາມຍາວ 313.6 ກິໂລແມັດ (ທາງເລກ 13 ເໜືອ, 21, 1D, 1C).</li>
                        <li><strong>ໂຄງການກໍ່ສ້າງເສັ້ນທາງນະຄອນຫຼວງວຽງຈັນ:</strong> ໂຄງການກໍ່ສ້າງໂຄງລ່າງເສັ້ນທາງ ຈຳນວນ 10 ເສັ້ນ ຂອງນະຄອນຫຼວງວຽງຈັນ.</li>
                        <li><strong>ໂຄງການປ້ອງກັນຕະຝັ່ງເຈື່ອນ ແຂວງຄຳມ່ວນ:</strong> ໂຄງການກໍ່ສ້າງປ້ອງກັນຕະຝັ່ງເຈື່ອນ ລວງຍາວ 19 ກິໂລແມັດ.</li>
                     </ul>`,
                zh: `<p>PSL 建筑是 PSL 集团的基石部门。在过去的十年里，我们成功在老挝各地交付了高质量的公共和私营部门项目。从区域高速公路网络到现代办公大楼，我们保持最高标准的安全性、耐用性和环保设计。</p><h4>分支机构</h4><p>• <strong>总部:</strong> 老挝万象市占塔布里县农塔泰村<br>• <strong>南部支部:</strong> 占巴塞省巴色市</p><h4>关键项目</h4><ul><li><strong>国防部战略项目:</strong> 位于万象和华潘省的无人驾驶车辆工厂、医疗技术工厂及专用设备设施。</li><li><strong>国家公路开发:</strong> 313.6 公里的道路研究、设计和施工，包括 13 号公路北段、21、1D 和 1C 号公路。</li><li><strong>万象道路基础设施:</strong> 万象市 10 条主要道路网络的建设与改善。</li><li><strong>甘蒙省河岸防护:</strong> 位于甘蒙省的 19 公里战略性河岸防侵蚀工程。</li></ul>`
            }
        },
        service: {
            title: { en: "PSL Service & Logistics", la: "ບໍລິສັດ ບໍລິການ ແລະ ໂລຈິດສະຕິກ PSL", zh: "PSL 服务与物流" },
            tag: { en: "Logistics & Enterprise Services", la: "ໂລຈິດສະຕິກ & ການບໍລິການວິສາຫະກິດ", zh: "物流与企业服务" },
            stats: {
                en: [
                    { label: "Sector", value: "Logistics & Facility Operations" },
                    { label: "Warehouses", value: "6 Regional Centers" },
                    { label: "Delivery Accuracy", value: "99.8% On-Time rate" }
                ],
                la: [
                    { label: "ຂະແໜງການ", value: "ໂລຈິດສະຕິກ & ການຄຸ້ມຄອງອາຄານ" },
                    { label: "ສາງສິນຄ້າ", value: "6 ສູນໃຫຍ່ໃນພາກພື້ນ" },
                    { label: "ຄວາມຖືກຕ້ອງໃນການສົ່ງ", value: "ກົງເວລາ 99.8%" }
                ],
                zh: [
                    { label: "领域", value: "物流与设施运营" },
                    { label: "仓库", value: "6个区域中心" },
                    { label: "交货准确率", value: "准时率 99.8%" }
                ]
            },
            desc: {
                en: `<p>PSL Service specializes in cold chain supply management, domestic distribution, and warehousing services. With our state-of-the-art cold-storage facilities, we support local agricultural exports and general commodity distribution, connecting Laos to ASEAN markets.</p>
                     <h4>Branches</h4>
                     <p>• <strong>Logistics Hub:</strong> Thanaleng Dry Port, Vientiane<br>
                     • <strong>Southern Branch:</strong> Pakse logistics center, Champasak</p>
                     <h4>Key Projects</h4>
                     <ul>
                        <li><strong>Vientiane Cold Storage Park:</strong> 5,000 sqm temperature-controlled facility for agricultural export products.</li>
                        <li><strong>Cross-Border Trucking Network:</strong> Daily scheduled freight cargo routes connecting Laos, Thailand, and Vietnam.</li>
                        <li><strong>Industrial Park Facilities Management:</strong> Full operations, security, and facilities support for Vientiane SEZ.</li>
                     </ul>`,
                la: `<p>ບໍລິສັດ ບໍລິການ PSL ມີຄວາມຊ່ຽວຊານໃນການຄຸ້ມຄອງລະບົບໂສ້ຄວາມເຢັນ, ການກະຈາຍສິນຄ້າພາຍໃນປະទេດ ແລະ ການບໍລິການສາງສິນຄ້າ. ດ້ວຍລະບົບສາງເກັບຮັກສາຄວາມເຢັນທີ່ທັນສະໄໝ, ພວກເຮົາໄດ້ສະໜັບສະໜູນການສົ່ງອອກຜະລິດຕະພັນກະສິກຳ ແລະ ການແຈກຢາຍສິນຄ້າທົ່ວໄປ, ເຄືອຂ່າຍການບໍລິການຂອງພວກເຮົາເຊື່ອມຕໍ່ປະເທດລາວເຂົ້າສູ່ຕະຫຼາດອາຊຽນ.</p>
                     <h4>ສາຂາ</h4>
                     <p>• <strong>ສູນບໍລິການໂລຈິດສະຕິກ:</strong> ທ່າບົກທ່ານາແລ້ງ, ນະຄອນຫຼວງວຽງຈັນ<br>
                     • <strong>ສາຂາພາກໃຕ້:</strong> ສູນກະຈາຍສິນຄ້າປາກເຊ, ແຂວງຈຳປາສັກ</p>
                     <h4>ໂຄງການທີ່ໂດດເດັ່ນ</h4>
                     <ul>
                        <li><strong>ສູນສາງເກັບຮັກສາຄວາມເຢັນ ວຽງຈັນ:</strong> ສູນເກັບສິນຄ້າຄວບຄຸມອຸນຫະພູມ ຂະໜາດ 5,000 ຕາແມັດ ສຳລັບຜະລິດຕະພັນກະສິກຳສົ່ງອອກ.</li>
                        <li><strong>ເຄືອຂ່າຍຂົນສົ່ງສິນຄ້າຂ້າມແດນ:</strong> ເສັ້ນທາງຂົນສົ່ງສິນຄ້າປະຈຳວັນ ເຊື່ອມຕໍ່ ລາວ, ໄທ ແລະ ຫວຽດນາມ.</li>
                        <li><strong>ການຄຸ້ມຄອງອາຄານເຂດອຸດສາຫະກຳ:</strong> ລະບົບປ້ອງກັນຄວາມປອດໄພ ແລະ ບໍລິການອາຄານໃນເຂດເສດຖະກິດພິເສດວຽງຈັນ.</li>
                     </ul>`,
                zh: `<p>PSL 服务专注于冷链供应管理、国内分销和仓储服务。凭借最先进的冷库设施，我们支持当地农产品出口和一般商品分销，将老挝与东盟市场连接起来。</p><h4>分支机构</h4><p>• <strong>物流中心:</strong> 万象塔纳楞陆港<br>• <strong>南部支部:</strong> 占巴塞巴色物流中心</p><h4>关键项目</h4><ul><li><strong>万象冷链仓储园:</strong> 用于农产品出口的 5,000 平方米温控设施。</li><li><strong>跨境卡车网络:</strong> 连接老挝、泰国和越南的每日定期货运路线。</li><li><strong>工业园设施管理:</strong> 为万象经济特区提供全面的运营、安全和设施支持。</li></ul>`
            }
        }
    }
};

// Document Load Event
document.addEventListener("DOMContentLoaded", () => {
    initTheme();
    initLanguage();
    initFilter();
    initModals();
    initScrollAnimations();
    fetchAndRenderActivities();
});

// Theme Setup
function initTheme() {
    const themeBtn = document.getElementById('theme-btn');
    document.documentElement.setAttribute('data-theme', currentTheme);

    themeBtn.addEventListener('click', () => {
        if (currentTheme === 'light') {
            currentTheme = 'dark';
        } else if (currentTheme === 'dark') {
            currentTheme = 'tiffany';
        } else {
            currentTheme = 'light';
        }
        document.documentElement.setAttribute('data-theme', currentTheme);
        localStorage.setItem('psl_theme', currentTheme);
    });
}

// Language Setup
function initLanguage() {
    const langToggleBtn = document.getElementById('lang-toggle-btn');
    updateLanguageUI();

    if (langToggleBtn) {
        langToggleBtn.addEventListener('click', (e) => {
            const targetOption = e.target.closest('.lang-btn-option');
            if (targetOption) {
                const selectedLang = targetOption.getAttribute('data-lang');
                if (selectedLang !== currentLang) {
                    currentLang = selectedLang;
                    localStorage.setItem('psl_lang', currentLang);
                    updateLanguageUI();
                }
            }
        });
    }
}

function updateLanguageUI() {
    // Set HTML lang attribute
    document.documentElement.setAttribute('lang', currentLang);
    
    // Set Document Title
    if (currentLang === 'en') {
        document.title = "PSL Group · Premium Diversified Enterprise";
    } else if (currentLang === 'zh') {
        document.title = "PSL 集团 · 优质多元化企业";
    } else {
        document.title = "ກຸ່ມບໍລິສັດ PSL · ວິສາຫະກິດລວມສູນຊັ້ນນຳ";
    }

        // Update dynamic fields from JavaScript database
    const heroDesc = document.getElementById('hero-desc');
    if (heroDesc) heroDesc.textContent = translations.heroDesc[currentLang];

    const visText = document.getElementById('vision-text');
    if (visText) visText.textContent = translations.visionText[currentLang];

    const visList = document.getElementById('vision-list');
    if (visList) visList.innerHTML = translations.visionList[currentLang];

    // Update data attribute translations
    document.querySelectorAll('[data-en][data-la]').forEach(el => {
        if (currentLang === 'en') {
            el.innerHTML = el.getAttribute('data-en');
        } else if (currentLang === 'zh' && el.hasAttribute('data-zh')) {
            el.innerHTML = el.getAttribute('data-zh');
        } else {
            el.innerHTML = el.getAttribute('data-la');
        }
    });

    // Update form placeholders
    const nameInput = document.getElementById('name');
    const emailInput = document.getElementById('email');
    const msgInput = document.getElementById('message');
    if (nameInput && emailInput && msgInput) {
        if (currentLang === 'en') {
            nameInput.placeholder = "e.g. Somphone";
            emailInput.placeholder = "e.g. somphone@email.com";
            msgInput.placeholder = "Write your inquiry details here...";
        } else if (currentLang === 'zh') {
            nameInput.placeholder = "例如：李雷";
            emailInput.placeholder = "例如：lilei@email.com";
            msgInput.placeholder = "在这里写下您的咨询详情...";
        } else {
            nameInput.placeholder = "ຕົວຢ່າງ: ສົມພອນ";
            emailInput.placeholder = "ຕົວຢ່າງ: somphone@email.com";
            msgInput.placeholder = "ຂຽນລາຍລະອຽດການສອບຖາມຂໍ້ມູນຂອງທ່ານຢູ່ບ່ອນນີ້...";
        }
    }
}

// Category Filtering logic using Bottom Floating Dock
function initFilter() {
    const dockItems = document.querySelectorAll('.dock-item');
    const tabContents = document.querySelectorAll('.tab-content');

    dockItems.forEach(item => {
        item.addEventListener('click', (e) => {
            e.preventDefault();
            
            const targetTabId = item.getAttribute('data-tab');
            if (!targetTabId) return;

            // Set active class on clicked dock item
            dockItems.forEach(di => di.classList.remove('active'));
            item.classList.add('active');

            // Show target tab, hide others
            tabContents.forEach(tab => {
                if (tab.id === targetTabId) {
                    tab.classList.add('active');
                    
                    // Force animations inside this tab to trigger since they were hidden
                    const animated = tab.querySelectorAll('.animate-on-scroll');
                    animated.forEach(el => {
                        el.classList.add('appear');
                        el.style.opacity = '1';
                        el.style.transform = 'translateY(0)';
                    });
                } else {
                    tab.classList.remove('active');
                }
            });
            
            // Scroll to top safely
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });
    });
}
// Interactive Project Details Dialog
function initModals() {
    const modal = document.getElementById('project-modal');
    const closeBtn = document.getElementById('modal-close');
    const projectCards = document.querySelectorAll('.project-card');

    projectCards.forEach(card => {
        card.addEventListener('click', () => {
            const projectId = card.getAttribute('data-project-id');
            const data = translations.projects[projectId];

            if (!data) return;

            // Load Content into Modal Elements
            document.getElementById('modal-img').src = `assets/${projectId}.png`;
            document.getElementById('modal-img').alt = data.title[currentLang];
            document.getElementById('modal-tag').textContent = data.tag[currentLang];
            document.getElementById('modal-title').textContent = data.title[currentLang];

            // Render stats grid
            const statsContainer = document.getElementById('modal-stats');
            statsContainer.innerHTML = '';
            data.stats[currentLang].forEach(stat => {
                const statDiv = document.createElement('div');
                statDiv.className = 'stat-item';
                statDiv.innerHTML = `
                    <span class="stat-label">${stat.label}</span>
                    <span class="stat-value">${stat.value}</span>
                `;
                statsContainer.appendChild(statDiv);
            });

            // Render descriptions
            document.getElementById('modal-desc').innerHTML = data.desc[currentLang];

            // Open HTML5 modal
            modal.showModal();
            document.body.style.overflow = 'hidden'; // Lock main scroll
        });
    });

    // Close Dialog events
    closeBtn.addEventListener('click', closeModal);
    
    // Close modal when clicking on background backdrop
    modal.addEventListener('click', (e) => {
        const rect = modal.getBoundingClientRect();
        const isInDialog = (rect.top <= e.clientY && e.clientY <= rect.top + rect.height &&
                            rect.left <= e.clientX && e.clientX <= rect.left + rect.width);
        
        // We close the modal only if clicking outside the wrapper content area
        const wrapper = modal.querySelector('.modal-wrapper');
        const wrapperRect = wrapper.getBoundingClientRect();
        const isInWrapper = (wrapperRect.top <= e.clientY && e.clientY <= wrapperRect.top + wrapperRect.height &&
                             wrapperRect.left <= e.clientX && e.clientX <= wrapperRect.left + wrapperRect.width);

        if (!isInWrapper) {
            closeModal();
        }
    });

    function closeModal() {
        // Add smooth slide down animation on exit
        const wrapper = modal.querySelector('.modal-wrapper');
        wrapper.style.animation = 'slideUp 0.4s cubic-bezier(0.16, 1, 0.3, 1) reverse forwards';
        
        setTimeout(() => {
            modal.close();
            document.body.style.overflow = 'auto'; // Restore scroll
            wrapper.style.animation = ''; // Reset animation styles
        }, 400);
    }
}

// Contact form simulation handling
function handleFormSubmit() {
    const form = document.getElementById('contact-form');
    const successMsg = document.getElementById('form-success');

    // Simple success animation
    form.style.opacity = '0';
    setTimeout(() => {
        form.style.display = 'none';
        successMsg.style.display = 'flex';
        successMsg.style.opacity = '0';
        setTimeout(() => {
            successMsg.style.opacity = '1';
        }, 50);
    }, 300);

    // Reset form after a simulation timer (e.g. 15s) so they can test it again
    setTimeout(() => {
        form.reset();
        successMsg.style.display = 'none';
        form.style.display = 'flex';
        setTimeout(() => {
            form.style.opacity = '1';
        }, 50);
    }, 15000);
}

// Fade-in scroll animations
function initScrollAnimations() {
    const animatedElements = document.querySelectorAll('.animate-on-scroll');

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('appear');
                observer.unobserve(entry.target); // Trigger only once
            }
        });
    }, {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px' // Trigger slightly before entering screen center
    });

    animatedElements.forEach(el => observer.observe(el));
}

// -----------------------------------------------------------------------------
// Dynamic Activity Feed Fetching
// -----------------------------------------------------------------------------
async function fetchAndRenderActivities() {
    const feedContainer = document.getElementById('activity-feed');
    if (!feedContainer) return;

    try {
        // Try the live API first (when the Node server is running).
        // Fall back to the static data.json file so the feed still works
        // on static hosts like GitHub Pages.
        let activities;
        try {
            const response = await fetch('/api/activities');
            if (!response.ok) throw new Error('API unavailable');
            activities = await response.json();
        } catch (apiError) {
            const staticResponse = await fetch('data.json');
            if (!staticResponse.ok) throw new Error('Could not load activity data');
            activities = await staticResponse.json();
        }

        if (activities.length === 0) {
            feedContainer.innerHTML = `<p style="text-align:center; color:var(--text-muted); grid-column: 1/-1;" data-en="No recent activities posted." data-la="ຍັງບໍ່ມີຂ່າວສານໃໝ່ໃນຕອນນີ້." data-zh="暂无近期活动。">No recent activities posted.</p>`;
            return;
        }

        let html = '';
        activities.forEach(act => {
            const dateStr = new Date(act.date).toLocaleDateString();
            // Always show a branded placeholder; layer the real photo on top.
            // If the photo is missing or fails to load, it is removed and the
            // placeholder shows through (no broken-image icons).
            const photoLayer = act.photoUrl
                ? `<img src="${act.photoUrl}" alt="Activity Photo" class="activity-img-photo" loading="lazy" onerror="this.remove()">`
                : '';
            const imgHtml = `<div class="activity-img"><img src="assets/logo.svg" alt="" class="activity-img-logo" aria-hidden="true">${photoLayer}</div>`;

            html += `
                <div class="activity-card">
                    ${imgHtml}
                    <div class="activity-content">
                        <span class="activity-date">${dateStr}</span>
                        <h3 class="activity-title">
                            <span class="en-text">${act.title.en || act.title.la || ''}</span>
                            <span class="lao-text">${act.title.la || act.title.en || ''}</span>
                            <span class="zh-text">${act.title.zh || act.title.en || ''}</span>
                        </h3>
                        <p class="activity-desc">
                            <span class="en-text">${act.desc.en || act.desc.la || ''}</span>
                            <span class="lao-text">${act.desc.la || act.desc.en || ''}</span>
                            <span class="zh-text">${act.desc.zh || act.desc.en || ''}</span>
                        </p>
                    </div>
                </div>
            `;
        });
        
        feedContainer.innerHTML = html;
        updateLanguageUI(); // ensure languages are correct
        
    } catch (error) {
        console.error('Error fetching activities:', error);
        feedContainer.innerHTML = `<p style="text-align:center; color:var(--text-muted); grid-column: 1/-1;">Unable to load activities right now.</p>`;
    }
}
