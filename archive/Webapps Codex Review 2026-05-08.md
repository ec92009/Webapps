# Webapps Codex Review 2026-05-08

Generated: 2026-05-08 00:00 Europe/Madrid

1/ General architecture

- Webapps is now mostly a static hub plus a few local apps, with canonical larger projects split into their own repos. Keep enforcing that boundary so old mirrors do not drift back into active development.
- The root maintenance script is a useful start. Extend it into a full hub audit that checks links, logos, canonical project URLs, archived mirrors, and dependency assumptions.

2/ UI

- The hub should look and behave like a project launcher, not a marketing site. Make the available apps easy to scan, with consistent cards, current status, and clear external/local labels.
- Logo assets are centralized, which is good. Add fallback behavior or validation for missing logos so a broken asset does not make a project look abandoned.

3/ UX

- Users need to know whether clicking a project opens a live local app, a GitHub Pages site, or an archived reference. Label these states consistently.
- Keep archive routes out of the main path unless recovery is the task. Too much visible legacy content creates confusion about what is current.

4/ Testing

- There are no visible browser tests. Add a static audit that checks all hub links, asset references, page titles, and canonical URLs.
- If the local apps remain active, add one Playwright smoke path per app: load, first interaction, and no console errors.

5/ Everything else

- The lowercase `archive/` exists, while this review workflow uses `Archive/`. Pick one convention or document why both exist.
- Keep the canonical-project list in README and the hub page generated from one source of truth if possible.

6/ My suggetions:

1. Extend `scripts/root_dependency_audit.py` into a full static hub integrity check.
2. Add visible project status labels: local app, external site, archived reference.
3. Generate README canonical links and hub project metadata from one small data file.
4. Add Playwright smoke tests for each active local app.
5. Normalize or document `Archive/` versus `archive/` usage.
