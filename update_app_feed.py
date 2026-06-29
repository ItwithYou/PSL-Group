import os

with open('app.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Add the fetch logic to the end of app.js
fetch_logic = """
// -----------------------------------------------------------------------------
// Dynamic Activity Feed Fetching
// -----------------------------------------------------------------------------
async function fetchAndRenderActivities() {
    const feedContainer = document.getElementById('activity-feed');
    if (!feedContainer) return;

    try {
        const response = await fetch('/api/activities');
        if (!response.ok) throw new Error('Network response was not ok');
        
        const activities = await response.json();
        
        if (activities.length === 0) {
            feedContainer.innerHTML = `<p style="text-align:center; color:var(--text-muted); grid-column: 1/-1;" data-en="No recent activities posted." data-la="ຍັງບໍ່ມີຂ່າວສານໃໝ່ໃນຕອນນີ້." data-zh="暂无近期活动。">No recent activities posted.</p>`;
            return;
        }

        let html = '';
        activities.forEach(act => {
            const dateStr = new Date(act.date).toLocaleDateString();
            const imgHtml = act.photoUrl ? `<img src="${act.photoUrl}" alt="Activity Photo" loading="lazy">` : '';
            
            html += `
                <div class="activity-card">
                    ${imgHtml ? `<div class="activity-img">${imgHtml}</div>` : ''}
                    <div class="activity-content">
                        <span class="activity-date">${dateStr}</span>
                        <h3 class="activity-title">
                            <span class="en-text">${act.title.en || act.title.la || ''}</span>
                            <span class="lao-text">${act.title.la || act.title.en || ''}</span>
                            <span class="zh-text">${act.title.zh || act.title.en || ''}</span>
                        </h3>
                        <p class="activity-desc">
                            <span class="en-text">${act.desc.en || act.desc.la || ''}</span>
                            <span class="lao-text">${act.desc.la || act.desc.en || ''}</span>
                            <span class="zh-text">${act.desc.zh || act.desc.en || ''}</span>
                        </p>
                    </div>
                </div>
            `;
        });
        
        feedContainer.innerHTML = html;
        updateLanguageUI(); // ensure languages are correct
        
    } catch (error) {
        console.error('Error fetching activities:', error);
        feedContainer.innerHTML = `<p style="text-align:center; color:red; grid-column: 1/-1;">Error loading activities. Ensure Node.js server is running.</p>`;
    }
}

// Call on load
document.addEventListener('DOMContentLoaded', () => {
    fetchAndRenderActivities();
});
"""

with open('app.js', 'a', encoding='utf-8') as f:
    f.write(fetch_logic)

print("app.js updated successfully with fetch logic.")
