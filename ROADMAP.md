# Roadmap: milestones → checkpoints → tasks

This file is the **execution plan** for [PLAN.md](PLAN.md). Every task has its own file under [tasks/](tasks/), written so that a cheap coding model can do it without guessing.

---

## 1. Roles

| Role | Who | Does |
|---|---|---|
| **Owner** | you | Does every `HUMAN` task (accounts, secrets, personal content, final Persian edit). Runs agents, tags approvals, pushes. |
| **Builder** | a cheap coding agent, in a fresh session per task | Does one `AGENT` task, commits it, writes `reports/<ID>.md` |
| **Reviewer** | Claude (strong model), on request | Reviews a finished **checkpoint**: reads reports and diffs, builds the site and looks at it, then writes `reviews/<checkpoint>.md` with **PASS** or **CHANGES NEEDED** plus exact `FIX-` tasks |

### Agent levels (which model to use)
| Level | Kind of work | Suggested model |
|---|---|---|
| `basic` | Create or edit files from exact content, run commands | cheapest (e.g. Haiku-class) |
| `standard` | Write a small Python script from a precise spec, or write Persian text | mid-range (e.g. Sonnet-class). For Persian, use a model that writes good Persian |

---

## 2. The loop

**For each task (in order inside a checkpoint):**
1. Open a **new** agent session in `~/Projects/personal-website`. One task per session keeps the context small and cheap.
2. Paste this prompt (change the path):
   ```text
   You are a coding agent. First read `tasks/AGENT_RULES.md` completely and follow it strictly.
   Then do ONLY the task in `tasks/M1/T1.2.1.md`. Do not start any other task.
   When finished, write the report and commit exactly as the rules say, then show me the report.
   ```
3. If the agent reports **BLOCKED**, don't patch it yourself. Bring it to the Reviewer.
4. Tick the task's box in the status table below.

**For each checkpoint (after its last task):**
5. Ask the Reviewer: **"Review checkpoint C1.2"**.
6. The Reviewer writes `reviews/C1.2.md` with a verdict.
   - **CHANGES NEEDED** → it contains `FIX-C1.2-1`, `FIX-C1.2-2`… in the same task format. Run each one with an agent:
     ```text
     You are a coding agent. First read `tasks/AGENT_RULES.md` completely and follow it strictly.
     Then do ONLY task FIX-C1.2-1 described in `reviews/C1.2.md`. Do not start any other task.
     When finished, write the report and commit exactly as the rules say, then show me the report.
     ```
     Then ask for a re-review.
   - **PASS** → run:
     ```bash
     git tag approved/C1.2
     ```
     From C1.5 on, also push so the site redeploys:
     ```bash
     git push && git push --tags
     ```
7. Move on to the next checkpoint.

**For each milestone:** the last checkpoint's review also covers the whole milestone (marked 🚦 **GATE**). Don't start the next milestone before the gate passes.

### Recurring tasks (after launch)
Files in `tasks/recurring/` take a `SLUG` that you give in the prompt:
```text
... Then do ONLY the task in `tasks/recurring/R3.md` with SLUG=2026-12-self-attention. ...
```

---

## 3. Key build decisions (already settled, so agents don't have to choose)

| Topic | Decision |
|---|---|
| Generator | Quarto, **two separate projects**: `en/` and `fa/` |
| Build | Each project renders into its own default `_site/`. `scripts/assemble_site.py` then copies `en/_site/` → `public/` and `fa/_site/` → `public/fa/`. CI deploys `public/` |
| URLs | English at `https://<user>.github.io/`, Persian at `https://<user>.github.io/fa/`. A post uses **the same folder name** in both languages |
| Shared files | The source of truth is `shared/` (styles, fonts, js, images, files, data). `scripts/sync_shared.py` copies it into `en/assets/` and `fa/assets/` before every render. Those copies are git-ignored and must never be edited |
| Post folder name | `YYYY-MM-slug`, e.g. `2026-12-self-attention` |
| Code execution | `.qmd` posts use `freeze: auto` (outputs stored in `_freeze/`, which is committed). `.ipynb` posts use their saved outputs. CI never runs heavy ML code |
| Persian UI text | Quarto has no Persian UI file, so we write our own: `fa/_language-fa.yml` |
| Persian dates | Gregorian, shown as `YYYY-MM-DD` |
| Fonts | Vazirmatn, self-hosted, for Persian. System font stack for English. No Google Fonts |
| Language switch | A navbar link plus a small script (`shared/js/lang-switch.html`) that maps `/x/` ↔ `/fa/x/` |
| 404 page | Only one, at the root (`en/404.qmd`), with English and Persian text |
| Personal data | Kept in `config/owner.yml` and `content-inputs/`. Agents only copy from there |
| Branching | Everything is on `main`. Approval = git tag `approved/<checkpoint>`. Only the Owner pushes |

---

## 4. Milestones overview

| # | Milestone | Outcome | Est. owner time |
|---|---|---|---|
| M0 | Prerequisites | Accounts, tools and personal info ready | 2 h |
| M1 | Foundation and bilingual spike 🚦 | A live bilingual skeleton (RTL, switcher, CI deploy). **Proves the architecture** | 3 h |
| M2 | Design and identity pages | Theme, About, Projects, Publications, CV | 4 h |
| M3 | Blog engine | Listings, feeds, post templates, style guide, interactive figures, series | 3 h |
| M4 | Community, SEO and analytics | Comments, social cards, sitemap, analytics | 1.5 h |
| M5 | Bilingual tooling | Glossary, translation prompt, pair checker, Persian linter | 2.5 h |
| M6 | Distribution and performance | Telegram announcements, external-asset audit, link check, Iran test | 2 h |
| M7 | First post and launch 🚀 | Post #1 in both languages, final QA, public launch | 8–10 h |
| M8 | Operating mode | Repeatable per-post pipeline | ~9 h per post |

At about 2.5 hours a week this comes to roughly **10–11 weeks to launch**. Start writing post #1 (T7.1.1) whenever you like during M2–M6.

---

## 5. Checkpoints and tasks (status table)

Legend: 👤 = HUMAN task, 🤖 = AGENT task (level in brackets).

### M0 — Prerequisites
| ✓ | ID | Task | Who |
|---|---|---|---|
| ☐ | [T0.1.1](tasks/M0/T0.1.1.md) | Create the GitHub repository and enable Pages | 👤 |
| ☐ | [T0.1.2](tasks/M0/T0.1.2.md) | Initialize the local git repo and first push | 👤 |
| ☐ | [T0.2.1](tasks/M0/T0.2.1.md) | Install local tools and record the Quarto version | 👤 |
| ☐ | [T0.2.2](tasks/M0/T0.2.2.md) | Choose and set up your agent tool | 👤 |
| ☐ | [T0.3.1](tasks/M0/T0.3.1.md) | Fill in `config/owner.yml` | 👤 |
| ☐ | [T0.3.2](tasks/M0/T0.3.2.md) | Gather content inputs (due before M2) | 👤 |

**C0 review:** the Reviewer checks that `config/owner.yml` and `.quarto-version` exist and that the remote is set.

### M1 — Foundation and bilingual spike 🚦
**C1.1 Repo scaffold**
| ✓ | ID | Task | Who |
|---|---|---|---|
| ☐ | [T1.1.1](tasks/M1/T1.1.1.md) | Create the folder structure and ignore files | 🤖 basic |
| ☐ | [T1.1.2](tasks/M1/T1.1.2.md) | Create the Python environment | 🤖 basic |
| ☐ | [T1.1.3](tasks/M1/T1.1.3.md) | Shared-asset sync script and base Makefile | 🤖 standard |

**C1.2 English skeleton**
| ☐ | [T1.2.1](tasks/M1/T1.2.1.md) | English Quarto project, home and blog pages | 🤖 basic |
| ☐ | [T1.2.2](tasks/M1/T1.2.2.md) | English test post (code, plot, math) | 🤖 basic |

**C1.3 Persian skeleton (RTL)**
| ☐ | [T1.3.1](tasks/M1/T1.3.1.md) | Self-host the Vazirmatn font | 🤖 basic |
| ☐ | [T1.3.2](tasks/M1/T1.3.2.md) | RTL stylesheet and font CSS | 🤖 basic |
| ☐ | [T1.3.3](tasks/M1/T1.3.3.md) | Persian UI strings file | 🤖 standard (Persian) |
| ☐ | [T1.3.4](tasks/M1/T1.3.4.md) | Persian Quarto project, pages and test post | 🤖 standard (Persian) |

**C1.4 Assemble and language switch**
| ☐ | [T1.4.1](tasks/M1/T1.4.1.md) | Site assembly script and `make build` / `make serve` | 🤖 standard |
| ☐ | [T1.4.2](tasks/M1/T1.4.2.md) | Language switcher | 🤖 basic |

**C1.5 Deploy** 🚦 GATE for M1
| ☐ | [T1.5.1](tasks/M1/T1.5.1.md) | GitHub Actions publish workflow | 🤖 basic |
| ☐ | [T1.5.2](tasks/M1/T1.5.2.md) | Push and check the live site | 👤 |

**🚦 M1 gate (Reviewer):**
- `/` and `/fa/` are both live, and `/fa/` is fully RTL with a Persian navbar.
- The switcher maps a post to its counterpart both ways.
- Code, plots and math render, and code/math stay LTR inside Persian pages.
- Vazirmatn loads from our own domain, and Persian search works.
- CI succeeds without running notebooks.
- If any of these fails and can't be fixed, the Reviewer rewrites M2+ for the fallback (babelquarto or Hugo) before you continue.

### M2 — Design and identity pages
**C2.1 Theme**
| ☐ | [T2.1.1](tasks/M2/T2.1.1.md) | Light and dark theme | 🤖 basic |
| ☐ | [T2.1.2](tasks/M2/T2.1.2.md) | Favicon and page footer | 🤖 basic |

**C2.2 Home / About**
| ☐ | [T2.2.1](tasks/M2/T2.2.1.md) | English home/about page | 🤖 basic |
| ☐ | [T2.2.2](tasks/M2/T2.2.2.md) | Persian home/about page (draft translation) | 🤖 standard (Persian) |
| ☐ | [T2.2.3](tasks/M2/T2.2.3.md) | Edit the Persian bio | 👤 |

**C2.3 Projects**
| ☐ | [T2.3.1](tasks/M2/T2.3.1.md) | Projects pages (EN + FA) from `content-inputs/projects.yml` | 🤖 standard (Persian) |

**C2.4 Publications and talks**
| ☐ | [T2.4.1](tasks/M2/T2.4.1.md) | Publications and talks pages (EN + FA) | 🤖 standard |

**C2.5 CV, 404 and navigation**
| ☐ | [T2.5.1](tasks/M2/T2.5.1.md) | CV pages and root 404 page | 🤖 standard (Persian) |
| ☐ | [T2.5.2](tasks/M2/T2.5.2.md) | Final M2 navbar for both languages | 🤖 basic |

**🚦 M2 gate (Reviewer):** visual review in the browser of every page in light and dark mode at phone and desktop width, with no invented personal data and no remaining `TODO(owner)`, except ones you've accepted.

### M3 — Blog engine
**C3.1 Listings and feeds**
| ☐ | [T3.1.1](tasks/M3/T3.1.1.md) | Final blog listings, date formats, RSS | 🤖 basic |

**C3.2 Post tooling**
| ☐ | [T3.2.1](tasks/M3/T3.2.1.md) | Post templates (EN + FA) | 🤖 basic |
| ☐ | [T3.2.2](tasks/M3/T3.2.2.md) | `new_post.py` and `make new-post` | 🤖 standard |

**C3.3 Style guide and RTL hardening**
| ☐ | [T3.3.1](tasks/M3/T3.3.1.md) | English style-guide page (every element) | 🤖 basic |
| ☐ | [T3.3.2](tasks/M3/T3.3.2.md) | Persian style-guide page | 🤖 standard (Persian) |
| — | FIX-C3.3-* | RTL fixes written by the Reviewer after the visual review | 🤖 |

**C3.4 Interactive figures**
| ☐ | [T3.4.1](tasks/M3/T3.4.1.md) | Observable JS and Plotly demos in the style guides | 🤖 basic |

**C3.5 Series**
| ☐ | [T3.5.1](tasks/M3/T3.5.1.md) | Series page and series front matter | 🤖 basic |

**🚦 M3 gate (Reviewer):** a new post can be created with one command, and every content element renders correctly in both directions.

### M4 — Community, SEO and analytics
**C4.1 Comments**
| ☐ | [T4.1.1](tasks/M4/T4.1.1.md) | Set up GitHub Discussions and Giscus | 👤 |
| ☐ | [T4.1.2](tasks/M4/T4.1.2.md) | Enable Giscus on posts (EN + FA) | 🤖 basic |

**C4.2 Social cards and SEO**
| ☐ | [T4.2.1](tasks/M4/T4.2.1.md) | Social card image, Open Graph, robots.txt | 🤖 standard |

**C4.3 Analytics**
| ☐ | [T4.3.1](tasks/M4/T4.3.1.md) | Create a GoatCounter account | 👤 |
| ☐ | [T4.3.2](tasks/M4/T4.3.2.md) | Add the analytics snippet | 🤖 basic |

**🚦 M4 gate (Reviewer).**

### M5 — Bilingual tooling
**C5.1 Glossary**
| ☐ | [T5.1.1](tasks/M5/T5.1.1.md) | Seed `glossary.yml` (60 terms, drafts) | 🤖 standard (Persian) |
| ☐ | [T5.1.2](tasks/M5/T5.1.2.md) | Review the glossary terms | 👤 |
| ☐ | [T5.1.3](tasks/M5/T5.1.3.md) | Glossary page generator and navbar link | 🤖 standard |

**C5.2 Translation workflow**
| ☐ | [T5.2.1](tasks/M5/T5.2.1.md) | Translation prompt file | 🤖 basic |
| ☐ | [T5.2.2](tasks/M5/T5.2.2.md) | `check_pairs.py` and `make check` | 🤖 standard |
| ☐ | [T5.2.3](tasks/M5/T5.2.3.md) | *(Optional, later)* `translate.py` with an LLM API | 🤖 standard |

**C5.3 Persian quality**
| ☐ | [T5.3.1](tasks/M5/T5.3.1.md) | `lint_fa.py` (Persian linter) added to `make check` | 🤖 standard |

**🚦 M5 gate (Reviewer).**

### M6 — Distribution and performance
**C6.1 Telegram**
| ☐ | [T6.1.1](tasks/M6/T6.1.1.md) | Create the Telegram channel and bot, add secrets | 👤 |
| ☐ | [T6.1.2](tasks/M6/T6.1.2.md) | `notify_telegram.py` | 🤖 standard |
| ☐ | [T6.1.3](tasks/M6/T6.1.3.md) | `announce.yml` workflow (manual, dry-run by default) | 🤖 basic |
| ☐ | [T6.1.4](tasks/M6/T6.1.4.md) | Telegram link on both home pages | 🤖 basic |

**C6.2 Performance and Iran accessibility**
| ☐ | [T6.2.1](tasks/M6/T6.2.1.md) | `audit_external.py` (lists third-party hosts) | 🤖 standard |
| ☐ | [T6.2.2](tasks/M6/T6.2.2.md) | `check_links.py` and image-size check in `make check` | 🤖 standard |
| — | FIX-C6.2-* | Self-host assets the audit flags (written by the Reviewer) | 🤖 |
| ☐ | [T6.2.3](tasks/M6/T6.2.3.md) | Lighthouse run and test from Iran | 👤 |

**🚦 M6 gate (Reviewer).**

### M7 — First post and launch 🚀
**C7.1 Post #1, English**
| ☐ | [T7.1.1](tasks/M7/T7.1.1.md) | Write post #1 (English) | 👤 |
| ☐ | [T7.1.2](tasks/M7/T7.1.2.md) | Technical proofread (report only, no edits) | 🤖 standard |

**C7.2 Post #1, Persian**
| ☐ | [T7.2.1](tasks/M7/T7.2.1.md) | Persian draft of post #1 | 🤖 standard (Persian) |
| ☐ | [T7.2.2](tasks/M7/T7.2.2.md) | Edit the Persian post and publish-ready checks | 👤 |

**C7.3 Pre-launch QA**
| ☐ | [T7.3.1](tasks/M7/T7.3.1.md) | Retire the test post, publish post #1, run the full QA (give the agent SLUG) | 🤖 basic |

**C7.4 Launch** 🚦
| ☐ | [T7.4.1](tasks/M7/T7.4.1.md) | Launch and announce | 👤 |

### M8 — Operating mode (repeat for every new post)
| Step | File | Who |
|---|---|---|
| R1 | [Scaffold the post](tasks/recurring/R1.md) | 🤖 basic |
| R2 | Write the English post (same as T7.1.1) | 👤 |
| R3 | [Technical proofread](tasks/recurring/R3.md) | 🤖 standard |
| R4 | [Persian draft](tasks/recurring/R4.md) | 🤖 standard (Persian) |
| R5 | Edit the Persian (same checklist as T7.2.2) | 👤 |
| R6 | [Publish checks](tasks/recurring/R6.md) | 🤖 basic |
| R7 | Ask the Reviewer: "Review post SLUG", then push and run the announce workflow | 👤 |

---

## 6. What the Reviewer checks at every checkpoint
1. Every task in the checkpoint has a report with status DONE and one commit, with message `<ID>: …`.
2. `git diff approved/<previous>..HEAD --stat` shows **only** the files the tasks allowed.
3. `make build` (from M1.4 on) succeeds on a clean tree, and `make check` (from M5 on) passes.
4. The pages look right in the browser: EN and FA, light and dark, phone and desktop widths.
5. There's no invented personal data, no secrets and no leftover `{{PLACEHOLDER}}`.
6. Every acceptance item in each task file is met.
