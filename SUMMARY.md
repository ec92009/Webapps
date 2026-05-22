# Conversation Summary

Date: 2026-05-22

## Scope

The Webapps repo is the GitHub Pages hub for local static apps and selected external project links. Lamps now lives as a standalone sibling repo at `/Users/ecohen/Dev/Lamps`, and the hub links to its published GitHub Pages site.

## Current Hub State

- Root hub version: `v83.9`.
- Local app folders in this repo: `conway/`, `reversi/`, `sortingalgos/`, and `tapmeplus1/`.
- The root hub includes a Lamps card that opens `https://ec92009.github.io/Lamps/` and tracks that site's visible version.
- Shared hub logo: `assets/logos/lamps-logo.svg`.

## Lamps State

- `/Users/ecohen/Dev/Lamps/index.html` is a dependency-free static lighting planner.
- It supports room modes, color temperature, individual lamp toggles/levels, shade colors, and saved scenes through browser localStorage.
- The app displays `v83.7` in the top bar.
- `/Users/ecohen/Dev/Lamps/AGENTS.md` documents the standalone project contract.

## Handoff Notes

- `.playwright-cli/` is ignored as local browser-test output.
- No package manager or build step is required for the main static apps.
- Local Webapps preview: run `python3 -m http.server 8000` from `/Users/ecohen/Dev/Webapps` and open `http://localhost:8000/`.
- Local Lamps preview: run `python3 -m http.server 8010` from `/Users/ecohen/Dev/Lamps` and open `http://localhost:8010/`.

## Deployment

- Repo: `https://github.com/ec92009/Webapps.git`
- GitHub Pages: `https://ec92009.github.io/Webapps/`
- Latest relevant hub/app version: `v83.7`
