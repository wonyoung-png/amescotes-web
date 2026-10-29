"""Journal: Weekly Signal 01 (2026-10, week 5) — bags/shoes/SLG/material/industry/demand. Photos: brand runway/product images, credited. Re-runnable."""
import json
from pathlib import Path
from PIL import Image
ROOT = Path(__file__).resolve().parents[1]; C = ROOT / 'content'; IMG = 'journal/weekly-01'; SLUG = 'weekly-signal-01'
def im(n):
    w, h = Image.open(ROOT / 'assets' / IMG / f'{n}.jpg').size
    return {'src': f'{IMG}/{n}.jpg', 'w': w, 'h': h}
vol = json.loads(next((ROOT.parent / 'incoming' / 'research').glob('searchad_*.json')).read_text(encoding='utf-8'))
def row(k, label): return [label, k, f"{vol[k]['total']:,}"]
bk = json.loads((ROOT.parent / 'incoming' / 'research' / 'blackkiwi_2026-10-29.json').read_text(encoding='utf-8')); bk.pop('_meta')
FW = ['스웨이드가방', '버건디가방', '볼링백', '빅백', '호보백', '토트백', '롱부츠', '앵클부츠', '첼시부츠', '더비슈즈', '가죽장갑', '카드지갑']
def pct(x): return f'{x:+.0%}'
def irow(k, v):
    # t = 2025-10..2026-09 monthly, now = last 30 days (9/29~10/28): MoM vs 2026-09, YoY vs 2025-10
    t, n = v['t'], v['now']; ser = t + [n]; hi, lo = max(ser), min(ser)
    xy = [(round(i * 120 / 12, 1), round(28 - (x - lo) / ((hi - lo) or 1) * 26, 1)) for i, x in enumerate(ser)]
    m, y = n / t[11] - 1, n / t[0] - 1
    return {'k': k, 'cat': v['cat'], 'pts': ' '.join(f'{p},{q}' for p, q in xy), 'end': xy[-1], 'idx': round(n / hi * 100),
            'mom': pct(m), 'yoy': pct(y), 'mc': 'up' if m > .1 else '', 'yc': 'up' if y > 0 else 'dn', 'm': m}
IROWS = sorted((irow(k, bk[k]) for k in FW), key=lambda r: -r['m'])
for r in IROWS: r.pop('m')
B = [
 {'t': 'p', 'v': ['이번 주부터 매주 월요일, 가방·슈즈·SLG와 소재, 업계 소식을 다섯 가지로 정리합니다.']},

 {'t': 'h', 'n': '01', 'eyebrow': 'BAGS', 'title': '이스트웨스트(EAST‑WEST) 숄더, 둥근 볼링백', 'sub': 'SS27 RUNWAY'},
 {'t': 'img', 'v': [im('bag')], 'cap': 'Ferragamo SS27 런웨이, 가로로 늘린 Hug · 사진: Ferragamo'},
 {'t': 'slide', 'label': '이스트웨스트(EAST‑WEST) 숄더백 레퍼런스', 'v': [im(f'ew{i}') for i in range(1, 9)]},
 {'t': 'slide', 'label': '둥근 볼링백 레퍼런스', 'v': [im(f'bw{i}') for i in range(1, 9)]},
 {'t': 'p', 'v': ['SS27 쇼에서 가장 자주 반복된 형태는 가로로 길고 높이가 낮은 이스트웨스트(EAST‑WEST) 숄더백, 손잡이가 두 개인 소프트 볼링백, 몸에 붙는 유연한 대형 토트입니다. 페라가모는 대표 가방 Hug의 비례를 가로로 다시 잡았다고 공식 설명했고, 전문 리서치 기관도 볼링백을 이번 시즌 주요 형태로 꼽았습니다.']},
 {'t': 'links', 'v': [['', 'Ferragamo SS27 쇼 공식 설명', 'https://www.ferragamo.com/shop/CoreMediaContentDisplay?catalogId=37054&externalSeoSegment=stories-ss27-show&langId=-1&storeId=31150&urlRequestType=Base'], ['', 'Future Snoops SS27 가방 공개 요약', 'https://www.futuresnoops.com/en/report/bags-seasonal-takeaways-women-accessories-ss-27-runway-key-items'], ['', 'Vogue Singapore SS27 가방 모음', 'https://vogue.sg/best-bags-spring-summer-2027/']]},

 {'t': 'h', 'n': '02', 'eyebrow': 'SHOES', 'title': '발레리나 플랫 다음은 더비와 브로그(BROGUE)', 'sub': 'SS27 RUNWAY'},
 {'t': 'img', 'v': [im('shoes')], 'cap': 'Ferragamo Tramezza 레이스업 · 사진: Ferragamo'},
 {'t': 'slide', 'label': '브로그(BROGUE)·더비 레퍼런스', 'v': [dict(im(f'shoe{i}'), cap=c) for i, c in zip([1, 2, 3, 7, 5, 6], ['', '', '', '', 'Church''s', ''])]},
 {'t': 'p', 'v': ['SS27 런웨이를 정리한 매체들은 브로그(BROGUE)·더비·옥스퍼드 같은 끈 있는 단화가 발레리나 플랫의 자리를 넘보고 있다고 봤습니다. 반대편에서는 장식과 조형미가 강한 힐도 함께 나왔습니다. 아직 일반 매체 정리뿐이라, 다음 주에 공식 룩과 전문 매체로 다시 확인합니다.', '국내에서는 로퍼 검색이 더비슈즈보다 많고, 발레리나플랫이라는 말은 거의 쓰이지 않습니다. 더비슈즈 검색은 지난달보다 37% 늘었지만 작년보다는 6% 낮습니다(아래 06).']},
 {'t': 'links', 'v': [['', 'Who What Wear · Spring 2027 shoe trends', 'https://www.whowhatwear.com/fashion/runway/spring-summer-shoe-trends-2027'], ['', 'Hypebae · SS27 runway footwear', 'https://hypebae.com/2026/9/best-footwear-fashion-week-ss27-spring-summer-2027-runways-sandy-liang-ugg-knwls-prada-mm6-maison-margiela-onitsuka-tiger-saint-laurent-chanel-info']]},

 {'t': 'h', 'n': '03', 'eyebrow': 'SLG', 'title': '작은 지갑이 브랜드의 입구가 된다', 'sub': 'SMALL LEATHER GOODS'},
 {'t': 'img', 'v': [im('slg')], 'cap': 'Bottega Veneta 인트레치아토 지갑 · 사진: Bottega Veneta'},
 {'t': 'slide', 'label': '명품 카드지갑·지갑 레퍼런스', 'v': [dict(im(f'w{i}'), cap=c) for i, c in enumerate(['Chanel', 'Miu Miu', 'Loewe', 'Loewe', 'Prada', 'Chanel'], 1)]},
 {'t': 'p', 'v': ['가방 가격이 해마다 오르면서 카드지갑 같은 작은 가죽 소품이 브랜드를 처음 사는 입구가 되고 있다는 분석이 나옵니다. 루이 비통도 이번 가을·겨울 남성 소품을 콤팩트 지갑, 카드홀더, 미니 백 중심으로 꾸렸습니다. 국내에서 카드지갑은 한 달 약 6만 회 검색되는 큰 단어지만, 작년 같은 때보다 24% 적게 찾습니다(아래 06).']},
 {'t': 'links', 'v': [['', 'Louis Vuitton · New in small leather goods', 'https://uk.louisvuitton.com/eng-gb/men/wallets-and-small-leather-goods/new-in-small-leather-goods/_/N-t1ko2dbb'], ['', 'Vogue Hong Kong · SLG 기사', 'https://voguehk.com/?p=185799']]},

 {'t': 'h', 'n': '04', 'eyebrow': 'MATERIAL', 'title': '가죽 자체가 표현이 되는 시즌', 'sub': 'LINEAPELLE · PREMIÈRE VISION'},
 {'t': 'img', 'v': [im('leather')], 'cap': 'SS27 가죽 디코딩 · 사진: Première Vision'},
 {'t': 'p', 'v': ['프르미에르 비전은 SS27 가죽 전망에서 소재 자체가 하나의 표현이 된다고 정리했습니다. 누벅·미세 샌딩·스웨이드처럼 손에 닿는 표면이 중심입니다. 리네아펠레는 지난 2월 밀라노에서 2027년 여름을 미리 보여주는 샘플 2,000점 이상을 전시했고, 9월 행사는 다음 가을·겨울 소재를 중심으로 열렸습니다.', '국내 검색량에서도 스웨이드가방이 숄더백·토트백보다 많았습니다. 계절 영향이 있어 몇 주 더 지켜봅니다.']},
 {'t': 'links', 'v': [['', 'Première Vision · SS27 Leather', 'https://www.premierevision.com/articles/5ae7cea9-a205-f111-8333-000d3a2973d4/spring-summer-27-decodings-leather'], ['', 'La Conceria · Lineapelle 9월 행사 미리보기', 'https://www.laconceria.it/en/fairs/lineapelle-gears-up-what-to-expect-from-23-to-25-september']]},

 {'t': 'h', 'n': '05', 'eyebrow': 'RULES', 'title': 'EU 산림파괴방지 규정, 가죽은 빠질까', 'sub': 'EUDR · 12월 30일 시행'},
 {'t': 'p', 'v': ['유럽연합의 산림파괴방지 규정(EUDR)은 대부분의 기업에 2026년 12월 30일부터 적용됩니다. 소가죽도 원래 대상 품목이었는데, 유럽연합 집행위원회가 올해 5월 가죽을 대상에서 빼는 안을 내놓았습니다. 아직 확정 전이며, 유럽 의회와 회원국이 막을 수 있습니다.', '유럽에 가죽 제품을 수출하는 브랜드라면 원피가 어느 나라, 어느 농장에서 왔는지 추적 자료를 미리 준비해 두는 편이 안전합니다.']},
 {'t': 'links', 'v': [['', 'Fern · 집행위원회, 가죽 제외 제안', 'https://www.fern.org/publications-insight/article/commission-rules-out-re-opening-eudr-but-drops-leather-from-goods-covered-by-it/'], ['', 'World Footwear · EUDR 품목 범위 개정', 'https://www.worldfootwear.com/news/eu-revises-product-scope-simplifies-deforestation-rules-ahead-of-2026-rollout-/11454.html']]},

 {'t': 'h', 'n': '06', 'eyebrow': 'MARKET PULSE', 'title': '26FW 관심도: 부츠·스웨이드는 오르는 중, 작년을 넘은 건 볼링백·버건디', 'sub': 'NAVER 관심도 · 지난달 대비 · 작년 대비'},
 {'t': 'p', 'v': ['지금 시즌인 26FW 단어만 모았습니다. 관심도는 최근 12개월 중 가장 많이 검색된 달을 100으로 놓고 최근 30일이 어디쯤인지 보여줍니다. 지난달 대비는 9월보다 얼마나 늘었는지, 작년 대비는 작년 10월보다 얼마나 많은지입니다.', '부츠와 스웨이드는 지난달보다 20~60% 늘며 시즌에 들어왔지만, 작년 같은 때보다는 30~66% 낮습니다. 작년보다 많이 찾는 단어는 볼링백(+48%)과 버건디가방(+21%) 두 개뿐입니다. 볼링백은 01번 런웨이 신호와 같은 방향이고, 버건디는 12개월 중 거의 최고치(92)입니다.', '검색은 이미 생긴 수요라서 기획의 출발점이 아니라 지금 실제로 찾는지 확인하는 용도로 씁니다. 광고와 상세 문구는 작년보다 늘어난 단어 중심으로, 줄어든 큰 단어(앵클부츠·스웨이드가방)는 비용 대비 효과를 지켜보는 쪽이 안전합니다.']},
 {'t': 'interest', 'rows': IROWS, 'cap': '자료: 블랙키위(네이버 검색 데이터), 2026년 10월 29일 조회. 흐름 = 2025년 10월~2026년 9월 월별 + 최근 30일(점). 최근 30일은 9월 29일~10월 28일이라 10월 말 상승분이 덜 들어가 작년 10월 전체보다 낮게 나올 수 있습니다. 숄더백은 조회 제한으로 다음 주에 추가합니다.'}, {'t': 'p', 'v': ['다음 주 Weekly Signal 02에서는 슈즈 신호를 공식 룩으로 다시 확인하고, 관심도의 첫 주간 변화를 정리합니다.']},
]
posts = json.loads((C / 'journal_posts.json').read_text(encoding='utf-8'))
posts[SLUG] = {'url': '', 'blocks': B}
(C / 'journal_posts.json').write_text(json.dumps(posts, ensure_ascii=False, indent=2), encoding='utf-8')
s = json.loads((C / 'site.json').read_text(encoding='utf-8'))
s['journal'] = [j for j in s['journal'] if j['slug'] != SLUG]
s['journal'].insert(0, {'url': '', 'image': f'{IMG}/cover.jpg', 'date': '2026.10.29', 'slug': SLUG})
(C / 'site.json').write_text(json.dumps(s, ensure_ascii=False, indent=2), encoding='utf-8')
HEAD = {'ko': {'tag': 'Weekly Signal', 'title': 'Weekly Signal 01 — 가방·슈즈·SLG 이번 주 다섯 가지'},
        'en': {'tag': 'Weekly Signal', 'title': 'Weekly Signal 01 — Five things this week in bags, shoes and SLGs'},
        'ja': {'tag': 'Weekly Signal', 'title': 'Weekly Signal 01 — バッグ・シューズ・SLG 今週の5つ'}}
for l, h in HEAD.items():
    p = C / f'{l}.json'; j = json.loads(p.read_text(encoding='utf-8'))
    j['journal']['posts'] = [x for x in j['journal']['posts'] if x.get('tag') != 'Weekly Signal']
    j['journal']['posts'].insert(0, h)
    p.write_text(json.dumps(j, ensure_ascii=False, indent=2), encoding='utf-8')
print(len(B))
