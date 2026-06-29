import re

with open("style.css", "r", encoding="utf-8") as f:
    css = f.read()

# 1. Remove old vision CSS
old_vision_css = r"""\.vision-glass-grid\s*{.*?}\s*\.vision-glass-card\s*{.*?}\s*\.vision-glass-card:hover\s*{.*?}\s*\.glass-icon\s*{.*?}\s*\.glass-text\s*{.*?}\s*\.card-honesty\s*{.*?}\s*\.card-safety\s*{.*?}\s*\.card-quality\s*{.*?}\s*\.card-art\s*{.*?}\s*\.card-time\s*{.*?}\s*"""
# We also have to be careful about not deleting other things. 
# It's better to just append the new CSS and maybe leave the old CSS (it won't hurt, but I can try to replace if I know the exact string).
# Actually, the user's requirement is just to add the orbit css. I'll just append it to the file.

orbit_css = """
/* ==========================================================================
   Orbit Vision Layout
   ========================================================================== */
.philosophy-content {
    width: 100%;
    padding: 2rem 0 6rem 0;
    overflow: hidden;
}

.orbit-container {
    position: relative;
    width: 700px;
    height: 700px;
    margin: 0 auto;
    border-radius: 50%;
    /* Optional subtle ring background */
    /* border: 1px dashed rgba(10, 37, 64, 0.1); */
}

.orbit-center {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 350px;
    text-align: center;
    z-index: 10;
    background: var(--bg-color);
    padding: 2rem;
    border-radius: 50%;
    box-shadow: 0 0 50px rgba(255,255,255,0.8);
}

.orbit-center .section-tag {
    justify-content: center;
    margin-bottom: 1rem;
}

.orbit-center .philosophy-text {
    font-size: 1.1rem;
    line-height: 1.7;
    margin: 0;
}

.glass-orb {
    position: absolute;
    width: 160px;
    height: 160px;
    background: rgba(255, 255, 255, 0.7);
    backdrop-filter: blur(15px);
    -webkit-backdrop-filter: blur(15px);
    border: 1px solid rgba(255, 255, 255, 0.6);
    border-radius: 50%;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    padding: 1rem;
    box-shadow: 0 15px 35px rgba(0,0,0,0.05);
    transition: all 0.5s cubic-bezier(0.25, 0.8, 0.25, 1);
    z-index: 5;
    cursor: default;
}

.orb-icon {
    font-size: 2.5rem;
    margin-bottom: 0.5rem;
    transition: transform 0.4s ease;
}

.orb-text {
    font-size: 0.85rem;
    font-weight: 600;
    color: var(--text-color);
    opacity: 0;
    transform: translateY(10px);
    transition: all 0.4s ease;
    position: absolute;
    bottom: 1.5rem;
}

/* Hover Effects */
.glass-orb:hover {
    transform: translate(-50%, -50%) translateY(-10px) scale(1.1) !important;
    z-index: 20;
}
.glass-orb:hover .orb-icon {
    transform: translateY(-10px);
}
.glass-orb:hover .orb-text {
    opacity: 1;
    transform: translateY(0);
}

/* Unique Glows */
.orb-honesty { box-shadow: 0 15px 35px rgba(0, 0, 255, 0.05); }
.orb-honesty:hover { box-shadow: 0 20px 50px rgba(0, 0, 255, 0.15), inset 0 0 0 2px rgba(0,0,255,0.1); }

.orb-safety { box-shadow: 0 15px 35px rgba(255, 165, 0, 0.05); }
.orb-safety:hover { box-shadow: 0 20px 50px rgba(255, 165, 0, 0.15), inset 0 0 0 2px rgba(255,165,0,0.1); }

.orb-quality { box-shadow: 0 15px 35px rgba(0, 255, 255, 0.05); }
.orb-quality:hover { box-shadow: 0 20px 50px rgba(0, 255, 255, 0.15), inset 0 0 0 2px rgba(0,255,255,0.1); }

.orb-art { box-shadow: 0 15px 35px rgba(255, 0, 255, 0.05); }
.orb-art:hover { box-shadow: 0 20px 50px rgba(255, 0, 255, 0.15), inset 0 0 0 2px rgba(255,0,255,0.1); }

.orb-time { box-shadow: 0 15px 35px rgba(0, 255, 0, 0.05); }
.orb-time:hover { box-shadow: 0 20px 50px rgba(0, 255, 0, 0.15), inset 0 0 0 2px rgba(0,255,0,0.1); }


/* Positioning (72 degrees apart) on a 350px radius circle */
/* r = 350px. 
   1: top center (0 deg) -> x=0, y=-r 
   2: top right (72 deg) -> x=r*sin(72), y=-r*cos(72) -> x=333, y=-108
   3: bottom right (144 deg) -> x=r*sin(144), y=-r*cos(144) -> x=206, y=283
   4: bottom left (216 deg) -> x=r*sin(216), y=-r*cos(216) -> x=-206, y=283
   5: top left (288 deg) -> x=r*sin(288), y=-r*cos(288) -> x=-333, y=-108
   Center of container is (350, 350).
*/
.orb-1 { top: 0%; left: 50%; transform: translate(-50%, -50%); }
.orb-2 { top: 19%; left: 97.5%; transform: translate(-50%, -50%); }
.orb-3 { top: 90%; left: 79%; transform: translate(-50%, -50%); }
.orb-4 { top: 90%; left: 21%; transform: translate(-50%, -50%); }
.orb-5 { top: 19%; left: 2.5%; transform: translate(-50%, -50%); }

/* Mobile Layout */
@media (max-width: 900px) {
    .orbit-container {
        width: 100%;
        height: auto;
        border-radius: 0;
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    
    .orbit-center {
        position: relative;
        top: 0; left: 0; transform: none;
        width: 100%;
        padding: 0 1rem;
        box-shadow: none;
        background: transparent;
        margin-bottom: 3rem;
    }
    
    #vision-list {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 1.5rem;
        width: 100%;
    }
    
    .glass-orb {
        position: relative;
        top: 0 !important; left: 0 !important; transform: none !important;
        width: 100%;
        height: auto;
        border-radius: 16px;
        padding: 2rem 1rem;
    }
    
    .glass-orb:hover {
        transform: translateY(-5px) !important;
    }
    
    .orb-icon {
        transform: none !important;
    }
    
    .orb-text {
        opacity: 1;
        transform: none;
        position: relative;
        bottom: 0;
        margin-top: 1rem;
    }
    
    /* Make the last odd orb span 2 columns */
    .glass-orb:last-child:nth-child(odd) {
        grid-column: 1 / -1;
    }
}
"""

if "Orbit Vision Layout" not in css:
    css += "\n" + orbit_css

with open("style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Appended orbit CSS")
