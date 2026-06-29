import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Add animate-on-scroll to contact card
content = content.replace('class="contact-card"', 'class="contact-card animate-on-scroll"')

# Add animate-on-scroll to hero text elements
content = content.replace('class="hero-title"', 'class="hero-title animate-on-scroll"')
content = content.replace('class="hero-subtitle"', 'class="hero-subtitle animate-on-scroll"')
content = content.replace('class="hero-desc"', 'class="hero-desc animate-on-scroll"')

# Add animate-on-scroll to section titles
content = content.replace('class="section-title"', 'class="section-title animate-on-scroll"')
content = content.replace('class="section-tag"', 'class="section-tag animate-on-scroll"')
content = content.replace('class="about-lead"', 'class="about-lead animate-on-scroll"')
content = content.replace('class="philosophy-text"', 'class="philosophy-text animate-on-scroll"')

# Add animate-on-scroll to about pillars
content = content.replace('class="about-pillar"', 'class="about-pillar animate-on-scroll"')

# Add animate-on-scroll to project entries
content = content.replace('class="project-entry"', 'class="project-entry animate-on-scroll"')

# Add animate-on-scroll to footer elements
content = content.replace('class="footer-brand"', 'class="footer-brand animate-on-scroll"')
content = content.replace('class="footer-group"', 'class="footer-group animate-on-scroll"')

# Remove any duplicates just in case
content = content.replace('animate-on-scroll animate-on-scroll', 'animate-on-scroll')

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Updated index.html with animate-on-scroll classes.")
