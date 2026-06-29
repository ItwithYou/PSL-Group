import re

html = open('index.html', 'r', encoding='utf-8').read()

tabs = re.findall(r'<div.*?class="[^"]*tab-content[^"]*".*?>', html)
print("TABS FOUND:", len(tabs))
for t in tabs:
    print(t)

dock = re.findall(r'<li class="dock-item.*?</li>', html, flags=re.DOTALL)
print("DOCK ITEMS:", len(dock))
for d in dock:
    print(d[:100].replace('\n', ' '))
