"""Download a URL list into a folder and make a numbered contact sheet: python urls_sheet.py urls.txt outdir sheet.jpg"""
import sys, urllib.request
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
urls = [u for u in Path(sys.argv[1]).read_text().split() if u]
out = Path(sys.argv[2]); out.mkdir(parents=True, exist_ok=True)
F = ImageFont.truetype('C:/Windows/Fonts/arial.ttf', 22)
cols, W, H = 10, 260, 350
S = Image.new('RGB', (cols * W, ((len(urls) + cols - 1) // cols) * H), 'white'); d = ImageDraw.Draw(S)
for i, u in enumerate(urls):
    p = out / f'{i:02d}.jpg'
    try:
        if not p.exists():
            p.write_bytes(urllib.request.urlopen(urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'}), timeout=20).read())
        im = Image.open(p).convert('RGB'); im.thumbnail((W - 6, H - 32))
    except Exception as e:
        print('fail', i, e); continue
    x, y = (i % cols) * W, (i // cols) * H
    S.paste(im, (x, y)); d.text((x + 4, y + H - 28), str(i), font=F, fill=(200, 0, 0))
S.save(sys.argv[3], quality=80); print(len(urls))
