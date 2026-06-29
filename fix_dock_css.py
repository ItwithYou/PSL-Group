css_dock_fix = """
/* ==========================================================================
   Dock Fixes
   ========================================================================== */
.dock-item {
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 0.5rem 1rem;
    border-radius: 30px;
    cursor: pointer;
    transition: all 0.3s ease;
    white-space: nowrap;
}

.dock-item:hover, .dock-item.active {
    background-color: var(--card-bg);
    box-shadow: 0 4px 15px rgba(0,0,0,0.05);
}

.dock-label {
    font-weight: 600;
    font-size: 0.95rem;
    color: var(--text-color);
    transition: color 0.3s ease;
}

.dock-item.active .dock-label {
    color: var(--accent-color);
}
"""

with open('style.css', 'a', encoding='utf-8') as f:
    f.write(css_dock_fix)
