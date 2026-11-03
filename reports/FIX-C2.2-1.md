# Report FIX-C2.2-1 — Re-copy resized profile photo

**Status:** DONE
**Agent/model:** Claude Code / Claude Haiku

## Files changed
- shared/images/profile.jpg (modified)
- reports/FIX-C2.2-1.md (created)

## What I did
- Copied `content-inputs/profile.JPG` unchanged over `shared/images/profile.jpg` with `cp`. No resize, re-encode or rename. `en/`, `fa/` and `content-inputs/` were not touched.
- Ran the Verify commands in order.

## Verify output
### `cmp content-inputs/profile.JPG shared/images/profile.jpg && echo "photo identical"`
```
photo identical
```
### `make build`
```
[1/3] posts/2026-10-hello-world/index.qmd
[2/3] index.qmd
[3/3] blog.qmd
Output created: _site/index.html
[1/3] posts/2026-10-hello-world/index.qmd
[2/3] index.qmd
[3/3] blog.qmd
Output created: _site/index.html
.venv/bin/python scripts/sync_shared.py
synced shared/ -> en/assets/ (9 files)
synced shared/ -> fa/assets/ (9 files)
quarto render en
quarto render fa
.venv/bin/python scripts/assemble_site.py
assembled public/ (79 files: en 39, fa 39)
```
(exit code 0; the build ran without the sandbox workaround)

### `ls -l public/assets/images/profile.jpg public/fa/assets/images/profile.jpg`
```
644  public/assets/images/profile.jpg  613.0K
644  public/fa/assets/images/profile.jpg  613.0K
```
### `grep -c 'profile.jpg' public/index.html public/fa/index.html`
```
public/index.html:1
public/fa/index.html:1
```

## Deviations from the task
None

## TODO(owner) items left
None

## Questions for reviewer
None
