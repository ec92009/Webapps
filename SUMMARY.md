# Conversation Summary

Date: 2026-05-27

## Scope

The Webapps repo is the GitHub Pages hub for local static apps and selected external project links. It now includes a public-safe S1 task-tree app under `s1/`.

## Current Hub State

- Root hub version: `v88.11`.
- Local app folders in this repo: `conway/`, `reversi/`, `s1/`, `sortingalgos/`, and `tapmeplus1/`.
- The root hub includes a Lamps card that opens `https://ec92009.github.io/Lamps/` and tracks that site's visible version.
- The root hub includes an S1 Task Tree card that opens `./s1/index.html`.
- The root hub includes Photos By Elie and Photos By Elie Music cards pinned to `v89.2`, including the direct Real Estate client link `https://ec92009.github.io/PhotosByElie/real-estate.html?v=89.2&client=elie`.
- Shared S1 logo: `assets/logos/s1-logo.svg`.

## S1 State

- `/Users/ecohen/Dev/Webapps/s1/index.html` is a dependency-free interactive task-tree dashboard.
- It maps the S1-for-all project into Manou, Agnes, and Elie lanes with click-to-expand subprojects, provider-level Safe / Locksmiths detail, lane-safe responsive spacing, filters including Done, search, counts, done-task witness cards, granular details, and copyable snapshots. The current queue has a single Next leaf: Agnes Ameli / FranceConnect access, with waiting badges expanding to blocker details.
- The public task tree now renders from `s1/task-tree.json`, which carries tree structure, node status, blockers, queue labels, task cards, and English/French copy. The app shell is presentation logic only.
- It is deliberately public-safe: no exact addresses, IDs, account data, scans, or sensitive documents.
- The app displays `v85.7`.
- It has an EN/FR language toggle. UI labels and operational text are loaded from `s1/task-tree.json`; any newly added untranslated string falls back to English until its French translation is added.

## Handoff Notes

- `.playwright-cli/` is ignored as local browser-test output.
- No package manager or build step is required for the main static apps.
- Local Webapps preview: run `python3 -m http.server 8000` from `/Users/ecohen/Dev/Webapps` and open `http://localhost:8000/`.
- Local S1 preview: run `python3 -m http.server 8000` from `/Users/ecohen/Dev/Webapps` and open `http://localhost:8000/s1/`.

## Deployment

- Repo: `https://github.com/ec92009/Webapps.git`
- GitHub Pages: `https://ec92009.github.io/Webapps/`
- Latest relevant hub/app version: `v88.11`

## 2026-05-27 Update

- Refreshed the Photos By Elie hub cards after the Real Estate v89.2 build.
- Updated the hub's visible version badge from `v88.10` to `v88.11`.
- Left unrelated local `AGENTS.md` changes untouched.
