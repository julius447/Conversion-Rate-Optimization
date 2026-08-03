#!/usr/bin/env python3
"""Slice full-page screenshots into readable tiles for visual analysis.
Output: data/screenshots/tiles/<slug>--<vp>--NN.png + tiles-index.json"""
import json, os
from PIL import Image

BASE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "screenshots")
TILES = os.path.join(BASE, "tiles")
os.makedirs(TILES, exist_ok=True)
TILE_H = {"mobile": 1500, "desktop": 1300}  # device px per tile
index = {}
for f in sorted(os.listdir(BASE)):
    if not f.endswith(".png") or "--" not in f:
        continue
    slug_vp = f[:-4]
    vp = "mobile" if slug_vp.endswith("mobile") else "desktop"
    im = Image.open(os.path.join(BASE, f))
    w, h = im.size
    th = TILE_H[vp]
    n = 0
    for y in range(0, h, th):
        tile = im.crop((0, y, w, min(y + th, h)))
        if tile.size[1] < 120:
            continue
        n += 1
        # downscale desktop tiles a bit to keep files light but readable
        if vp == "desktop" and w > 1800:
            tile = tile.resize((1440, int(tile.size[1] * 1440 / w)))
        tile.save(os.path.join(TILES, f"{slug_vp}--{n:02d}.png"), optimize=True)
    index[slug_vp] = {"tiles": n, "full_height_px": h, "width_px": w}
json.dump(index, open(os.path.join(BASE, "tiles-index.json"), "w"), indent=1)
print(f"{sum(v['tiles'] for v in index.values())} tiles from {len(index)} screenshots")
for k, v in index.items():
    print(f"  {k}: {v['tiles']} tiles (h={v['full_height_px']}px)")
