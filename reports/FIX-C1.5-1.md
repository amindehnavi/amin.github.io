# Report FIX-C1.5-1 — mirror Persian navbar group spacing

**Status:** DONE
**Agent/model:** Codex / GPT-6.1 Terra (low)

## Files changed
- shared/styles/rtl.scss (modified)
- reports/FIX-C1.5-1.md (created)

## What I did
- Appended desktop-only RTL navbar margin corrections for Bootstrap's physical margin utilities.
- Built both language projects and inspected the stylesheet diff and repository status.

## Verify output
### `make build`
```text
.venv/bin/python scripts/sync_shared.py
synced shared/ -> en/assets/ (5 files)
synced shared/ -> fa/assets/ (5 files)
quarto render en
[1/3] posts/2026-10-hello-world/index.qmd
[2/3] index.qmd
[3/3] blog.qmd

Output created: _site/index.html

quarto render fa
[1/3] posts/2026-10-hello-world/index.qmd
[2/3] index.qmd
[3/3] blog.qmd

Output created: _site/index.html

.venv/bin/python scripts/assemble_site.py
assembled public/ (67 files: en 33, fa 33)
```
### `git diff -- shared/styles/rtl.scss`
```diff
diff --git a/shared/styles/rtl.scss b/shared/styles/rtl.scss
index febdb6c..b6dd157 100644
--- a/shared/styles/rtl.scss
+++ b/shared/styles/rtl.scss
@@ -35,3 +35,16 @@ mjx-container:not([display="true"]) {
 body {
   line-height: 1.9;
 }
+
+/* Correct Bootstrap's physical margin utilities for RTL navigation. */
+@media (min-width: 992px) {
+  html[dir="rtl"] #quarto-header .navbar-nav.me-auto {
+    margin-right: 0 !important;
+    margin-left: auto !important;
+  }
+
+  html[dir="rtl"] #quarto-header .navbar-nav.ms-auto {
+    margin-left: 0 !important;
+    margin-right: auto !important;
+  }
+}
```
### `git status --short`
```text
 M reviews/C1.5.md
 M shared/styles/rtl.scss
 M tasks/M0/T0.1.2.md
?? AGENTS.md
```

## Deviations from the task
None

## TODO(owner) items left
None

## Questions for reviewer
- Please check desktop navigation and expanded phone navigation in both English and Persian in a browser.
