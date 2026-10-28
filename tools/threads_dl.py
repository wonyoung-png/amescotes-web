"""Download Threads image URLs (incoming/threads_urls.txt) and make a contact sheet."""
import urllib.request
from pathlib import Path
from PIL import Image
R = Path(__file__).resolve().parents[2] / 'incoming'
D = R / 'threads'; D.mkdir(exist_ok=True)
urls = [u for u in (R / 'threads_urls.txt').read_text().split() if u]
ims = []
for i, u in enumerate(urls):
    p = D / f't{i:02d}.jpg'
    if not p.exists():
        p.write_bytes(urllib.request.urlopen(urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'}), timeout=20).read())
    im = Image.open(p).convert('RGB'); im.thumbnail((360, 480)); ims.append(im)
cols = 5; rows = (len(ims) + cols - 1) // cols
S = Image.new('RGB', (370 * cols, 490 * rows), 'white')
for k, im in enumerate(ims): S.paste(im, ((k % cols) * 370, (k // cols) * 490))
S.save(R / 'threads_sheet.jpg', quality=82); print(len(ims))
