"""'#label' + URL lines -> download to outdir/<row>_<n>.jpg and one row per label: python group_sheet.py list.txt outdir sheet.jpg"""
import sys, urllib.request
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
groups = []
for l in Path(sys.argv[1]).read_text(encoding='utf-8').splitlines():
    l = l.strip()
    if l.startswith('#'): groups.append((l[1:], []))
    elif l: groups[-1][1].append(l)
out = Path(sys.argv[2]); out.mkdir(parents=True, exist_ok=True)
F = ImageFont.truetype('C:/Windows/Fonts/arial.ttf', 18); B = ImageFont.truetype('C:/Windows/Fonts/arialbd.ttf', 20)
W, H, L = 200, 270, 230
S = Image.new('RGB', (L + 10 * W, len(groups) * H), 'white'); d = ImageDraw.Draw(S)
for r, (lab, us) in enumerate(groups):
    y = r * H; d.multiline_text((8, y + 100), lab.replace(' ', '\n', 2), font=B, fill=(0, 0, 0))
    for n, u in enumerate(us[:10]):
        p = out / f'{r:02d}_{n}.jpg'
        try:
            if not p.exists():
                p.write_bytes(urllib.request.urlopen(urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'}), timeout=20).read())
            im = Image.open(p).convert('RGB'); im.thumbnail((W - 6, H - 28))
        except Exception as e:
            print('fail', r, n, e); continue
        x = L + n * W; S.paste(im, (x, y)); d.text((x + 3, y + H - 24), f'{r}-{n}', font=F, fill=(200, 0, 0))
S.save(sys.argv[3], quality=78); print(len(groups))
