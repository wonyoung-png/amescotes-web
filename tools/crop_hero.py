"""Hero = hanging hides only: crop the original above the Chinese slogan banner."""
import os
from pathlib import Path
from PIL import Image, ImageOps
R = Path(__file__).resolve().parent.parent
src = os.path.join('G:' + os.sep, '공유 드라이브', 'LUMEN', '비주얼', '작업이미지', 'iCloud 사진 (2)', 'iCloud 사진', 'ATLM6854-1.JPG')
im = ImageOps.exif_transpose(Image.open(src)).convert('RGB'); W, H = im.size
im = im.crop((0, 0, W, int(H * 0.56)))
im.thumbnail((2400, 2400)); im.save(R / 'assets/img/work/hero.jpg', quality=82, optimize=True, progressive=True)
im.resize((900, int(900 * im.height / im.width))).save(R / 'check/hero_new.jpg')
print(W, H, '->', im.size)
