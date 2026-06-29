import re

with open("style.css", "r", encoding="utf-8") as f:
    css = f.read()

# Make roadmap path container centered and add space
pattern_container = re.compile(r'\.roadmap-path-container\s*{.*?}', re.DOTALL)
new_container = """.roadmap-path-container {
    position: relative;
    display: flex;
    justify-content: center; /* Center the items instead of space-between */
    align-items: center;
    padding: 12rem 2rem;
    width: 100%;
    max-width: 1200px;
    margin: 0 auto;
    gap: 2rem; /* Add gap for centering */
}"""
if ".roadmap-path-container" in css:
    css = pattern_container.sub(new_container, css)


# Fix the roadmap-card styling and animations
# The user wants art and premium feel. Let's make sure the timeline is gorgeous.
pattern_card = re.compile(r'\.roadmap-card\s*{.*?}', re.DOTALL)
new_card = """.roadmap-card {
    position: absolute;
    width: 300px; /* Fixed width instead of 100% to ensure they don't stretch */
    background: rgba(255, 255, 255, 0.7); /* Slightly more transparent */
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border: 1px solid rgba(197, 160, 89, 0.4); /* Gold border but softer */
    border-top: 3px solid var(--accent-color); /* Premium gold accent top */
    padding: 2.5rem 2rem; /* More padding */
    border-radius: 16px; /* Smoother border radius */
    box-shadow: 0 15px 35px rgba(0, 0, 0, 0.05), inset 0 0 0 1px rgba(255, 255, 255, 0.5); /* Glowing inner border */
    opacity: 0;
    animation: fadeInUpCard 0.8s cubic-bezier(0.25, 0.8, 0.25, 1) forwards; /* Smoother animation curve */
    transition: transform 0.4s cubic-bezier(0.25, 0.8, 0.25, 1), box-shadow 0.4s ease, border-color 0.4s ease;
}"""
if ".roadmap-card" in css:
    css = pattern_card.sub(new_card, css)


# Fix the zigzag positioning to be more precise
pattern_zigzag = re.compile(r'\.roadmap-stop:nth-child\(1\) \.roadmap-card { bottom: 30px; animation-delay: 0\.5s; }\s*\.roadmap-stop:nth-child\(2\) \.roadmap-card { top: 30px; animation-delay: 0\.8s; }\s*\.roadmap-stop:nth-child\(3\) \.roadmap-card { bottom: 30px; animation-delay: 1\.1s; }', re.DOTALL)

new_zigzag = """/* Precise Staggered Zig-Zag Layout */
.roadmap-stop:nth-child(1) .roadmap-card { 
    bottom: 40px; 
    animation-delay: 0.5s; 
}
.roadmap-stop:nth-child(2) .roadmap-card { 
    top: 40px; 
    animation-delay: 0.8s; 
}
.roadmap-stop:nth-child(3) .roadmap-card { 
    bottom: 40px; 
    animation-delay: 1.1s; 
}

/* Add a connecting vertical line from dot to card */
.roadmap-stop:nth-child(1)::before,
.roadmap-stop:nth-child(3)::before {
    content: '';
    position: absolute;
    bottom: 10px;
    left: 50%;
    width: 2px;
    height: 30px;
    background: linear-gradient(to top, var(--accent-color), transparent);
    transform: translateX(-50%);
    opacity: 0;
    animation: fadeInLine 0.5s ease forwards 0.5s;
}
.roadmap-stop:nth-child(3)::before { animation-delay: 1.1s; }

.roadmap-stop:nth-child(2)::before {
    content: '';
    position: absolute;
    top: 10px;
    left: 50%;
    width: 2px;
    height: 30px;
    background: linear-gradient(to bottom, var(--accent-color), transparent);
    transform: translateX(-50%);
    opacity: 0;
    animation: fadeInLine 0.5s ease forwards 0.8s;
}

@keyframes fadeInLine {
    to { opacity: 1; }
}
"""
if ".roadmap-stop:nth-child(1)" in css:
    css = pattern_zigzag.sub(new_zigzag, css)


# Fix hover effect to be premium
pattern_hover = re.compile(r'\.roadmap-card:hover\s*{\s*box-shadow:\s*0 25px 50px rgba\(0, 0, 0, 0\.1\);\s*}', re.DOTALL)
new_hover = """.roadmap-card:hover {
    box-shadow: 0 30px 60px rgba(0, 0, 0, 0.08), 0 0 40px rgba(197, 160, 89, 0.15), inset 0 0 0 1px rgba(255, 255, 255, 0.8);
    border-color: rgba(255, 255, 255, 0.8);
}"""
if ".roadmap-card:hover" in css:
    css = pattern_hover.sub(new_hover, css)

# Make year look premium
year_css = """
.roadmap-year {
    display: inline-block;
    background: var(--accent-color);
    color: white;
    padding: 0.3rem 1rem;
    border-radius: 20px;
    font-size: 0.85rem;
    font-weight: 700;
    margin-bottom: 1rem;
    box-shadow: 0 5px 15px rgba(197, 160, 89, 0.4);
}
.roadmap-card h4 {
    font-size: 1.25rem;
    margin-bottom: 0.5rem;
    color: var(--text-color);
}
.roadmap-card p {
    font-size: 0.9rem;
    color: var(--text-color);
    opacity: 0.8;
}
"""
if ".roadmap-year" not in css:
    # insert before @media
    css = css.replace("@media (max-width: 900px)", year_css + "\n@media (max-width: 900px)")


with open("style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Updated roadmap CSS for premium feel")
