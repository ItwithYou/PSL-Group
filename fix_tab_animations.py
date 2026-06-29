import re

with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

new_tab_logic = """            // Show target tab, hide others
            tabContents.forEach(tab => {
                if (tab.id === targetTabId) {
                    tab.classList.add('active');
                    
                    // Force animations inside this tab to trigger since they were hidden
                    const animated = tab.querySelectorAll('.animate-on-scroll');
                    animated.forEach(el => {
                        el.classList.add('appear');
                    });
                } else {
                    tab.classList.remove('active');
                }
            });"""

# We just need to replace the inner tab logic
js = re.sub(r'// Show target tab, hide others.*?tab\.classList\.remove\(\'active\'\);\s*\}\s*\}\);', new_tab_logic, js, flags=re.DOTALL)

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js)
print("Tab animation logic fixed.")
