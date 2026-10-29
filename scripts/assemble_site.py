"""Combine en/_site and fa/_site into public/ (Persian under public/fa/). Run after rendering both sites."""

import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EN = ROOT / "en" / "_site"
FA = ROOT / "fa" / "_site"
OUT = ROOT / "public"


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
    (OUT / ".nojekyll").touch()
    n_en = sum(path.is_file() for path in EN.rglob("*"))
    n_fa = sum(path.is_file() for path in FA.rglob("*"))
    total = sum(path.is_file() for path in OUT.rglob("*"))
    print(f"assembled public/ ({total} files: en {n_en}, fa {n_fa})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
