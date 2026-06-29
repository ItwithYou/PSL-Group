import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# The footer text is probably something like <div class="footer-right">Inspired by Reckon House</div>
# Or <p>Inspired by Reckon House</p>
# We will use regex to remove anything containing Inspired by Reckon House
html = re.sub(r'<[^>]*>Inspired by Reckon House</[^>]*>', '', html, flags=re.IGNORECASE)
html = re.sub(r'Inspired by Reckon House', '', html, flags=re.IGNORECASE)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Reckon House removed!")
