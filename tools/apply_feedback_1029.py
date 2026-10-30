"""Feedback board 10/29: China MOQ 150, sample 2 weeks~, map Guangzhou names + Qingdao office. Re-runnable."""
import json
from pathlib import Path
C = Path(__file__).resolve().parents[1] / 'content'
def edit(name, fn):
    p = C / name; s = p.read_text(encoding='utf-8'); s2 = fn(s); p.write_text(s2, encoding='utf-8'); return s != s2
R = {
 'ko': [('중국 200개부터', '중국 150개부터'), ('2컬러 200개부터 볼륨 생산', '150개부터 볼륨 생산'), ('중국 (200개~)', '중국 (150개~)'),
        ('중국 생산은 스타일당 2컬러 200개부터', '중국 생산은 150개부터'), ('약 2주입니다.', '약 2주부터 걸립니다.')],
 'en': [('200 in China', '150 in China'), ('Volume production from 200 pieces in 2 colours.', 'Volume production from 150 pieces.'), ('China (200 pcs~)', 'China (150 pcs~)'),
        ('from 200 pcs per style in 2 colours for production in China', 'from 150 pcs for production in China'), ('About two weeks.', 'From about two weeks.')],
 'ja': [('中国200個から', '中国150個から'), ('2色200個から量産。', '150個から量産。'), ('中国(200個~)', '中国(150個~)'),
        ('中国生産は1スタイル2色200個から', '中国生産は150個から'), ('約2週間です。', '約2週間からです。')],
}
COMMON = [('"200 pcs~ / 2 col."', '"150 pcs~"'), ('"≈ 2 weeks"', '"≈ 2 weeks~"'), ('"Guangzhou Office"', '"Guangzhou"'), ('"Guangzhou Factory"', '"Guangzhou"')]
QD = {'ko': {'n': 'Qingdao', 'k': '오피스', 'p': '칭다오 오피스.'}, 'en': {'n': 'Qingdao', 'k': 'Office', 'p': 'Our Qingdao office.'}, 'ja': {'n': 'Qingdao', 'k': 'オフィス', 'p': '青島オフィス。'}}
s = json.loads((C / 'site.json').read_text(encoding='utf-8'))
add = not any(p['f'] == 'office' and p['c'] == [120.38, 36.07] for p in s['places'])
if add:
    s['places'].append({'f': 'office', 'c': [120.38, 36.07], 'o': [12, -14]})
    (C / 'site.json').write_text(json.dumps(s, ensure_ascii=False, indent=2), encoding='utf-8')
for lang, pairs in R.items():
    def fn(t, pairs=pairs):
        for a, b in pairs + COMMON:
            t = t.replace(a, b)
        return t
    edit(f'{lang}.json', fn)
    if add:
        p = C / f'{lang}.json'; j = json.loads(p.read_text(encoding='utf-8')); j['global']['places'].append(QD[lang])
        p.write_text(json.dumps(j, ensure_ascii=False, indent=2), encoding='utf-8')
# self-check: no old values left
for lang in R:
    t = (C / f'{lang}.json').read_text(encoding='utf-8')
    for bad in ['200 pcs~ / 2 col.', 'Guangzhou Office', 'Guangzhou Factory', '"≈ 2 weeks"', '200개부터', '200 pieces', '200個']:
        assert bad not in t, (lang, bad)
print('ok, qingdao office added' if add else 'ok')
