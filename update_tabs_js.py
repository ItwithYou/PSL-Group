import re

with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# We want to replace initFilter completely.
# Let's find function initFilter() and replace it.

new_init_filter = """
// Tab Navigation logic using Bottom Floating Dock
function initFilter() {
    const dockItems = document.querySelectorAll('.dock-item');
    const tabContents = document.querySelectorAll('.tab-content');

    dockItems.forEach(item => {
        item.addEventListener('click', (e) => {
            e.preventDefault();
            
            const targetTabId = item.getAttribute('data-tab');
            if (!targetTabId) return;

            // Set active class on clicked dock item
            dockItems.forEach(di => di.classList.remove('active'));
            item.classList.add('active');

            // Show target tab, hide others
            tabContents.forEach(tab => {
                if (tab.id === targetTabId) {
                    tab.classList.add('active');
                } else {
                    tab.classList.remove('active');
                }
            });
            
            // Scroll to top
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });
    });
}
"""

js = re.sub(r'// Category Filtering logic.*?function initFilter\(\) \{.*?(?=\n// Modal Logic)', new_init_filter, js, flags=re.DOTALL)

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("app.js updated for tabs.")
