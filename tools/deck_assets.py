"""Company-profile deck images (incoming/figma, via layout.json order) -> assets/img/deck/*.jpg."""
import json
from pathlib import Path
from PIL import Image
R = Path(__file__).resolve().parents[2]
D, OUT = R / 'incoming' / 'figma', R / 'web' / 'assets' / 'img' / 'deck'
OUT.mkdir(parents=True, exist_ok=True)
L = json.loads((D / 'layout.json').read_text(encoding='utf-8'))
files = {p.name.split('_')[2].split('.')[0]: p for p in D.glob('img_*')}
plan = {'10': ('pps', 900), '12': ('cat', 900), '13': ('mat', 900), '15': ('pf', 700), '16': ('net', 900), '6': ('vision', 1400)}
for s, (pre, size) in plan.items():
    for i, (*_, h) in enumerate(L[s], 1):
        im = Image.open(files[h])
        if im.mode in ('RGBA', 'LA', 'P'):
            im = im.convert('RGBA'); bg = Image.new('RGB', im.size, 'white'); bg.paste(im, mask=im.split()[-1]); im = bg
        im = im.convert('RGB'); im.thumbnail((size, size))
        name = pre if pre == 'vision' else f'{pre}{i:02d}'
        im.save(OUT / f'{name}.jpg', quality=82, optimize=True, progressive=True)
print(len(list(OUT.glob('*.jpg'))))
