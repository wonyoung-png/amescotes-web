"""Feedback 10/30: service/footer images, Business range with photos (from the company deck), step 06 wording. Re-runnable."""
import json
from pathlib import Path
from PIL import Image
R = Path(__file__).resolve().parents[1]; C = R / 'content'; FIG = R.parent / 'incoming' / 'figma'; OUT = R / 'assets' / 'img' / 'range'
OUT.mkdir(parents=True, exist_ok=True)
# deck slide 11 "Business range" photos, row by row
PICS = {'product': ['317ba73e', '06e89929', '9afad11b', '629c2e6a', '438ed385'],
        'material': ['3b70c3be', 'b3defde2', '2e7c6687', '09f2cbbb', '9f09e5a3'],
        'market': ['83648bab', '4526e4e2', '29e751be', 'd7ba5c21', 'd191877a']}
for g, hs in PICS.items():
    for i, h in enumerate(hs, 1):
        im = Image.open(next(FIG.glob(f'img_s11_{h}.*'))).convert('RGB')
        w, ht = im.size; s = min(w, ht); im = im.crop(((w - s) // 2, (ht - s) // 2, (w - s) // 2 + s, (ht - s) // 2 + s)).resize((640, 640), Image.LANCZOS)
        im.save(OUT / f'{g}{i}.jpg', quality=84)
RANGE = {
 'ko': [['Product range', ['Bags', 'Belts', 'SLGs', 'Shoes', '키링 · 리빙 등']], ['Material range', ['천연가죽', '스플릿 가죽', '비건 레더', '패브릭', 'PVC 등 특수 소재']], ['Market range', ['Luxury', 'Premium', 'Contemporary', 'Wholesale', '아티스트 굿즈 등']]],
 'en': [['Product range', ['Bags', 'Belts', 'SLGs', 'Shoes', 'Keyrings, living & more']], ['Material range', ['Genuine leather', 'Split leather', 'Vegan leather', 'Fabric', 'PVC & special materials']], ['Market range', ['Luxury', 'Premium', 'Contemporary', 'Wholesale', 'Artist merchandise & more']]],
 'ja': [['Product range', ['Bags', 'Belts', 'SLGs', 'Shoes', 'キーリング・リビングなど']], ['Material range', ['本革', 'スプリットレザー', 'ヴィーガンレザー', 'ファブリック', 'PVCなどの特殊素材']], ['Market range', ['Luxury', 'Premium', 'Contemporary', 'Wholesale', 'アーティストグッズなど']]],
}
STEP6 = {'ko': ('한국 또는 칭다오 라인에서 양산합니다.', '한국 또는 중국 생산 라인에서 양산합니다.'),
         'en': ('Volume production on our lines in Korea or Qingdao.', 'Volume production on our lines in Korea or China.'),
         'ja': ('韓国または青島のラインで量産します。', '韓国または中国の生産ラインで量産します。')}
for lang in RANGE:
    p = C / f'{lang}.json'; j = json.loads(p.read_text(encoding='utf-8'))
    j['range']['groups'] = [{'label': lab, 'key': k, 'items': items} for (lab, items), k in zip(RANGE[lang], PICS)]
    for s in j['make']['b']:
        if s[2] == STEP6[lang][0]: s[2] = STEP6[lang][1]
    assert any(s[2] == STEP6[lang][1] for s in j['make']['b']), lang
    p.write_text(json.dumps(j, ensure_ascii=False, indent=2), encoding='utf-8')
s = json.loads((C / 'site.json').read_text(encoding='utf-8'))
for ch, img in zip(s['chapters'], ['cut/oem.png', 'cut/odm.png', 'cut/process.png']): ch['image'] = img
s['footer_image'] = 'cut/footer.png'
(C / 'site.json').write_text(json.dumps(s, ensure_ascii=False, indent=2), encoding='utf-8')
print('ok')
