# Codex Daily Review — 2026-05-05

## Architecture
- Clean “static hub + sub-sites” layout; no build step keeps iteration fast for simple marketing/portfolio pages.
- Content is spread across many folders (plus duplicated site mirrors); a single `index.json` (site metadata) could reduce manual hub edits.

## UI
- The hub (`index.html`) should enforce one visual system (type scale, spacing, card layout) so sub-sites feel intentionally “different”, not accidental.
- Consider a shared header/footer include pattern to avoid drift across folders (even a tiny vanilla JS include helper).

## UX
- Add a short “Where am I?” breadcrumb or top-nav on sub-sites so users can return to the hub without the back button.
- Local preview instructions are good; add a 1-line note about GitHub Pages deployment assumptions (paths, case sensitivity).

## Misc
- There’s already a `Codex.Review.2026.05.02.md`; this repo benefits from periodic “link integrity + mobile sanity” spot checks.
