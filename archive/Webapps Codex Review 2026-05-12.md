# Webapps Codex Review 2026-05-12

Reviewed: 2026-05-12

1/ General architecture

- Webapps is now a static hub for a few local apps, with canonical project mirrors moved out to their own repos.
- The README clearly states canonical ownership, which is important for avoiding stale edits to byElie, PhotosByElie, or OleaTax copies.
- The live app folders are plain HTML/CSS/JS with no build step. That keeps deployment simple.
- The maintenance script for root dependency/audit work is a good sign; expand this approach to link and route validation.

2/ UI

- The hub should stay utilitarian: clear links to Conway, Reversi, sorting algorithms, and TapMePlus1.
- Each mini-app is self-contained, but shared navigation/back-to-hub treatment would help users recover from deep links.
- Avoid turning the hub into a marketing site; its job is to launch tools quickly.

3/ UX

- Users should immediately understand which apps are active and which external repos own related brands/sites.
- Archive routes should not be discoverable from the live hub except through maintenance docs.
- For games/tools, preserving state and reset controls matter more than decorative polish.
- Make each app touch-friendly enough for casual mobile use if GitHub Pages is the public surface.

4/ Testing

- No app tests were visible.
- Add a static route/link audit covering hub links, app entrypoints, assets, and archive exclusions.
- Add browser smoke tests for each mini-app: load, basic interaction, reset/new game where relevant, and mobile viewport.
- Existing dependency audit docs suggest this repo is ready for lightweight CI-style checks.

5/ Everything else

- The repo has both lowercase `archive/` and newly created `Archive/` for review archiving. Keep their purposes distinct or consolidate naming later.
- Continue keeping canonical brand projects out of this repo except for links.
- Add a simple publishing checklist for GitHub Pages.

6/ My suggetions:

1. Add a `scripts/validate_static_site.py` check for hub links, app entrypoints, required assets, and forbidden archive links.
2. Add Playwright smoke tests for Conway, Reversi, sorting algorithms, TapMePlus1, and the root hub.
3. Give each mini-app a consistent back-to-hub affordance and reset/new-game control where applicable.
4. Document the difference between `archive/` content and `Archive/` review files, or consolidate later.
5. Keep canonical project ownership notes prominent so brand-site edits happen in their own repos.
6. Add a short GitHub Pages publish/checklist section to README.
