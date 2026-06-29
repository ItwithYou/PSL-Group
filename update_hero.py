import re

with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Update heroDesc to the new company summary
new_hero = """heroDesc: {
        en: "PSL Group is a 100% Lao-owned company founded in 2018. Restructured in 2025 with a registered capital of 50 Billion LAK, we specialize in major infrastructure development, government defense procurement, and advanced technological innovation.",
        la: "ບໍລິສັດ ພີເອັດສແອວ ກໍ່ສ້າງຄົບວົງຈອນ ຈຳກັດຜູ້ດຽວ (PSL) ແມ່ນບໍລິສັດຂອງຄົນລາວ 100% ທີ່ສ້າງຕັ້ງຂຶ້ນໃນປີ 2018 ແລະ ໄດ້ປ່ຽນແປງໂຄງຮ່າງໃນປີ 2025 ເປັນ ກຸ່ມບໍລິສັດ PSL Group ດ້ວຍທຶນຈົດທະບຽນ 50 ຕື້ກີບ. ພວກເຮົາມີຄວາມຊ່ຽວຊານໃນການພັດທະນາໂຄງລ່າງພື້ນຖານ, ການຈັດຊື້-ຈັດຈ້າງໃຫ້ພາກລັດ, ແລະ ການພັດທະນາເຕັກໂນໂລຊີອັນທັນສະໄໝ.",
        zh: "PSL集团是一家成立于2018年的100%老挝全资公司。我们在2025年进行了重组，注册资本为500亿基普。我们专注于重大基础设施开发、政府国防采购以及先进技术创新。"
    }"""

js = re.sub(r'heroDesc:\s*\{.*?\}', new_hero, js, flags=re.DOTALL)

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Updated heroDesc in app.js!")
