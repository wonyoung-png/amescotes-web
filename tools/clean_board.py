"""Clean-tone process picks board: two rows (Bags / Shoes), MAIN + alt per step."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
R = Path(__file__).resolve().parents[2] / 'incoming' / 'pins'
BAG = [('01 Pattern', ['clean/09_1', 'clean/09_3']), ('02 Material', ['clean/11_8', 'clean/02_3']),
       ('03 Cutting', ['clean/02_7', 'clean/02_0']), ('04 Sample', ['clean/10_1', 'clean/08_0']),
       ('05 Sewing', ['clean/12_0', 'clean/12_3']), ('06 Production', ['clean/10_6', 'clean/10_5']),
       ('07 QC', ['clean/13_0', 'clean/13_1']), ('08 Packing', ['clean/15_0', 'clean/15_8'])]
SHOE = [('01 Design', ['clean/03_0', 'clean/04_6']), ('02 Pattern', ['clean/01_6', 'clean/01_2']),
        ('03 Cutting', ['clean/02_5', 'clean/02_8']), ('04 Upper', ['clean/03_5', 'clean/03_4']),
        ('05 Assembly', ['clean/06_3', 'clean/06_6']), ('06 Sole', ['clean/06_4', 'clean/06_0']),
        ('07 QC', ['clean/07_7', 'clean/07_5']), ('08 Packing', ['clean/14_0', 'clean/14_7'])]
F = ImageFont.truetype('C:/Windows/Fonts/arialbd.ttf', 22); f = ImageFont.truetype('C:/Windows/Fonts/arial.ttf', 15)
W, H = 230, 300
def block(title, steps):
    S = Image.new('RGB', (len(steps) * (W + 8), 40 + 2 * (H + 8)), (238, 244, 239)); d = ImageDraw.Draw(S)
    d.text((6, 6), title, font=F, fill=(15, 26, 22))
    for c, (lab, ks) in enumerate(steps):
        x = c * (W + 8)
        for r, k in enumerate(ks):
            y = 40 + r * (H + 8)
            im = Image.open(R / f'{k}.jpg').convert('RGB'); im.thumbnail((W, H - 22))
            S.paste(im, (x + (W - im.width) // 2, y))
            d.text((x + 2, y + H - 20), (lab if r == 0 else 'alt') + '  ' + k.split('/')[1], font=f, fill=(31, 74, 61) if r == 0 else (130, 130, 130))
    return S
a, b = block('BAGS', BAG), block('SHOES', SHOE)
S = Image.new('RGB', (max(a.width, b.width), a.height + b.height + 20), (238, 244, 239)); S.paste(a, (0, 0)); S.paste(b, (0, a.height + 20))
S.save(R.parent / 'clean_board.jpg', quality=84); print('ok')

