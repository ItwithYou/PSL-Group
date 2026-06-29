import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the phone number globally
html = html.replace('+856 20 XX XXX XXX', '+856 20 2898 8888')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Phone number updated in index.html!")
