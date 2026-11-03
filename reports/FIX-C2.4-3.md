# Report FIX-C2.4-3 — Let listing-table cells wrap long words

**Status:** DONE
**Agent/model:** Claude Code / Claude Haiku

## Files changed
- shared/styles/base.scss (modified)
- reports/FIX-C2.4-3.md (created)

## What I did
- Read `tasks/AGENT_RULES.md`, `AGENTS.md`, and the FIX-C2.4-3 section of `reviews/C2.4.md`.
- Appended the specified block, exactly as written, at the end of `shared/styles/base.scss` in the `scss:rules` section, after the existing `figure img` rule and one blank line. No existing content was changed.
- Ran `make build` from the repository root. It succeeded (exit 0) on the first try, so no retry was needed.
- Ran the Verify commands below.

## Verify output
### `make build`
```
.venv/bin/python scripts/sync_shared.py
synced shared/ -> en/assets/ (11 files)
synced shared/ -> fa/assets/ (11 files)
quarto render en
...
Output created: _site/index.html

quarto render fa
...
Output created: _site/index.html

.venv/bin/python scripts/assemble_site.py
assembled public/ (90 files: en 45, fa 44)
```
(Trimmed. The full output is shorter than 60 lines. A second run also exited 0.)

### `grep -c 'overflow-wrap:anywhere\|overflow-wrap: anywhere' public/site_libs/bootstrap/bootstrap*.min.css public/fa/site_libs/bootstrap/bootstrap*.min.css`
```
public/site_libs/bootstrap/bootstrap-2edc99e5f694be9a8a63487939a9a7ab.min.css:1
public/site_libs/bootstrap/bootstrap-dark-ea31c730ab387e288a2f14481139b772.min.css:1
public/fa/site_libs/bootstrap/bootstrap-8b2a972bf0a826d3478583d29559bd3c.min.css:1
public/fa/site_libs/bootstrap/bootstrap-dark-4fb950bfa7ce21f10c2bcc255328fe8a.min.css:1
```

### `git diff --stat HEAD -- shared/styles/base.scss`
```
 shared/styles/base.scss | 5 +++++
 1 file changed, 5 insertions(+)
```

## Deviations from the task
None

## TODO(owner) items left
None

## Questions for reviewer
None
