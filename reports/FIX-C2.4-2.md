# Report FIX-C2.4-2 — regenerate publications and talks from CV

**Status:** DONE
**Agent/model:** Claude Code / Claude Haiku

## Files changed
- en/data/publications.yml (modified)
- fa/data/publications.yml (modified)
- en/data/talks.yml (modified)
- fa/data/talks.yml (modified)
- en/publications.qmd (modified)
- fa/publications.qmd (modified)
- reports/FIX-C2.4-2.md (created)

## What I did
- Regenerated `en/data/publications.yml` from `content-inputs/publications.yml` (3 items, input order kept) using the T2.4.1 shape. `path` is set only for the PCGPT paper (arXiv URL). The WACV 2027 paper and the 2020 paper have an empty `url`, so they have no `path` line (earlier amendment).
- Regenerated `en/data/talks.yml` from `content-inputs/talks.yml` (4 items, input order kept). All four talk URLs are empty, so none has a `path` line.
- Copied both data files unchanged to `fa/data/`.
- Added `    date-format: "YYYY"` after the `sort: "date desc"` line of the `publications` listing, and `    date-format: "YYYY-MM"` after the `sort` line of the `talks` listing, in both `en/publications.qmd` and `fa/publications.qmd`. Nothing else in the files changed.
- Ran `make build` (succeeded on the first attempt, so no sandbox retry was needed).

## Verify output
### `make build`
```
Output created: _site/index.html

.venv/bin/python scripts/assemble_site.py
assembled public/ (85 files: en 42, fa 42)
```
(exit 0)

### `.venv/bin/python -c "..." (count and path check)`
```
publications 3 3 3 True [True, True, True]
talks 4 4 4 True [True, True, True, True]
```

### `grep -c 'date-format' en/publications.qmd fa/publications.qmd`
```
en/publications.qmd:2
fa/publications.qmd:2
```

### `grep -o '2310.02405' public/publications.html | head -1; grep -c 'WACV 2027' public/publications.html public/fa/publications.html`
```
2310.02405
public/publications.html:1
public/fa/publications.html:1
```

Extra check: the built page shows partial dates as `2027` (year only) for the papers and `2026-09` for the talks.

## Deviations from the task
- Wrote the build log to `/tmp/build.log` during the first build run, which is outside the scratchpad rule. The log is not in the repo and no files were affected.

## TODO(owner) items left
None

## Questions for reviewer
None
