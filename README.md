# PSL Group — Corporate Website

The official multi-language (Lao / English / 中文) website for **PSL Group**, a
diversified enterprise based in Laos.

## Project structure

| File | Purpose |
|------|---------|
| `index.html` | Main public website |
| `style.css` | All site styling |
| `app.js` | Frontend logic: language switching, theming, modals, news feed |
| `admin.html` | Admin panel for posting company news (requires the local server) |
| `server.js` | Express backend: news API + photo uploads (for local admin use) |
| `data.json` | The company news / activities content |
| `package.json` | Node dependencies for the local server |

## Viewing the site

The public site is fully static. Open `index.html` in a browser, or serve the
folder with any static server. The news feed loads from `data.json`.

## Running the admin panel locally

The admin panel (`admin.html`) lets you add and delete news with photo uploads.
It needs the Node server running:

```bash
npm install
node server.js
```

Then open:

- Website: <http://localhost:3000/>
- Admin panel: <http://localhost:3000/admin.html>

Posting through the admin panel writes to `data.json` and saves photos to an
`uploads/` folder. After adding news locally, commit the updated `data.json`
(and any new images) so the changes appear on the live site.

## Deployment (GitHub Pages)

The site is published with **GitHub Pages** serving the static files
directly from the `main` branch.

Setup (in the GitHub repo): **Settings → Pages → Build and deployment**,
set **Source** to **Deploy from a branch**, choose branch **`main`** and
folder **`/ (root)`**, then **Save**. Every push to `main` re-publishes
the site automatically. The live URL is
<https://itwithyou.github.io/PSL-Group/>.

The published site serves the static files and reads news from `data.json`.
The live API (admin posting/uploads) only runs when you start `server.js`
locally — `app.js` automatically falls back to `data.json` when the API isn't
available, so the public feed always works online.
