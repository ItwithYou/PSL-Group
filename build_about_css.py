import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace Chronology and Timeline CSS
chrono_pattern = r'/\* ==========================================================================\n   Chronology & Timeline\n   ========================================================================== \*/.*?/\* ==========================================================================\n   Organization Structure'

new_chrono_css = """/* ==========================================================================
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
   Organization Structure"""

css = re.sub(chrono_pattern, new_chrono_css, css, flags=re.DOTALL)

# Replace Organization Structure CSS
org_pattern = r'/\* ==========================================================================\n   Organization Structure\n   ========================================================================== \*/.*?/\* ==========================================================================\n   Project Showcase'

new_org_css = """/* ==========================================================================
   Organization Structure
   ========================================================================== */
.org-section {
    padding: 4rem 2rem;
    background-color: transparent;
    text-align: center;
}

.org-header {
    margin-bottom: 4rem;
}

/* Tree Structure Wrapper */
.org-tree-wrapper {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin: 0 auto;
    width: 100%;
    max-width: 1200px;
    overflow-x: auto;
    padding: 1rem 0 3rem 0;
}

.tree-level {
    display: flex;
    justify-content: center;
    position: relative;
    width: 100%;
}

.tree-nodes-row {
    display: flex;
    justify-content: center;
    gap: 3rem;
    width: 100%;
}

.tree-nodes-row.five-cols {
    gap: 1.5rem;
    flex-wrap: nowrap;
}

/* Connecting Lines */
.tree-line.vertical {
    width: 2px;
    height: 40px;
    background-color: var(--accent-color);
    margin: 0 auto;
}

.tree-line.vertical.center-passthrough {
    height: 100%;
    position: absolute;
    top: -20px; /* Connects to horizontal branch above */
    left: 50%;
    transform: translateX(-50%);
    z-index: -1;
}

.tree-branch-horizontal {
    position: absolute;
    top: -20px;
    height: 2px;
    background-color: var(--accent-color);
}

.tree-branch-horizontal.wide {
    width: calc(100% - 50% - 200px); /* Approx distance between Advisor and VP */
}

.tree-branch-horizontal.super-wide {
    width: 80%; /* Covers the 5 units */
}

/* Node Cards */
.tree-node {
    background: var(--card-bg);
    border: 1px solid var(--border-color);
    border-radius: 12px;
    padding: 1.5rem 1rem;
    min-width: 180px;
    max-width: 240px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.05);
    display: flex;
    flex-direction: column;
    align-items: center;
    position: relative;
}

.tree-node::before {
    content: '';
    position: absolute;
    top: -20px;
    left: 50%;
    width: 2px;
    height: 20px;
    background-color: var(--accent-color);
}

.president-node::before {
    display: none; /* Top node has no line above */
}

/* Special Highlighting */
.president-node {
    background: linear-gradient(135deg, var(--card-bg) 0%, rgba(212, 175, 55, 0.1) 100%);
    border: 2px solid var(--accent-color);
}

.advisor-node {
    background: rgba(59, 130, 246, 0.05);
    border-color: rgba(59, 130, 246, 0.3);
}

.vp-node {
    background: rgba(245, 158, 11, 0.05);
    border-color: rgba(245, 158, 11, 0.3);
}

.manager-node {
    background: rgba(16, 185, 129, 0.05);
    border-color: rgba(16, 185, 129, 0.3);
}

.unit-node {
    background: var(--card-bg);
    min-width: 150px;
    font-size: 0.9rem;
    padding: 1.2rem 0.8rem;
}

/* Typography inside Nodes */
.tree-node h4 {
    font-size: 1.1rem;
    color: var(--text-color);
    margin-bottom: 0.5rem;
    text-align: center;
}

.tree-node p {
    font-size: 0.9rem;
    color: var(--text-muted);
    text-align: center;
    margin: 0;
}

.unit-node h4 {
    font-size: 1rem;
    margin: 0;
}

/* Mobile Scroll Support */
@media (max-width: 1024px) {
    .tree-nodes-row.five-cols {
        min-width: 900px; /* Force scroll */
    }
    .tree-branch-horizontal.super-wide {
        width: 800px;
    }
}

/* ==========================================================================
   Project Showcase"""

css = re.sub(org_pattern, new_org_css, css, flags=re.DOTALL)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("CSS updated for Roadmap and Organization Tree!")
