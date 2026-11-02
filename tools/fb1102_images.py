"""Feedback 11/2: replace product grid tiles pf04-06 (row 1, items 4-6 on PC) with the uploaded photos.
Same uniform square as fb1030_images.py / cutout_products.py; BiRefNet keeps thin straps."""
import shutil
from pathlib import Path
from PIL import Image
from rembg import new_session, remove
R = Path(__file__).resolve().parents[2]; SRC = R / 'incoming' / 'fb1102'; CUT = R / 'incoming' / 'cutouts'; A = R / 'web' / 'assets'
UP = Path(r'C:\Users\이원영~1\AppData\Local\Temp\claude\C--Users-----AMES\7bff7085-9466-4468-a921-83fdf8107b0e\scratchpad\artifact-files\4a548447-5593-4162-b847-8c739e36d49b')
GRID = {'pf04': 'cd7b41235f4302ac64287966a5f2fea3', 'pf05': 'e5b77795cb1fcfcb7ad580a3f8c9c559', 'pf06': '3ba02a9a8d690fb3afc619bc1d1c3d16'}
SRC.mkdir(parents=True, exist_ok=True)
ses = new_session('birefnet-general')
S, AREA = 1000, 0.34  # same as cutout_products.py
for name, h in GRID.items():
    src = SRC / f'{h}.jpg'
    if not src.exists(): shutil.copy(UP / f'{h}.jpg', src)
    c = CUT / f'fb1102_{name}.png'
    if not c.exists(): remove(Image.open(src).convert('RGB'), session=ses).save(c)
    im = Image.open(c); im = im.crop(im.getchannel('A').point(lambda a: 255 if a > 20 else 0).getbbox())
    solid = sum(1 for a in im.getchannel('A').get_flattened_data() if a > 128)
    k = min((AREA * S * S / max(solid, 1)) ** 0.5, S / max(im.size)); im = im.resize((round(im.width * k), round(im.height * k)), Image.LANCZOS)
    bg = Image.new('RGBA', (S, S), (0, 0, 0, 0)); bg.paste(im, ((S - im.width) // 2, (S - im.height) // 2), im)
    bg.resize((800, 800), Image.LANCZOS).save(A / 'img' / 'deck' / f'{name}.webp', quality=88, method=6)
    print(name, im.size)
