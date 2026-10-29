"""Naver DataLab search trend (monthly, relative 0-100) for keyword groups -> incoming/research/datalab_<date>.json.
Keys: ~/.claude/naver/datalab_keys.json. Usage: python datalab_trend.py 2025-10-01 2026-10-28"""
import json, sys, urllib.request
from pathlib import Path
k = json.loads((Path.home() / '.claude/naver/datalab_keys.json').read_text(encoding='utf-8-sig'))
cid = k.get('client_id') or k.get('id') or list(k.values())[0]; sec = k.get('client_secret') or k.get('secret') or list(k.values())[1]
GROUPS = {  # DataLab allows 5 groups per call; values are relative within one call
 'bags': [('볼링백', ['볼링백']), ('위빙백', ['위빙백', '라탄백']), ('호보백', ['호보백']), ('토트백', ['토트백']), ('클러치', ['클러치백'])],
 'shoes': [('메리제인', ['메리제인', '메리제인슈즈']), ('로퍼', ['로퍼']), ('발레리나플랫', ['발레리나플랫', '플랫슈즈']), ('더비슈즈', ['더비슈즈']), ('뮬', ['뮬'])],
 'slg': [('카드지갑', ['카드지갑']), ('반지갑', ['반지갑']), ('키링', ['키링', '백참']), ('파우치', ['파우치']), ('스트랩', ['폰스트랩'])],
}
start, end = sys.argv[1], sys.argv[2]
out = {}
for name, gs in GROUPS.items():
    body = json.dumps({'startDate': start, 'endDate': end, 'timeUnit': 'month',
                       'keywordGroups': [{'groupName': g, 'keywords': kw} for g, kw in gs]}).encode()
    req = urllib.request.Request('https://openapi.naver.com/v1/datalab/search', data=body, method='POST',
                                 headers={'X-Naver-Client-Id': cid, 'X-Naver-Client-Secret': sec, 'Content-Type': 'application/json'})
    out[name] = json.loads(urllib.request.urlopen(req, timeout=20).read())
p = Path(__file__).resolve().parents[2] / 'incoming' / 'research'; p.mkdir(parents=True, exist_ok=True)
f = p / f'datalab_{end}.json'; f.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding='utf-8')
for name, r in out.items():
    print('==', name)
    for g in r['results']:
        d = g['data']; first, last = d[0]['ratio'], d[-1]['ratio']; peak = max(d, key=lambda x: x['ratio'])
        yoy = next((x['ratio'] for x in d if x['period'].startswith(end[:2] + str(int(end[2:4]) - 1) + end[4:7])), None)
        print(f"{g['title']}: {d[0]['period'][:7]} {first:.1f} -> {d[-1]['period'][:7]} {last:.1f} | peak {peak['period'][:7]} {peak['ratio']:.1f}")
