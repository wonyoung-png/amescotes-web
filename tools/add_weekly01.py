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
def irow(k, v):
    # 12 months (2025-10..2026-09) + last 30 days; season s[0..11] = Jan..Dec share; now≈Oct, compare to Jul (t[9]) and Oct 2025 (t[0])
    t, n, s = v['t'], v['now'], v['s']; ser = t + [n]; hi = max(ser); lo = min(ser)
    xy = [(round(i * 120 / 12, 1), round(28 - (x - lo) / ((hi - lo) or 1) * 26, 1)) for i, x in enumerate(ser)]
    a = n / t[9] - 1; e = s[9] / s[6] - 1; x = (1 + a) / (1 + e) - 1
    vs, cls = ('계절보다 강함', 'up') if x > .15 else (('계절보다 약함', 'dn') if x < -.15 else ('계절 수준', ''))
    return {'k': k, 'cat': v['cat'], 'pts': ' '.join(f'{p},{q}' for p, q in xy), 'end': xy[-1], 'idx': round(n / hi * 100),
            'chg': f'{a:+.0%}', 'vs': f'{vs} ({x:+.0%})', 'cls': cls, 'yoy': f'{n / t[0] - 1:+.0%}', 'x': x}
IROWS = sorted((irow(k, v) for k, v in bk.items()), key=lambda r: -r['x'])
for r in IROWS: r.pop('x')
B = [
 {'t': 'p', 'v': ['이번 주부터 매주 월요일, 가방·슈즈·SLG와 소재, 업계 소식을 다섯 가지로 정리합니다. 항목마다 근거의 등급을 적었습니다. A는 공식 원문, B는 전문 매체, C는 일반 매체, D는 검색량 같은 수요 숫자입니다. C만 있는 내용은 "더 확인할 신호"로만 씁니다.']},
 {'t': 'note', 'v': '맨 위 사진: Celine · Prada · Chanel SS27 (Vogue Singapore, Hypebae). 이미지 저작권은 각 브랜드와 매체에 있습니다.'},

 {'t': 'h', 'n': '01', 'eyebrow': 'BAGS · 근거 A·B', 'title': '낮고 긴 숄더, 둥근 볼링백', 'sub': 'SS27 RUNWAY'},
 {'t': 'img', 'v': [im('bag')], 'cap': 'Ferragamo SS27 런웨이, 가로로 늘린 Hug · 사진: Ferragamo'},
 {'t': 'p', 'v': ['SS27 쇼에서 가장 자주 반복된 형태는 가로로 길고 높이가 낮은 숄더백, 손잡이가 두 개인 소프트 볼링백, 몸에 붙는 유연한 대형 토트입니다. 페라가모는 대표 가방 Hug의 비례를 가로로 다시 잡았다고 공식 설명했고, 전문 리서치 기관도 볼링백을 이번 시즌 주요 형태로 꼽았습니다.']},
 {'t': 'check', 'v': ['가로형은 입구 유효폭과 지퍼 길이부터 확인합니다. 길고 얕을수록 물건을 꺼내기 어렵습니다.', '볼링백은 물건을 넣었을 때 바닥이 처지는지, 손잡이 두 개가 서로 부딪히는지 샘플로 봅니다.']},
 {'t': 'links', 'v': [['A', 'Ferragamo SS27 쇼 공식 설명', 'https://www.ferragamo.com/shop/CoreMediaContentDisplay?catalogId=37054&externalSeoSegment=stories-ss27-show&langId=-1&storeId=31150&urlRequestType=Base'], ['B', 'Future Snoops SS27 가방 공개 요약', 'https://www.futuresnoops.com/en/report/bags-seasonal-takeaways-women-accessories-ss-27-runway-key-items'], ['B', 'Vogue Singapore SS27 가방 모음', 'https://vogue.sg/best-bags-spring-summer-2027/']]},

 {'t': 'h', 'n': '02', 'eyebrow': 'SHOES · 근거 C (확인 중)', 'title': '발레리나 플랫 다음은 더비와 브로그(BROGUE)', 'sub': 'SS27 RUNWAY'},
 {'t': 'img', 'v': [im('shoes')], 'cap': 'Ferragamo Tramezza 레이스업 · 사진: Ferragamo'},
 {'t': 'set', 'v': [dict(im(f'shoe{i}'), cap=c) for i, c in zip([1, 2, 3, 7, 5, 6], ['', '', '', '', 'Church''s', ''])]},
 {'t': 'note', 'v': '레퍼런스: 핀터레스트에서 저장이 많은 브로그·더비 구두 사진. 저작권은 각 게시자에게 있습니다.'},
 {'t': 'p', 'v': ['SS27 런웨이를 정리한 매체들은 브로그(BROGUE)·더비·옥스퍼드 같은 끈 있는 단화가 발레리나 플랫의 자리를 넘보고 있다고 봤습니다. 반대편에서는 장식과 조형미가 강한 힐도 함께 나왔습니다. 아직 일반 매체 정리뿐이라, 다음 주에 공식 룩과 전문 매체로 다시 확인합니다.', '국내에서는 로퍼 검색이 더비슈즈보다 많고, 발레리나플랫이라는 말은 거의 쓰이지 않습니다. 더비슈즈의 가을 상승은 아래 06에서 계절 수준으로 나왔습니다.']},
 {'t': 'check', 'v': ['끈 있는 단화는 라스트(발틀)에서 앞코 볼륨과 등 높이가 인상을 좌우합니다. 기존 로퍼 라스트를 그대로 쓰면 둔해 보이기 쉽습니다.']},
 {'t': 'links', 'v': [['C', 'Who What Wear · Spring 2027 shoe trends', 'https://www.whowhatwear.com/fashion/runway/spring-summer-shoe-trends-2027'], ['C', 'Hypebae · SS27 runway footwear', 'https://hypebae.com/2026/9/best-footwear-fashion-week-ss27-spring-summer-2027-runways-sandy-liang-ugg-knwls-prada-mm6-maison-margiela-onitsuka-tiger-saint-laurent-chanel-info']]},

 {'t': 'h', 'n': '03', 'eyebrow': 'SLG · 근거 A·C', 'title': '작은 지갑이 브랜드의 입구가 된다', 'sub': 'SMALL LEATHER GOODS'},
 {'t': 'img', 'v': [im('slg')], 'cap': 'Bottega Veneta 인트레치아토 지갑 · 사진: Bottega Veneta'},
 {'t': 'set', 'v': [dict(im(f'w{i}'), cap=c) for i, c in enumerate(['Chanel', 'Miu Miu', 'Loewe', 'Loewe', 'Prada', 'Chanel'], 1)]},
 {'t': 'note', 'v': '레퍼런스: 핀터레스트에서 저장이 많은 명품 카드지갑·지갑 사진. 저작권은 각 브랜드와 게시자에게 있습니다.'},
 {'t': 'p', 'v': ['가방 가격이 해마다 오르면서 카드지갑 같은 작은 가죽 소품이 브랜드를 처음 사는 입구가 되고 있다는 분석이 나옵니다. 루이 비통도 이번 가을·겨울 남성 소품을 콤팩트 지갑, 카드홀더, 미니 백 중심으로 꾸렸습니다. 국내에서 카드지갑은 한 달 약 6만 회 검색되는 큰 단어지만, 관심도는 작년 같은 때보다 낮습니다(아래 06).']},
 {'t': 'check', 'v': ['카드 슬롯은 가죽을 얇게 깎는 피할 두께가 완성도를 정합니다. 겹치는 부분이 두꺼우면 카드가 빡빡해집니다.', '작은 제품일수록 엣지 마감이 눈에 잘 띕니다. 엣지 코트 횟수를 샘플 단계에서 정해 둡니다.']},
 {'t': 'links', 'v': [['A', 'Louis Vuitton · New in small leather goods', 'https://uk.louisvuitton.com/eng-gb/men/wallets-and-small-leather-goods/new-in-small-leather-goods/_/N-t1ko2dbb'], ['C', 'Vogue Hong Kong · SLG 기사', 'https://voguehk.com/?p=185799']]},

 {'t': 'h', 'n': '04', 'eyebrow': 'MATERIAL · 근거 A', 'title': '가죽 자체가 표현이 되는 시즌', 'sub': 'LINEAPELLE · PREMIÈRE VISION'},
 {'t': 'img', 'v': [im('leather')], 'cap': 'SS27 가죽 디코딩 · 사진: Première Vision'},
 {'t': 'p', 'v': ['프르미에르 비전은 SS27 가죽 전망에서 소재 자체가 하나의 표현이 된다고 정리했습니다. 누벅·미세 샌딩·스웨이드처럼 손에 닿는 표면이 중심입니다. 리네아펠레는 지난 2월 밀라노에서 2027년 여름을 미리 보여주는 샘플 2,000점 이상을 전시했고, 9월 행사는 다음 가을·겨울 소재를 중심으로 열렸습니다.', '국내 검색량에서도 스웨이드가방이 숄더백·토트백보다 많았습니다. 계절 영향이 있어 몇 주 더 지켜봅니다.']},
 {'t': 'check', 'v': ['스웨이드·누벅은 마찰 이염과 물 자국을 먼저 테스트합니다. 보강재를 붙인 뒤 촉감이 달라지지 않는지도 확인합니다.']},
 {'t': 'links', 'v': [['A', 'Première Vision · SS27 Leather', 'https://www.premierevision.com/articles/5ae7cea9-a205-f111-8333-000d3a2973d4/spring-summer-27-decodings-leather'], ['B', 'La Conceria · Lineapelle 9월 행사 미리보기', 'https://www.laconceria.it/en/fairs/lineapelle-gears-up-what-to-expect-from-23-to-25-september']]},

 {'t': 'h', 'n': '05', 'eyebrow': 'RULES · 근거 B (확정 전)', 'title': 'EU 산림파괴방지 규정, 가죽은 빠질까', 'sub': 'EUDR · 12월 30일 시행'},
 {'t': 'p', 'v': ['유럽연합의 산림파괴방지 규정(EUDR)은 대부분의 기업에 2026년 12월 30일부터 적용됩니다. 소가죽도 원래 대상 품목이었는데, 유럽연합 집행위원회가 올해 5월 가죽을 대상에서 빼는 안을 내놓았습니다. 아직 확정 전이며, 유럽 의회와 회원국이 막을 수 있습니다.', '유럽에 가죽 제품을 수출하는 브랜드라면 원피가 어느 나라, 어느 농장에서 왔는지 추적 자료를 미리 준비해 두는 편이 안전합니다.']},
 {'t': 'links', 'v': [['B', 'Fern · 집행위원회, 가죽 제외 제안', 'https://www.fern.org/publications-insight/article/commission-rules-out-re-opening-eudr-but-drops-leather-from-goods-covered-by-it/'], ['B', 'World Footwear · EUDR 품목 범위 개정', 'https://www.worldfootwear.com/news/eu-revises-product-scope-simplifies-deforestation-rules-ahead-of-2026-rollout-/11454.html']]},

 {'t': 'h', 'n': '06', 'eyebrow': 'MARKET PULSE · 근거 D', 'title': '관심도: 볼링백만 계절을 앞질렀다', 'sub': 'NAVER 관심도 · 지금 수요 확인용'},
 {'t': 'p', 'v': ['관심도는 최근 12개월 중 가장 많이 검색된 달을 100으로 놓고, 최근 30일이 어디쯤인지 보여주는 숫자입니다. 검색은 이미 생긴 수요라서 기획의 출발점이 아니라 "지금 실제로 찾는지" 확인하는 용도로 씁니다. 기획은 소재 박람회(12~18개월 전)와 런웨이(6~9개월 전)에서 먼저 잡습니다.', '계절 대비는 같은 기간 해마다 반복되는 계절 변화를 빼고 남은 힘입니다. 가을에 더비슈즈 검색이 늘어난 건 매년 있는 일이라 계절 수준입니다. 볼링백은 계절 예상보다 52% 더 올랐고 12개월 중 최고치라, 01번 런웨이 신호와 국내 수요가 같은 방향입니다.']},
 {'t': 'interest', 'rows': IROWS, 'cap': '자료: 블랙키위(네이버 검색 데이터), 2026년 10월 29일 조회. 흐름 = 2025년 10월~2026년 9월 월별 + 최근 30일(점). 3개월 변화 = 최근 30일 ÷ 7월. 계절 대비 = 3개월 변화를 해마다 반복되는 7월→10월 변화로 나눈 값. 숄더백·로퍼·호보백·메리제인·스웨이드가방·발레리나플랫은 조회 제한으로 다음 주에 추가합니다.'}, {'t': 'p', 'v': ['다음 주 Weekly Signal 02에서는 슈즈 신호를 공식 룩으로 다시 확인하고, 관심도의 첫 주간 변화를 정리합니다.']},
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
