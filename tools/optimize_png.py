#!/usr/bin/env python3
"""Shrink the raw screenshots written by tools/screenshots.kc (uncompressed PNG) for use in README.md.
   python3 tools/optimize_png.py docs/screenshots/raw docs/screenshots      (needs Pillow)"""
import sys, os
from PIL import Image

src, dst = sys.argv[1], sys.argv[2]
os.makedirs(dst, exist_ok=True)
for name in sorted(os.listdir(src)):
    if not name.endswith(".png"):
        continue
    im = Image.open(os.path.join(src, name)).convert("RGB")
    q = im.quantize(colors=256, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.FLOYDSTEINBERG)
    out = os.path.join(dst, name.lower())
    q.save(out, optimize=True)
    print(f"{name:28s} {os.path.getsize(os.path.join(src, name))//1024:5d} KB -> {os.path.getsize(out)//1024:4d} KB")
