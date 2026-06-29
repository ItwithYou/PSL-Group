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

This repo deploys automatically to **GitHub Pages** via
`.github/workflows/deploy.yml` on every push to `main`.

One-time setup: in the GitHub repo, go to **Settings → Pages** and set
**Build and deployment → Source** to **GitHub Actions**.

The published site serves the static files and reads news from `data.json`.
The live API (admin posting/uploads) only runs when you start `server.js`
locally — `app.js` automatically falls back to `data.json` when the API isn't
available, so the public feed always works online.
