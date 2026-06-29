import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

tabs = re.findall(r'<div[^>]*id="tab-[^>]*>', html)
print("Tabs found:", tabs)
