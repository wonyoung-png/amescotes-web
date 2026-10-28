"""Shoe-process Pinterest picks board: one main + alternates per step, labeled."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
R = Path(__file__).resolve().parents[2] / 'incoming' / 'pins'
P = [('01 Last', ['shoe2/19', 'shoe/13']), ('02 Pattern', ['shoe/17', 'shoe2/26', 'shoe2/24']),
     ('03 Cutting', ['shoe2/07', 'shoe/18', 'shoe2/04']), ('04 Upper', ['shoe2/25']),
     ('05 Lasting', ['shoe2/33', 'shoe/44']), ('06 Sole', ['shoe2/35', 'shoe/30']),
     ('07 Finish', ['shoe/49', 'shoe2/26']), ('08 Workshop', ['shoe2/04', 'shoe2/00'])]
F = ImageFont.truetype('C:/Windows/Fonts/arialbd.ttf', 26); f = ImageFont.truetype('C:/Windows/Fonts/arial.ttf', 18)
W, H = 300, 380
S = Image.new('RGB', (190 + 3 * (W + 10), len(P) * (H + 10)), (238, 244, 239)); d = ImageDraw.Draw(S)
for r, (lab, ks) in enumerate(P):
    y = r * (H + 10); d.text((14, y + H // 2 - 14), lab, font=F, fill=(15, 26, 22))
    for c, k in enumerate(ks):
        im = Image.open(R / f'{k}.jpg').convert('RGB'); im.thumbnail((W, H - 26))
        x = 190 + c * (W + 10); S.paste(im, (x, y))
        d.text((x + 4, y + H - 24), ('MAIN  ' if c == 0 else 'alt  ') + k, font=f, fill=(31, 74, 61) if c == 0 else (120, 120, 120))
S.save(R.parent / 'shoe_board.jpg', quality=82); print('ok')
