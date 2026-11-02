"""Feedback 11/2 (2nd batch): replace product grid tiles pf28-30 (row 4, items 4-6 on PC) with the uploaded photos.
Same pipeline as fb1102_images.py: BiRefNet cutout, uniform square S=1000 AREA=0.34, 800x800 webp q88."""
import shutil
from pathlib import Path
from PIL import Image
from rembg import new_session, remove
R = Path(__file__).resolve().parents[2]; SRC = R / 'incoming' / 'fb1102'; CUT = R / 'incoming' / 'cutouts'; A = R / 'web' / 'assets'
UP = Path(r'C:\Users\이원영~1\AppData\Local\Temp\claude\C--Users-----AMES\ebd2b1d5-e6eb-4bc7-99ed-fa2035be87ad\scratchpad\artifact-files\4a548447-5593-4162-b847-8c739e36d49b')
GRID = {'pf28': '2059af497cd877031582a67483248c35', 'pf29': '391855b83c7c4fb23abf485adef16304', 'pf30': '3d1c4955768483fb73e6dde0dde36137'}
SRC.mkdir(parents=True, exist_ok=True)
ses = new_session('birefnet-general')
S, AREA = 1000, 0.34
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
