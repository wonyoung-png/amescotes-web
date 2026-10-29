"""Naver SearchAd keywordstool: last-30-day search volume (PC+mobile) for given keywords -> incoming/research/searchad_<date>.json.
Usage: python searchad_volume.py 볼링백 위빙백 ...  (5 per call, batched)"""
import base64, hashlib, hmac, json, sys, time, urllib.parse, urllib.request, datetime
from pathlib import Path
k = json.loads((Path.home() / '.claude/naver/keys.json').read_text(encoding='utf-8-sig'))
def call(kws):
    ts = str(int(time.time() * 1000)); uri = '/keywordstool'
    sig = base64.b64encode(hmac.new(k['secret_key'].encode(), f'{ts}.GET.{uri}'.encode(), hashlib.sha256).digest()).decode()
    q = urllib.parse.urlencode({'hintKeywords': ','.join(w.replace(' ', '') for w in kws), 'showDetail': 1})
    req = urllib.request.Request(f'https://api.searchad.naver.com{uri}?{q}', headers={'X-Timestamp': ts, 'X-API-KEY': k['api_key'], 'X-Customer': str(k['customer_id']), 'X-Signature': sig})
    return json.loads(urllib.request.urlopen(req, timeout=20).read().decode('utf-8'))['keywordList']
num = lambda v: 5 if isinstance(v, str) else v  # "< 10" -> 5
words = sys.argv[1:]; res = {}
for i in range(0, len(words), 5):
    batch = words[i:i + 5]
    for row in call(batch):
        if row['relKeyword'] in [w.replace(' ', '') for w in batch]:
            res[row['relKeyword']] = {'pc': row['monthlyPcQcCnt'], 'mobile': row['monthlyMobileQcCnt'], 'total': num(row['monthlyPcQcCnt']) + num(row['monthlyMobileQcCnt']), 'comp': row['compIdx']}
    time.sleep(0.4)
d = datetime.date.today().isoformat()
p = Path(__file__).resolve().parents[2] / 'incoming' / 'research'; p.mkdir(parents=True, exist_ok=True)
(p / f'searchad_{d}.json').write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding='utf-8')
for w, r in sorted(res.items(), key=lambda x: -x[1]['total']): print(f"{w}\t{r['total']:,}\t{r['comp']}")
