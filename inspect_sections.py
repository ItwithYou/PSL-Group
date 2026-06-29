import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# I will find all sections by searching for <section...>
sections = re.findall(r'<section.*?>.*?</section>', html, flags=re.DOTALL)

# Let's see what sections we have:
print("Sections found:", len(sections))
for s in sections:
    print(re.search(r'<section.*?>', s).group(0))

