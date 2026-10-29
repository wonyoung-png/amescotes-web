"""Globe: add Shenzhen/Guangzhou offices and Dongguan/Guangzhou/Yiwu factories (ko/en/ja). Re-runnable."""
import json
from pathlib import Path
C = Path(__file__).resolve().parents[1] / 'content'
NEW = [  # (f, coords, label offset, {lang: (name, kind, text)})
 ('office', [114.06, 22.54], [12, 16], {'ko': ('Shenzhen', '오피스', '선전 오피스.'), 'en': ('Shenzhen', 'Office', 'Our Shenzhen office.'), 'ja': ('Shenzhen', 'オフィス', '深センオフィス。')}),
 ('office', [113.20, 23.18], [-124, -10], {'ko': ('Guangzhou Office', '오피스', '광저우 오피스.'), 'en': ('Guangzhou Office', 'Office', 'Our Guangzhou office.'), 'ja': ('Guangzhou Office', 'オフィス', '広州オフィス。')}),
 ('make', [113.75, 23.02], [14, -4], {'ko': ('Dongguan', '공장', '동관 생산 공장.'), 'en': ('Dongguan', 'Factory', 'Production in Dongguan.'), 'ja': ('Dongguan', '工場', '東莞の生産工場。')}),
 ('make', [113.32, 23.08], [-132, 12], {'ko': ('Guangzhou Factory', '공장', '광저우 생산 공장.'), 'en': ('Guangzhou Factory', 'Factory', 'Production in Guangzhou.'), 'ja': ('Guangzhou Factory', '工場', '広州の生産工場。')}),
 ('make', [120.07, 29.31], [12, 4], {'ko': ('Yiwu', '공장', '이우 생산 공장.'), 'en': ('Yiwu', 'Factory', 'Production in Yiwu.'), 'ja': ('Yiwu', '工場', '義烏の生産工場。')}),
]
TEXT = {'ko': '서울에서 개발하고, 칭다오·동관·광저우·이우에서 생산하고, 일본과 동남아로 보냅니다. 지구본을 끌어서 돌려 보세요.',
        'en': 'Developed in Seoul, produced in Qingdao, Dongguan, Guangzhou and Yiwu, shipped to Japan and Southeast Asia. Drag the globe to spin it.',
        'ja': 'ソウルで開発し、青島・東莞・広州・義烏で生産し、日本と東南アジアへ届けます。地球儀をドラッグして回してみてください。'}
s = json.loads((C / 'site.json').read_text(encoding='utf-8'))
base = len(s['places']) if len(s['places']) <= 5 else 5
s['places'] = s['places'][:base] + [{'f': f, 'c': c, 'o': o} for f, c, o, _ in NEW]
(C / 'site.json').write_text(json.dumps(s, ensure_ascii=False, indent=2), encoding='utf-8')
for l in ('ko', 'en', 'ja'):
    p = C / f'{l}.json'; j = json.loads(p.read_text(encoding='utf-8'))
    j['global']['places'] = j['global']['places'][:base] + [{'n': t[l][0], 'k': t[l][1], 'p': t[l][2]} for *_, t in NEW]
    j['global']['text'] = TEXT[l]
    p.write_text(json.dumps(j, ensure_ascii=False, indent=2), encoding='utf-8')
print(len(s['places']))
