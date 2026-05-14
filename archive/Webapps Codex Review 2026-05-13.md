# Webapps Codex Review 2026-05-13

Reviewed: 2026-05-13

1/ General architecture

- Webapps is a static hub for small apps, with canonical brand/site projects moved to their own repos.
- The README clearly explains canonical ownership, which helps avoid stale edits to mirrored projects.
- Live app folders use plain HTML/CSS/JS without a build step, keeping GitHub Pages deployment simple.
- The existing root dependency/audit script is a good pattern; extend it to routes, links, and app smoke checks.

2/ UI

- The hub should stay utilitarian: clear links to Conway, Reversi, sorting algorithms, and TapMePlus1.
- Each mini-app should have consistent back-to-hub navigation and reset/new-game behavior where relevant.
- Avoid turning the hub into a marketing site; this repo's job is fast access to tools and demos.
- Mobile touch targets matter because these apps are likely to be tried casually from GitHub Pages.

3/ UX

- Users should immediately know which apps are active and which external repos own related brands/sites.
- Archive routes should not be discoverable from the live hub except through maintenance docs.
- For games/tools, state preservation and restart controls matter more than decorative polish.
- A small publish checklist would make Pages updates safer.

4/ Testing

- No app tests were visible.
- Add static route/link validation covering hub links, app entrypoints, assets, and archive exclusions.
- Add browser smoke tests for each mini-app: load, basic interaction, reset/new game, and mobile viewport.
- Keep the dependency audit script strict and make it part of a local validation command.

5/ Everything else

- This repo now has both `archive/` content and review `Archive/` usage. Document the distinction or consolidate later.
- Keep canonical project ownership notes prominent.
- Avoid reintroducing full copies of byElie, PhotosByElie, or OleaTax here.

6/ My suggetions:

1. Add `scripts/validate_static_site.py` for hub links, app entrypoints, required assets, and forbidden archive links.
2. Add Playwright smoke tests for Conway, Reversi, sorting algorithms, TapMePlus1, and the root hub.
3. Give each mini-app a consistent back-to-hub affordance and reset/new-game control.
4. Document the difference between `archive/` content and `Archive/` review files.
5. Keep canonical ownership notes visible so brand-site edits happen in their own repos.
6. Add a short GitHub Pages publish checklist to README.
