# Webapps

Static website workspace copied from `/Users/ecohen/Codex/web/github.io` and prepared as a standalone git project.

## Structure

- `index.html`: local landing page for the available sites
- `assets/`: shared logos and images
- `PhotosByElie/`, `conway/`, `reversi/`, `sortingalgos/`: static site/app folders
- By Elie is linked from the hub as an external GitHub Pages project at `https://ec92009.github.io/byElie/`
- `oleamediaco/`, `oleataxco/`, `oleataxco-v25/`: marketing sites and supporting assets

## Photos By Elie

- Hub card points to the standalone PhotosByElie GitHub Pages site at `https://ec92009.github.io/PhotosByElie/`.
- `PhotosByElie/` is also mirrored inside this repo for direct hub-relative access.
- Current mirrored PhotosByElie version: `v63.8`.
- Collections are France, USA, Spain, Mexico, and AI, with AI last.
- The mirrored AI gallery includes resized Leonardo-generated JPG assets in `PhotosByElie/assets/ai/`.
- Photo detail pages auto-sync resolution checkbox changes to the localStorage basket.
- The basket is the source of truth and prevents duplicate charges for the same photo.

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

## Summary

See `SUMMARY.md` for the current cross-repo conversation handoff.
