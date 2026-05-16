# Webapps Codex Review 2026-05-15

1/ General architecture:
- Webapps is now a hub plus local static apps, while canonical business/photo sites live in separate repos. Keep enforcing that boundary so archived mirrors do not return to the live tree.
- The `.claude/worktrees` content is being counted by simple repo scans and can obscure the real source. Consider excluding or archiving generated worktrees outside the active source tree.

2/ UI:
- The hub should stay simple and utilitarian: clear links to active local apps and canonical external sites.
- Avoid re-styling archived projects from this repo; visual work belongs in the canonical project repos.

3/ UX:
- Users should never wonder whether they are on a canonical page or an archived mirror. Make archive routes visibly archival and keep live navigation pointed to active projects only.
- The README does a good job explaining canonical project ownership; keep it current as folders move.

4/ Testing:
- No tests were found. Add a static route/link audit that ensures hub links resolve and no live path points into `archive/` accidentally.
- Add a quick local server smoke test for `index.html`, Conway, Reversi, sorting, and TapMePlus1.

5/ Everything else:
- Existing review files live under lowercase `archive/`; this run uses `Archive/` per instruction for Codex review archival. Consider standardizing later if that does not break local convention.
- Keep `SUMMARY.md` as handoff context, not a replacement for README maintenance.

6/ My suggetions:
1. Add a static hub link checker that rejects accidental archive links.
2. Move or ignore generated worktree folders from routine source scans.
3. Add smoke tests for each live local app route.
4. Standardize review archive naming if future automation depends on `Archive/`.
5. Keep canonical-project links current in README and the hub.
