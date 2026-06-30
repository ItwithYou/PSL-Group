// JavaScript Logic for PSL Group Corporate Website

// Global State
let currentLang = localStorage.getItem('psl_lang') || 'la';
// Key + default must match the anti-FOUC script in index.html ('theme' / 'tiffany')
let currentTheme = localStorage.getItem('theme') || 'tiffany';

// Translations Database
const translations = {
    heroDesc: {
        en: "Welcome to PSL Group.<br><br>PSL Construction Complete Sole Co., Ltd. is a proud 100% Lao-invested enterprise established in 2018. With continuous growth and expansion, we upgraded our structure to become a full-fledged PSL Group in 2025. We have extensive expertise and rich experience in infrastructure development, government procurement and contracting, and advanced technology development, contributing to the sustainable development of the nation.",
        la: "ຍິນດີຕ້ອນຮັບເຂົ້າສູ່ ກຸ່ມບໍລິສັດ ພີເອັດສແອວ (PSL Group).<br><br>ກຸ່ມບໍລິສັດ PSL ແມ່ນຄວາມພາກພູມໃຈຂອງທຸລະກິດທີ່ລົງທຶນໂດຍຄົນລາວ 100% ເຊິ່ງໄດ້ຮັບການສ້າງຕັ້ງຂຶ້ນໃນປີ 2018. ດ້ວຍການເຕີບໃຫຍ່ ແລະ ການຂະຫຍາຍຕົວຢ່າງຕໍ່ເນື່ອງ, ພວກເຮົາໄດ້ຍົກລະດັບໂຄງສ້າງກາຍເປັນ ກຸ່ມບໍລິສັດ PSL Group ຢ່າງເຕັມຮູບແບບໃນປີ 2025. ພວກເຮົາມີຄວາມຊ່ຽວຊານ ແລະ ປະສົບການອັນອຸດົມສົມບູນ ໃນການພັດທະນາພື້ນຖານໂຄງລ່າງ, ການສະໜອງວຽກງານຈັດຊື້-ຈັດຈ້າງໃຫ້ແກ່ອົງການຈັດຕັ້ງພາກລັດ, ແລະ ການພັດທະນາເຕັກໂນໂລຊີອັນທັນສະໄໝ ເພື່ອປະກອບສ່ວນເຂົ້າໃນການສ້າງສາພັດທະນາປະເທດຊາດຢ່າງຍືນຍົງ.",
        zh: "欢迎来到 PSL 集团。<br><br>PSL 建筑综合独资有限公司是一家引以为豪的 100% 老挝全资企业，成立于2018年。随着业务的持续增长和扩张，我们在2025年全面升级为 PSL 集团。我们在基础设施开发、政府采购与承包以及先进技术开发方面拥有丰富的专业知识和经验，致力于为国家的可持续发展做出贡献。"
    },
            visionText: {
            en: "PSL will step up to become an international leader in comprehensive infrastructure development by integrating innovation and modern technology into the construction process to create sustainable works, elevate the quality of life for society, and build trust for project owners. This is achieved through a development strategy that emphasizes the use of innovation, sustainable cooperation with domestic and international experts, and a focus on developing Lao personnel into professionals under the 5 core factors that form our commitment: transparency and honesty in every step of the work, safety standards as the highest priority, excellent quality according to international standards, architectural beauty in harmony with the environment, and strict on-time delivery for maximum customer satisfaction.",
            la: "PSL ຈະກ້າວຂຶ້ນເປັນຜູ້ນຳດ້ານການພັດທະນາພື້ນຖານໂຄງລ່າງຄົບວົງຈອນໃນລະດັບສາກົນ ໂດຍການເຊື່ອມໂຍງນະວັດຕະກຳ ແລະ ເຕັກໂນໂລຊີທີ່ທັນສະໄໝເຂົ້າໃນຂະບວນການກໍ່ສ້າງ ເພື່ອສ້າງສັນຜົນງານທີ່ຍືນຍົງ, ຍົກລະດັບຄຸນນະພາບຊີວິດຂອງສັງຄົມ ແລະ ສ້າງຄວາມເຊື່ອໝັ້ນໃຫ້ແກ່ເຈົ້າຂອງໂຄງການ ໂດຍຜ່ານແຜນຍຸດທະສາດການພັດທະນາທີ່ເນັ້ນການນຳໃຊ້ນະວັດຕະກຳ, ການຮ່ວມມືແບບຍືນຍົງກັບຜູ້ຊ່ຽວຊານທັງພາຍໃນ ແລະ ຕ່າງປະເທດ, ພ້ອມທັງເອົາໃຈໃສ່ພັດທະນາບຸກຄະລາກອນລາວໃຫ້ເປັນມືອາຊີບ ພາຍໃຕ້ 5 ປັດໃຈຫຼັກທີ່ເປັນຄຳໝັ້ນສັນຍາຂອງພວກເຮົາ ຄື: ຄວາມຊື່ສັດໂປ່ງໃສ ໃນທຸກຂັ້ນຕອນການເຮັດວຽກ, ມາດຕະຖານຄວາມປອດໄພ ທີ່ເປັນບຸລິມະສິດສູງສຸດ, ຄຸນນະພາບທີ່ດີເລີດ ຕາມມາດຕະຖານສາກົນ, ຄວາມສວຍງາມທາງສະຖາປັດຕະຍະກຳ ທີ່ສອດຄ່ອງກັບສະພາບແວດລ້ອມ, ແລະ ການສົ່ງມອບຜົນງານຕາມກຳນົດເວລາ ຢ່າງເຄັ່ງຄັດເພື່ອຄວາມພຶງພໍໃຈສູງສຸດຂອງລູກຄ້າ.",
            zh: "PSL 致力于成为国际全面基础设施开发的领导者，通过将创新和现代技术融入施工过程，创造可持续的工程，提升社会生活质量，并建立项目业主的信任。这通过强调利用创新的发展战略、与国内外专家的可持续合作，以及致力于将老挝人员培养为专业人才来实现。我们的承诺基于 5 个核心因素：在工作的每个环节保持透明和诚实、将安全标准作为最高优先级、符合国际标准的卓越质量、与环境和谐相处的建筑之美，以及严格按时交付以实现最大的客户满意度。"
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
    initCompanyInfoPopup();
    initOrgChartCenter();
    initSubsMarquee();

    // -----------------------------------------------------------------------------
    // Sticky Header Morphing
    // -----------------------------------------------------------------------------
    const header = document.querySelector('.header-container');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }
    });

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
        localStorage.setItem('theme', currentTheme);
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
    if (heroDesc) heroDesc.innerHTML = translations.heroDesc[currentLang];

    const visText = document.getElementById('vision-text');
    if (visText) visText.textContent = translations.visionText[currentLang];

    const visList = document.getElementById('vision-list');
    if (visList) {
        const content = translations.visionList[currentLang];
        // Duplicate content for seamless infinite marquee loop
        visList.innerHTML = content + content;
    }

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

// Smooth Scrolling for Dock Navigation
function initFilter() {
    const dockItems = document.querySelectorAll('.dock-item');

    dockItems.forEach(item => {
        item.addEventListener('click', (e) => {
            const targetId = item.getAttribute('href');
            if (targetId && targetId.startsWith('#')) {
                const targetElement = document.querySelector(targetId);
                if (targetElement) {
                    e.preventDefault(); // Prevent instant jump
                    
                    // Smooth scroll to target section
                    targetElement.scrollIntoView({ behavior: 'smooth', block: 'start' });
                    
                    // Update active class immediately for better UX
                    dockItems.forEach(di => di.classList.remove('active'));
                    item.classList.add('active');
                } else if (targetId === '#home' || targetId === '#') {
                    e.preventDefault();
                    window.scrollTo({ top: 0, behavior: 'smooth' });
                }
            }
        });
    });
}
// Duplicate the subsidiaries track so the marquee loops seamlessly
function initSubsMarquee() {
    const track = document.getElementById('subs-track');
    if (track && !track.dataset.cloned) {
        track.innerHTML += track.innerHTML;
        track.dataset.cloned = '1';
    }
}

// Scale the original org chart so the WHOLE tree fits the screen width on phones
function initOrgChartCenter() {
    const sc = document.querySelector('.org-scroll');
    const wrap = document.querySelector('.org-template-wrapper');
    if (!sc || !wrap) return;

    const fit = () => {
        if (window.innerWidth > 768) {
            // Desktop: leave the chart at its natural size
            wrap.style.transform = '';
            sc.style.height = '';
            return;
        }
        // Reset to measure the natural (unscaled) size. Use !important to beat
        // leftover shrink-hack CSS rules on .org-template-wrapper.
        wrap.style.setProperty('transform', 'none', 'important');
        wrap.style.setProperty('zoom', '1', 'important');
        const naturalW = wrap.scrollWidth;
        const naturalH = wrap.scrollHeight;
        const avail = sc.clientWidth;
        if (!naturalW || !avail) return;
        const scale = Math.min(1, avail / naturalW);
        wrap.style.setProperty('transform-origin', 'top left', 'important');
        wrap.style.setProperty('transform', 'scale(' + scale + ')', 'important');
        // Collapse the empty space the transform leaves behind
        sc.style.height = Math.ceil(naturalH * scale) + 'px';
    };

    fit();
    setTimeout(fit, 250);
    window.addEventListener('resize', fit);
    window.addEventListener('load', fit);
}

// Company Info popup (mobile): button opens the contact details in a modal
function initCompanyInfoPopup() {
    const trigger = document.getElementById('company-info-trigger');
    const modal = document.getElementById('company-info-modal');
    const body = document.getElementById('company-info-body');
    const source = document.querySelector('.hero-meta');
    if (!trigger || !modal || !body || !source) return;

    const open = () => {
        // Clone the live info card content so it stays in one place
        body.innerHTML = source.innerHTML;
        if (typeof updateLanguageUI === 'function') updateLanguageUI();
        modal.hidden = false;
        requestAnimationFrame(() => modal.classList.add('open'));
        document.body.style.overflow = 'hidden';
    };
    const close = () => {
        modal.classList.remove('open');
        document.body.style.overflow = '';
        setTimeout(() => { modal.hidden = true; }, 250);
    };

    trigger.addEventListener('click', open);
    modal.querySelectorAll('[data-info-close]').forEach(el => el.addEventListener('click', close));
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && !modal.hidden) close();
    });
}

// Interactive Project Details Dialog
function initModals() {
    const modal = document.getElementById('project-modal');
    const closeBtn = document.getElementById('modal-close');
    const projectCards = document.querySelectorAll('.vision-glass-card');

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
            const imgHtml = `<div class="activity-img"><img src="assets/logo_transparent.png" alt="" class="activity-img-logo" aria-hidden="true">${photoLayer}</div>`;

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

    // ==========================================================================
    // Scroll Spy & Premium Reveal Animations
    // ==========================================================================

    const sections = document.querySelectorAll('.page-section');
    const dockItems = document.querySelectorAll('.dock-item');

    // Scroll Spy to highlight dock icons
    const observerOptions = {
        root: null,
        rootMargin: '-30% 0px -70% 0px', // Trigger when section is in top 30% of viewport
        threshold: 0
    };

    const sectionObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                // Remove active from all
                dockItems.forEach(item => item.classList.remove('active'));
                
                // Add active to corresponding dock item
                const id = entry.target.getAttribute('id');
                const correspondingDock = document.querySelector(`.dock-item[href="#${id}"]`);
                if (correspondingDock) {
                    correspondingDock.classList.add('active');
                }
                
                // Trigger any animations inside this section
                const animatedElements = entry.target.querySelectorAll('.animate-on-scroll:not(.animated)');
                animatedElements.forEach((el, index) => {
                    setTimeout(() => {
                        el.style.opacity = '1';
                        el.style.transform = 'translateY(0) scale(1)';
                        el.classList.add('animated');
                    }, index * 100);
                });
            }
        });
    }, observerOptions);

    sections.forEach(section => {
        sectionObserver.observe(section);
    });

    // Smooth scroll for dock items
    dockItems.forEach(item => {
        item.addEventListener('click', (e) => {
            e.preventDefault();
            const targetId = item.getAttribute('href');
            const targetSection = document.querySelector(targetId);
            if (targetSection) {
                targetSection.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });

    // Auto-hide bottom dock on scroll down
    let lastScrollY = window.scrollY;
    const dockContainer = document.querySelector('.dock-container');
    
    window.addEventListener('scroll', () => {
        if (!dockContainer) return;
        const currentScrollY = window.scrollY;
        
        // Hide dock if scrolling down and not near top
        if (currentScrollY > lastScrollY && currentScrollY > 150) {
            dockContainer.classList.add('dock-hidden');
        } else {
            // Show dock if scrolling up
            dockContainer.classList.remove('dock-hidden');
        }
        lastScrollY = currentScrollY;
    }, { passive: true });


// Lightbox Logic
document.addEventListener('DOMContentLoaded', () => {
    const lightbox = document.getElementById('lightbox');
    if (!lightbox) return;
    const lightboxImg = document.getElementById('lightbox-img');
    const closeBtn = document.querySelector('.lightbox-close');

    // Add click to all project images
    document.querySelectorAll('.project-card-img').forEach(img => {
        img.style.cursor = 'pointer';
        // Add click listener to the whole card for better UX, or just image
        img.addEventListener('click', (e) => {
            e.stopPropagation(); // prevent card click if we had one
            lightbox.style.display = 'block';
            lightboxImg.src = img.src;
        });
    });

    // Close logic
    closeBtn.addEventListener('click', () => {
        lightbox.style.display = 'none';
    });
    lightbox.addEventListener('click', (e) => {
        if (e.target !== lightboxImg) {
            lightbox.style.display = 'none';
        }
    });
});

// Mobile Dock Toggle Logic
document.addEventListener('DOMContentLoaded', () => {
    const dockToggle = document.getElementById('mobile-dock-toggle');
    const floatingDock = document.getElementById('floating-dock');
    
    if(dockToggle && floatingDock) {
        dockToggle.addEventListener('click', (e) => {
            e.stopPropagation();
            floatingDock.classList.toggle('show');
        });
        
        // Hide dock when clicking anywhere else
        document.addEventListener('click', (e) => {
            if(!floatingDock.contains(e.target) && !dockToggle.contains(e.target)) {
                floatingDock.classList.remove('show');
            }
        });
        
        // Hide dock when a tab is clicked
        const dockItems = floatingDock.querySelectorAll('.dock-item');
        dockItems.forEach(item => {
            item.addEventListener('click', () => {
                floatingDock.classList.remove('show');
            });
        });
    }
});
