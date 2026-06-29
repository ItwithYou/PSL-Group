import re

new_admin_html = """<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Admin Portal - PSL Group</title>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg-color: #f7f6f2;
            --card-bg: #ffffff;
            --text-color: #0e0f11;
            --text-muted: #5e6469;
            --accent-color: #c4a97f; /* Gold */
            --danger-color: #dc3545;
            --border-color: #eae9e4;
        }
        body {
            font-family: 'Outfit', sans-serif;
            background-color: var(--bg-color);
            color: var(--text-color);
            margin: 0;
            padding: 2rem;
            display: flex;
            justify-content: center;
            gap: 2rem;
            flex-wrap: wrap;
        }
        .admin-container {
            background-color: var(--card-bg);
            padding: 2.5rem;
            border-radius: 12px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.05);
            width: 100%;
            max-width: 600px;
            border: 1px solid var(--border-color);
        }
        .dashboard-container {
            background-color: var(--card-bg);
            padding: 2.5rem;
            border-radius: 12px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.05);
            width: 100%;
            max-width: 600px;
            border: 1px solid var(--border-color);
            align-self: flex-start;
        }
        h1 { margin-top: 0; font-weight: 600; color: #8b0000; }
        h2 { font-weight: 600; margin-top: 0; }
        .form-group { margin-bottom: 1.5rem; }
        label { display: block; margin-bottom: 0.5rem; font-weight: 500; font-size: 0.9rem; }
        input[type="text"], input[type="date"], textarea, input[type="file"] {
            width: 100%; padding: 0.75rem; border: 1px solid var(--border-color);
            border-radius: 6px; font-family: inherit; box-sizing: border-box; background-color: var(--bg-color);
        }
        textarea { resize: vertical; height: 100px; }
        .btn {
            background-color: var(--accent-color); color: #fff; border: none;
            padding: 0.75rem 1.5rem; border-radius: 6px; cursor: pointer;
            font-weight: 600; font-family: inherit; width: 100%; font-size: 1rem;
            transition: background-color 0.3s;
        }
        .btn:hover { opacity: 0.9; }
        .btn-danger { background-color: var(--danger-color); padding: 0.4rem 0.8rem; font-size: 0.85rem; width: auto; }
        .success-msg { display: none; background-color: #d4edda; color: #155724; padding: 1rem; border-radius: 6px; margin-bottom: 1.5rem; font-weight: 500; }
        .lang-section { border-left: 3px solid var(--accent-color); padding-left: 1rem; margin-bottom: 1rem; }
        
        .news-list { display: flex; flex-direction: column; gap: 1rem; margin-top: 1.5rem; }
        .news-item {
            border: 1px solid var(--border-color); padding: 1rem; border-radius: 8px;
            display: flex; justify-content: space-between; align-items: center; background: var(--bg-color);
        }
        .news-info h4 { margin: 0 0 0.25rem 0; font-size: 1rem; }
        .news-info p { margin: 0; font-size: 0.85rem; color: var(--text-muted); }
    </style>
</head>
<body>

<!-- Post Activity Form -->
<div class="admin-container">
    <h1>PSL Admin Portal</h1>
    <h2>Post Company News</h2>
    <div class="success-msg" id="success-msg">Activity posted successfully! It is now live on the website.</div>
    
    <form id="activityForm">
        
        <div class="form-group">
            <label>Date</label>
            <input type="date" id="date" name="date" required>
        </div>

        <div class="form-group">
            <label>Upload Photo</label>
            <input type="file" id="photo" name="photo" accept="image/*" required>
        </div>

        <h3>English Translation</h3>
        <div class="lang-section">
            <div class="form-group">
                <label>Title (English)</label>
                <input type="text" name="titleEn" placeholder="e.g. Ribbon Cutting Ceremony">
            </div>
            <div class="form-group">
                <label>Description (English)</label>
                <textarea name="descEn" placeholder="Enter details here..."></textarea>
            </div>
        </div>

        <h3>Lao Translation (Optional)</h3>
        <div class="lang-section">
            <div class="form-group">
                <label>Title (Lao)</label>
                <input type="text" name="titleLa" placeholder="ຫົວຂໍ້ຂ່າວ...">
            </div>
            <div class="form-group">
                <label>Description (Lao)</label>
                <textarea name="descLa" placeholder="ລາຍລະອຽດ..."></textarea>
            </div>
        </div>

        <h3>Chinese Translation (Optional)</h3>
        <div class="lang-section">
            <div class="form-group">
                <label>Title (Chinese)</label>
                <input type="text" name="titleZh" placeholder="标题...">
            </div>
            <div class="form-group">
                <label>Description (Chinese)</label>
                <textarea name="descZh" placeholder="内容..."></textarea>
            </div>
        </div>

        <button type="submit" class="btn" id="submitBtn">Post Activity to Website</button>
    </form>
</div>

<!-- Manage Activities Dashboard -->
<div class="dashboard-container">
    <h2>Manage Existing News</h2>
    <p style="font-size: 0.9rem; color: var(--text-muted); margin-bottom: 0;">Below are all news items currently live on your website.</p>
    <div class="news-list" id="news-list">
        <p>Loading news...</p>
    </div>
</div>

<script>
    // Handle form submission
    document.getElementById('activityForm').addEventListener('submit', async (e) => {
        e.preventDefault();
        
        const btn = document.getElementById('submitBtn');
        btn.textContent = 'Posting...';
        btn.disabled = true;

        const formData = new FormData(e.target);

        try {
            const res = await fetch('/api/activities', {
                method: 'POST',
                body: formData
            });
            const data = await res.json();
            
            if(data.success) {
                document.getElementById('success-msg').style.display = 'block';
                e.target.reset();
                document.getElementById('date').valueAsDate = new Date();
                
                setTimeout(() => {
                    document.getElementById('success-msg').style.display = 'none';
                }, 4000);

                // Refresh the list immediately
                loadNews();
            }
        } catch(err) {
            alert('Error posting activity. Is the server running?');
            console.error(err);
        }

        btn.textContent = 'Post Activity to Website';
        btn.disabled = false;
    });

    // Set default date to today
    document.getElementById('date').valueAsDate = new Date();

    // Fetch and display existing news
    async function loadNews() {
        const listDiv = document.getElementById('news-list');
        try {
            const res = await fetch('/api/activities');
            if(!res.ok) throw new Error('Server error');
            const activities = await res.json();
            
            if(activities.length === 0) {
                listDiv.innerHTML = '<p>No news posted yet.</p>';
                return;
            }

            listDiv.innerHTML = '';
            activities.forEach(act => {
                // Use the Lao title if available, otherwise fallback to English
                const title = act.title.la || act.title.en || 'Untitled News';
                const dateStr = new Date(act.date).toLocaleDateString();

                const item = document.createElement('div');
                item.className = 'news-item';
                item.innerHTML = `
                    <div class="news-info">
                        <h4>${title}</h4>
                        <p>${dateStr}</p>
                    </div>
                    <button class="btn btn-danger" onclick="deleteNews('${act.id}')">Delete</button>
                `;
                listDiv.appendChild(item);
            });
        } catch(e) {
            listDiv.innerHTML = '<p style="color:red;">Error loading news from server.</p>';
            console.error(e);
        }
    }

    // Delete a news item
    async function deleteNews(id) {
        if(!confirm('Are you sure you want to delete this news item?')) return;
        
        try {
            const res = await fetch(`/api/activities/${id}`, { method: 'DELETE' });
            if(res.ok) {
                loadNews();
            } else {
                alert('Failed to delete news.');
            }
        } catch(e) {
            alert('Error deleting news.');
            console.error(e);
        }
    }

    // Load news on init
    loadNews();
</script>

</body>
</html>"""

with open('admin.html', 'w', encoding='utf-8') as f:
    f.write(new_admin_html)

print("admin.html updated successfully!")
