# Webapps

Static website workspace copied from `/Users/ecohen/Codex/web/github.io` and prepared as a standalone git project.

## Structure

- `index.html`: local landing page for the available sites
- `assets/`: shared logos and images
- `conway/`, `reversi/`, `sortingalgos/`, `tapmeplus1/`: local static app folders opened directly by the hub
- `scripts/`: repo maintenance scripts
- `docs/`: generated and hand-written maintenance notes
- `archive/`: removed mirrors, legacy routes, and review notes kept for recovery

## Canonical Projects

- By Elie is canonical at `/Users/ecohen/Dev/byElie` and published at `https://ec92009.github.io/byElie/`.
- Photos By Elie is canonical at `/Users/ecohen/Dev/photosByElie` and published at `https://ec92009.github.io/PhotosByElie/`.
- Olea Tax Co is canonical at `/Users/ecohen/Dev/OleaTax` and published at `https://ec92009.github.io/OleaTax/`.
- Webapps keeps only hub-required local apps in the live tree; old nested mirrors and unlinked variants live under `archive/`.

## Dependencies

This repo does not currently require a package manager or build step for the main sites.

- Browser: all pages are plain HTML/CSS/JS
- Local preview: `python3 -m http.server`
- External assets: some pages load Google Fonts at runtime

## GitHub

The local repo is configured with:

- `origin`: `https://github.com/ec92009/Webapps.git`

The local workspace lives at `/Users/ecohen/Dev/Webapps` and is synced to the GitHub repository above.

## Summary

See `SUMMARY.md` for the current cross-repo conversation handoff.
