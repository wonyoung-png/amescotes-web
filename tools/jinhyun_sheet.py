"""Contact sheet of incoming/jinhyun (HEIC/JPG) with index numbers, to pick shoe-process shots."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageOps
from pillow_heif import register_heif_opener
register_heif_opener()
R = Path(__file__).resolve().parents[2] / 'incoming'
fs = sorted(p for p in (R / 'jinhyun').rglob('*') if p.suffix.lower() in ('.heic', '.jpg'))
F = ImageFont.truetype('C:/Windows/Fonts/arial.ttf', 20)
cols, W, H = 12, 220, 290
S = Image.new('RGB', (cols * W, ((len(fs) + cols - 1) // cols) * H), 'white'); d = ImageDraw.Draw(S)
for i, p in enumerate(fs):
    im = ImageOps.exif_transpose(Image.open(p)).convert('RGB'); im.thumbnail((W - 6, H - 30))
    x, y = (i % cols) * W, (i // cols) * H
    S.paste(im, (x, y)); d.text((x + 4, y + H - 26), str(i), font=F, fill=(200, 0, 0))
S.save(R / 'jinhyun_sheet.jpg', quality=80)
(R / 'jinhyun_index.txt').write_text('\n'.join(f'{i}\t{p.relative_to(R)}' for i, p in enumerate(fs)), encoding='utf-8')
print(len(fs))
