"""Copy shared/ into en/assets/ and fa/assets/. Run: .venv/bin/python scripts/sync_shared.py"""

from pathlib import Path
import shutil
import sys

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "shared"
DESTS = [ROOT / "en" / "assets", ROOT / "fa" / "assets"]


def main() -> int:
    if not SRC.is_dir():
        print("error: shared/ folder not found", file=sys.stderr)
        return 1

    for dest in DESTS:
        if dest.name != "assets" or dest.parent.name not in ("en", "fa"):
            print(f"error: refusing to delete {dest}", file=sys.stderr)
            return 1
        if dest.exists():
            shutil.rmtree(dest)
        shutil.copytree(SRC, dest, ignore=shutil.ignore_patterns(".gitkeep", ".DS_Store"))
        count = sum(1 for path in dest.rglob("*") if path.is_file())
        print(f"synced shared/ -> {dest.parent.name}/assets/ ({count} files)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
