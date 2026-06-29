import re

with open("style.css", "r", encoding="utf-8") as f:
    css = f.read()

# FIX 1: THE ROADMAP CATASTROPHE
# We need to completely wipe the current roadmap section and replace it with clean CSS.
start_marker = "/* Horizontal Roadmap Layout"
end_marker = "/* Organization Structure (Template Style)"

start_idx = css.find(start_marker)
end_idx = css.find(end_marker)

if start_idx != -1 and end_idx != -1:
    clean_roadmap = """/* Horizontal Roadmap Layout
   ========================================================================== */
.roadmap-path-container {
    position: relative;
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 12rem 2rem;
    width: 100%;
    max-width: 1200px;
    margin: 0 auto;
    gap: 2rem;
}

/* The Horizontal Line */
.roadmap-path-container::before {
    content: '';
    position: absolute;
    top: 50%;
    left: 2rem;
    right: 2rem;
    height: 2px;
    background: var(--accent-color);
    transform: translateY(-50%);
    z-index: 0;
    width: 0;
    animation: drawLine 1.5s ease-out forwards;
}

@keyframes drawLine {
    to { width: calc(100% - 4rem); }
}

.roadmap-stop {
    position: relative;
    display: flex;
    justify-content: center;
    align-items: center;
    width: 320px;
    z-index: 1;
}

/* The Connection Point */
.roadmap-point {
    width: 16px;
    height: 16px;
    background: #ffffff;
    border: 3px solid var(--accent-color);
    border-radius: 50%;
    box-shadow: 0 0 15px rgba(197, 160, 89, 0.6);
    position: relative;
    z-index: 2;
}

[data-theme="dark"] .roadmap-point {
    background: var(--bg-color);
}

/* The Glassmorphism Card */
.roadmap-card {
    position: absolute;
    width: 300px;
    background: rgba(255, 255, 255, 0.7);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border: 1px solid rgba(197, 160, 89, 0.4);
    border-top: 3px solid var(--accent-color);
    padding: 2.5rem 2rem;
    border-radius: 16px;
    box-shadow: 0 15px 35px rgba(0, 0, 0, 0.05), inset 0 0 0 1px rgba(255, 255, 255, 0.5);
    opacity: 0;
    animation: fadeInUpCard 0.8s cubic-bezier(0.25, 0.8, 0.25, 1) forwards;
    transition: transform 0.4s cubic-bezier(0.25, 0.8, 0.25, 1), box-shadow 0.4s ease, border-color 0.4s ease;
}

[data-theme="dark"] .roadmap-card {
    background: rgba(10, 37, 64, 0.8);
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
}

@keyframes fadeInUpCard {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
}

/* Precise Staggered Zig-Zag Layout */
.roadmap-stop:nth-child(1) .roadmap-card { bottom: 40px; animation-delay: 0.5s; }
.roadmap-stop:nth-child(2) .roadmap-card { top: 40px; animation-delay: 0.8s; }
.roadmap-stop:nth-child(3) .roadmap-card { bottom: 40px; animation-delay: 1.1s; }

/* Connecting Vertical Lines */
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

.roadmap-card:hover {
    box-shadow: 0 30px 60px rgba(0, 0, 0, 0.08), 0 0 40px rgba(197, 160, 89, 0.15), inset 0 0 0 1px rgba(255, 255, 255, 0.8);
    border-color: rgba(255, 255, 255, 0.8);
}
.roadmap-stop:nth-child(1) .roadmap-card:hover { transform: translateY(-5px); }
.roadmap-stop:nth-child(2) .roadmap-card:hover { transform: translateY(5px); }
.roadmap-stop:nth-child(3) .roadmap-card:hover { transform: translateY(-5px); }

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

@media (max-width: 900px) {
    .roadmap-path-container {
        padding: 14rem 2rem;
        overflow-x: auto;
        justify-content: flex-start;
        gap: 2rem;
        scroll-snap-type: x mandatory;
        scrollbar-width: none;
    }
    .roadmap-path-container::-webkit-scrollbar {
        display: none;
    }
    .roadmap-path-container::before {
        width: 1000px !important;
        animation: none;
    }
    .roadmap-stop {
        min-width: 280px;
        scroll-snap-align: center;
    }
}

"""
    # Replace the chunk
    css = css[:start_idx] + clean_roadmap + "\n\n" + css[end_idx:]


# FIX 2: NEWS GRID
# Find activity-feed-grid and change to 4 columns
old_grid_pattern = re.compile(r'\.activity-feed-grid\s*{[^}]+}')

def replace_grid(match):
    return """.activity-feed-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 1.5rem;
    margin-top: 3rem;
}
@media (max-width: 1200px) {
    .activity-feed-grid { grid-template-columns: repeat(2, 1fr); }
}
@media (max-width: 768px) {
    .activity-feed-grid { grid-template-columns: 1fr; }
}"""

css = old_grid_pattern.sub(replace_grid, css)

with open("style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Fixed roadmap and news layouts")
