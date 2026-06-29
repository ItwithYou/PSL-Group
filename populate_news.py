import json
import time

now = int(time.time() * 1000)
day = 24 * 60 * 60 * 1000

data = [
    {
        "id": str(now),
        "date": "2026-06-29",
        "photoUrl": "assets/u17-support.jpg",
        "title": {
            "en": "PSL Group Supports Laos U17 National Team",
            "la": "ບໍລິສັດ PSL Group ສະໜັບສະໜູນທີມຊາດລາວ U17 ດ້ວຍງົບປະມານ 100,000,000 ກີບ",
            "zh": "PSL集团支持老挝U17国家队"
        },
        "desc": {
            "en": "PSL Group proudly supports the Laos U17 National Team with 100,000,000 LAK for reaching the final 4 in the ASEAN U17 Boys' Championship 2026 in Indonesia. We are honored to stand by our team and support the bright future of youth football in Laos.",
            "la": "ບໍລິສັດ PSL Group ເປັນຢ່າງສູງ ທີ່ໃຫ້ການສະໜັບສະໜູນ ທີມຊາດລາວ ຮຸ່ນອາຍຸບໍ່ເກີນ 17 ປີ ຈໍານວນ 100,000,000 ກີບ ຕໍ່ຜົນງານສາມາຜ່ານເຂົ້າຮອບ 4 ທີມສຸດທ້າຍ ໃນການແຂ່ງຂັນບານເຕະ ເຍົາວະຊົນຮຸ່ນອາຍຸບໍ່ເກີນ 17 ປີ ຊີງແຊ້ມອາຊຽນ ປະຈໍາປີ 2026 ທີ່ປະເທດອິນໂດເນເຊຍ. ພວກເຮົາຂໍຂອບໃຈທຸກໆທ່ານເປັນຢ່າງສູງທີ່ຢູ່ຂ້າງພວກເຮົາ, ເຊຍພວກເຮົາ ແລະ ສະໜັບສະໜູນພວກເຮົາມາໂດຍຕະຫຼອດ.",
            "zh": "PSL集团自豪地为老挝U17国家队提供100,000,000基普的支持，庆祝其在印尼举办的2026年东盟U17青年足球锦标赛中打入四强。我们非常荣幸能与我们的球队站在一起，支持老挝青年足球的光明未来。"
        },
        "timestamp": now
    },
    {
        "id": str(now - day*3),
        "date": "2026-06-26",
        "photoUrl": "assets/construction.png",
        "title": {
            "en": "Infrastructure Milestone: Highway Construction",
            "la": "ຄວາມສຳເລັດໂຄງລ່າງພື້ນຖານ: ການກໍ່ສ້າງທາງດ່ວນ",
            "zh": "基础设施里程碑：高速公路建设"
        },
        "desc": {
            "en": "PSL Construction has successfully completed a key segment of the Central Laos Highway project, significantly enhancing logistics, safety, and trade routes across the region.",
            "la": "ບໍລິສັດ ກໍ່ສ້າງ PSL ໄດ້ສຳເລັດການກໍ່ສ້າງທາງດ່ວນພາກກາງ ເຊິ່ງຈະຊ່ວຍສົ່ງເສີມເສັ້ນທາງການຄ້າ ແລະ ໂລຈິດສະຕິກ ໃຫ້ມີຄວາມສະດວກ ແລະ ປອດໄພຍິ່ງຂຶ້ນ.",
            "zh": "PSL建筑成功完成了老挝中部高速公路项目的关键路段，显著提升了整个地区的物流、安全和贸易路线。"
        },
        "timestamp": now - day*3
    },
    {
        "id": str(now - day*10),
        "date": "2026-06-19",
        "photoUrl": "assets/service.png",
        "title": {
            "en": "PSL Service Expands Cold Chain Fleet",
            "la": "ບໍລິການ PSL ຂະຫຍາຍກອງທັບລົດຂົນສົ່ງຄວາມເຢັນ",
            "zh": "PSL服务扩充冷链车队"
        },
        "desc": {
            "en": "Expanding our capacity to serve the region, PSL Service has added 20 new refrigerated trucks to our cross-border logistics fleet, ensuring high-quality agricultural exports.",
            "la": "ເພື່ອຂະຫຍາຍຄວາມສາມາດໃນການບໍລິການ, ບໍລິການ PSL ໄດ້ເພີ່ມລົດບັນທຸກຄວາມເຢັນໃໝ່ 20 ຄັນ ເຂົ້າໃນກອງທັບລົດຂົນສົ່ງຂ້າມແດນ ເພື່ອຮັບປະກັນຄຸນນະພາບສິນຄ້າກະສິກຳສົ່ງອອກ.",
            "zh": "为了提升服务区域的能力，PSL服务为其跨境物流车队新增了20辆冷藏卡车，确保高质量的农产品出口。"
        },
        "timestamp": now - day*10
    },
    {
        "id": str(now - day*25),
        "date": "2026-06-04",
        "photoUrl": "",
        "title": {
            "en": "Community Safety Awareness Program",
            "la": "ໂຄງການປູກຈິດສຳນຶກຄວາມປອດໄພຊຸມຊົນ",
            "zh": "社区安全意识项目"
        },
        "desc": {
            "en": "The PSL Environment & Safety Unit hosted a seminar on workplace safety and environmental protection for local communities in Vientiane, reaffirming our commitment to sustainable development.",
            "la": "ໜ່ວຍງານ ສິ່ງແວດລ້ອມ ແລະ ຄວາມປອດໄພ ໄດ້ຈັດສຳມະນາກ່ຽວກັບຄວາມປອດໄພໃນບ່ອນເຮັດວຽກ ແລະ ການປົກປັກຮັກສາສິ່ງແວດລ້ອມໃຫ້ແກ່ຊຸມຊົນໃນນະຄອນຫຼວງວຽງຈັນ.",
            "zh": "PSL环境与安全组为万象当地社区举办了关于工作场所安全和环境保护的研讨会，重申了我们对可持续发展的承诺。"
        },
        "timestamp": now - day*25
    },
    {
        "id": str(now - day*45),
        "date": "2026-05-15",
        "photoUrl": "",
        "title": {
            "en": "New Strategic Partnership for Construction Tech",
            "la": "ການຮ່ວມມືຍຸດທະສາດໃໝ່ດ້ານເຕັກໂນໂລຊີກໍ່ສ້າງ",
            "zh": "建筑技术的新战略合作伙伴关系"
        },
        "desc": {
            "en": "PSL Group has signed an MoU with international partners to integrate advanced, eco-friendly technologies into our upcoming megaprojects, aiming to elevate national construction standards.",
            "la": "ກຸ່ມບໍລິສັດ PSL ໄດ້ລົງນາມໃນບົດບັນທຶກຄວາມເຂົ້າໃຈ ກັບຄູ່ຄ້າຕ່າງປະເທດ ເພື່ອນຳໃຊ້ເຕັກໂນໂລຊີທີ່ທັນສະໄໝ ແລະ ເປັນມິດຕໍ່ສິ່ງແວດລ້ອມ ເຂົ້າໃນໂຄງການຂະໜາດໃຫຍ່.",
            "zh": "PSL集团与国际合作伙伴签署了谅解备忘录，将先进的环保技术整合到即将到来的大型项目中，旨在提升国家建筑标准。"
        },
        "timestamp": now - day*45
    }
]

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("data.json populated with 5 news items!")
