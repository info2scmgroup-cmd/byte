# Byte Global Technologies — Website

Corporate website for **BYTEGLOBAL TECHNOLOGIES PRIVATE LIMITED** (brand: *Byte Global Technologies*) — *Building What's Next*.

A fast, static, multi-page site (plain HTML/CSS/JS — no build step required to serve). The logo is embedded in every page, so pages render correctly even in isolation.

## Structure

```
.
├── index.html              # Home
├── about.html              # About + company info + credentials
├── services.html           # Services overview
├── services/               # 8 service detail pages
│   ├── artificial-intelligence.html
│   ├── software-engineering.html
│   └── ... (6 more)
├── industries.html
├── talent.html
├── global-presence.html    # HQ office map + global markets
├── insights.html
├── careers.html
├── contact.html            # Address, map, Get Directions, credentials
├── assets/                 # Logo variants + favicon (also embedded inline)
├── build_byteglobal.py     # Source of truth — regenerates every page
├── world_paths.txt         # World-map geometry (public-domain geography)
├── world_nodes.txt         # Market coordinates
└── .github/workflows/deploy.yml   # Auto-deploy to GitHub Pages
```

## Editing content

All content lives in clean Python data structures at the top of `build_byteglobal.py`
(services, industries, jobs, insights, company details, etc.). Edit there, then rebuild:

```bash
pip install Pillow --break-system-packages   # only needed once, for asset steps
python3 build_byteglobal.py                  # regenerates all HTML into this folder
```

Verified corporate details (legal name, CIN, GSTIN, Udyam, registered address) are constants
near the top of the script — update them in one place and every page stays consistent.

## Deploy (GitHub Pages — automatic)

This repo ships a workflow that publishes the site on every push to `main`.

1. Push the repo to GitHub (see below).
2. On GitHub: **Settings → Pages → Build and deployment → Source: GitHub Actions**.
3. Push any change to `main` — the site deploys automatically. The live URL appears
   under the workflow run and in **Settings → Pages**.

To serve from a custom domain (e.g. `www.byteglobal.in`), add it under **Settings → Pages → Custom domain**
and create a `CNAME` file in the repo root containing `www.byteglobal.in`.

## Run locally

```bash
python3 -m http.server 8000
# then open http://localhost:8000
```

---

© 2026 Byte Global Technologies Private Limited. All Rights Reserved.
