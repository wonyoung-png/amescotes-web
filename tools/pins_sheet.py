"""Download pins.json images (incoming/pins/<step>/NN.jpg) and make one contact sheet per step."""
import json, urllib.request, io, os
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
R = Path(__file__).resolve().parents[2] / 'incoming'
pins = json.loads((R / 'pins.json').read_text(encoding='utf-8'))
F = ImageFont.truetype('C:/Windows/Fonts/arial.ttf', 18)
rows = []
for step, items in pins.items():
    d = R / 'pins' / step; d.mkdir(parents=True, exist_ok=True); ims = []
    for n, it in enumerate(items):
        p = d / f'{n:02d}.jpg'
        if not p.exists():
            try:
                req = urllib.request.Request(it['src'], headers={'User-Agent': 'Mozilla/5.0'})
                p.write_bytes(urllib.request.urlopen(req, timeout=20).read())
            except Exception as e:
                print('fail', step, n, e); continue
        im = Image.open(p).convert('RGB'); im.thumbnail((200, 260)); ims.append((n, im))
    rows.append((step, ims))
W = 200 * 16 + 140
s = Image.new('RGB', (W, 290 * len(rows)), 'white'); dr = ImageDraw.Draw(s)
for r, (step, ims) in enumerate(rows):
    y = r * 290; dr.text((6, y + 120), step, font=F, fill=(0, 0, 0))
    for n, im in ims:
        x = 140 + n * 200; s.paste(im, (x, y)); dr.text((x + 4, y + 264), str(n), font=F, fill=(200, 0, 0))
s.save(R / 'pins_sheet.jpg', quality=78)
print('ok')
