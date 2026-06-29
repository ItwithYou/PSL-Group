import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

if '.tab-content' not in css:
    tab_css = """
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
"""
    with open('style.css', 'a', encoding='utf-8') as f:
        f.write(tab_css)
    print("Tab CSS appended to style.css")
else:
    print("Tab CSS already exists in style.css. Maybe it's being overridden?")

# Also, the floating dock looks crammed because I removed the .dock-link elements but kept the styles for them maybe?
# The new dock HTML uses just .dock-item > .dock-label.
# Let's check how .dock-item and .dock-label are styled.
