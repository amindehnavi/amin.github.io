"""Combine en/_site and fa/_site into public/ (Persian under public/fa/). Run after rendering both sites."""

import json
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EN = ROOT / "en" / "_site"
FA = ROOT / "fa" / "_site"
OUT = ROOT / "public"
DRAFT_RE = re.compile(r"^draft:\s*true\s*$")


def front_matter_lines(folder: Path) -> list[str]:
    """Return the YAML front matter lines of a post folder's index.qmd or index.ipynb."""
    text = ""
    qmd = folder / "index.qmd"
    ipynb = folder / "index.ipynb"
    if qmd.is_file():
        text = qmd.read_text(encoding="utf-8")
    elif ipynb.is_file():
        try:
            cells = json.loads(ipynb.read_text(encoding="utf-8")).get("cells", [])
        except ValueError:
            return []
        if cells and cells[0].get("cell_type") == "raw":
            source = cells[0].get("source", "")
            text = source if isinstance(source, str) else "".join(source)
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return []
    result = []
    for line in lines[1:]:
        if line.strip() == "---":
            break
        result.append(line)
    return result


def remove_drafts() -> None:
    for lang, out_posts in (("en", OUT / "posts"), ("fa", OUT / "fa" / "posts")):
        posts = ROOT / lang / "posts"
        if not posts.is_dir():
            continue
        for folder in sorted(posts.iterdir()):
            if not folder.is_dir():
                continue
            if not ((folder / "index.qmd").is_file() or (folder / "index.ipynb").is_file()):
                continue
            if any(DRAFT_RE.match(line) for line in front_matter_lines(folder)):
                target = out_posts / folder.name
                if target.exists():
                    shutil.rmtree(target)
                print(f"skipped draft: {lang}/posts/{folder.name}")


def main() -> int:
    if not EN.is_dir():
        print('error: en/_site not found - run "make render-en" first', file=sys.stderr)
        return 1
    if not FA.is_dir():
        print('error: fa/_site not found - run "make render-fa" first', file=sys.stderr)
        return 1
    if (EN / "fa").exists():
        print("error: en/_site/fa exists and would collide with the Persian site", file=sys.stderr)
        return 1

    if OUT.exists():
        shutil.rmtree(OUT)
    shutil.copytree(EN, OUT)
    shutil.copytree(FA, OUT / "fa")
    remove_drafts()
    (OUT / ".nojekyll").touch()
    n_en = sum(path.is_file() for path in EN.rglob("*"))
    n_fa = sum(path.is_file() for path in FA.rglob("*"))
    total = sum(path.is_file() for path in OUT.rglob("*"))
    print(f"assembled public/ ({total} files: en {n_en}, fa {n_fa})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
