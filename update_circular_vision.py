import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# The section we want to replace starts at /* ========================================================================== \n   Vision Glassmorphism Cards
old_block_pattern = r'/\* ==========================================================================\n   Vision Glassmorphism Cards\n   ========================================================================== \*/.*'

new_block = """/* ==========================================================================
   Vision Glassmorphism Cards (Premium Circular)
   ========================================================================== */
.vision-glass-grid {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 2.5rem;
    margin-top: 4rem;
    width: 100%;
    padding-bottom: 2rem;
}

.vision-glass-card {
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
    gap: 0.8rem;
    box-shadow: 
        0 25px 45px rgba(0, 0, 0, 0.2), 
        inset 0 1px 0 rgba(255, 255, 255, 0.3),
        inset 0 -1px 0 rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(255, 255, 255, 0.08);
    position: relative;
    overflow: hidden;
    z-index: 1;
}

[data-theme="light"] .vision-glass-card {
    background: linear-gradient(135deg, rgba(255, 255, 255, 0.8) 0%, rgba(255, 255, 255, 0.4) 100%);
    box-shadow: 
        0 25px 45px rgba(31, 38, 135, 0.1),
        inset 0 2px 0 rgba(255, 255, 255, 0.8),
        inset 0 -1px 0 rgba(255, 255, 255, 0.3);
    border: 1px solid rgba(255, 255, 255, 0.5);
}

.glass-icon {
    font-size: 2.5rem;
    filter: drop-shadow(0 2px 4px rgba(0,0,0,0.2));
    z-index: 2;
    margin-bottom: 0.2rem;
}

.glass-text {
    font-size: 0.95rem;
    font-weight: 600;
    color: var(--text-color);
    line-height: 1.4;
    z-index: 2;
}

/* Color Matching Glows */
.vision-glass-card::before {
    content: '';
    position: absolute;
    top: -50%;
    left: -50%;
    width: 200%;
    height: 200%;
    background: radial-gradient(circle, var(--glow-color) 0%, transparent 60%);
    opacity: 0.25;
    z-index: 0;
    pointer-events: none;
}

.card-honesty { --glow-color: #3b82f6; border-bottom: 2px solid #3b82f6; } 
.card-safety { --glow-color: #f59e0b; border-bottom: 2px solid #f59e0b; } 
.card-quality { --glow-color: #8b5cf6; border-bottom: 2px solid #8b5cf6; } 
.card-art { --glow-color: #ec4899; border-bottom: 2px solid #ec4899; } 
.card-time { --glow-color: #10b981; border-bottom: 2px solid #10b981; } 

@media (max-width: 600px) {
    .vision-glass-card {
        width: 180px;
        height: 180px;
        padding: 1rem;
    }
    .glass-icon { font-size: 2rem; }
    .glass-text { font-size: 0.85rem; }
}
"""

css = re.sub(old_block_pattern, new_block, css, flags=re.DOTALL)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Circular glass CSS updated!")
