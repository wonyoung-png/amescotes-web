"""Larger previews of chosen gallery items: python tools/zoom_items.py 13 18 62 -> check/zoom.jpg"""
import json, sys
from pathlib import Path
from PIL import Image
R = Path(__file__).resolve().parent.parent
g = json.loads((R / 'content/gallery.json').read_text(encoding='utf-8'))
ims = [Image.open(R / f'assets/gallery/{g[int(i)]["id"]}.jpg' if g[int(i)]['type'] == 'photo' else R / f'assets/gallery/{g[int(i)]["id"]}_s.jpg').convert('RGB') for i in sys.argv[1:]]
for im in ims: im.thumbnail((700, 700))
s = Image.new('RGB', (sum(i.width for i in ims) + 10 * len(ims), max(i.height for i in ims)), 'white'); x = 0
for im in ims: s.paste(im, (x, 0)); x += im.width + 10
s.save(R / 'check/zoom.jpg', quality=85)
