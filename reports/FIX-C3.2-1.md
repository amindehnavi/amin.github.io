# Report FIX-C3.2-1 — Strict post dates; keep drafts out of public/

**Status:** DONE
**Agent/model:** Claude Code / Claude Sonnet

## Files changed
- scripts/new_post.py (modified)
- scripts/assemble_site.py (modified)
- reports/FIX-C3.2-1.md (created)

## What I did
- new_post.py: added a `re.fullmatch(r"\d{4}-\d{2}-\d{2}", args.date)` check before `strptime`, with the existing message and exit code 2.
- assemble_site.py: added `remove_drafts()`, called after both `copytree` calls and before `.nojekyll`. It reads front matter from `index.qmd` or the first raw cell of `index.ipynb`, using the standard library only. For `draft: true` it runs `shutil.rmtree` on the output folder and prints `skipped draft: <lang>/posts/<folder>`. Existing checks, messages and the final count line are unchanged.
- Ran Verify and the cleanup.

## Verify output
### unpadded date
```
error: date must be YYYY-MM-DD
exit=2
```
No folder was created (`ls en/posts` showed only 2026-10-hello-world and _metadata.yml).
### make new-post ... && make build | tail
```
created en/posts/2026-11-zz-draft/index.qmd
created fa/posts/2026-11-zz-draft/index.qmd
skipped draft: en/posts/2026-11-zz-draft
skipped draft: fa/posts/2026-11-zz-draft
assembled public/ (92 files: en 48, fa 47)
```
### ls public/posts public/fa/posts
```
public/fa/posts:
2026-10-hello-world

public/posts:
2026-10-hello-world
```
### ls hello-world index.html
```
public/fa/posts/2026-10-hello-world/index.html
public/posts/2026-10-hello-world/index.html
```
### Cleanup
```
assembled public/ (92 files: en 46, fa 45)
 M scripts/assemble_site.py
 M scripts/new_post.py
?? .claude/
```
(The report was written after this status.)

## Deviations from the task
None. The `en`/`fa` counts in the assembled line are counted from `_site`, so they still included draft files in the first build (48/47); the total is counted from `OUT` after removal, as specified.

## TODO(owner) items left
None

## Questions for reviewer
None
