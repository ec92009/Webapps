# Webapps Codex Review 2026-05-10

Timestamp: 2026-05-10 02:04 CEST

1/ General architecture:

- This repo is a hub plus multiple static projects and archived imports. The main risk is unclear ownership: active projects, external canonical repos, and archived references need machine-readable status.
- `scripts/root_dependency_audit.py` is the right direction. It should become the source of truth for hub integrity and stale references.

2/ UI:

- The root index should visibly distinguish active apps, historical demos, and links that now live in standalone repos.
- Hub cards should be generated from metadata so labels, links, and repo status do not drift.

3/ UX:

- Users arriving at the hub need to know what is usable now and what is archived.
- Add one consistent "open locally / public URL / source repo" pattern for each active app.

4/ Testing:

- There are no browser smoke tests. Add Playwright checks for the root page and active project pages.
- Expand the dependency audit to verify links, assets, archive references, and duplicate canonical ownership.

5/ Everything else:

- Normalize the relationship between lowercase `archive/` and review `Archive/` folders so automation and humans do not confuse them.
- Keep PhotosByElie/byElie copies clearly marked as archived now that they have standalone repos.

6/ My suggetions:

1. Add a metadata file listing each project as active, external, archived, or reference-only.
2. Generate root hub cards and README links from that metadata file.
3. Expand `scripts/root_dependency_audit.py` into a full static hub integrity check.
4. Add Playwright smoke tests for the root page and active local apps.
5. Document `archive/` versus `Archive/` naming and automation behavior.
