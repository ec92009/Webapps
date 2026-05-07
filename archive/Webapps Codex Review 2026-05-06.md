# Webapps Codex Review 2026-05-06

Timestamp: 2026-05-06 02:02 CEST

## 1/ General architecture

- This repo is a multi-site static workspace; keep project boundaries strict so shared changes do not accidentally alter unrelated sites.
- The root index and project folders should remain simple static assets unless a build system becomes clearly necessary.
- Keep archived projects under `archive/` and make active vs. historical status explicit in the root README.
- Shared assets should have clear ownership and cache-busting rules.

## 2/ UI

- The root index should work as a directory/dashboard for active sites, not as a marketing page.
- Give each active project card enough metadata to identify status, public URL, and local path.
- Keep visual styles restrained and consistent across the root while allowing project-specific pages to keep their own identities.

## 3/ UX

- Add a consistent local preview command and URL list for every active site.
- Make external/public URLs visible in README and, where useful, in the root index.
- Avoid burying current work behind archived folders with similar names.

## 4/ Testing

- Extend the dependency/static audit script into a general smoke check for missing assets, broken links, duplicate IDs, and unreferenced active pages.
- Add a mobile viewport screenshot pass for active public pages after major visual changes.
- Keep tests build-free unless a project introduces real dependencies.

## 5/ Everything else

- The repo has many archived docs and assets; a quarterly cleanup pass would keep searches focused.
- Add per-project status notes to `TODO.md` so the next development round does not start by re-triaging everything.
- Keep `.DS_Store` and generated cache artifacts out of the repo.

## 6/ My suggetions:

1. Add an active-project registry used by both README and root index.
2. Expand the root audit script to check links, assets, duplicate IDs, and active URL coverage.
3. Mark archived projects clearly and remove them from normal active-site workflows.
4. Add public/local URL tables for each active project.
5. Run mobile screenshot checks for every externally visible site before publishing changes.
