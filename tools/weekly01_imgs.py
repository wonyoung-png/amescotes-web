"""Weekly Signal 01: pick luxury/contemporary photos from incoming/wk01 -> assets/journal/weekly-01 (+ 4-panel cover)."""
from pathlib import Path
from PIL import Image
ROOT = Path(__file__).resolve().parents[1]; SRC = ROOT.parent / 'incoming' / 'wk01'; OUT = ROOT / 'assets' / 'journal' / 'weekly-01'
PICK = {'bag': '00_4', 'shoes': '01_3', 'slg': '02_4', 'leather': '02_1'}  # Prada, Marni, Bottega Veneta, Première Vision
for n, s in PICK.items():
    im = Image.open(SRC / f'{s}.jpg').convert('RGB'); im.thumbnail((1400, 1400)); im.save(OUT / f'{n}.jpg', quality=88)
H = 1100; panels = [Image.open(SRC / f'{s}.jpg').convert('RGB') for s in ['00_6', '00_4', '01_0', '00_7']]  # Celine, Prada, Chanel shoe, Chanel bag
W = H * 4 // 3 * 4 // 4; pw = 2200 // 4
cv = Image.new('RGB', (pw * 4, H), '#E2ECE5')
for i, p in enumerate(panels):
    r = max(pw / p.width, H / p.height); p = p.resize((round(p.width * r), round(p.height * r)))
    l, t = (p.width - pw) // 2, (p.height - H) // 3
    cv.paste(p.crop((l, t, l + pw, t + H)), (i * pw, 0))
cv.save(OUT / 'cover.jpg', quality=86); print('ok')
