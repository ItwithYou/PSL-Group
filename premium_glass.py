import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace the glass card CSS block
old_card_css = r"""\.vision-glass-card \{
    background: rgba\(255, 255, 255, 0\.05\);.*?position: relative;
    overflow: hidden;
\}"""

new_card_css = """/* Ultra-Premium Glassmorphism */
.vision-glass-card {
    background: linear-gradient(135deg, rgba(255, 255, 255, 0.12) 0%, rgba(255, 255, 255, 0.02) 100%);
    backdrop-filter: blur(40px);
    -webkit-backdrop-filter: blur(40px);
    border-radius: 24px;
    padding: 2.5rem 2rem;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    gap: 1.2rem;
    box-shadow: 
        0 25px 45px rgba(0, 0, 0, 0.2), 
        inset 0 1px 0 rgba(255, 255, 255, 0.3),
        inset 0 -1px 0 rgba(255, 255, 255, 0.05);
    transition: all 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    border: 1px solid rgba(255, 255, 255, 0.08);
    position: relative;
    overflow: hidden;
    z-index: 1;
}"""

css = re.sub(old_card_css, new_card_css, css, flags=re.DOTALL)

# Replace the light mode override
old_light_css = r"""\[data-theme="light"\] \.vision-glass-card \{
    background: rgba\(255, 255, 255, 0\.4\);
    box-shadow: 0 8px 32px 0 rgba\(31, 38, 135, 0\.07\);
    border: 1px solid rgba\(255, 255, 255, 0\.4\);
\}"""

new_light_css = """[data-theme="light"] .vision-glass-card {
    background: linear-gradient(135deg, rgba(255, 255, 255, 0.8) 0%, rgba(255, 255, 255, 0.4) 100%);
    box-shadow: 
        0 25px 45px rgba(31, 38, 135, 0.1),
        inset 0 2px 0 rgba(255, 255, 255, 0.8),
        inset 0 -1px 0 rgba(255, 255, 255, 0.3);
    border: 1px solid rgba(255, 255, 255, 0.5);
}"""

css = re.sub(old_light_css, new_light_css, css, flags=re.DOTALL)

# Upgrade Hover effect
old_hover_css = r"""\.vision-glass-card:hover \{
    transform: translateY\(-5px\);
\}"""

new_hover_css = """.vision-glass-card:hover {
    transform: translateY(-10px) scale(1.02);
    background: linear-gradient(135deg, rgba(255, 255, 255, 0.18) 0%, rgba(255, 255, 255, 0.05) 100%);
    box-shadow: 
        0 35px 55px rgba(0, 0, 0, 0.3),
        inset 0 1px 0 rgba(255, 255, 255, 0.4);
    z-index: 10;
}
[data-theme="light"] .vision-glass-card:hover {
    background: linear-gradient(135deg, rgba(255, 255, 255, 0.95) 0%, rgba(255, 255, 255, 0.6) 100%);
    box-shadow: 
        0 35px 55px rgba(31, 38, 135, 0.15),
        inset 0 2px 0 rgba(255, 255, 255, 1);
}"""

css = re.sub(old_hover_css, new_hover_css, css, flags=re.DOTALL)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Premium glass applied!")
