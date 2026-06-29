css_block = """
/* ==========================================================================
   Organization Structure Section
   ========================================================================== */
.org-section {
    padding: 8rem 2rem;
    max-width: 1200px;
    margin: 0 auto;
    position: relative;
    z-index: 10;
}

.org-header {
    margin-bottom: 5rem;
    text-align: center;
}

.org-tree-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    position: relative;
}

/* Top Level */
.top-level {
    margin-bottom: 4rem;
    position: relative;
    z-index: 2;
}

.top-level::after {
    content: '';
    position: absolute;
    bottom: -4rem;
    left: 50%;
    transform: translateX(-50%);
    width: 2px;
    height: 4rem;
    background-color: var(--border-color);
    z-index: -1;
}

/* Second Level Branches */
.org-level-branches {
    display: flex;
    justify-content: center;
    gap: 2rem;
    flex-wrap: wrap;
    position: relative;
    width: 100%;
}

/* Horizontal connecting line */
.org-level-branches::before {
    content: '';
    position: absolute;
    top: -2px;
    left: calc(12.5% + 1rem); /* Roughly centering the line above the cards depending on wrap */
    right: calc(12.5% + 1rem);
    height: 2px;
    background-color: var(--border-color);
    z-index: 1;
}

/* Vertical lines dropping down to cards */
.org-branch {
    flex: 1 1 200px;
    max-width: 280px;
    position: relative;
    display: flex;
    justify-content: center;
    padding-top: 2rem;
}

.org-branch::before {
    content: '';
    position: absolute;
    top: 0;
    left: 50%;
    transform: translateX(-50%);
    width: 2px;
    height: 2rem;
    background-color: var(--border-color);
    z-index: 1;
}

/* Card Styling */
.org-card {
    background-color: var(--card-bg);
    border: 1px solid var(--border-light);
    border-radius: 12px;
    padding: 2rem 1.5rem;
    text-align: center;
    width: 100%;
    transition: all 0.4s ease;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.05);
    position: relative;
    z-index: 2;
    overflow: hidden;
}

[data-theme="dark"] .org-card,
[data-theme="tiffany"] .org-card {
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
}

.org-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: linear-gradient(135deg, rgba(255,255,255,0.05) 0%, rgba(255,255,255,0) 100%);
    pointer-events: none;
}

.org-card:hover {
    transform: translateY(-8px);
    border-color: var(--accent-color);
    box-shadow: 0 15px 40px rgba(0, 0, 0, 0.1);
}

[data-theme="tiffany"] .org-card:hover {
    box-shadow: 0 0 20px rgba(10, 186, 181, 0.2);
}

.primary-card {
    min-width: 320px;
    border-top: 4px solid var(--accent-color);
}

.secondary-card {
    border-top: 3px solid var(--text-muted);
}

.secondary-card:hover {
    border-top-color: var(--accent-color);
}

/* Text and Icons inside cards */
.org-icon {
    width: 48px;
    height: 48px;
    margin: 0 auto 1.5rem auto;
    background-color: rgba(10, 186, 181, 0.1); /* Subtle accent bg */
    color: var(--accent-color);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: all 0.3s ease;
}

[data-theme="tiffany"] .org-icon {
    color: var(--text-color);
    background-color: rgba(196, 169, 127, 0.2);
}

.org-card:hover .org-icon {
    background-color: var(--accent-color);
    color: #fff;
    transform: scale(1.1);
}

[data-theme="tiffany"] .org-card:hover .org-icon {
    background-color: var(--text-color);
    color: var(--bg-color);
}

.org-card h3 {
    font-size: 1.25rem;
    font-weight: 700;
    color: var(--text-color);
    margin-bottom: 0.5rem;
}

.org-card h4 {
    font-size: 1.1rem;
    font-weight: 600;
    color: var(--text-color);
    margin-bottom: 0.5rem;
    line-height: 1.4;
}

.org-card p {
    font-size: 0.9rem;
    color: var(--text-muted);
}

/* Responsive Org Chart */
@media (max-width: 900px) {
    .org-level-branches::before {
        display: none; /* Hide horizontal line on mobile */
    }
    
    .org-branch {
        flex: 1 1 100%;
        max-width: 350px;
        padding-top: 1rem;
        margin-bottom: 2rem;
    }

    .org-branch::before {
        display: none; /* Hide top drop lines */
    }

    .top-level::after {
        display: none;
    }
}
"""

with open('style.css', 'a', encoding='utf-8') as f:
    f.write(css_block)

print("Appended org structure css successfully.")
