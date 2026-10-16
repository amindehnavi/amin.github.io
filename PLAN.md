# Personal Website — Build Plan

A bilingual (English + Persian) personal site and ML/DL blog, hosted free on GitHub Pages.

---

## 1. Goals and constraints

| | |
|---|---|
| **Purpose** | (1) Introduce myself: bio, projects, CV, publications and talks. (2) Teach what I learn in ML/DL, e.g. a series on Transformers. |
| **Audience** | Mainly Persian-speaking learners, since there is little good Persian ML/DL content. English readers come second (recruiters, the wider community). |
| **Languages** | **Fully bilingual.** Every page and post exists in English and Persian (RTL). |
| **Translation** | I write in English → an LLM drafts the Persian → I edit it. |
| **Address** | `https://<username>.github.io` (free). A custom domain can be added later without breaking anything. |
| **Time budget** | About 2–3 hours a week, so the build has to happen in small sessions and the posting pace has to be sustainable. |
| **Must-have features** | LaTeX math, highlighted code, Jupyter notebooks as posts, interactive figures, comments, RSS, Telegram announcements, search. |

**Success after 6 months:** the site is live, has 5–6 bilingual posts, a Telegram channel with its first few hundred readers, and an "about" section I'm happy to send to recruiters.

---

## 2. Tech stack decision

### Choice: **Quarto**, as two sibling projects (`en/` and `fa/`), built by GitHub Actions and deployed to GitHub Pages

**Why Quarto**
- **Notebook-first.** An `.ipynb` or a `.qmd` file with Python cells *is* the blog post. Code, outputs, plots and math render without extra work. This is what makes ML posts cheap to produce, and I'll use it in every post.
- **Math and code built in:** MathJax/KaTeX, syntax highlighting, code copy buttons, callouts, footnotes, cross-references and citations (BibTeX).
- **Interactive figures without a server:** Observable JS (`{ojs}` cells), Plotly and Altair outputs, or plain JS/D3. All of them stay static and work on GitHub Pages.
- **Blog features built in:** listing pages, categories, RSS feeds, client-side search, Giscus comments, "about" page templates, Open Graph cards.
- **`freeze`:** notebooks run only on my laptop. CI just renders the stored outputs, so the CI machine never needs PyTorch or a GPU.
- **Python-native,** which fits my ML background, and I barely need any JavaScript.

**The weak spot: multilingual.** Quarto has per-document `lang` and `dir: rtl` settings, but no built-in multilingual *site* support (no per-language navbar or language switcher). The third-party package [babelquarto](https://docs.ropensci.org/babelquarto/) adds this, but it needs R, its docs don't cover blog listings, and it says nothing about RTL. So the plan uses a simple DIY setup that I fully control:

```
en/  → Quarto project → renders to en/_site/ ─┐
fa/  → Quarto project → renders to fa/_site/ ─┴→ scripts/assemble_site.py → public/   (English at /, Persian at /fa/)
```

Each language gets its own navbar text, `lang`, `dir`, listing, RSS feed, search index and Giscus language. A post uses **the same slug** in both trees (`en/posts/attention/` ↔ `fa/posts/attention/`), so a 20-line JS language switcher only has to swap the `/fa/` path prefix.

> ⚠️ Milestone M1 is a **spike that confirms this setup works** (see the gate checklist). If it fails, fall back in this order: (a) babelquarto, or (b) Hugo, which has first-class i18n and RTL, with notebooks converted to Markdown by `nbconvert`.

### Alternatives considered

| Option | Pros | Why not the main choice |
|---|---|---|
| Hugo (PaperMod/Blowfish) | Best i18n and RTL support, very fast | Notebooks are second-class (need a conversion step), and interactive figures are fiddly |
| Jekyll + al-folio | Nice academic "about"/publications pages, native to GitHub Pages | Weak multilingual and RTL support, Ruby toolchain, average notebook support |
| Astro | Most flexible, modern, built-in i18n routing | Means writing the most code, and notebooks need a custom pipeline. Too much work for 2–3 hours a week |

---

## 3. Information architecture

### Pages (in both languages)

| EN | FA | Content |
|---|---|---|
| Home / About | خانه / درباره من | Photo, short bio, what I work on, links (GitHub, LinkedIn, Scholar, email, Telegram), latest 3 posts |
| Blog | نوشته‌ها | Post listing with category filters and RSS |
| Series | مجموعه‌ها | Grouped series, e.g. "Transformers from Scratch" |
| Projects | پروژه‌ها | Grid of project cards (image, one-liner, repo/demo links) |
| Publications & Talks | مقالات و ارائه‌ها | Driven by `publications.yml` / `talks.yml` (one data source for both languages) |
| CV | رزومه | Short HTML summary plus a PDF download (English PDF is the primary one) |
| Glossary | واژه‌نامه | EN ↔ FA ML terminology table generated from `glossary.yml`. Useful in its own right and gives the site a unique angle |
| 404 | ۴۰۴ | Friendly not-found page |

### Navbar
English: `Home · Blog · Series · Projects · Publications · CV · Glossary` … `[فارسی]`. Persian: the mirrored version with `[English]`. Search is added automatically. GitHub and RSS links are in the footer.

### Repository layout

```
<username>.github.io/                 # public GitHub repo (this folder)
├── PLAN.md  ROADMAP.md               # the plan and the execution roadmap
├── tasks/                            # one file per agent/human task (+ AGENT_RULES.md)
├── reports/  reviews/                # agent reports, reviewer verdicts
├── config/owner.yml                  # personal values (the only source for agents)
├── content-inputs/                   # bio, photo, projects, CV, publications written by me
├── Makefile                          # sync / preview-en / preview-fa / build / serve / new-post / check / check-links / audit
├── requirements.txt                  # light site-level Python deps (CI uses these)
├── .quarto-version                   # pinned Quarto version for CI
├── shared/                           # the ONLY place to edit shared files
│   ├── styles/  base.scss  dark.scss  rtl.scss  fonts-fa.css
│   ├── fonts/   Vazirmatn (self-hosted)
│   ├── js/      lang-switch.html  analytics.html
│   ├── images/  favicon, profile, social card, project images
│   ├── files/   cv.pdf
│   └── data/    glossary.yml
├── en/                               # English Quarto project
│   ├── _quarto.yml  index.qmd  blog.qmd  series.qmd  projects.qmd  publications.qmd  cv.qmd  404.qmd  style-guide.qmd
│   ├── data/    projects.yml  publications.yml  talks.yml
│   ├── posts/<YYYY-MM-slug>/index.qmd   (+ images)
│   ├── assets/                       # copy of shared/ made by `make sync` (git-ignored)
│   └── _freeze/                      # committed: stored code outputs
├── fa/                               # Persian project, same structure and same post folder names
├── templates/post/  en.qmd  fa.qmd
├── prompts/translate_en_to_fa.md
├── scripts/  sync_shared  assemble_site  new_post  build_glossary  check_pairs  lint_fa
│            check_links  check_images  audit_external  make_social_card  notify_telegram
└── .github/workflows/  publish.yml  announce.yml
```

---

## 4. Build architecture (settled)

The exact configuration lives in the task files. The decisions behind it are listed in [ROADMAP.md §3](ROADMAP.md). In short:
- Each language is its own Quarto project with its own `lang`, `dir`, navbar, listing, RSS feed, search index, Giscus category and UI language.
- Quarto has no Persian UI strings, so `fa/_language-fa.yml` provides them.
- `make sync` copies `shared/` into each project's `assets/` folder, because Quarto only sees files inside a project.
- `make build` renders both projects into their own `_site/` folders and assembles them into `public/`. This avoids two projects writing into one output folder.
- CI (`publish.yml`) installs only the light `requirements.txt`, builds, checks internal links and deploys `public/`. Code outputs come from the committed `_freeze/` folders.
- Persian pages: Vazirmatn is self-hosted. Code, output and display math are forced left-to-right, and `[English]{.ltr}` isolates English fragments.

---


## 5. Bilingual and translation workflow

### Per-post workflow
1. **Learn and experiment** in a notebook (`en/posts/<slug>/index.ipynb`), or write a `.qmd` with code cells.
2. **Write the English post** and run `quarto preview en` locally (this executes the cells and updates `_freeze`).
3. **Draft the Persian version**, either way:
   - *Start simple:* an agent runs the recurring task `tasks/recurring/R4.md`, which follows `prompts/translate_en_to_fa.md`. The full per-post pipeline is R1–R7 in [ROADMAP.md](ROADMAP.md) (M8).
   - *Later (optional task T5.2.3):* a `scripts/translate.py`. It sends only the prose (Markdown cells / non-code blocks) to the Claude API with `glossary.yml` as context, leaves code, math, shortcodes and front-matter keys untouched, and writes `fa/posts/<slug>/…` with `draft: true`. Building it is also good practice for my agents/LLM-tooling learning.
4. **Edit the Persian by hand** (checklist below), then set `draft: false`.
5. `make check`, which should report no missing pairs, then commit and push. CI deploys.
6. **Announce**: run the `announce` workflow with the slug (see §7).

**Rule:** the Persian version may lag the English one by up to **2 weeks**. During that time the English post can go live, and the Persian listing shows nothing for it yet.

### Translation prompt essentials
- Audience: Persian-speaking students and engineers. Natural, clear, semi-formal Persian (not a word-by-word translation).
- **Never** change code, math, URLs, file paths, shortcodes or front-matter keys. Translate only the `title` / `description` values.
- Terminology comes from `glossary.yml`. On first mention write the Persian term with the English in parentheses: «توجه (Attention)». After that, use the Persian term or the commonly used loanword, as the glossary says.
- Use the correct نیم‌فاصله (ZWNJ): «می‌شود», «داده‌ها», «شبکه‌های».

### `glossary.yml` format
```yaml
- en: attention
  fa: توجه
  fa_alt: [اتنشن]
  farhangestan: توجه       # official equivalent, when one exists
  note: "Keep 'Attention' in parentheses on first use."
- en: embedding
  fa: بردار تعبیه
  fa_alt: [امبدینگ]
```
This one file feeds both the translation prompt (consistency) and the public Glossary page (value for readers).

### Persian editing checklist
- [ ] Terms match the glossary, and English appears in parentheses on first use
- [ ] ZWNJ (نیم‌فاصله) is correct, and Arabic «ي/ك» is replaced with Persian «ی/ک»
- [ ] Sentences read naturally in Persian, not as calques of English
- [ ] Mixed LTR fragments (`model.fit()`, "GPT-2") don't scramble the line
- [ ] Figure captions, alt text, callout titles and the post `description` are translated
- [ ] Digits: pick one convention and stick to it. Suggestion: Persian digits in prose, Latin digits in code and math.

---

## 6. Blog content system

### Post types (to match the 2–3 h/week budget)
| Type | Size | Pace |
|---|---|---|
| **Deep dive** | 1,500–3,000 words, notebook, figures | ~1 per month |
| **Paper notes** | 500–800 words, key ideas + one figure | optional, between deep dives |
| **TIL / short** | 200–400 words | whenever |

### Deep-dive post template
1. **TL;DR**: 3 bullet points
2. **Prerequisites**: links to earlier posts and the glossary
3. **Intuition first**: analogy and a diagram
4. **The math**: introduced gradually, every symbol defined
5. **Code**: minimal PyTorch/NumPy, runnable top to bottom
6. **Interactive figure**: e.g. an attention heatmap with a slider (`{ojs}`)
7. **Common pitfalls / misconceptions**
8. **Terms in this post**: EN ↔ FA mini table, generated from the glossary
9. **Further reading**: papers, videos, books
10. **Download**: notebook + `requirements.txt` (and a Colab badge, noting that Colab may not be reachable from Iranian IPs)

### Front matter (same keys in both languages)
```yaml
---
title: "Attention, Intuitively"
description: "What attention computes and why it works, built up from dot products."
date: 2026-12-01
categories: [transformers, nlp, from-scratch]
series: "Transformers from Scratch"
series-order: 1
image: thumbnail.png        # used for listings and social cards
draft: false
---
```

### First series: *Transformers from Scratch*
1. Why sequence models needed attention (RNN limits, intuition)
2. Self-attention: dot products, softmax, Q/K/V, with an interactive heatmap
3. Multi-head attention and what the heads learn
4. Positional encodings (sinusoidal, learned, RoPE)
5. The full encoder/decoder block (residuals, LayerNorm, FFN)
6. Train a tiny GPT on Persian text (a nice hook for the audience)

**Next series ideas,** based on my CV background: *From CNNs to Vision Transformers*, *Diffusion models intuitively*, *Building LLM agents*.

### Interactive figures, from cheapest to heaviest
1. Static Matplotlib output (the default)
2. Plotly/Altair output from the notebook (hover and zoom, no extra code)
3. `{ojs}` cells with sliders for "what if" explorations
4. In-browser Python (Pyodide / `quarto-live`). This downloads 10 MB or more, so it's **avoided by default** because many Iranian readers have slow connections.

---

## 7. Audience, distribution and community

- **Telegram channel** (main channel for Iranian learners): one announcement per post in Persian with the link, and the English link underneath.
  - Automate it with `announce.yml` (manual dispatch, input = slug): `notify_telegram.py` reads the post's title and description and calls the Bot API. Secrets: `TELEGRAM_BOT_TOKEN`, `TELEGRAM_CHAT_ID`.
  - Manual dispatch is chosen over fully automatic posting because at one post a month it's simpler and can never double-post.
- **Virgool (ویرگول):** cross-post the Persian version, or a summary with a canonical link, to reach Persian readers who don't know the site yet.
- **LinkedIn / X:** short English announcement with the social card image.
- **RSS:** `/blog.xml` and `/fa/blog.xml`. An RSS-to-email newsletter (e.g. Buttondown) can come later (M8).
- **Comments:** Giscus (GitHub Discussions) with one discussion category per language. Readers need a GitHub account, which is acceptable for this audience.
- **Analytics:** GoatCounter (free, no cookies, lightweight). No Google Analytics.

### Iran-specific accessibility
- **Self-host fonts** (Vazirmatn, Inter). No Google Fonts or other Google CDNs.
- Check whether MathJax/KaTeX and Quarto's other CDN assets load quickly from Iran. Self-host them if not.
- Keep pages light: WebP images, compressed figures, lazy-loaded interactives.
- Before launch, ask 2–3 friends in Iran to test the site on mobile data, both with and without a VPN.
- Offer notebook downloads directly, not only via Colab.

---

## 8. Roadmap

The full execution plan, with **milestones → checkpoints → tasks**, is in [ROADMAP.md](ROADMAP.md). Every task has its own file in `tasks/`, written for cheap coding agents, and every checkpoint ends with a review.

| Milestone | Outcome |
|---|---|
| M0 Prerequisites | Accounts, tools, personal info |
| M1 Foundation and bilingual spike 🚦 | A live bilingual skeleton that proves the architecture |
| M2 Design and identity | Theme, About, Projects, Publications, CV |
| M3 Blog engine | Listings, templates, style guide, interactive figures, series |
| M4 Community, SEO and analytics | Comments, social cards, analytics |
| M5 Bilingual tooling | Glossary, translation prompt, pair checker, Persian linter |
| M6 Distribution and performance | Telegram, asset audit, link checks, Iran test |
| M7 First post and launch 🚀 | Post #1 in both languages, QA, launch |
| M8 Operating mode | Repeatable per-post pipeline (`tasks/recurring/`) |

### Effort reality check
A bilingual deep dive takes about **9–10 hours** (learning + notebook ~4 h, English writing ~3 h, Persian editing ~1.5 h, publishing + promotion ~0.5 h). At 2.5 h/week that comes to roughly **one post a month**. Since the learning is happening anyway, the extra cost is mostly writing.

---


## 9. Definition of done for launch
- [ ] Both languages are live, RTL is correct, and the language switcher works on every page
- [ ] About, Projects, Publications & Talks, CV and Glossary are filled in
- [ ] At least one published bilingual deep-dive post with math, code, a notebook download and an interactive figure
- [ ] Comments, RSS, search and analytics work
- [ ] The Telegram announcement flow has been tested
- [ ] Lighthouse scores ≥ 90 for performance and accessibility on mobile
- [ ] Tested from Iran

---

## 10. Risks and mitigations

| Risk | Mitigation |
|---|---|
| Bilingual setup in Quarto turns out painful | M1 gate with a clear fallback (babelquarto → Hugo) |
| Bilingual work doubles the writing time and causes burnout | AI draft + edit; the Persian version may lag by 2 weeks; mix in short posts |
| Infrastructure tinkering eats the writing time | Hard cap: the site ships at M7; new features only after 3 posts |
| Site or CDN assets slow or blocked in Iran | Self-hosted assets, light pages, real tests from inside Iran |
| Inconsistent Persian terminology | A single `glossary.yml` used by both the prompt and the glossary page |
| Notebooks break when library versions change | `freeze` + a `requirements.txt` per post |

---

## 11. Open decisions (decide while building)
- Site name/tagline in both languages (set in `config/owner.yml`)
- ~~Date display on Persian pages~~ → decided: Gregorian `YYYY-MM-DD` (Jalali can come later with a small script)
- Default landing page: English at `/` (current plan) or detect the browser language and suggest `/fa/`
- ~~Persian digits convention~~ → decided: Persian digits in prose, Latin digits in code, math, tables and front matter
- Whether to add a custom domain once the site has traction
