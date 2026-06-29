import re

new_css = """

/* ==========================================================================
   Premium News & Activity Cards
   ========================================================================== */
.activity-feed {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
    gap: 2.5rem;
    padding: 2rem 0;
}

.activity-card {
    background: #7a0000; /* Deep PSL Red */
    border-radius: 16px;
    overflow: hidden;
    box-shadow: 0 15px 35px rgba(122, 0, 0, 0.15);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    display: flex;
    flex-direction: column;
    height: 100%;
}

.activity-card:hover {
    transform: translateY(-8px);
    box-shadow: 0 20px 40px rgba(122, 0, 0, 0.25);
}

.activity-img {
    width: 100%;
    height: 220px;
    background-color: #f0f0f0; /* Fallback */
}

.activity-img img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    display: block;
    border-bottom: 3px solid #d4af37; /* Gold divider */
}

.activity-content {
    padding: 2rem;
    flex-grow: 1;
    display: flex;
    flex-direction: column;
}

.activity-date {
    font-size: 0.85rem;
    color: rgba(255, 255, 255, 0.7);
    margin-bottom: 0.8rem;
    font-weight: 500;
    text-transform: uppercase;
    letter-spacing: 1px;
}

.activity-title {
    color: #d4af37; /* Premium Gold */
    font-size: 1.4rem;
    margin-top: 0;
    margin-bottom: 1rem;
    line-height: 1.4;
    font-weight: 600;
}

.activity-desc {
    color: #ffffff;
    font-size: 0.95rem;
    line-height: 1.6;
    margin-bottom: 0;
    opacity: 0.95;
}
"""

with open('style.css', 'a', encoding='utf-8') as f:
    f.write(new_css)

print("Premium News CSS appended to style.css!")
