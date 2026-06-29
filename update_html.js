const fs = require('fs');
const path = require('path');

const indexPath = path.join(__dirname, 'index.html');
let content = fs.readFileSync(indexPath, 'utf-8');

// 1. Update language switcher
content = content.replace(
    /<button class="lang-btn-option" data-lang="en">EN<\/button>/g,
    '<button class="lang-btn-option" data-lang="en">EN</button>\n                    <button class="lang-btn-option" data-lang="zh">中文</button>'
);

// 2. Update theme toggle
content = content.replace(
    /<svg class="moon-icon"[^>]*>.*?<\/svg>/g,
    `$&
                    <svg class="gem-icon" xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M6 3h12l4 6-10 13L2 9Z"/><path d="M11 3 8 9l4 13"/><path d="M13 3l3 6-4 13"/><path d="M2 9h20"/></svg>`
);

// 3. Update title
content = content.replace(
    /<span class="en-text">PSL Group<\/span>/g,
    '<span class="en-text">PSL Group</span>\n                        <span class="zh-text">PSL 集团</span>'
);

// 4. Update card titles
content = content.replace(
    /<span class="lao-text">ບໍລິສັດ ກໍ່ສ້າງ PSL<\/span>/g,
    '<span class="lao-text">ບໍລິສັດ ກໍ່ສ້າງ PSL</span>\n                                <span class="zh-text">PSL 建筑</span>'
);
content = content.replace(
    /<span class="lao-text">ບໍລິສັດ ບໍລິການ ແລະ ໂລຈິດສະຕິກ PSL<\/span>/g,
    '<span class="lao-text">ບໍລິສັດ ບໍລິການ ແລະ ໂລຈິດສະຕິກ PSL</span>\n                                <span class="zh-text">PSL 服务与物流</span>'
);
content = content.replace(
    /<span class="lao-text">ບໍລິສັດ ກະສິກຳອັດສະລິຍະ PSL<\/span>/g,
    '<span class="lao-text">ບໍລິສັດ ກະສິກຳອັດສະລິຍະ PSL</span>\n                                <span class="zh-text">PSL 智能农业</span>'
);
content = content.replace(
    /<span class="lao-text">ບໍລິສັດ ພະລັງງານ ແລະ ການຄ້າ PSL<\/span>/g,
    '<span class="lao-text">ບໍລິສັດ ພະລັງງານ ແລະ ການຄ້າ PSL</span>\n                                <span class="zh-text">PSL 能源与贸易</span>'
);

// 5. Add data-zh to elements with data-en and data-la
const zhTranslations = {
    'FIELD': '领域',
    'Conglomerate': '企业集团',
    'HEADQUARTERS': '总部',
    'Vientiane, Laos': '老挝，万象',
    'ACTIVE SINCE': '成立年份',
    'STATUS': '状态',
    'Practicing & Growing': '发展中',
    'Subsidiary Divisions': '下属企业',
    'View Structure': '查看结构',
    'View Services': '查看服务',
    'View Agriculture': '查看农业',
    'View Resources': '查看资源',
    'Designing & constructing national infrastructure, bridges, highways, and modern urban environments.': '设计和建设国家基础设施、桥梁、高速公路和现代城市环境。',
    'Integrating logistics management, cold chain storage, freight forwarding, and corporate facilities support.': '整合物流管理、冷链仓储、货运代理和企业设施支持。',
    'Pioneering modern organic farming, automated greenhouse engineering, and export-grade sustainable produce.': '开创现代有机农业、自动化温室工程和出口级可持续农产品。',
    'Developing sustainable hydro, solar power initiatives and managing cross-border commercial trading networks.': '开发可持续的水电、太阳能项目并管理跨境商业贸易网络。',
    'Corporate Evolution Index': '企业发展历程',
    'A timeline mapping structural milestones, capital expansion, and active sectors since inception.': '自成立以来的结构里程碑、资本扩张和活跃部门的时间表。',
    'Establishment & Foundations': '成立与基础',
    'Founded PSL Group with PSL Construction. Secured major infrastructure projects in Central Laos.': '与 PSL 建筑一起成立了 PSL 集团。在老挝中部获得了主要的基础设施项目。',
    'Expansion into Logistics': '扩展到物流',
    'Launched PSL Service, establishing cold chain warehouses and cross-border transport corridors.': '推出了 PSL 服务，建立冷链仓库和跨境运输走廊。',
    'Smart Farming Initiatives': '智能农业倡议',
    'Introduced PSL Agriculture. Built automated commercial greenhouses in Vientiane and Champasak.': '引入了 PSL 农业。在万象和占巴塞建立自动化商业温室。',
    'Renewable Energy Entry': '进入可再生能源',
    'Founded PSL Energy & Trading, integrating solar technology and cross-border commodity trading.': '成立 PSL 能源与贸易，整合太阳能技术和跨境商品贸易。',
    'Strategic Integration': '战略整合',
    'Unified all subsidiaries under the modern PSL Group management system, advancing eco-friendly development.': '在现代 PSL 集团管理系统下统一下属所有子公司，推进环保发展。',
    'THE THROUGH-LINE': '经营理念',
    'Start a partnership with PSL Group.': '与 PSL 集团建立合作。',
    'Get in touch with our division offices or corporate relations.': '请联系我们的分公司或公共关系部门。',
    'Email': '电子邮件',
    'Phone': '电话',
    'Offices': '办公地址',
    'Lane Xang Avenue, Hatsady, Chanthabouly, Vientiane, Laos': '老挝万象市占塔布里县哈萨迪村澜沧大道',
    'Your Name': '您的姓名',
    'Email Address': '电子邮件地址',
    'Interested Sector': '感兴趣的领域',
    'General Inquiry': '一般咨询',
    'PSL Construction': 'PSL 建筑',
    'PSL Service & Logistics': 'PSL 服务与物流',
    'PSL Smart Agriculture': 'PSL 智能农业',
    'PSL Energy & Trading': 'PSL 能源与贸易',
    'Your Message': '您的留言',
    'Send Inquiry': '发送咨询',
    'Inquiry sent successfully. Our team will contact you shortly.': '咨询发送成功。我们的团队将尽快与您联系。',
    '© 2026 PSL Group. All rights reserved.': '© 2026 PSL 集团。保留所有权利。',
    'Inspired by Reckon House': '受 Reckon House 启发',
    'Construction': '建筑',
    'Service': '服务',
    'Agriculture': '农业',
    'Energy': '能源',
    'Contact': '联系'
};

content = content.replace(/data-en="([^"]+)"\s+data-la="([^"]+)"/g, (match, en, la) => {
    let zh = zhTranslations[en] || en;
    return `data-en="${en}" data-la="${la}" data-zh="${zh}"`;
});

fs.writeFileSync(indexPath, content, 'utf-8');
console.log('index.html updated successfully.');
