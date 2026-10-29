# Report FIX-C1.2-1 — correct README deployment URLs

**Status:** DONE
**Agent/model:** Codex / GPT-6.1 Terra

## Files changed
- README.md (modified)
- reports/FIX-C1.2-1.md (created)

## What I did
- Corrected the English and Persian site URLs to use the confirmed deployment base.

## Verify output
### `cat README.md`
```
# amin.github.io

Source of my bilingual (English / فارسی) personal website and ML blog, built with [Quarto](https://quarto.org).

- English: https://amindehnavi.github.io/amin.github.io/
- فارسی: https://amindehnavi.github.io/amin.github.io/fa/

See `PLAN.md` for the plan and `ROADMAP.md` for the build roadmap.
```
### `git diff -- README.md`
```
diff --git a/README.md b/README.md
index c9e2eef..e03fb4f 100644
--- a/README.md
+++ b/README.md
@@ -2,7 +2,7 @@
 
 Source of my bilingual (English / فارسی) personal website and ML blog, built with [Quarto](https://quarto.org).
 
-- English: https://amin.github.io/
-- فارسی: https://amin.github.io/fa/
+- English: https://amindehnavi.github.io/amin.github.io/
+- فارسی: https://amindehnavi.github.io/amin.github.io/fa/
 
 See `PLAN.md` for the plan and `ROADMAP.md` for the build roadmap.
```

## Deviations from the task
None

## TODO(owner) items left
None

## Questions for reviewer
None
