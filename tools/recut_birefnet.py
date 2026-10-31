"""Re-cut product shots with BiRefNet (keeps thin light straps that isnet drops) and report where it recovers pixels.
Writes incoming/cutouts/bir_<name>.png; prints names whose solid area grew > 3% vs the current isnet cutout."""
import json
from pathlib import Path
from PIL import Image
from rembg import new_session, remove
R = Path(__file__).resolve().parents[2]
D, CUT = R / 'incoming' / 'figma', R / 'incoming' / 'cutouts'
L = json.loads((D / 'layout.json').read_text(encoding='utf-8'))
raw = {p.name.split('_')[2].split('.')[0]: p for p in D.glob('img_*')}
jobs = [(raw[h], f'pf{i:02d}') for i, (*_, h) in enumerate(L['15'], 1)]
jobs += [(D / f'x_{k}{i:02d}.jpg', f'{k}{i:02d}') for k in ('cat', 'mat') for i in range(1, 6)]
jobs += [(p, p.stem) for p in sorted((R / 'incoming' / 'extra').glob('pf*.*'))]
solid = lambda im: sum(1 for a in im.getchannel('A').get_flattened_data() if a > 128)
ses = new_session('birefnet-general')
for src, name in jobs:
    b = CUT / f'bir_{name}.png'
    if not b.exists():
        remove(Image.open(src).convert('RGB'), session=ses).save(b)
    old, new = solid(Image.open(CUT / f'{name}.png')), solid(Image.open(b))
    if new > old * 1.03: print(name, old, new, f'+{(new / old - 1) * 100:.0f}%')
