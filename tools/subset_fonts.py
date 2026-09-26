# SPDX-License-Identifier: MIT
"""Re-subset the self-hosted fonts to exactly the characters tower-study.html uses.

Run this after changing any on-screen text (window.I18N or the HUD markup):

    pip install fonttools brotli
    python3 tools/subset_fonts.py

The source fonts come from github.com/google/fonts (SIL OFL 1.1, no Reserved Font
Names) and are cached in tools/.font-cache/. Output goes to static/fonts/."""
import os, subprocess

from fontTools import subset
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE = os.path.join(ROOT, "tools", ".font-cache")
OUT = os.path.join(ROOT, "static", "fonts")
SRC = "https://raw.githubusercontent.com/google/fonts/main/ofl/"
SOURCES = {
    "NotoSerifSC.ttf": "notoserifsc/NotoSerifSC%5Bwght%5D.ttf",
    "ZCOOLXiaoWei.ttf": "zcoolxiaowei/ZCOOLXiaoWei-Regular.ttf",
    "Cormorant-Italic.ttf": "cormorantgaramond/CormorantGaramond-Italic%5Bwght%5D.ttf",
}
# (source, output, weight to pin on a variable font)
FACES = [
    ("NotoSerifSC.ttf", "noto-serif-sc-500.woff2", 500),
    ("NotoSerifSC.ttf", "noto-serif-sc-700.woff2", 700),
    ("ZCOOLXiaoWei.ttf", "zcool-xiaowei-400.woff2", None),
    ("Cormorant-Italic.ttf", "cormorant-garamond-600-italic.woff2", 600),
]


def fetch(name):
    path = os.path.join(CACHE, name)
    if not os.path.exists(path):
        os.makedirs(CACHE, exist_ok=True)
        print("downloading", name)
        subprocess.run(["curl", "-sSfL", "-o", path, SRC + SOURCES[name]], check=True)
    return path


def main():
    text = open(os.path.join(ROOT, "tower-study.html"), encoding="utf-8").read()
    unicodes = sorted({ord(c) for c in text if ord(c) > 0x7E} | set(range(0x20, 0x7F)))
    print(f"{len(unicodes)} characters")
    for src, out, wght in FACES:
        font = TTFont(fetch(src))
        opts = subset.Options()
        opts.flavor = "woff2"
        opts.hinting = False
        opts.name_IDs = [0, 1, 2, 3, 4, 5, 6, 13, 14]
        opts.layout_features = ["*"]
        sub = subset.Subsetter(opts)
        sub.populate(unicodes=unicodes)
        sub.subset(font)
        if wght is not None:
            font = instancer.instantiateVariableFont(font, {"wght": wght})
        font.flavor = "woff2"
        font.save(os.path.join(OUT, out))
        print(f"  {out}: {os.path.getsize(os.path.join(OUT, out)) // 1024} KB")


if __name__ == "__main__":
    main()
