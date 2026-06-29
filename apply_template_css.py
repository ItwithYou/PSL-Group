import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace the Org Chart CSS block
org_pattern = r'/\* ==========================================================================\n   Organization Structure\n   ========================================================================== \*/.*?/\* ==========================================================================\n   Project Showcase'

new_org_css = """/* ==========================================================================
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

/* ==========================================================================
   Project Showcase"""

css = re.sub(org_pattern, new_org_css, css, flags=re.DOTALL)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("CSS updated to template style!")
