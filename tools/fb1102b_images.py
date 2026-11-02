"""Feedback 11/2 (2nd batch): row 2 items 5-7 -> pf13-15, row 5 item 3 -> pf35, row 5 items 5-6 -> pf37-38.
Same uniform square as fb1030_images.py / cutout_products.py; BiRefNet keeps thin straps."""
import shutil
from pathlib import Path
from PIL import Image
from rembg import new_session, remove
R = Path(__file__).resolve().parents[2]; SRC = R / 'incoming' / 'fb1102'; CUT = R / 'incoming' / 'cutouts'; A = R / 'web' / 'assets'
UP = Path(r'C:\Users\이원영~1\AppData\Local\Temp\claude\C--Users-----AMES\7bff7085-9466-4468-a921-83fdf8107b0e\scratchpad\artifact-files\4a548447-5593-4162-b847-8c739e36d49b')
GRID = {'pf13': '0e89b130da0145603fe1f3e00abb5ca7', 'pf14': '3d3ad1409cf0fdf2f56b4938650d5691', 'pf15': '4e8f11436d18fd5f286241828a68ff66',
        'pf35': 'e0fcf25ca921e7f760e11d665543f1f7', 'pf37': '79e1a13197006311ec3b6d4cadd73677', 'pf38': 'da42f9710fc81363ee2960f05aa5786a'}
SRC.mkdir(parents=True, exist_ok=True)
ses = new_session('birefnet-general')
S, AREA = 1000, 0.34  # same as cutout_products.py
for name, h in GRID.items():
    src = SRC / f'{h}.jpg'
    if not src.exists(): shutil.copy(UP / f'{h}.jpg', src)
    c = CUT / f'fb1102b_{name}.png'
    if not c.exists(): remove(Image.open(src).convert('RGB'), session=ses).save(c)
    im = Image.open(c); im = im.crop(im.getchannel('A').point(lambda a: 255 if a > 20 else 0).getbbox())
    solid = sum(1 for a in im.getchannel('A').get_flattened_data() if a > 128)
    k = min((AREA * S * S / max(solid, 1)) ** 0.5, S / max(im.size)); im = im.resize((round(im.width * k), round(im.height * k)), Image.LANCZOS)
    bg = Image.new('RGBA', (S, S), (0, 0, 0, 0)); bg.paste(im, ((S - im.width) // 2, (S - im.height) // 2), im)
    bg.resize((800, 800), Image.LANCZOS).save(A / 'img' / 'deck' / f'{name}.webp', quality=88, method=6)
    print(name, im.size)
