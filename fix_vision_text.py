import re

with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

new_vision_text = """        philosophyText1: {
            en: "Committed to being a leader in comprehensive construction conglomerates through strategic partnerships with domestic and international partners to elevate construction technology to be modern and outstanding. We focus on building trust and meeting customer needs with international standard quality and impressive service, driven by 5 key success factors:",
            la: "ມຸ່ງໝັ້ນສູ່ການເປັນຜູ້ນຳດ້ານກຸ່ມບໍລິສັດກໍ່ສ້າງຄົບວົງຈອນ ໂດຍການຮ່ວມມືຍຸດທະສາດກັບຄູ່ຄ້າທັງພາຍໃນ ແລະ ຕ່າງປະເທດ ເພື່ອຍົກລະດັບເຕັກໂນໂລຊີການກໍ່ສ້າງໃຫ້ທັນສະໄໝ ແລະ ໂດດເດັ່ນ. ພວກເຮົາມຸ່ງເນັ້ນການສ້າງຄວາມເຊື່ອໝັ້ນ, ຕອບສະໜອງຄວາມຕ້ອງການຂອງລູກຄ້າດ້ວຍຄຸນນະພາບມາດຕະຖານສາກົນ ແລະ ການບໍລິການທີ່ປະທັບໃຈ ພາຍໃຕ້ການຂັບເຄື່ອນຂອງ 5 ປັດໄຈຫຼັກສູ່ຄວາມສຳເລັດ",
            zh: "致力于通过与国内外合作伙伴的战略合作，成为综合性建筑企业集团的领导者，提升现代卓越的建筑技术。我们注重建立信任，以国际标准的质量和令人印象深刻的服务满足客户需求，受5个关键成功因素的驱动："
        },"""

js = re.sub(r'philosophyText1:\s*\{.*?\},', new_vision_text, js, flags=re.DOTALL)

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Vision text updated successfully!")
