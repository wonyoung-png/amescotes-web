"""Background-remove product shots and re-place them on one uniform transparent square (same margin, centered).
Products pf01-36 from the deck originals; category/material heroes cat01-05, mat01-05 from the slide exports."""
import json
from pathlib import Path
from PIL import Image
from rembg import new_session, remove
R = Path(__file__).resolve().parents[2]
D, OUT, CUT = R / 'incoming' / 'figma', R / 'web' / 'assets' / 'img' / 'deck', R / 'incoming' / 'cutouts'
CUT.mkdir(exist_ok=True)
L = json.loads((D / 'layout.json').read_text(encoding='utf-8'))
raw = {p.name.split('_')[2].split('.')[0]: p for p in D.glob('img_*')}
jobs = [(raw[h], f'pf{i:02d}') for i, (*_, h) in enumerate(L['15'], 1)]
jobs += [(D / f'x_{k}{i:02d}.jpg', f'{k}{i:02d}') for k in ('cat', 'mat') for i in range(1, 6)]
jobs += [(p, p.stem) for p in sorted((R / 'incoming' / 'extra').glob('pf*.*'))]  # client product pages added by hand
S, FILL = 1000, 0.74  # canvas px, share of the canvas the product's longer side takes
ses = new_session('isnet-general-use')
for src, name in jobs:
    cut = CUT / f'{name}.png'
    if not cut.exists():
        remove(Image.open(src).convert('RGB') if Image.open(src).mode != 'RGBA' else Image.open(src), session=ses, post_process_mask=True).save(cut)
    im = Image.open(cut); im = im.crop(im.getchannel('A').point(lambda a: 255 if a > 20 else 0).getbbox())
    k = S * FILL / max(im.size); im = im.resize((max(1, round(im.width * k)), max(1, round(im.height * k))), Image.LANCZOS)
    bg = Image.new('RGBA', (S, S), (0, 0, 0, 0)); bg.paste(im, ((S - im.width) // 2, (S - im.height) // 2), im)
    bg.resize((800, 800), Image.LANCZOS).save(OUT / f'{name}.webp', quality=88, method=6)
print(len(jobs))
