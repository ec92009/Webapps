# Webapps Codex Review 2026-05-05

Generated: 2026-05-05 10:36:54 CEST

1/ General architecture

- Webapps acts as a static hub plus several nested site/game projects. That is useful for local browsing, but it creates version drift because some projects also live as standalone repos.
- The root index hardcodes project versions and links. Consider generating it from a small manifest so versions, URLs, logos, and descriptions stay consistent.
- There are many web files and a root dependency-audit script. Formalize that script into a recurring health check for broken links, missing assets, and duplicate standalone/nested project divergence.

2/ UI

- The hub UI is simple and scannable, but the card style is generic compared with the branded sites it links to.
- Add grouping by purpose: client sites, games, tools, and external apps. This will scale better than one long card grid.

3/ UX

- The hub should distinguish local-only projects from public GitHub Pages links. Users need to know whether a button opens a local folder, a public URL, or an external repo.
- Add last-reviewed or version metadata to reduce confusion when a nested copy lags a standalone repo.

4/ Testing

- Add static tests for every link and asset path in the hub and subprojects.
- Add screenshot smoke tests for key games/sites if this remains the multi-project publication surface.

5/ Everything else

- The existing older review was archived to `Archive/` for this run.
- Decide whether `Archive/` or `archive/` is canonical; both now exist in related projects.

6/ My suggetions:

1. Create a `sites.json` manifest and generate the root index from it.
2. Add a link/asset checker for all HTML files.
3. Add grouping labels for client sites, games, tools, and external apps.
4. Document which nested projects are canonical versus mirrors.
5. Normalize review/archive folder naming across the repo.
