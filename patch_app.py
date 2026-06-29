import re

with open('app.js', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add zh translations
# heroDesc
content = content.replace(
    'la: "ກຸ່ມບໍລິສັດ PSL ແມ່ນກຸ່ມທຸລະກິດຮ່ວມມືແບບຄົບວົງຈອນຊັ້ນນຳໃນປະເທດລາວ. ກວມເອົາຂະແໜງການກໍ່ສ້າງ ແລະ ໂຄງລ່າງພື້ນຖານ, ການບໍລິການໂລຈິດສະຕິກ, ກະສິກຳແບບຍືນຍົງ, ແລະ ພະລັງງານທົດແທນ. ບັນດາຂະແໜງການເຫຼົ່ານີ້ດຳເນີນງານຮ່ວມກັນ ເພື່ອຂັບເຄື່ອນການພັດທະນາແບບຍືນຍົງ ແລະ ການເຊື່ອມໂຍງໃນພາກພື້ນ."\n    }',
    'la: "ກຸ່ມບໍລິສັດ PSL ແມ່ນກຸ່ມທຸລະກິດຮ່ວມມືແບບຄົບວົງຈອນຊັ້ນນຳໃນປະເທດລາວ. ກວມເອົາຂະແໜງການກໍ່ສ້າງ ແລະ ໂຄງລ່າງພື້ນຖານ, ການບໍລິການໂລຈິດສະຕິກ, ກະສິກຳແບບຍືນຍົງ, ແລະ ພະລັງງານທົດແທນ. ບັນດາຂະແໜງການເຫຼົ່ານີ້ດຳເນີນງານຮ່ວມກັນ ເພື່ອຂັບເຄື່ອນການພັດທະນາແບບຍືນຍົງ ແລະ ການເຊື່ອມໂຍງໃນພາກພື້ນ.",\n        zh: "PSL集团是老挝领先的多学科跨国企业集团。我们的业务涵盖基础设施、建筑、物流服务、可持续农业和可再生能源，致力于协同推动可持续发展和区域连接。"\n    }'
)

# philosophyText1
content = content.replace(
    'la: "ຢູ່ ກຸ່ມບໍລິສັດ PSL, ພວກເຮົາເຊື່ອໝັ້ນວ່າແຕ່ລະຂະແໜງການບໍ່ແມ່ນສິ່ງແຍກສ່ວນ, ແຕ່ແມ່ນພາກສ່ວນຂອງລະບົບນິເວດທຸລະກິດທີ່ເປັນເອກະພາບ. ເຫຼັກກ້າທີ່ພວກເຮົາຕິດຕັ້ງໃນໂຄງການກໍ່ສ້າງ, ໂລຈິດສະຕິກໂສ້ຄວາມເຢັນສຳລັບຂົນສົ່ງພືດອິນຊີ, ແລະ ລະບົບພະລັງງານແສງຕາເວັນສີຂຽວ - ລ້ວນແຕ່ຮ່ວມວິໄສທັດດຽວກັນ."\n    }',
    'la: "ຢູ່ ກຸ່ມບໍລິສັດ PSL, ພວກເຮົາເຊື່ອໝັ້ນວ່າແຕ່ລະຂະແໜງການບໍ່ແມ່ນສິ່ງແຍກສ່ວນ, ແຕ່ແມ່ນພາກສ່ວນຂອງລະບົບນິເວດທຸລະກິດທີ່ເປັນເອກະພາບ. ເຫຼັກກ້າທີ່ພວກເຮົາຕິດຕັ້ງໃນໂຄງການກໍ່ສ້າງ, ໂລຈິດສະຕິກໂສ້ຄວາມເຢັນສຳລັບຂົນສົ່ງພືດອິນຊີ, ແລະ ລະບົບພະລັງງານແສງຕາເວັນສີຂຽວ - ລ້ວນແຕ່ຮ່ວມວິໄສທັດດຽວກັນ.",\n        zh: "在PSL集团，我们相信各个行业并非孤立存在，而是统一生态系统的组成部分。我们在建筑项目中使用的钢材，运送有机作物的冷链物流，以及注入电网的清洁能源——它们都共享同一个愿景。"\n    }'
)

# philosophyText2
content = content.replace(
    'la: "ການເຕີບໂຕແບບຍືນຍົງ. ການເຊື່ອມໂຍງລະດັບພາກພື້ນ. ຄຸນນະພາບທີ່ບໍ່ມີການຫຼຸດຜ່ອນ. ພວກເຮົາເຊື່ອມໂຍງການວາງແຜນ ແລະ ການຈັດຕັ້ງປະຕິບັດຢ່າງເປັນລະບົບ, ເຮັດໃຫ້ແນວຄິດ ແລະ ການປະຕິບັດຕົວຈິງຢູ່ຄຽງຄູ່ກັນສະເໝີ. ນີ້ຄືປັດສະຍາຫຼັກຂອງພວກເຮົາ."\n    },',
    'la: "ການເຕີບໂຕແບບຍືນຍົງ. ການເຊື່ອມໂຍງລະດັບພາກພື້ນ. ຄຸນນະພາບທີ່ບໍ່ມີການຫຼຸດຜ່ອນ. ພວກເຮົາເຊື່ອມໂຍງການວາງແຜນ ແລະ ການຈັດຕັ້ງປະຕິບັດຢ່າງເປັນລະບົບ, ເຮັດໃຫ້ແນວຄິດ ແລະ ການປະຕິບັດຕົວຈິງຢູ່ຄຽງຄູ່ກັນສະເໝີ. ນີ້ຄືປັດສະຍາຫຼັກຂອງພວກເຮົາ.",\n        zh: "可持续增长。区域一体化。毫不妥协的质量。我们将规划和执行直接联系起来，使思想和实践紧密结合。这就是我们的经营理念。"\n    },'
)

# construction
content = content.replace('la: "ບໍລິສັດ ກໍ່ສ້າງ PSL" }', 'la: "ບໍລິສັດ ກໍ່ສ້າງ PSL", zh: "PSL 建筑" }')
content = content.replace('la: "ການກໍ່ສ້າງ & ໂຄງລ່າງພື້ນຖານ" }', 'la: "ການກໍ່ສ້າງ & ໂຄງລ່າງພື້ນຖານ", zh: "建筑与基础设施" }')

c_stats = """                la: [
                    { label: "ຂະແໜງການ", value: "ການພັດທະນາໂຄງລ່າງພື້ນຖານ" },
                    { label: "ໂຄງການທີ່ສຳເລັດ", value: "45+ ໂຄງການໃຫຍ່" },
                    { label: "ວຽກງານຫຼັກ", value: "ທາງດ່ວນ, ຂົວ, ອາຄານການຄ້າ" }
                ]
            },"""
c_stats_new = """                la: [
                    { label: "ຂະແໜງການ", value: "ການພັດທະນາໂຄງລ່າງພື້ນຖານ" },
                    { label: "ໂຄງການທີ່ສຳເລັດ", value: "45+ ໂຄງການໃຫຍ່" },
                    { label: "ວຽກງານຫຼັກ", value: "ທາງດ່ວນ, ຂົວ, ອາຄານການຄ້າ" }
                ],
                zh: [
                    { label: "领域", value: "基础设施开发" },
                    { label: "已完成项目", value: "45+ 大型项目" },
                    { label: "重点领域", value: "高速公路、桥梁、商业地产" }
                ]
            },"""
content = content.replace(c_stats, c_stats_new)
content = re.sub(r'(la: `<p>ບໍລິສັດ ກໍ່ສ້າງ PSL.*?</ul>`)', r'\1,\n                zh: `<p>PSL 建筑是 PSL 集团的基石部门。在过去的十年里，我们成功在老挝各地交付了高质量的公共和私营部门项目。从区域高速公路网络到现代办公大楼，我们保持最高标准的安全性、耐用性和环保设计。</p><h4>分支机构</h4><p>• <strong>总部:</strong> 老挝万象市占塔布里县农塔泰村<br>• <strong>南部支部:</strong> 占巴塞省巴色市</p><h4>关键项目</h4><ul><li><strong>13号公路南部恢复:</strong> 120公里的公路沥青路面和桥梁结构。</li><li><strong>万象城市道路改善:</strong> 城市大道的现代化与智能排水。</li><li><strong>湄公河堤防开发:</strong> 沿河的结构加固和公园。</li></ul>`', content, flags=re.DOTALL)

# service
content = content.replace('la: "ບໍລິສັດ ບໍລິການ ແລະ ໂລຈິດສະຕິກ PSL" }', 'la: "ບໍລິສັດ ບໍລິການ ແລະ ໂລຈິດສະຕິກ PSL", zh: "PSL 服务与物流" }')
content = content.replace('la: "ໂລຈິດສະຕິກ & ການບໍລິການວິສາຫະກິດ" }', 'la: "ໂລຈິດສະຕິກ & ການບໍລິການວິສາຫະກິດ", zh: "物流与企业服务" }')

s_stats = """                la: [
                    { label: "ຂະແໜງການ", value: "ໂລຈິດສະຕິກ & ການຄຸ້ມຄອງອາຄານ" },
                    { label: "ສາງສິນຄ້າ", value: "6 ສູນໃຫຍ່ໃນພາກພື້ນ" },
                    { label: "ຄວາມຖືກຕ້ອງໃນການສົ່ງ", value: "ກົງເວລາ 99.8%" }
                ]
            },"""
s_stats_new = """                la: [
                    { label: "ຂະແໜງການ", value: "ໂລຈິດສະຕິກ & ການຄຸ້ມຄອງອາຄານ" },
                    { label: "ສາງສິນຄ້າ", value: "6 ສູນໃຫຍ່ໃນພາກພື້ນ" },
                    { label: "ຄວາມຖືກຕ້ອງໃນການສົ່ງ", value: "ກົງເວລາ 99.8%" }
                ],
                zh: [
                    { label: "领域", value: "物流与设施运营" },
                    { label: "仓库", value: "6个区域中心" },
                    { label: "交货准确率", value: "准时率 99.8%" }
                ]
            },"""
content = content.replace(s_stats, s_stats_new)
content = re.sub(r'(la: `<p>ບໍລິສັດ ບໍລິການ PSL.*?</ul>`)', r'\1,\n                zh: `<p>PSL 服务专注于冷链供应管理、国内分销和仓储服务。凭借最先进的冷库设施，我们支持当地农产品出口和一般商品分销，将老挝与东盟市场连接起来。</p><h4>分支机构</h4><p>• <strong>物流中心:</strong> 万象塔纳楞陆港<br>• <strong>南部支部:</strong> 占巴塞巴色物流中心</p><h4>关键项目</h4><ul><li><strong>万象冷链仓储园:</strong> 用于农产品出口的 5,000 平方米温控设施。</li><li><strong>跨境卡车网络:</strong> 连接老挝、泰国和越南的每日定期货运路线。</li><li><strong>工业园设施管理:</strong> 为万象经济特区提供全面的运营、安全和设施支持。</li></ul>`', content, flags=re.DOTALL)

# agriculture
content = content.replace('la: "ບໍລິສັດ ກະສິກຳອັດສະລິຍະ PSL" }', 'la: "ບໍລິສັດ ກະສິກຳອັດສະລິຍະ PSL", zh: "PSL 智能农业" }')
content = content.replace('la: "ກະສິກຳອັດສະລິຍະ & ຍືນຍົງ" }', 'la: "ກະສິກຳອັດສະລິຍະ & ຍືນຍົງ", zh: "智能与可持续农业" }')

a_stats = """                la: [
                    { label: "ຂະແໜງການ", value: "ກະສິກຳແບບຊັດເຈນ" },
                    { label: "ພື້ນທີ່ຄຸ້ມຄອງ", value: "250 ເຮັກຕາ" },
                    { label: "ເຕັກໂນໂລຊີຫຼັກ", value: "ລະບົບຫົດນໍ້າຢອດໃນເຮືອນຮົ່ມອັດຕະໂນມັດ" }
                ]
            },"""
a_stats_new = """                la: [
                    { label: "ຂະແໜງການ", value: "ກະສິກຳແບບຊັດເຈນ" },
                    { label: "ພື້ນທີ່ຄຸ້ມຄອງ", value: "250 ເຮັກຕາ" },
                    { label: "ເຕັກໂນໂລຊີຫຼັກ", value: "ລະບົບຫົດນໍ້າຢອດໃນເຮືອນຮົ່ມອັດຕະໂນມັດ" }
                ],
                zh: [
                    { label: "领域", value: "精准农业" },
                    { label: "管理农田", value: "250 公顷" },
                    { label: "核心技术", value: "自动化温室滴灌系统" }
                ]
            },"""
content = content.replace(a_stats, a_stats_new)
content = re.sub(r'(la: `<p>ບໍລິສັດ ກະສິກຳ PSL.*?</ul>`)', r'\1,\n                zh: `<p>PSL 农业融合了传统农业遗产和现代自动化技术。我们使用先进的滴灌和环境控制系统管理有机温室，确保本地消费和国际出口的无农药高产农产品。</p><h4>分支机构</h4><p>• <strong>高地种植园:</strong> 占巴塞省波罗芬高原<br>• <strong>研发温室中心:</strong> 万象哈塞丰区</p><h4>关键项目</h4><ul><li><strong>波罗芬有机咖啡农场:</strong> 150公顷的高级有机阿拉比卡咖啡种植园，在树冠下种植。</li><li><strong>物联网智能温室综合体:</strong> 自动化水培系统，种植高级甜瓜和有机沙拉蔬菜。</li><li><strong>生物肥料生产厂:</strong> 生产有机堆肥，供应国内农场并减少化学品使用。</li></ul>`', content, flags=re.DOTALL)

# energy
content = content.replace('la: "ບໍລິສັດ ພະລັງງານ ແລະ ການຄ້າ PSL" }', 'la: "ບໍລິສັດ ພະລັງງານ ແລະ ການຄ້າ PSL", zh: "PSL 能源与贸易" }')
content = content.replace('la: "ພະລັງງານສະອາດ & ການຄ້າສາກົນ" }', 'la: "ພະລັງງານສະອາດ & ການຄ້າສາກົນ", zh: "清洁能源与全球贸易" }')

e_stats = """                la: [
                    { label: "ຂະແໜງການ", value: "ພະລັງງານທົດແທນ & ຫ່ວງໂສ້ອຸປະທານ" },
                    { label: "ກຳລັງຜະລິດແສງຕາເວັນ", value: "15 ເມກາວັດ (MW)" },
                    { label: "ຂອບເຂດເຄືອຂ່າຍ", value: "ລາວ, ໄທ, ຫວຽດນາມ, ຈີນ" }
                ]
            },"""
e_stats_new = """                la: [
                    { label: "ຂະແໜງການ", value: "ພະລັງງານທົດແທນ & ຫ່ວງໂສ້ອຸປະທານ" },
                    { label: "ກຳລັງຜະລິດແສງຕາເວັນ", value: "15 ເມກາວັດ (MW)" },
                    { label: "ຂອບເຂດເຄືອຂ່າຍ", value: "ລາວ, ໄທ, ຫວຽດນາມ, ຈີນ" }
                ],
                zh: [
                    { label: "领域", value: "可再生能源与供应链" },
                    { label: "太阳能组合", value: "15 兆瓦 (MW)" },
                    { label: "网络范围", value: "老挝、泰国、越南、中国" }
                ]
            },"""
content = content.replace(e_stats, e_stats_new)
content = re.sub(r'(la: `<p>ບໍລິສັດ ພະລັງງານ ແລະ ການຄ້າ PSL.*?</ul>`)', r'\1,\n                zh: `<p>PSL 能源与贸易致力于扩大老挝的清洁能源资源。我们投资于太阳能农场基础设施和小型水电项目，同时为可再生商品和绿色设备提供跨境商业贸易网络。</p><h4>分支机构</h4><p>• <strong>能源与太阳能部门:</strong> 万象赛色塔区<br>• <strong>贸易办公室:</strong> 中国云南省昆明分公司</p><h4>关键项目</h4><ul><li><strong>15MW 万象太阳能电网:</strong> 并网的清洁太阳能发电，为老挝国家电力公司（EDL）供电。</li><li><strong>南立小型水电项目:</strong> 清洁径流式水力发电，供应当地地区。</li><li><strong>绿色科技进口:</strong> 供应电动汽车（EV）充电站和电池组系统。</li></ul>`', content, flags=re.DOTALL)


# Update initTheme
theme_func = """function initTheme() {
    const themeBtn = document.getElementById('theme-btn');
    document.documentElement.setAttribute('data-theme', currentTheme);

    themeBtn.addEventListener('click', () => {
        currentTheme = currentTheme === 'light' ? 'dark' : 'light';
        document.documentElement.setAttribute('data-theme', currentTheme);
        localStorage.setItem('psl_theme', currentTheme);
    });
}"""

theme_func_new = """function initTheme() {
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
}"""
content = content.replace(theme_func, theme_func_new)


# Update updateLanguageUI
langUI_func = """    // Update data attribute translations
    document.querySelectorAll('[data-en][data-la]').forEach(el => {
        el.innerHTML = currentLang === 'en' ? el.getAttribute('data-en') : el.getAttribute('data-la');
    });"""

langUI_func_new = """    // Update data attribute translations
    document.querySelectorAll('[data-en][data-la]').forEach(el => {
        if (currentLang === 'en') {
            el.innerHTML = el.getAttribute('data-en');
        } else if (currentLang === 'zh' && el.hasAttribute('data-zh')) {
            el.innerHTML = el.getAttribute('data-zh');
        } else {
            el.innerHTML = el.getAttribute('data-la');
        }
    });"""
content = content.replace(langUI_func, langUI_func_new)

# Update placeholders for zh
placeholders_func = """    if (nameInput && emailInput && msgInput) {
        if (currentLang === 'en') {
            nameInput.placeholder = "e.g. Somphone";
            emailInput.placeholder = "e.g. somphone@email.com";
            msgInput.placeholder = "Write your inquiry details here...";
        } else {
            nameInput.placeholder = "ຕົວຢ່າງ: ສົມພອນ";
            emailInput.placeholder = "ຕົວຢ່າງ: somphone@email.com";
            msgInput.placeholder = "ຂຽນລາຍລະອຽດການສອບຖາມຂໍ້ມູນຂອງທ່ານຢູ່ບ່ອນນີ້...";
        }
    }"""

placeholders_func_new = """    if (nameInput && emailInput && msgInput) {
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
    }"""
content = content.replace(placeholders_func, placeholders_func_new)

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(content)

print('app.js updated successfully.')
