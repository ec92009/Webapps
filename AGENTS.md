# AGENTS.md

Repo-level working preferences for `/Users/ecohen/Dev/Webapps`.

## Response Protocol

- If a task may take more than a few seconds, send a short acknowledgment before doing the work.
- When working in this repo, read and follow the nearest applicable `AGENTS.md` before making changes.
- For website changes intended to be viewed externally, commit and push once the change is complete unless the user asks not to.

## Defaults

- Prefer `rg` and `rg --files` for search.
- Prefer small, direct edits over broad refactors.
- Prefer Python for one-off scripts and automation tasks.
- If Python dependencies are introduced, prefer `uv` for environment and package management.

## Repo Workflow

- Run commands from the repo root: `/Users/ecohen/Dev/Webapps` unless a subproject requires otherwise.
- Make small, clear commits.
- Default to keeping `main` pushable.
- Use branches for larger changes; preferred branch prefix: `codex/`.
- After modifying a project, update the relevant docs when needed.

## Versioning

- Use visible app versions in the form `vX.Y`.
- `X` is the number of days since `2026-02-28`.
- `Y` increments with each build/change on that same day.
- Example: on `2026-03-31`, start at `v31.0`, then `v31.1`, `v31.2`, and so on.
- When updating the app UI version badge, always bump the minor version for each new build.

## Workspace Structure

- Repo root: `/Users/ecohen/Dev/Webapps`
- Top-level index: `/Users/ecohen/Dev/Webapps/index.html`
- Shared assets: `/Users/ecohen/Dev/Webapps/assets`
- Project folders:
  - `/Users/ecohen/Dev/Webapps/byElie`
  - `/Users/ecohen/Dev/Webapps/conway`
  - `/Users/ecohen/Dev/Webapps/reversi`
  - `/Users/ecohen/Dev/Webapps/sortingalgos`
  - `/Users/ecohen/Dev/Webapps/oleamediaco`
  - `/Users/ecohen/Dev/Webapps/oleataxco`
  - `/Users/ecohen/Dev/Webapps/oleataxco-v25`

## Project Boundaries

- Keep changes scoped to the project folder requested by the user unless they explicitly ask for cross-project work.
- Avoid shared visual or structural refactors across multiple site folders unless explicitly requested.
- Keep commit messages project-scoped when possible, for example: `oleamediaco: ...`, `oleataxco: ...`, or `byelie: ...`.

## Local Preview

- Start a local server from the repo root with `python3 -m http.server 8000`.
- Main index: `http://localhost:8000/`
- Example project URLs:
  - `http://localhost:8000/oleamediaco/`
  - `http://localhost:8000/oleataxco/`
  - `http://localhost:8000/byElie/`

## Execution Discipline

- Prefer deterministic tooling over manual repetition.
- Before adding new scripts, check whether the repo already contains a file or workflow that solves the task.
- If a task fails, read the full error, fix the cause, and retest.
- Keep secrets out of source files. Use ignored local config files for credentials.

## Python Hygiene

- Do not commit virtual environments such as `.venv/`.
- Do not commit Python cache artifacts such as `__pycache__/` or `*.pyc`.
- If Python tooling in this repo grows beyond a single script, add project config such as `pyproject.toml`.

## Safety

- Do not delete or overwrite user files without explicit confirmation.
- Do not rewrite Git history unless explicitly requested.
