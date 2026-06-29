import re

with open('app.js', 'r', encoding='utf-8') as f:
    content = f.read()

en_old = '''                     <ul>
                        <li><strong>Highway 13 South Rehabilitation:</strong> 120 km of highway asphalt pavement and bridge structures.</li>
                        <li><strong>Vientiane Urban Road Improvement:</strong> Modernization of urban avenues with smart drainage.</li>
                        <li><strong>Mekong River Embankment Development:</strong> Structural reinforcement and public parks along the riverfront.</li>
                     </ul>'''

en_new = '''                     <ul>
                        <li><strong>Ministry of Defense Strategic Projects:</strong> Unmanned vehicle factory, medical technology factory, and specialized facilities in Vientiane & Houaphanh.</li>
                        <li><strong>National Highway Development:</strong> 313.6 km of road study, design, and construction, including Route 13 North, Route 21, 1D, and 1C.</li>
                        <li><strong>Vientiane Road Infrastructure:</strong> Construction and improvement of 10 major road networks within Vientiane Capital.</li>
                        <li><strong>Khammouane Riverbank Protection:</strong> 19 km of strategic riverbank erosion protection in Khammouane Province.</li>
                     </ul>'''

la_old = '''                     <ul>
                        <li><strong>ໂຄງການບູລະນະປະຕິເສດທາງເລກທີ 13 ໃຕ້:</strong> ປູຢາງທາງດ່ວນ ແລະ ໂຄງສ້າງຂົວ ຄວາມຍາວ 120 ກິໂລແມັດ.</li>
                        <li><strong>ໂຄງການປັບປຸງເສັ້ນທາງຕົວເມືອງວຽງຈັນ:</strong> ປັບປຸງເສັ້ນທາງຕົວເມືອງໃຫ້ທັນສະໄໝ ພ້ອມລະບົບລະບາຍນໍ້າອັດສະລິຍະ.</li>
                        <li><strong>ໂຄງການພັດທະນາພະນັງກັນເຈື່ອນແຄມຂອງ:</strong> ເສີມຄວາມແຂງແຮງຂອງຕາຝັ່ງເຈື່ອນ ແລະ ພັດທະນາສວນສາທາລະນະແຄມຂອງ ນະຄອນຫຼວງວຽງຈັນ.</li>
                     </ul>'''

la_new = '''                     <ul>
                        <li><strong>ໂຄງການຍຸດທະສາດບູລິມະສິດ ກະຊວງປ້ອງກັນປະເທດ:</strong> ໂຮງງານພັດທະນາເຕັກໂນໂລຊີການຢາ-ການແພດ, ໂຮງງານພັດທະນາຍານພາຫະນະບໍ່ມີຄົນຂັບ ຢູ່ນະຄອນຫຼວງວຽງຈັນ ແລະ ແຂວງຫົວພັນ.</li>
                        <li><strong>ໂຄງການພັດທະນາເສັ້ນທາງແຫ່ງຊາດ:</strong> ສຶກສາ, ອອກແບບ ແລະ ກໍ່ສ້າງເສັ້ນທາງ ລວມຄວາມຍາວ 313.6 ກິໂລແມັດ (ທາງເລກ 13 ເໜືອ, 21, 1D, 1C).</li>
                        <li><strong>ໂຄງການກໍ່ສ້າງເສັ້ນທາງນະຄອນຫຼວງວຽງຈັນ:</strong> ໂຄງການກໍ່ສ້າງໂຄງລ່າງເສັ້ນທາງ ຈຳນວນ 10 ເສັ້ນ ຂອງນະຄອນຫຼວງວຽງຈັນ.</li>
                        <li><strong>ໂຄງການປ້ອງກັນຕະຝັ່ງເຈື່ອນ ແຂວງຄຳມ່ວນ:</strong> ໂຄງການກໍ່ສ້າງປ້ອງກັນຕະຝັ່ງເຈື່ອນ ລວງຍາວ 19 ກິໂລແມັດ.</li>
                     </ul>'''

zh_old = '''<h4>关键项目</h4><ul><li><strong>13号公路南部恢复:</strong> 120公里的公路沥青路面和桥梁结构。</li><li><strong>万象城市道路改善:</strong> 城市大道的现代化与智能排水。</li><li><strong>湄公河堤防开发:</strong> 沿河的结构加固和公园。</li></ul>`'''

zh_new = '''<h4>关键项目</h4><ul><li><strong>国防部战略项目:</strong> 位于万象和华潘省的无人驾驶车辆工厂、医疗技术工厂及专用设备设施。</li><li><strong>国家公路开发:</strong> 313.6 公里的道路研究、设计和施工，包括 13 号公路北段、21、1D 和 1C 号公路。</li><li><strong>万象道路基础设施:</strong> 万象市 10 条主要道路网络的建设与改善。</li><li><strong>甘蒙省河岸防护:</strong> 位于甘蒙省的 19 公里战略性河岸防侵蚀工程。</li></ul>`'''


content = content.replace(en_old, en_new)
content = content.replace(la_old, la_new)
content = content.replace(zh_old, zh_new)

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated successfully.")
