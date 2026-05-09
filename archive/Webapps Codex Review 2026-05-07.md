# Webapps Codex Review 2026-05-07

Reviewed at: 2026-05-07 00:00 Europe/Madrid

1/ General architecture:
- The repo is a static multi-app workspace. Keep each app self-contained, but add a small shared policy for assets, previews, and dependency checks so subprojects do not drift.
- The top-level index should be treated as a router/catalog, not a dumping ground for app-specific behavior.
- Add a lightweight manifest describing each app path, status, public URL, and test command.

2/ UI:
- The root index should make project identity and status easy to scan: app name, short purpose, status, and open link.
- Avoid letting archived or experimental apps look equally current unless that is intentional.
- Shared visual treatment is helpful at the catalog level, but each app can keep its own design language.

3/ UX:
- Add clear local preview instructions and public URLs for each active app.
- Separate active projects from archived experiments so users do not wander into stale surfaces.
- Make broken/missing assets obvious during review with a local audit command.

4/ Testing:
- Expand `scripts/root_dependency_audit.py` or add a sibling script to check internal links, assets, and top-level app entrypoints.
- Add a simple static-server smoke pass that fetches each active index page.
- Add accessibility checks for the root catalog and active apps when they change.

5/ Everything else:
- Create `Archive/` consistently now that review files use that folder name; keep old lowercase `archive/` for site content only if needed.
- `README.md`, `TODO.md`, and `SUMMARY.md` should identify active apps and archival boundaries.
- Keep generated Claude worktrees out of production review signals.

6/ My suggetions:
1. Add an app manifest for active, archived, and experimental projects.
2. Improve the root index as a clear project catalog.
3. Add static link/asset smoke checks for active apps.
4. Clarify `Archive/` versus `archive/` usage.
5. Update README with preview and deployment status per app.
