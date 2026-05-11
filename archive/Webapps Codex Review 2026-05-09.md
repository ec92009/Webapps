# Webapps Codex Review 2026-05-09

Generated: 2026-05-09 00:00 Europe/Madrid

1/ General architecture

- Webapps is now a static hub plus small local apps, while larger projects have their own repos. Keep that boundary strict so archived mirrors do not become accidental active code.
- Extend the root dependency audit into a full hub integrity check covering links, logos, canonical URLs, archive routes, and project status metadata.

2/ UI

- The hub should behave like a project launcher. Cards should show consistent status, target type, logo, and whether the project opens local, external, or archived content.
- Centralized logo assets are good; add validation/fallbacks so missing logos do not make current projects look broken.

3/ UX

- Users need clear expectations before clicking: live site, local static app, GitHub Pages project, or archived reference.
- Keep archive routes out of the main journey unless recovery/history is the user's goal.

4/ Testing

- No browser tests are visible. Add a static audit for links, assets, page titles, canonical project URLs, and archive references.
- Add one Playwright smoke per active local app if those apps remain part of the hub.

5/ Everything else

- This repo has both lowercase `archive/` and the daily-review convention of `Archive/`. Normalize or document the split.
- Consider generating the README canonical list and hub metadata from one small data file.

6/ My suggetions:

1. Expand `scripts/root_dependency_audit.py` into a full static hub integrity check.
2. Add project status labels: local app, external site, GitHub Pages, archived reference.
3. Generate hub cards and README canonical links from one metadata file.
4. Add Playwright smoke tests for each active local app.
5. Normalize or document lowercase `archive/` versus review `Archive/` usage.
