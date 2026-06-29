css = """
/* ==========================================================================
   Vision List Styling
   ========================================================================== */
.vision-list {
    list-style: none;
    padding: 0;
    margin: 2rem 0 0 0;
    text-align: left;
    display: inline-block;
}

.vision-list li {
    font-size: 1.1rem;
    color: var(--text-color);
    margin-bottom: 0.8rem;
    position: relative;
    padding-left: 2rem;
    line-height: 1.6;
}

.vision-list li::before {
    content: '✓';
    position: absolute;
    left: 0;
    color: var(--accent-color);
    font-weight: bold;
    font-size: 1.2rem;
}

@media (max-width: 768px) {
    .vision-list li {
        font-size: 1rem;
    }
}
"""

with open('style.css', 'a', encoding='utf-8') as f:
    f.write(css)
print("CSS appended.")
