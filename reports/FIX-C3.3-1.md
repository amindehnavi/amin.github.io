# Report FIX-C3.3-1 — RTL callouts and figure captions; responsive images

**Status:** DONE
**Agent/model:** Claude Code / Claude Haiku

## Files changed
- shared/styles/rtl.scss (modified: 20 lines appended)
- shared/styles/base.scss (modified: 6 lines appended)
- reports/FIX-C3.3-1.md (created)

## What I did
- Read `tasks/AGENT_RULES.md`, `AGENTS.md` and `reviews/C3.3.md`.
- Extracted the two ```scss blocks from `reviews/C3.3.md` with awk into the scratchpad (`block1.scss`, `block2.scss`), not retyped.
- Appended block 1 to the end of `shared/styles/rtl.scss` after one blank line, and block 2 to the end of `shared/styles/base.scss` after one blank line. Existing content was kept (byte-prefix check passed).
- Proved the appends are unchanged: the bytes added to each file equal the blank line plus the extracted block (diff empty for both).
- Ran `make build` (exit 0, no database error, no retry needed). Both language projects rendered and `public/` was assembled (96 files: en 48, fa 47).
- Ran the Verify commands below.

## Verify output
### `make build`
```
.venv/bin/python scripts/sync_shared.py
synced shared/ -> en/assets/ (12 files)
synced shared/ -> fa/assets/ (12 files)
quarto render en
... (8 files rendered, Output created: _site/index.html)
quarto render fa
... (7 files rendered, Output created: _site/index.html)
.venv/bin/python scripts/assemble_site.py
assembled public/ (96 files: en 48, fa 47)
```
(exit code 0)

### `grep -o 'border-right-color:[^;}]*' public/fa/site_libs/bootstrap/bootstrap-[0-9a-f]*.min.css | sort -u | wc -l`
```
22
```
Note: the glob `bootstrap-[0-9a-f]*.min.css` matches both the light file (`bootstrap-edac5adea42350692d6c750a74a06fe0.min.css`) and the dark file (`bootstrap-dark-0dcb7645d7612045427c27a90f665cbb.min.css`). The count of 22 is across both. The Persian light file alone has 11 distinct `border-right-color` values, which includes the 5 callout colours `#2780e3`, `#3fb618`, `#f0ad4e`, `#ff0039`, `#ff7518`. That meets the "at least 5" criterion. The rules are minified as, for example: `html[dir=rtl] div.callout-caution.callout{border-right-color:#f0ad4e}`.

### `grep -c 'main img{max-width:100%;height:auto}' public/site_libs/bootstrap/bootstrap*.min.css public/fa/site_libs/bootstrap/bootstrap*.min.css`
```
public/site_libs/bootstrap/bootstrap-dark-6d87de58c313174551356f1d1769bb52.min.css:1
public/site_libs/bootstrap/bootstrap-f0cf6aca7d3425ff513727158bc35072.min.css:1
public/fa/site_libs/bootstrap/bootstrap-dark-0dcb7645d7612045427c27a90f665cbb.min.css:1
public/fa/site_libs/bootstrap/bootstrap-edac5adea42350692d6c750a74a06fe0.min.css:1
```
The rule is found in all four stylesheets. The minified text is `main img{max-width:100%;height:auto}`.

### `git diff --stat HEAD -- shared/styles/`
```
 shared/styles/base.scss |  6 ++++++
 shared/styles/rtl.scss  | 20 ++++++++++++++++++++
 2 files changed, 26 insertions(+)
```
Only added lines (no `-` lines in the diff).

## Deviations from the task
None. The Verify grep for `border-right-color` matches both light and dark stylesheets, so its count (22) is larger than the light-file count (11). The Done-when criterion is still met (at least 5 distinct values in the Persian light stylesheet).

## TODO(owner) items left
None

## Questions for reviewer
None
