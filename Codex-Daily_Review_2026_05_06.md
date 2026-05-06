# Codex Daily Review — 2026-05-06

## Architecture
- Repo-as-hub for multiple static sites is pragmatic; the main risk is drift/duplication across subfolders.
- Consider a small “shared assets + shared JS/CSS” contract (and enforce it) to avoid subtle mismatches.

## UI
- Hub page needs to be opinionated: strong visual hierarchy, consistent card sizing, and clear “what is this?” labeling.
- Ensure all embedded/mirrored sites inherit the same favicon/typography baseline where possible.

## UX
- Make local preview frictionless: one canonical command + a short “common gotchas” section (cache, paths, mixed origins).
- Add lightweight navigation consistency (home/back affordance) so users don’t feel trapped in sub-sites.

## Misc
- This repo will benefit from an explicit policy on mirrored vs. canonical sources (what gets copied, when, and why).
