# Conversation Summary

Date: 2026-05-22

## Scope

The Webapps repo is the GitHub Pages hub for local static apps and selected external project links. The current handoff adds a new local Lamps app and keeps the hub card/version metadata aligned with that app.

## Current Hub State

- Root hub version: `v83.7`.
- New local app: `lamps/` at version `v83.7`.
- New shared logo: `assets/logos/lamps-logo.svg`.
- The root hub includes a Lamps card that opens `./lamps/index.html` and uses the same visible version as the app.

## Lamps State

- `lamps/index.html` is a dependency-free static lighting planner.
- It supports room modes, color temperature, individual lamp toggles/levels, shade colors, and saved scenes through browser localStorage.
- The app follows the Webapps visible version pattern and displays `v83.7` in the top bar.
- `lamps/AGENTS.md` documents the sub-project contract: keep the parent hub card version aligned with the Lamps visible version.

## Handoff Notes

- `.playwright-cli/` is ignored as local browser-test output.
- No package manager or build step is required for the main static apps.
- Local preview: run `python3 -m http.server 8000` from `/Users/ecohen/Dev/Webapps` and open `http://localhost:8000/lamps/`.

## Deployment

- Repo: `https://github.com/ec92009/Webapps.git`
- GitHub Pages: `https://ec92009.github.io/Webapps/`
- Latest relevant hub/app version: `v83.7`
