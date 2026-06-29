import json
import time

now = int(time.time() * 1000)
day = 24 * 60 * 60 * 1000

data = [
    {
        "id": str(now),
        "date": "2026-06-10",
        "photoUrl": "assets/u17-support.jpg", 
        "title": {
            "en": "PSL Group Donates Over 780 Million LAK to Houaphanh Province",
            "la": "ກຸ່ມບໍລິສັດ PSL ມອບເງິນຊ່ວຍເຫຼືອລວມມູນຄ່າກວ່າ 780 ລ້ານກີບ ໃຫ້ແກ່ແຂວງຫົວພັນ",
            "zh": "PSL集团向华潘省捐赠超过7.8亿基普"
        },
        "desc": {
            "en": "During a working visit to Houaphanh province from June 8-10, 2026, Col. Phouangthong Suyavong, Vice President of PSL Group, mobilized funds from Nissan Mining Development Co., Ltd. (200M LAK) and PSL Group (580.7M LAK). The donations supported local districts and military units with motorcycles, solar lights, computers, and infrastructure improvements.",
            "la": "ໃນລະຫວ່າງວັນທີ 8-10 ມິຖຸນາ 2026 ທີ່ເມືອງຊ່ອນ, ເມືອງຮຽມ ແລະ ເມືອງຫົວເມືອງ ແຂວງຫົວພັນ. ສະຫາຍ ພັນເອກ ນາງ ພວງທອງ ສຸຍະວົງ ຮອງຜູ້ອໍານວຍການ ກຸ່ມບໍລິສັດ PSL ໄດ້ປຸກລະດົມທຶນນຳບໍລິສັດ ນິດສັນພັດທະນາບໍ່ແຮ່ຈຳກັດ 200ລ້ານ ກີບ ແລະ ກຸ່ມບໍລິສັດ PSL 580ລ້ານກວ່າກີບ ເພື່ອມອບໃຫ້ບັນດາເມືອງ, ຕາແສງ ແລະ ກົມກອງທະຫານ ລວມມີ: ເງິນຊື້ລົດຈັກ, ດອກໄຟໂຊລາເຊວ, ຄອມພີວເຕີ ແລະ ປັບປຸງຄ້າຍຄູ.",
            "zh": "2026年6月8日至10日在华潘省视察期间，PSL集团副总裁Phouangthong Suyavong上校及代表团筹集了来自日产矿业开发有限公司的2亿基普及PSL集团的5.807亿基普，用于支持当地乡镇和军队的物资及基础设施建设。"
        },
        "timestamp": now
    },
    {
        "id": str(now - day*5),
        "date": "2026-05-15",
        "photoUrl": "assets/real_1.jpg",
        "title": {
            "en": "PSL Group Supports Laos U17 National Team",
            "la": "ບໍລິສັດ PSL Group ສະໜັບສະໜູນທີມຊາດລາວ U17",
            "zh": "PSL集团支持老挝U17国家队"
        },
        "desc": {
            "en": "PSL Group proudly supports the Laos U17 National Team with 100,000,000 LAK for reaching the final 4 in the ASEAN U17 Boys' Championship 2026 in Indonesia. We are honored to stand by our team and support the bright future of youth football in Laos.",
            "la": "ບໍລິສັດ PSL Group ເປັນຢ່າງສູງ ທີ່ໃຫ້ການສະໜັບສະໜູນ ທີມຊາດລາວ ຮຸ່ນອາຍຸບໍ່ເກີນ 17 ປີ ຈໍານວນ 100,000,000 ກີບ ຕໍ່ຜົນງານສາມາຜ່ານເຂົ້າຮອບ 4 ທີມສຸດທ້າຍ ໃນການແຂ່ງຂັນບານເຕະ ເຍົາວະຊົນຮຸ່ນອາຍຸບໍ່ເກີນ 17 ປີ ຊີງແຊ້ມອາຊຽນ ປະຈໍາປີ 2026 ທີ່ປະເທດອິນໂດເນເຊຍ. ພວກເຮົາຂໍຂອບໃຈທຸກໆທ່ານ ແລະ ສັນຍາວ່າຈະເຮັດໃຫ້ທີ່ສຸດໃນທຸກໆໂອກາດ.",
            "zh": "PSL集团自豪地为老挝U17国家队提供1亿基普的支持，庆祝其在印尼举办的2026年东盟U17青年足球锦标赛中打入四强。我们非常荣幸能与球队并肩作战，支持老挝青年足球的发展。"
        },
        "timestamp": now - day*5
    },
    {
        "id": str(now - day*10),
        "date": "2026-05-01",
        "photoUrl": "assets/real_2.png",
        "title": {
            "en": "A Decade of Philanthropy: Over 30 Billion LAK Donated",
            "la": "10 ປີແຫ່ງການຊ່ວຍເຫຼືອສັງຄົມ: ບໍລິສັດ PSL ມອບເງິນກວ່າ 30 ຕື້ກີບ",
            "zh": "十年慈善回顾：PSL捐赠超过300亿基普"
        },
        "desc": {
            "en": "Over the past 10 years, PSL Group has continuously contributed to the nation and society, donating over 30 Billion LAK. This includes aid for the Attapeu dam collapse, COVID-19 relief, flood assistance, and a recent 2 Billion LAK donation for hailstorm victims. We will soon donate 106 computers and 53 printers worth 1.2 Billion LAK.",
            "la": "ຕະຫຼອດໄລຍະເວລາ 10 ປີຜ່ານມາ, ບໍລິສັດ PSL ໄດ້ຊຸກຍູ້ອຸປະຖຳຊ່ວຍເຫຼືອສັງຄົມແລ້ວ ຫຼາຍກວ່າ 30 ຕື້ກີບ ໂດຍສະເພາະເຫດການເຂື່ອນແຕກທີ່ອັດຕະປື, ໂຄວິດ-19, ໄພທຳມະຊາດ ແລະ ຫຼ້າສຸດແມ່ນເຫດການໝາກເຫັບຕົກທີ່ໄດ້ມອບ 2 ຕື້ກີບ. ໃນໄວໆນີ້ ຈະສືບຕໍ່ມອບຄອມພິວເຕີ 106 ເຄື່ອງ ແລະ ປີ່ນເຕີ 53 ຊຸດ ລວມມູນຄ່າ 1.2 ຕື້ກີບ ໃຫ້ແກ່ເຂດຫ່າງໄກສອກຫຼີກ.",
            "zh": "在过去的十年里，PSL集团持续为国家和社会做出贡献，累计捐助超过300亿基普。这包括对阿速坡大坝溃决、COVID-19疫情、洪水灾害的救援，以及近期为冰雹灾民捐赠的20亿基普。我们还计划向偏远地区捐赠价值12亿基普的106台电脑和53台打印机。"
        },
        "timestamp": now - day*10
    },
    {
        "id": str(now - day*15),
        "date": "2024-09-19",
        "photoUrl": "assets/real_3.png",
        "title": {
            "en": "PSL Service Ltd. Donates 200 Million LAK for Flood Relief",
            "la": "ບໍລິສັດ PSL Service Ltd ມອບເງິນ 200 ລ້ານກີບ ຊ່ວຍເຫຼືອຜູ້ປະສົບໄພນໍ້າຖ້ວມ",
            "zh": "PSL Service Ltd. 捐赠2亿基普用于洪水救援"
        },
        "desc": {
            "en": "On Sept 19, 2024, Ms. Phouangthong Suyavong, President of PSL Service Sole Co., Ltd., donated 200,000,000 LAK to the Lao People's Revolutionary Youth Union to support flood victims in Luang Namtha and other affected provinces, reaffirming our commitment to helping communities recover.",
            "la": "ວັນທີ 19 ກັນຍາ 2024, ທ່ານ ນາງ ພວງທອງ ສຸຍະວົງ ປະທານບໍລິສັດ PSL Service Sole Co., Ltd. ໄດ້ນໍາເອົາເງິນສົດ ມູນຄ່າ 200,000,000 ກີບ ມາມອບໃຫ້ສູນກາງຊາວໜຸ່ມປະຊາຊົນປະຕິວັດລາວ ເພື່ອປະກອບສ່ວນຊ່ວຍເຫຼືອຜູ້ປະສົບໄພນໍ້າຖ້ວມ ທີ່ແຂວງຫຼວງນໍ້າທາ ແລະ ບັນດາແຂວງທີ່ໄດ້ຮັບຜົນກະທົບ. ທາງສູນກາງຊາວໜຸ່ມໄດ້ມອບຫຼຽນຊາວໜຸ່ມຕະລຸມບອນເພື່ອເປັນການສະແດງຄວາມຮູ້ບຸນຄຸນ.",
            "zh": "2024年9月19日，PSL Service Sole Co., Ltd.总裁Phouangthong Suyavong女士向老挝人民革命青年团捐赠了2亿基普，用于支持琅南塔省及其他受灾省份的洪水灾民，重申了我们帮助社区重建的承诺。"
        },
        "timestamp": now - day*15
    }
]

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Updated data.json with the 4 provided news items.")
