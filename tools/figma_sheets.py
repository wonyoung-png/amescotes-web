"""incoming/figma: name .bin images by real format, then slide contact sheets (s01..s83) in 2 halves."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
D = Path(__file__).resolve().parents[2] / 'incoming' / 'figma'
for b in D.glob('*.bin'):
    h = b.read_bytes()[:12]
    ext = 'png' if h.startswith(b'\x89PNG') else 'jpg' if h.startswith(b'\xff\xd8') else 'gif' if h[:3] == b'GIF' else 'webp' if h[8:12] == b'WEBP' else 'bin'
    b.rename(b.with_suffix('.' + ext))
F = ImageFont.truetype('C:/Windows/Fonts/arialbd.ttf', 22)
ss = sorted(D.glob('s[0-9][0-9].jpg'))
for half, part in enumerate((ss[:42], ss[42:])):
    cols, W, H = 6, 480, 300
    S = Image.new('RGB', (cols * W, ((len(part) + cols - 1) // cols) * H), 'white'); d = ImageDraw.Draw(S)
    for k, p in enumerate(part):
        im = Image.open(p).convert('RGB'); im.thumbnail((W - 8, H - 8)); x, y = (k % cols) * W, (k // cols) * H
        S.paste(im, (x, y)); d.rectangle((x, y, x + 46, y + 28), fill=(200, 0, 0)); d.text((x + 6, y + 2), p.stem[1:], font=F, fill='white')
    S.save(D.parent / f'figma_sheet_{half + 1}.jpg', quality=78)
print(len(ss), len(list(D.glob('img_*'))))
