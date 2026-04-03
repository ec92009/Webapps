# Webapps

Static website workspace copied from `/Users/ecohen/Codex/web/github.io` and prepared as a standalone git project.

## Structure

- `index.html`: local landing page for the available sites
- `assets/`: shared logos and images
- `byElie/`, `conway/`, `reversi/`, `sortingalgos/`: static site/app folders
- `oleamediaco/`, `oleataxco/`, `oleataxco-v25/`: marketing sites and supporting assets

## Dependencies

This repo does not currently require a package manager or build step for the main sites.

- Browser: all pages are plain HTML/CSS/JS
- Local preview: `python3 -m http.server`
- External assets: some pages load Google Fonts at runtime
- PDF helper: `oleamediaco/source/make_offer_pdfs.py` uses macOS `sips`

## GitHub

The local repo is configured with:

- `origin`: `https://github.com/ec92009/Webapps.git`

The local workspace lives at `/Users/ecohen/Dev/Webapps` and is synced to the GitHub repository above.
