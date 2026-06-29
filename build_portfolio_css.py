import re

new_css = """

/* ==========================================================================
   Corporate Portfolio Section (New Projects Tab)
   ========================================================================== */
.portfolio-section {
    padding: 4rem 2rem;
    max-width: 1200px;
    margin: 0 auto;
}

.portfolio-header {
    text-align: center;
    margin-bottom: 4rem;
}

.portfolio-subtitle {
    color: var(--text-muted);
    font-size: 1.1rem;
    max-width: 600px;
    margin: 1rem auto 0;
}

.portfolio-tier {
    margin-bottom: 5rem;
    position: relative;
}

.tier-header {
    display: flex;
    align-items: center;
    gap: 1.5rem;
    margin-bottom: 2rem;
    border-bottom: 2px solid var(--border-color);
    padding-bottom: 1rem;
}

.tier-header h3 {
    font-size: 1.8rem;
    margin: 0;
    color: var(--text-color);
}

.tier-badge {
    background: linear-gradient(135deg, #d4af37, #c29d5b);
    color: white;
    padding: 0.4rem 1rem;
    border-radius: 30px;
    font-weight: 600;
    font-size: 0.95rem;
    box-shadow: 0 4px 10px rgba(212, 175, 55, 0.3);
}

.tier-subtitle {
    font-size: 1.1rem;
    color: var(--text-muted);
    margin-bottom: 2rem;
    margin-top: -1rem;
}

/* Tier 1 Grid */
.tier-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
    gap: 2rem;
}

.portfolio-card {
    position: relative;
    background: var(--card-bg);
    border-radius: 16px;
    padding: 2.5rem 2rem;
    box-shadow: 0 10px 30px rgba(0,0,0,0.05);
    border: 1px solid var(--border-color);
    transition: transform 0.3s ease;
    overflow: hidden;
}

.portfolio-card:hover {
    transform: translateY(-5px);
}

.card-glass-bg {
    position: absolute;
    top: 0; left: 0; right: 0; height: 5px;
    background: linear-gradient(90deg, #8b0000, #d4af37);
}

.card-icon {
    font-size: 2.5rem;
    margin-bottom: 1rem;
}

.portfolio-card h4 {
    font-size: 1.25rem;
    margin: 0 0 0.5rem 0;
    color: var(--text-color);
}

.card-value {
    font-size: 1.5rem;
    font-weight: 700;
    color: #d4af37;
    margin: 0 0 1.5rem 0;
}

.card-desc {
    color: var(--text-muted);
    line-height: 1.6;
    margin: 0;
}

.card-list {
    list-style: none;
    padding: 0;
    margin: 0;
}

.card-list li {
    position: relative;
    padding-left: 1.5rem;
    margin-bottom: 0.8rem;
    color: var(--text-muted);
    line-height: 1.4;
}

.card-list li::before {
    content: '•';
    color: #8b0000;
    font-size: 1.5rem;
    position: absolute;
    left: 0;
    top: -4px;
}

/* Tier 2 Highways */
.highway-list {
    display: flex;
    flex-direction: column;
    gap: 1rem;
}

.highway-item {
    display: flex;
    align-items: center;
    background: var(--card-bg);
    border: 1px solid var(--border-color);
    border-radius: 12px;
    padding: 1.5rem;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.highway-item:hover {
    box-shadow: 0 8px 25px rgba(0,0,0,0.05);
    border-color: #d4af37;
}

.hw-icon {
    font-size: 2rem;
    margin-right: 1.5rem;
}

.hw-details {
    flex-grow: 1;
}

.hw-details h4 {
    margin: 0 0 0.3rem 0;
    font-size: 1.2rem;
    color: var(--text-color);
}

.hw-details p {
    margin: 0;
    color: var(--text-muted);
    font-size: 0.95rem;
}

.hw-length {
    font-size: 1.25rem;
    font-weight: 600;
    color: #8b0000;
    background: rgba(139, 0, 0, 0.05);
    padding: 0.5rem 1rem;
    border-radius: 8px;
}

/* Tier 3 Past Projects */
.past-projects-container {
    background: var(--card-bg);
    border: 1px solid var(--border-color);
    border-radius: 16px;
    padding: 2rem;
}

.past-list {
    list-style: none;
    padding: 0;
    margin: 0;
    display: grid;
    grid-template-columns: 1fr;
    gap: 1rem;
}

.past-list li {
    padding: 1rem;
    border-bottom: 1px solid var(--border-color);
    color: var(--text-color);
    font-size: 1rem;
    position: relative;
    padding-left: 2rem;
}

.past-list li:last-child {
    border-bottom: none;
}

.past-list li::before {
    content: '✓';
    position: absolute;
    left: 0;
    color: #d4af37;
    font-weight: bold;
}

@media (min-width: 768px) {
    .past-list {
        grid-template-columns: 1fr 1fr;
        gap: 1.5rem;
    }
    .past-list li {
        border-bottom: none;
        border-left: 1px solid var(--border-color);
        padding-left: 1.5rem;
    }
    .past-list li::before {
        left: -8px;
        background: var(--card-bg);
        width: 16px;
        text-align: center;
    }
}
"""

with open('style.css', 'a', encoding='utf-8') as f:
    f.write(new_css)

print("Corporate Portfolio CSS appended to style.css!")
