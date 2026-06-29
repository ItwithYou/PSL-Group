import json

with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Update photos
data[0]["photoUrl"] = "assets/news1.jpg"
data[1]["photoUrl"] = "assets/news2.jpg"
data[2]["photoUrl"] = "assets/news3.jpg"
data[3]["photoUrl"] = "assets/news4.jpg"

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Updated data.json with matched photos.")
