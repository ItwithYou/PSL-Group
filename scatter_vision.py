import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace the old grid styling
old_grid_css = r"""\.vision-glass-grid \{
    display: grid;
    grid-template-columns: repeat\(auto-fit, minmax\(240px, 1fr\)\);
    gap: 1\.5rem;
    margin-top: 2rem;
    width: 100%;
\}"""

new_grid_css = """/* Asymmetrical Modern "Scattered" Bento Grid */
.vision-glass-grid {
    display: grid;
    grid-template-columns: repeat(6, 1fr);
    grid-auto-rows: minmax(120px, auto);
    gap: 1.5rem;
    margin-top: 3rem;
    width: 100%;
    padding-bottom: 2rem;
}

.vision-glass-card {
    background: rgba(255, 255, 255, 0.05);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border-radius: 20px;
    padding: 2rem;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: flex-start;
    gap: 1rem;
    box-shadow: 0 15px 35px rgba(0, 0, 0, 0.1);
    transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    border: 1px solid rgba(255, 255, 255, 0.1);
    position: relative;
    overflow: hidden;
}

/* Specific sizing and positioning for the "scattered" modern look */
.vision-glass-card:nth-child(1) { grid-column: span 4; } /* Large top left */
.vision-glass-card:nth-child(2) { grid-column: span 2; } /* Small top right */
.vision-glass-card:nth-child(3) { grid-column: span 2; } /* Bottom left */
.vision-glass-card:nth-child(4) { grid-column: span 2; transform: translateY(20px); } /* Bottom middle, shifted down */
.vision-glass-card:nth-child(5) { grid-column: span 2; transform: translateY(-20px); } /* Bottom right, shifted up */

@media (max-width: 992px) {
    .vision-glass-grid { grid-template-columns: repeat(2, 1fr); }
    .vision-glass-card:nth-child(1) { grid-column: span 2; }
    .vision-glass-card:nth-child(2) { grid-column: span 1; }
    .vision-glass-card:nth-child(3) { grid-column: span 1; }
    .vision-glass-card:nth-child(4) { grid-column: span 1; transform: none; }
    .vision-glass-card:nth-child(5) { grid-column: span 1; transform: none; }
}

@media (max-width: 600px) {
    .vision-glass-grid { display: flex; flex-direction: column; }
    .vision-glass-card { transform: none !important; }
}"""

# Perform replacement
css = re.sub(old_grid_css, new_grid_css, css, flags=re.DOTALL)

# Also fix the inner card layout since we changed it to flex-direction column for the bento look
card_css_old = r"""\.vision-glass-card \{
    background: rgba\(255, 255, 255, 0\.05\);
.*?
\}"""
# We already included .vision-glass-card inside new_grid_css, so we must remove the old .vision-glass-card block completely to prevent conflict.
css = re.sub(card_css_old, '', css, flags=re.DOTALL)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Scattered bento grid applied!")
