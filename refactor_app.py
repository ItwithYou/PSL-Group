import json

with open('app.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Wait, app.js is a javascript file containing an object. It's not standard JSON.
# I will use a simple find-and-replace approach using re.

import re

with open('app.js', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update heroDesc
en_hero = '"PSL Group is a premier multi-disciplinary conglomerate based in Laos. Spanning across infrastructure, construction, logistics services, sustainable agriculture, and renewable energy, our operations work in synergy to drive sustainable development and regional connection."'
en_hero_new = '"PSL Group is a premier multi-disciplinary conglomerate based in Laos. Spanning across major infrastructure, construction, and enterprise logistics services, our operations work in synergy to drive sustainable development and regional connection."'
content = content.replace(en_hero, en_hero_new)

la_hero = '"ກຸ່ມບໍລິສັດ PSL ແມ່ນກຸ່ມທຸລະກິດຮ່ວມມືແບບຄົບວົງຈອນຊັ້ນນຳໃນປະເທດລາວ. ກວມເອົາຂະແໜງການກໍ່ສ້າງ ແລະ ໂຄງລ່າງພື້ນຖານ, ການບໍລິການໂລຈິດສະຕິກ, ກະສິກຳແບບຍືນຍົງ, ແລະ ພະລັງງານທົດແທນ. ບັນດາຂະແໜງການເຫຼົ່ານີ້ດຳເນີນງານຮ່ວມກັນ ເພື່ອຂັບເຄື່ອນການພັດທະນາແບບຍືນຍົງ ແລະ ການເຊື່ອມໂຍງໃນພາກພື້ນ."'
la_hero_new = '"ກຸ່ມບໍລິສັດ PSL ແມ່ນກຸ່ມທຸລະກິດຊັ້ນນຳໃນປະເທດລາວ. ກວມເອົາຂະແໜງການກໍ່ສ້າງ ແລະ ໂຄງລ່າງພື້ນຖານ, ແລະ ການບໍລິການໂລຈິດສະຕິກ. ບັນດາຂະແໜງການເຫຼົ່ານີ້ດຳເນີນງານຮ່ວມກັນ ເພື່ອຂັບເຄື່ອນການພັດທະນາແບບຍືນຍົງ ແລະ ການເຊື່ອມໂຍງໃນພາກພື້ນ."'
content = content.replace(la_hero, la_hero_new)

zh_hero = '"PSL集团是老挝领先的多学科跨国企业集团。我们的业务涵盖基础设施、建筑、物流服务、可持续农业和可再生能源，致力于协同推动可持续发展和区域连接。"'
zh_hero_new = '"PSL集团是老挝领先的多学科企业集团。我们的业务涵盖主要基础设施、建筑和企业物流服务，致力于协同推动可持续发展和区域连接。"'
content = content.replace(zh_hero, zh_hero_new)

# 2. Update philosophyText1 (remove organic crops and solar energy)
en_phil1 = '"At PSL Group, we believe that separate sectors are not silos, but parts of a unified eco-system. The steel we mount in our building projects, the cold chain logistics that deliver organic crops, the clean energy feeding the grid - they share a single vision."'
en_phil1_new = '"At PSL Group, we believe that separate sectors are not silos, but parts of a unified eco-system. The steel we mount in our building projects and the logistics networks that connect our region - they share a single vision."'
content = content.replace(en_phil1, en_phil1_new)

la_phil1 = '"ຢູ່ ກຸ່ມບໍລິສັດ PSL, ພວກເຮົາເຊື່ອໝັ້ນວ່າແຕ່ລະຂະແໜງການບໍ່ແມ່ນສິ່ງແຍກສ່ວນ, ແຕ່ແມ່ນພາກສ່ວນຂອງລະບົບນິເວດທຸລະກິດທີ່ເປັນເອກະພາບ. ເຫຼັກກ້າທີ່ພວກເຮົາຕິດຕັ້ງໃນໂຄງການກໍ່ສ້າງ, ໂລຈິດສະຕິກໂສ້ຄວາມເຢັນສຳລັບຂົນສົ່ງພືດອິນຊີ, ແລະ ລະບົບພະລັງງານແສງຕາເວັນສີຂຽວ - ລ້ວນແຕ່ຮ່ວມວິໄສທັດດຽວກັນ."'
la_phil1_new = '"ຢູ່ ກຸ່ມບໍລິສັດ PSL, ພວກເຮົາເຊື່ອໝັ້ນວ່າແຕ່ລະຂະແໜງການບໍ່ແມ່ນສິ່ງແຍກສ່ວນ, ແຕ່ແມ່ນພາກສ່ວນຂອງລະບົບນິເວດທຸລະກິດທີ່ເປັນເອກະພາບ. ເຫຼັກກ້າທີ່ພວກເຮົາຕິດຕັ້ງໃນໂຄງການກໍ່ສ້າງ, ແລະ ເຄືອຂ່າຍໂລຈິດສະຕິກທີ່ເຊື່ອມຕໍ່ພາກພື້ນຂອງພວກເຮົາ - ລ້ວນແຕ່ຮ່ວມວິໄສທັດດຽວກັນ."'
content = content.replace(la_phil1, la_phil1_new)

zh_phil1 = '"在PSL集团，我们相信各个行业并非孤立存在，而是统一生态系统的组成部分。我们在建筑项目中使用的钢材，运送有机作物的冷链物流，以及注入电网的清洁能源——它们都共享同一个愿景。"'
zh_phil1_new = '"在PSL集团，我们相信各个行业并非孤立存在，而是统一生态系统的组成部分。我们在建筑项目中使用的钢材，以及连接我们地区的物流网络——它们都共享同一个愿景。"'
content = content.replace(zh_phil1, zh_phil1_new)

# 3. Rename "PSL Construction" to "PSL Construction Complete Sole Co., Ltd."
content = content.replace('"PSL Construction"', '"PSL Construction Complete Sole Co., Ltd."')
content = content.replace('"ບໍລິສັດ ກໍ່ສ້າງ PSL"', '"ບໍລິສັດ ກໍ່ສ້າງຄົບວົງຈອນ ພີເອັສແອລ ຈຳກັດຜູ້ດຽວ"')
content = content.replace('"PSL 建筑"', '"PSL 建筑独资有限公司"')

# 4. Remove Agriculture and Energy from projects object
# We need to find the `agriculture:` key to the end of `energy: {...}` and remove it.
# This requires a bit of careful regex or manual substring finding.
# Let's find the start of agriculture:
ag_start = content.find('agriculture: {')
if ag_start != -1:
    # We want to keep everything before agriculture:
    # However, there's a comma before it.
    comma_before = content.rfind(',', 0, ag_start)
    
    # We need to find where energy ends. Energy is the last object before `}` of projects.
    energy_end_str = '            }\n        }\n    }\n};'
    energy_end = content.find(energy_end_str)
    
    if energy_end != -1:
        # Construct the new content
        new_content = content[:comma_before] + '\n        }\n    }\n};'
        # Let's preserve the rest of the file after the translations block
        rest_of_file = content[energy_end + len(energy_end_str):]
        content = new_content + rest_of_file

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(content)

print("app.js refactored successfully.")
