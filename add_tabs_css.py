css_tabs = """
/* ==========================================================================
   Tab Navigation System
   ========================================================================== */
.tab-content {
    display: none;
    animation: fadeIn 0.5s ease;
}

.tab-content.active {
    display: block;
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(10px); }
    to { opacity: 1; transform: translateY(0); }
}

/* Activity Feed Styling */
.activity-feed-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
    gap: 2rem;
    margin-top: 3rem;
}

.activity-card {
    background: var(--card-bg);
    border: 1px solid var(--border-light);
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 5px 15px rgba(0,0,0,0.05);
    transition: transform 0.3s;
}

.activity-card:hover {
    transform: translateY(-5px);
    border-color: var(--accent-color);
}

.activity-img img {
    width: 100%;
    height: 220px;
    object-fit: cover;
    display: block;
}

.activity-content {
    padding: 1.5rem;
}

.activity-date {
    font-size: 0.85rem;
    color: var(--accent-color);
    font-weight: 600;
    margin-bottom: 0.5rem;
    display: block;
}

.activity-title {
    font-size: 1.25rem;
    margin: 0 0 1rem 0;
    color: var(--text-color);
}

.activity-desc {
    color: var(--text-muted);
    font-size: 0.95rem;
    line-height: 1.5;
}
"""

with open('style.css', 'a', encoding='utf-8') as f:
    f.write(css_tabs)

print("Tabs CSS added.")
