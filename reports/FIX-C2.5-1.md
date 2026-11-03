# Report FIX-C2.5-1 — Scroll wide display math inside its box

**Status:** DONE
**Agent/model:** Claude Code / Claude Haiku

## Files changed
- shared/styles/base.scss (modified)
- reports/FIX-C2.5-1.md (created)

## What I did
- Read `tasks/AGENT_RULES.md`, `AGENTS.md` and the FIX-C2.5-1 section of `reviews/C2.5.md`.
- Appended the exact SCSS block from the review at the end of the `scss:rules` section in `shared/styles/base.scss`, separated from the previous rule by one blank line. Existing content unchanged.
- Ran `make build`; it succeeded on the first attempt (no sandbox retry needed).
- Ran the grep check and the diff check listed below.

## Verify output
### `make build`
```
.venv/bin/python scripts/sync_shared.py
synced shared/ -> en/assets/ (11 files)
synced shared/ -> fa/assets/ (11 files)
quarto render en
[1/7] posts/2026-10-hello-world/index.qmd
[2/7] 404.qmd
[3/7] projects.qmd
[4/7] index.qmd
[5/7] publications.qmd
[6/7] cv.qmd
[7/7] blog.qmd

Output created: _site/index.html

quarto render fa
[1/6] posts/2026-10-hello-world/index.qmd
[2/6] projects.qmd
[3/6] index.qmd
[4/6] publications.qmd
[5/6] cv.qmd
[6/6] blog.qmd

Output created: _site/index.html

.venv/bin/python scripts/assemble_site.py
assembled public/ (90 files: en 45, fa 44)
```
(Exit code 0. The build was run twice; the second run's exit code was 0 as well.)

### `grep -c 'mjx-container\[display=true\]{overflow-x:auto\|mjx-container\[display="true"\]{overflow-x:auto\|overflow-x: auto' public/site_libs/bootstrap/bootstrap*.min.css public/fa/site_libs/bootstrap/bootstrap*.min.css`
```
public/site_libs/bootstrap/bootstrap-91f77f268eb2dd77ec456f6a9026399f.min.css:1
public/site_libs/bootstrap/bootstrap-dark-f91881fdc77476cff40615d1307dbcd9.min.css:1
public/fa/site_libs/bootstrap/bootstrap-dark-b0ee03a541cad7fd6ae7331046b8f8e5.min.css:1
public/fa/site_libs/bootstrap/bootstrap-e56530a66d004cde860864e3c4133f42.min.css:1
```

### `git diff --stat HEAD -- shared/styles/base.scss`
```
 shared/styles/base.scss | 7 +++++++
 1 file changed, 7 insertions(+)
```
Added lines only:
```
+
+/* Wide display equations scroll inside their own box instead of widening the page on phones. */
+mjx-container[display="true"] {
+  overflow-x: auto;
+  overflow-y: hidden;
+  max-width: 100%;
+}
```

## Deviations from the task
None

## TODO(owner) items left
None

## Questions for reviewer
None
