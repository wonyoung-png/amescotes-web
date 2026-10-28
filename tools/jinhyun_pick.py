"""Export picked jinhyun shots (by contact-sheet index) as JPG: python jinhyun_pick.py OUTDIR name=idx ..."""
import sys
from pathlib import Path
from PIL import Image, ImageOps
from pillow_heif import register_heif_opener
register_heif_opener()
R = Path(__file__).resolve().parents[2] / 'incoming'
idx = dict(l.split('\t') for l in (R / 'jinhyun_index.txt').read_text(encoding='utf-8').splitlines())
out = Path(sys.argv[1]); out.mkdir(parents=True, exist_ok=True)
for a in sys.argv[2:]:
    name, i = a.split('=')
    im = ImageOps.exif_transpose(Image.open(R / idx[i])).convert('RGB'); im.thumbnail((1400, 1400))
    im.save(out / f'{name}.jpg', quality=82, optimize=True, progressive=True)
print('ok')
