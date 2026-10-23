"""Contact sheets of every image the site uses (gallery + work photos) for visual review -> check/zh_N.jpg"""
import json, os
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

R = Path(__file__).resolve().parent.parent
F = ImageFont.truetype('C:/Windows/Fonts/arial.ttf', 16)
g = json.loads((R / 'content/gallery.json').read_text(encoding='utf-8'))
items = [(f'G{i}', R / f'assets/gallery/{x["id"]}_s.jpg') for i, x in enumerate(g)]
items += [(f'W:{f}', R / 'assets/img/work' / f) for f in sorted(os.listdir(R / 'assets/img/work'))]
T, C = 260, 8
for part in range(0, len(items), 48):
    ch = items[part:part + 48]
    s = Image.new('RGB', (C * T, ((len(ch) + C - 1) // C) * (T + 20)), 'white'); d = ImageDraw.Draw(s)
    for k, (n, p) in enumerate(ch):
        im = Image.open(p).convert('RGB'); im.thumbnail((T - 4, T - 4))
        x, y = (k % C) * T, (k // C) * (T + 20); s.paste(im, (x, y)); d.text((x + 2, y + T), n, font=F, fill=(200, 0, 0))
    s.save(R / f'check/zh_{part // 48}.jpg', quality=82)
print(len(items))
