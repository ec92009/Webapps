# Conversation Summary

Date: 2026-05-24

## Scope

The Webapps repo is the GitHub Pages hub for local static apps and selected external project links. It now includes a public-safe S1 task-tree app under `s1/`.

## Current Hub State

- Root hub version: `v85.2`.
- Local app folders in this repo: `conway/`, `reversi/`, `s1/`, `sortingalgos/`, and `tapmeplus1/`.
- The root hub includes a Lamps card that opens `https://ec92009.github.io/Lamps/` and tracks that site's visible version.
- The root hub includes an S1 Task Tree card that opens `./s1/index.html`.
- Shared S1 logo: `assets/logos/s1-logo.svg`.

## S1 State

- `/Users/ecohen/Dev/Webapps/s1/index.html` is a dependency-free interactive task-tree dashboard.
- It maps the S1-for-all project into Manou, Agnes, and Elie lanes with click-to-expand subprojects, provider-level Safe / Locksmiths detail, filters including Done, search, counts, done-task witness cards, granular details, and copyable snapshots.
- It is deliberately public-safe: no exact addresses, IDs, account data, scans, or sensitive documents.
- The app displays `v85.2`.

## Handoff Notes

- `.playwright-cli/` is ignored as local browser-test output.
- No package manager or build step is required for the main static apps.
- Local Webapps preview: run `python3 -m http.server 8000` from `/Users/ecohen/Dev/Webapps` and open `http://localhost:8000/`.
- Local S1 preview: run `python3 -m http.server 8000` from `/Users/ecohen/Dev/Webapps` and open `http://localhost:8000/s1/`.

## Deployment

- Repo: `https://github.com/ec92009/Webapps.git`
- GitHub Pages: `https://ec92009.github.io/Webapps/`
- Latest relevant hub/app version: `v85.2`
