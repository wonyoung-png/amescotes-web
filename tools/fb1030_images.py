"""Feedback 10/30: cut out the uploaded product photos.
Grid tiles pf19-21 use the same uniform square as cutout_products.py; chapter/footer images are trimmed transparent PNGs."""
from pathlib import Path
from PIL import Image
from rembg import new_session, remove
R = Path(__file__).resolve().parents[2]; SRC = R / 'incoming' / 'fb1030'; CUT = R / 'incoming' / 'cutouts'; A = R / 'web' / 'assets'
F = lambda h: next(SRC.glob(h + '.*'))
GRID = {'pf19': 'f4fe3d386c3fa5a7503edcc5337ba658', 'pf20': 'f136860445640df4e2da390bed9ec99b', 'pf21': 'be848a60a1509ccdd62c6d95a25981b0'}
FREE = {'oem': '6853382f3eb7f420a20d20fac46b7a16', 'odm': 'bd2fd131172e4b70ebe8ae983433b220', 'process': '5c1c2e5edac14c0bcf319e32e578d252', 'footer': 'cbb3c8b9fda09a44aec7ee227d263b60'}
ses = new_session('isnet-general-use')
def cut(name, h):
    c = CUT / f'fb1030_{name}.png'
    if not c.exists():
        im = Image.open(F(h)).convert('RGB'); im.thumbnail((2000, 2000))
        remove(im, session=ses, post_process_mask=True).save(c)
    im = Image.open(c); return im.crop(im.getchannel('A').point(lambda a: 255 if a > 20 else 0).getbbox())
S, AREA = 1000, 0.34  # same as cutout_products.py
for name, h in GRID.items():
    im = cut(name, h); solid = sum(1 for a in im.getchannel('A').get_flattened_data() if a > 128)
    k = min((AREA * S * S / max(solid, 1)) ** 0.5, S / max(im.size)); im = im.resize((round(im.width * k), round(im.height * k)), Image.LANCZOS)
    bg = Image.new('RGBA', (S, S), (0, 0, 0, 0)); bg.paste(im, ((S - im.width) // 2, (S - im.height) // 2), im)
    bg.resize((800, 800), Image.LANCZOS).save(A / 'img' / 'deck' / f'{name}.webp', quality=88, method=6)
for name, h in FREE.items():
    im = cut(name, h); im.thumbnail((1200, 1200), Image.LANCZOS); im.save(A / 'cut' / f'{name}.png', optimize=True)
    print(name, im.size)
