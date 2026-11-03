# Repository Guidelines

## Project Structure & Module Organization
This repository is currently a planning scaffold for a bilingual English/Persian Quarto personal website and ML/DL blog hosted on GitHub Pages.
- `PLAN.md` describes architecture and content workflows; `ROADMAP.md` defines milestones and review gates.
- `tasks/M0/` through `tasks/M7/` contain implementation specifications; `tasks/recurring/` covers ongoing publishing work.
- `config/owner.yml` holds owner-provided public profile values; `.quarto-version` pins Quarto.
- Planned directories include `en/` and `fa/` for separate Quarto projects, `shared/` for assets, and `scripts/` for tooling. They are not implemented yet. English output will occupy `public/`, with Persian under `public/fa/`.

## Build, Test, and Development Commands
No Makefile, runnable site, or automated test suite exists yet. Use the pinned Quarto version and follow the relevant task before expecting these planned commands to work:
- `make sync`: copy shared assets into both language projects.
- `make preview-en` / `make preview-fa`: preview a language locally.
- `make build`: render both projects and assemble `public/`.
- `make serve`: build and serve the assembled site on port 8000.
- `make check`: validate bilingual pairing, Persian text, and images as implemented.

Run commands from the repository root. Python tooling targets Python 3.11+ through `.venv/bin/python`.

## Coding Style & Naming Conventions
Use UTF-8, LF endings, and a final newline. YAML uses two-space indentation; Makefile recipes require tabs. Python scripts use the standard library unless their task explicitly permits dependencies. No formatter or linter configuration exists yet.

Use matching `YYYY-MM-slug` post folders in both languages. Edit shared assets only in `shared/`, never generated `en/assets/` or `fa/assets/`. Preserve Persian characters, ZWNJ spacing, and RTL readability.

## Testing Guidelines
Run each task's `Verify` commands and check every “Done when” criterion. No test framework or coverage threshold is configured. For site changes, check both languages, links, code/math rendering, and mobile/RTL layout. Preserve committed `_freeze/` outputs and notebook outputs; CI must not execute heavy ML workloads.

## Commit & Pull Request Guidelines
History includes `T0.2.1: record Quarto version`; prefer `<TASK-ID>: <task title>` for task work. Keep changes task-scoped. The roadmap uses `main`, checkpoint reviews, and owner-controlled pushes. If opening a PR, identify the task, summarize changes, include verification results, and attach screenshots for visual changes.

## Agent & Configuration Rules
For task-file work, read `tasks/AGENT_RULES.md` first and respect allowed-file lists and reporting requirements. Source personal information only from `config/owner.yml` or owner-provided inputs. Never invent profile content or commit secrets.
