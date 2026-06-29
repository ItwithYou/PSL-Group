import os

with open("style.css", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Compress Hero Section Padding
old_hero = """.hero-section {
    padding: 5rem 0 4rem 0;
    border-bottom: 1px solid var(--border-color);
}"""
new_hero = """.hero-section {
    padding: 2.5rem 0 1rem 0;
    border-bottom: 1px solid var(--border-color);
}"""
content = content.replace(old_hero, new_hero)

# 2. Compress Philosophy Section Padding
old_phil = """.philosophy-section {
    padding: 6.5rem 0;
    border-bottom: 1px solid var(--border-color);
}"""
new_phil = """.philosophy-section {
    padding: 2rem 0;
    border-bottom: 1px solid var(--border-color);
}"""
content = content.replace(old_phil, new_phil)

# 3. Fix the 5 things to fit on one line and be responsive
old_glass_grid = """.vision-glass-grid {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 2.5rem;
    margin-top: 4rem;
    width: 100%;
    padding-bottom: 2rem;
}"""
new_glass_grid = """.vision-glass-grid {
    display: flex;
    flex-wrap: nowrap;
    justify-content: space-between;
    align-items: center;
    gap: 1.5rem;
    margin-top: 2rem;
    width: 100%;
    padding-bottom: 2rem;
    overflow-x: auto; /* In case screen is extremely small, it will scroll instead of break layout */
}"""
content = content.replace(old_glass_grid, new_glass_grid)

# 4. Make glass cards responsive circles
old_glass_card = """.vision-glass-card {
    background: linear-gradient(135deg, rgba(255, 255, 255, 0.12) 0%, rgba(255, 255, 255, 0.02) 100%);
    backdrop-filter: blur(40px);
    -webkit-backdrop-filter: blur(40px);
    border-radius: 50%;
    width: 220px;
    height: 220px;
    padding: 1.5rem;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    border: 1px solid rgba(255, 255, 255, 0.1);
    box-shadow: 0 15px 35px rgba(0, 0, 0, 0.2);
    position: relative;
    cursor: pointer;
    transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}"""
new_glass_card = """.vision-glass-card {
    background: linear-gradient(135deg, rgba(255, 255, 255, 0.12) 0%, rgba(255, 255, 255, 0.02) 100%);
    backdrop-filter: blur(40px);
    -webkit-backdrop-filter: blur(40px);
    border-radius: 50%;
    width: clamp(130px, 16vw, 180px);
    height: clamp(130px, 16vw, 180px);
    padding: clamp(0.5rem, 1vw, 1.25rem);
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    border: 1px solid rgba(255, 255, 255, 0.1);
    box-shadow: 0 15px 35px rgba(0, 0, 0, 0.2);
    position: relative;
    cursor: pointer;
    flex-shrink: 0;
    transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}"""
content = content.replace(old_glass_card, new_glass_card)

# 5. Fix icons and text inside the circles to scale
old_glass_icon = """.glass-icon {
    font-size: 2.5rem;
    margin-bottom: 0.75rem;
    z-index: 2;
}

.glass-text {
    font-size: 0.95rem;
    font-weight: 500;
    color: var(--text-color);
    line-height: 1.4;
    z-index: 2;
}"""
new_glass_icon = """.glass-icon {
    font-size: clamp(1.5rem, 2vw, 2.5rem);
    margin-bottom: 0.5rem;
    z-index: 2;
}

.glass-text {
    font-size: clamp(0.7rem, 0.8vw, 0.95rem);
    font-weight: 500;
    color: var(--text-color);
    line-height: 1.3;
    z-index: 2;
}"""
content = content.replace(old_glass_icon, new_glass_icon)

with open("style.css", "w", encoding="utf-8") as f:
    f.write(content)
print("Updated CSS to fix one-page layout and single row 5-things.")
