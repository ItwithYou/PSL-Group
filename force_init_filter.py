import re

with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

new_init_filter = """
// Category Filtering logic using Bottom Floating Dock
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
                    
                    // Force animations inside this tab to trigger since they were hidden
                    const animated = tab.querySelectorAll('.animate-on-scroll');
                    animated.forEach(el => {
                        el.classList.add('appear');
                        el.style.opacity = '1';
                        el.style.transform = 'translateY(0)';
                    });
                } else {
                    tab.classList.remove('active');
                }
            });
            
            // Scroll to top safely
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });
    });
}
"""

js = re.sub(r'// Category Filtering logic using Bottom Floating Dock\s*function initFilter\(\) \{.*?\}\s*(?=\n// Interactive Project Details Dialog)', new_init_filter.strip(), js, flags=re.DOTALL)

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js)
print("app.js completely replaced initFilter")
