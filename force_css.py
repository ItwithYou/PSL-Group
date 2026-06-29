import re

new_css = """

/* ==========================================================================
   Roadmap Timeline
   ========================================================================== */
.roadmap-section {
    padding: 6rem 2rem;
    position: relative;
    max-width: 1000px;
    margin: 0 auto;
}

.roadmap-header {
    text-align: center;
    margin-bottom: 5rem;
}

.roadmap-path-container {
    position: relative;
    padding: 2rem 0;
}

/* The Winding Path */
.roadmap-path-container::before {
    content: '';
    position: absolute;
    top: 0;
    bottom: 0;
    left: 50%;
    width: 4px;
    background: linear-gradient(to bottom, transparent, var(--accent-color), var(--accent-color), transparent);
    transform: translateX(-50%);
    border-radius: 4px;
}

.roadmap-stop {
    display: flex;
    justify-content: space-between;
    align-items: center;
    width: 100%;
    margin-bottom: 4rem;
    position: relative;
}

/* Alternate Left and Right Stops */
.roadmap-stop.left-stop {
    flex-direction: row-reverse;
}

.roadmap-card {
    width: 45%;
    background: var(--card-bg);
    border: 1px solid var(--border-color);
    padding: 2rem;
    border-radius: 16px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.05);
    position: relative;
    transition: transform 0.3s ease;
}

.roadmap-card:hover {
    transform: translateY(-5px);
}

.roadmap-point {
    width: 24px;
    height: 24px;
    background-color: var(--card-bg);
    border: 4px solid var(--accent-color);
    border-radius: 50%;
    position: absolute;
    left: 50%;
    transform: translateX(-50%);
    z-index: 2;
    box-shadow: 0 0 0 6px rgba(212, 175, 55, 0.2);
}

/* Connector Lines */
.roadmap-card::before {
    content: '';
    position: absolute;
    top: 50%;
    width: 10%;
    height: 2px;
    background-color: var(--accent-color);
    z-index: 1;
}

.left-stop .roadmap-card::before {
    right: -10%;
}

.right-stop .roadmap-card::before {
    left: -10%;
}

.roadmap-year {
    display: inline-block;
    padding: 0.4rem 1.2rem;
    background: var(--accent-color);
    color: var(--bg-color);
    font-weight: bold;
    border-radius: 20px;
    font-size: 0.9rem;
    margin-bottom: 1rem;
}

.roadmap-card h4 {
    font-size: 1.3rem;
    margin-bottom: 0.8rem;
    color: var(--text-color);
}

.roadmap-card p {
    color: var(--text-muted);
    line-height: 1.6;
}

@media (max-width: 768px) {
    .roadmap-path-container::before {
        left: 30px;
    }
    .roadmap-point {
        left: 30px;
    }
    .roadmap-stop {
        flex-direction: column !important;
        align-items: flex-end;
    }
    .roadmap-card {
        width: calc(100% - 70px);
    }
    .roadmap-card::before {
        display: none;
    }
}


/* ==========================================================================
   Organization Structure (Template Style)
   ========================================================================== */
.org-section {
    padding: 5rem 2rem;
    background-color: transparent;
    text-align: center;
}

.org-template-wrapper {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin: 0 auto;
    width: 100%;
    max-width: 1200px;
    padding-top: 2rem;
}

.org-center-chain {
    display: flex;
    flex-direction: column;
    align-items: center;
}

.org-capsule {
    padding: 1rem 2rem;
    border-radius: 40px;
    min-width: 250px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    box-shadow: 0 4px 15px rgba(0,0,0,0.05);
    z-index: 2;
    position: relative;
}

.org-capsule h4 {
    font-size: 1.1rem;
    margin-bottom: 0.3rem;
}

.org-capsule p {
    font-size: 0.9rem;
    margin: 0;
}

.solid-gold {
    background: #c29d5b; /* Muted gold from image */
    color: #fff;
    border: none;
}

.solid-gold h4, .solid-gold p {
    color: #fff;
}

.outline-gold {
    background: var(--card-bg);
    border: 2px solid #c29d5b;
    color: #c29d5b;
}

.outline-gold h4 {
    color: #c29d5b;
}

.outline-gold p {
    color: var(--text-muted);
}

.org-v-line {
    width: 2px;
    background-color: #c29d5b;
}

.org-v-line.center {
    height: 40px;
}

.org-v-line.short {
    height: 30px;
}

.org-h-split {
    width: 66%; /* Spans across 3 columns */
    height: 2px;
    background-color: #c29d5b;
}

.org-columns-container {
    display: flex;
    justify-content: center;
    gap: 3rem;
    width: 100%;
    margin-top: 0;
}

.org-column {
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 320px;
}

/* The vertical tree in the columns */
.org-left-tree {
    display: flex;
    flex-direction: column;
    width: 100%;
    position: relative;
    padding-left: 20px;
    margin-top: 10px;
}

.org-left-line {
    position: absolute;
    left: 20px;
    top: 0;
    bottom: 40px; /* stops before the last item's center */
    width: 2px;
    background-color: #c29d5b;
    z-index: 1;
}

.org-list-item {
    display: flex;
    align-items: center;
    margin-top: 25px;
    position: relative;
    z-index: 2;
}

.org-h-connector {
    width: 20px;
    height: 2px;
    background-color: #c29d5b;
}

.org-card-modern {
    background: var(--card-bg);
    border-radius: 16px;
    border-top: 4px solid #c29d5b;
    box-shadow: 0 8px 25px rgba(0,0,0,0.06);
    padding: 1.5rem;
    width: 100%;
    text-align: left;
    margin-left: -2px; /* Connects flush with connector */
}

.org-card-modern h4 {
    color: var(--text-color);
    font-size: 1.05rem;
    margin: 0;
}

@media (max-width: 1024px) {
    .org-columns-container {
        flex-direction: column;
        align-items: center;
        gap: 2rem;
    }
    .org-h-split {
        width: 2px;
        height: 40px;
    }
}
"""

with open('style.css', 'a', encoding='utf-8') as f:
    f.write(new_css)

print("CSS successfully appended!")
