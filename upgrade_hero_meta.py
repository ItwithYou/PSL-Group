import re

with open("style.css", "r", encoding="utf-8") as f:
    content = f.read()

old_meta = """.hero-meta {
    background-color: var(--card-bg);
    border: 1px solid var(--border-color);
    border-top: 4px solid var(--accent-color);
    border-radius: 16px;
    padding: 3rem;
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.05);
    display: flex;
    flex-direction: column;
    gap: 2rem;
    transition: transform 0.4s cubic-bezier(0.25, 0.8, 0.25, 1), box-shadow 0.4s ease;
}

.hero-meta:hover {
    transform: translateY(-8px);
    box-shadow: 0 25px 50px rgba(0, 0, 0, 0.1);
}"""

new_meta = """.hero-meta {
    background: rgba(255, 255, 255, 0.45);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border: 1px solid rgba(255, 255, 255, 0.5);
    border-top: 4px solid var(--accent-color);
    border-radius: 16px;
    padding: 3.5rem 3rem;
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.08), inset 0 0 0 1px rgba(255, 255, 255, 0.3);
    display: flex;
    flex-direction: column;
    gap: 2.5rem;
    transition: transform 0.4s cubic-bezier(0.25, 0.8, 0.25, 1), box-shadow 0.4s ease, border-color 0.4s ease;
}

.hero-meta:hover {
    transform: translateY(-8px);
    box-shadow: 0 30px 60px rgba(0, 0, 0, 0.12), 0 0 30px rgba(197, 160, 89, 0.15), inset 0 0 0 1px rgba(255, 255, 255, 0.5);
    border-color: rgba(255, 255, 255, 0.8);
}

[data-theme="dark"] .hero-meta {
    background: rgba(10, 37, 64, 0.45);
    border: 1px solid rgba(255, 255, 255, 0.1);
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3), inset 0 0 0 1px rgba(255, 255, 255, 0.05);
}
[data-theme="dark"] .hero-meta:hover {
    box-shadow: 0 30px 60px rgba(0, 0, 0, 0.4), 0 0 30px rgba(197, 160, 89, 0.15), inset 0 0 0 1px rgba(255, 255, 255, 0.15);
    border-color: rgba(255, 255, 255, 0.25);
}"""

if old_meta in content:
    content = content.replace(old_meta, new_meta)
else:
    print("WARNING: Could not find old_meta in style.css")

with open("style.css", "w", encoding="utf-8") as f:
    f.write(content)
print("Updated .hero-meta glassmorphism")
