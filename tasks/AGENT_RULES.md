# Rules for every agent task

**Read this whole file before you start. These rules override anything else, except the task file's own explicit instructions.**

You are a coding agent working inside a git repository (the folder that contains `tasks/`). The project is a bilingual (English + Persian) personal website built with **Quarto** and hosted on **GitHub Pages**. You will be given **one task file**. Do that task and nothing else.

---

## 1. Scope: do exactly one task

1. Do **only** the task you were given. Never start the next task, even if it looks easy.
2. Create or change **only** the files listed under **"Files you may create or change"** in the task. The one exception is your report file `reports/<TASK-ID>.md`, which you may always create.
3. If you think some other file needs to change, **do not change it**. Write it under "Questions for reviewer" in your report.
4. Don't refactor, rename, reformat, reorder or "improve" anything the task doesn't mention.
5. When the task says **"exact content"**, copy it character for character. The only thing you change is the `{{PLACEHOLDERS}}` (see §2).
6. When the task says **"spec"** (for scripts), write code that does exactly what the spec says: same file names, same command-line options, same messages, same exit codes. Add nothing extra.

## 2. Placeholders

- Text in double braces like `{{GITHUB_USERNAME}}` is a placeholder.
- Replace it with the value from `config/owner.yml`. The key is the placeholder name in lowercase (`{{GITHUB_USERNAME}}` → `github_username`, `{{NAME_FA}}` → `name_fa`).
- If that value is empty or missing, **STOP** and report `BLOCKED: config/owner.yml is missing <key>`.
- Never leave `{{` … `}}` in a file you create. The only exception is Quarto shortcodes, which look like `{{< ... >}}` (with `<`). Leave those exactly as written.
- In templates, tokens like `__TITLE__` are **not** placeholders. Leave them as they are, unless the task tells you to replace them.

## 3. Never invent personal information

Names, bio text, job titles, employers, projects, publications, talks, dates of past events, and links come **only** from `config/owner.yml` or the files in `content-inputs/`.
If something you need is missing, write `TODO(owner): <what is needed>` in its place and list it in your report. Never make up an example person, project or paper.

## 4. Forbidden actions

- `git push`, `git pull`, `git rebase`, `git reset --hard`, `git commit --amend`, `git stash`, `--force` anything, and deleting branches or tags.
- Changing GitHub settings, creating accounts on any website, and handling passwords, tokens or API keys. **Never write a secret or token into any file.**
- Installing global software (`brew`, `npm -g`, `sudo`, system-wide `pip`). Python packages go only into `.venv/`, and only when the task says to install them.
- Changing the Quarto version or the file `.quarto-version`.
- Deleting files or folders, unless the task explicitly says so.
- Editing anything in `tasks/` or `reviews/`, or the files `PLAN.md`, `ROADMAP.md`, `config/owner.yml`.
- Downloading anything other than the exact URLs the task names.

## 5. Conventions

- Files: UTF-8, LF line endings, one newline at the end of the file.
- YAML: 2-space indentation, never tabs. Put a string in double quotes if it contains `:`, `#`, `{`, `}`, `[`, `]`, `@`, `*`, `&`, or begins with a quote.
- Makefile: every recipe line must begin with a **TAB** character, not spaces.
- Python: 3.11+, **standard library only** unless the task lists packages. Run scripts with `.venv/bin/python` (on CI: `python`). Every script gets a short docstring at the top saying what it does and how to run it.
- Persian text:
  - Use Persian `ی` and `ک`, never Arabic `ي` or `ك`.
  - Use the zero-width non-joiner (نیم‌فاصله, U+200C) where Persian needs it: «می‌شود», «داده‌ها», «شبکه‌های عصبی», «نوشته‌ها».
  - Use Persian punctuation `،` `؛` `؟` inside Persian sentences.
  - Write naturally and semi-formally (like a good textbook), not word-for-word from English.
- Paths in tasks are relative to the repository root. Run commands from the repository root.

## 6. When something fails

- If a command fails, read the error and fix it **only inside your allowed files**, then retry.
- After **2 failed attempts on the same problem, STOP**. Set the status to `BLOCKED` and paste the full error into the report.
- Never "make it pass" by deleting checks, skipping steps, changing other files, installing new tools or weakening the task.
- If the task's instructions look wrong or contradict each other, **STOP and ask** in the report. Don't guess.

## 7. Verify

Run **every** command in the task's **"Verify"** section, in order, from the repository root. Paste each command and its output into the report. Trim long output to the first 30 and last 30 lines. The task is only `DONE` when every "Done when" item is true.

## 8. Finish

1. Write `reports/<TASK-ID>.md` using the template below.
2. If the status is **DONE**:
   - `git add` exactly the files you created or changed, plus the report. Don't use `git add -A` or `git add .`.
   - `git commit -m "<TASK-ID>: <task title>"`. Use one commit per task.
3. If the status is **BLOCKED**: do **not** commit. Leave your changes in place and stop.
4. Finally, print the report content in your reply.

### Report template (`reports/<TASK-ID>.md`)

```markdown
# Report <TASK-ID> — <task title>

**Status:** DONE | BLOCKED
**Agent/model:** <tool and model name>

## Files changed
- path/one (created | modified)

## What I did
- one bullet per task step, in order

## Verify output
### `<command 1>`
```
<output>
```
### `<command 2>`
...

## Deviations from the task
None | <exactly what differs and why>

## TODO(owner) items left
None | <list>

## Questions for reviewer
None | <list>
```
