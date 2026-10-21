"""Fill in the release details in index.html and write the site.

Usage: python3 build.py <release.json> <output directory> [<font directory>]

<release.json> is the output of
    gh release view --json tagName,publishedAt,assets
for the latest release, or "{}" if there is none yet.
The download links always point to releases/latest, so they stay valid
even if the site is not rebuilt after a release.

Placeholders in index.html:
    {{REPO_URL}}        https://github.com/<owner>/<repo>, from $GITHUB_REPOSITORY
    {{VERSION}}         tag of the latest release, e.g. "version v2026.1"
    {{DATE}}            its publication date, e.g. "21 October 2026"
    {{SIZE:<file>}}     size of that release asset, e.g. "1.4 MB"

If a font directory is given, the Latin Modern files that index.html
expects are copied into fonts/ (on Ubuntu: package fonts-lmodern).
"""

import json
import os
import re
import shutil
import sys
from datetime import datetime
from pathlib import Path

HERE = Path(__file__).resolve().parent
FONTS = [
    "lmroman10-regular.otf",
    "lmroman10-italic.otf",
    "lmroman10-bold.otf",
    "lmmono10-regular.otf",
]


def human_size(n):
    if n < 1000 * 1000:
        return f"{n / 1000:.0f} kB"
    return f"{n / 1000 / 1000:.1f} MB"


def main():
    if len(sys.argv) not in (3, 4):
        sys.exit(__doc__)
    release = json.loads(Path(sys.argv[1]).read_text() or "{}")
    out = Path(sys.argv[2])

    repo = os.environ.get("GITHUB_REPOSITORY", "P4ntomime/LaTeX-Workshop-ECE")
    tag = release.get("tagName")
    published = release.get("publishedAt")
    sizes = {a["name"]: a["size"] for a in release.get("assets", [])}

    values = {
        "REPO_URL": f"https://github.com/{repo}",
        "VERSION": f"version {tag}" if tag else "latest version",
        "DATE": "",
    }
    if published:
        date = datetime.fromisoformat(published.replace("Z", "+00:00"))
        values["DATE"] = f"{date.day} {date:%B %Y}"

    def fill(match):
        key = match.group(1)
        if key.startswith("SIZE:"):
            size = sizes.get(key[len("SIZE:"):])
            return human_size(size) if size is not None else ""
        if key not in values:
            sys.exit(f"index.html: unknown placeholder {{{{{key}}}}}")
        return values[key]

    html = (HERE / "index.html").read_text(encoding="utf-8")
    html = re.sub(r"\{\{([^}]+)\}\}", fill, html)

    # Start from an empty folder, but never delete one that is not a site.
    if out.exists():
        if any(out.iterdir()) and not (out / "index.html").exists():
            sys.exit(f"{out} is not empty and has no index.html; not deleting it")
        shutil.rmtree(out)
    out.mkdir(parents=True)
    (out / "index.html").write_text(html, encoding="utf-8")

    if len(sys.argv) == 4:
        (out / "fonts").mkdir()
        for name in FONTS:
            shutil.copy(Path(sys.argv[3]) / name, out / "fonts" / name)

    print(f"wrote {out}/ ({tag or 'no release yet'})")


if __name__ == "__main__":
    main()
