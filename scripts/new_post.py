"""Create a new post in en/posts and fa/posts from templates/post. Run: make new-post ARGS='--slug my-topic --title-en "My Topic"'"""

import argparse
import datetime
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SLUG_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")


def fail(message: str) -> int:
    print(f"error: {message}", file=sys.stderr)
    return 2


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a new post in both languages.")
    parser.add_argument("--slug", required=True)
    parser.add_argument("--title-en", required=True)
    parser.add_argument("--title-fa", default="TODO(owner): Persian title")
    parser.add_argument("--date", default=datetime.date.today().isoformat())
    parser.add_argument("--series", default=None)
    parser.add_argument("--series-order", default=None)
    args = parser.parse_args()

    if not SLUG_RE.match(args.slug):
        return fail("slug must be lowercase words joined by dashes")
    try:
        parsed = datetime.datetime.strptime(args.date, "%Y-%m-%d").date()
    except ValueError:
        return fail("date must be YYYY-MM-DD")
    if (args.series is None) != (args.series_order is None):
        return fail("--series and --series-order must be used together")
    if args.series_order is not None:
        try:
            order = int(args.series_order)
        except ValueError:
            return fail("--series-order must be a positive integer")
        if order < 1:
            return fail("--series-order must be a positive integer")

    folder = f"{parsed.strftime('%Y-%m')}-{args.slug}"
    targets = {lang: ROOT / lang / "posts" / folder for lang in ("en", "fa")}
    if any(path.exists() for path in targets.values()):
        return fail(f"post folder already exists: {folder}")

    titles = {"en": args.title_en, "fa": args.title_fa}
    for lang in ("en", "fa"):
        text = (ROOT / "templates" / "post" / f"{lang}.qmd").read_text(encoding="utf-8")
        text = text.replace("__TITLE__", titles[lang].replace('"', '\\"'))
        text = text.replace("__DATE__", args.date)
        if args.series is not None:
            text = text.replace("__SERIES__", args.series)
            text = text.replace("__SERIES_ORDER__", str(order))
        else:
            text = "".join(
                line
                for line in text.splitlines(keepends=True)
                if "__SERIES__" not in line and "__SERIES_ORDER__" not in line
            )
        targets[lang].mkdir(parents=True)
        with open(targets[lang] / "index.qmd", "w", encoding="utf-8", newline="\n") as fh:
            fh.write(text)
        print(f"created {lang}/posts/{folder}/index.qmd")
    return 0


if __name__ == "__main__":
    sys.exit(main())
