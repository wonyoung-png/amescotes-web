"""Journal Issue 00 (SS27 bag trends, from AMESCOTES_Journal_Issue00_Concept_20261029.pdf) as the newest journal post. Re-runnable."""
import json
from pathlib import Path
from PIL import Image
ROOT = Path(__file__).resolve().parents[1]; C = ROOT / 'content'; IMG = 'journal/issue-00'
SLUG = 'issue-00'
def im(n):
    w, h = Image.open(ROOT / 'assets' / IMG / f'{n}.jpg').size
    return {'src': f'{IMG}/{n}.jpg', 'w': w, 'h': h}
CH = [  # (img, eyebrow, title, sub, paragraphs, caption, source)
 ('02', 'LOEWE / OFFICIAL', 'Flamenco Flap', 'SPRING SUMMER 2027 PRECOLLECTION',
  ['로에베는 SS27 프리컬렉션에서 부드러운 가죽의 플라멩코 플랩을 선보였다. 시그니처 매듭은 서로 맞물리는 금속 장식으로 재해석했다.', '몸판과 플랩에 자연스러운 주름이 잡히고, 전면의 금속 장식이 중심을 잡는다.'],
  'LOEWE SS27 Precollection', '자료: LOEWE SS27 Precollection. 사진: Talia Chetrit / LOEWE. 확인: 2026.10.29.'),
 ('03', 'S/S 27 / RUNWAY', 'Double-Strap Dominance', 'SPRING SUMMER 2027',
  ['디올, 질 샌더, 칼마이어, 토리버치는 SS27에서 두 개의 핸들을 갖춘 가방을 선보였다.', '디올의 작은 백과 질 샌더의 큰 백처럼, 같은 두 핸들 구성 안에서도 크기와 입구 형태는 다양하다.'],
  '좌상 Dior · 우상 Jil Sander · 좌하 Kallmeyer · 우하 Tory Burch', '자료: Who What Wear(2026.10.22). 사진: Launchmetrics Spotlight / Dior · Jil Sander · Tory Burch; Kallmeyer.'),
 ('04', 'S/S 27 / RUNWAY', 'The Downtown Weave', 'SPRING SUMMER 2027',
  ['위빙 백이 트렌치코트와 데님에 더해졌다. 휴양지뿐 아니라 도시의 일상복에도 함께 등장했다.', '촘촘한 짜임의 숄더백부터 격자 무늬의 플랩 백, 성글게 엮은 버킷 백까지 형태도 다양하다.'],
  '좌상 Altuzarra · 우상 Bottega Veneta · 좌하 Burberry · 우하 Hermès', '자료: Who What Wear(2026.10.22). 사진: Launchmetrics Spotlight / Altuzarra · Bottega Veneta · Burberry · Hermès.'),
 ('05', 'S/S 27 / RUNWAY', 'Serpentine Shades', 'SPRING SUMMER 2027',
  ['펜디는 레드, 미우미우는 퍼플, 프라다는 그린으로 스네이크스킨 패턴을 선보였다.', '같은 패턴도 컬러에 따라 인상이 달라진다. 뉴트럴 톤과 선명한 유색 패턴이 한 시즌에 함께 보인다.'],
  '좌상 Dior · 우상 Fendi · 좌하 Miu Miu · 우하 Prada', '자료: Who What Wear(2026.10.22). 사진: Launchmetrics Spotlight / Dior · Fendi · Miu Miu · Prada.'),
 ('06', 'S/S 27 / RUNWAY', 'On Body', 'SPRING SUMMER 2027',
  ['허리에 매는 가방, 목걸이형 파우치, 손목에 거는 가방이 SS27에 함께 등장했다.', '작은 수납공간을 몸 가까이 착용하거나, 스트랩을 손목에 감는 방식으로 활용했다.'],
  '좌상 Bottega Veneta · 우상 Hermès · 좌하 Miu Miu · 우하 Michael Kors', '자료: Who What Wear(2026.10.22). 사진: Launchmetrics Spotlight / Bottega Veneta · Hermès · Miu Miu · Michael Kors.'),
 ('07', 'S/S 27 / RUNWAY', 'Hand Carry', 'SPRING SUMMER 2027',
  ['보테가 베네타, 셀린느, 로에베, 샤넬은 손에 쥐는 가방을 선보였다. 봉투와 서류 케이스를 닮은 얇은 형태가 눈에 띈다.', '사진에서는 얇은 봉투형 클러치와 핸들을 접어 손으로 감싸 쥔 가방을 함께 볼 수 있다.'],
  '좌상 Bottega Veneta · 우상 Celine · 좌하 LOEWE · 우하 Chanel', '자료: Who What Wear(2026.10.22). 사진: Launchmetrics Spotlight / Bottega Veneta · LOEWE · Chanel; Celine.'),
 ('08', 'ELLE / S/S 27 REFERENCE', 'Satin Is Coming for Your Handbag Collection', 'LOULOU DE SAISON / SPRING SUMMER 2027',
  ['ELLE는 SS27의 새틴 가방이 클러치에서 숄더와 톱핸들 형태로 확장됐다고 짚었다. 셀린느는 토트백도 선보였다.', 'Loulou de Saison은 애플 그린 새틴 백을 블랙 의상에 매치했다. 부드러운 주름과 광택이 드러난다.'],
  'Loulou de Saison', '자료: ELLE, Meg Donohue(2026.10.20). 사진: Courtesy of Loulou de Saison. 컬렉션: SS27.'),
]
blocks = [{'t': 'p', 'v': ['AMESCOTES Journal의 첫 호입니다. SS27 컬렉션에서 눈에 띈 가방의 흐름 일곱 가지와, 다음 두 시즌의 예측 컬러를 한 권에 모았습니다.']}]
for n, (img, eb, title, sub, ps, cap, src) in enumerate(CH, 2):
    blocks += [{'t': 'h', 'n': f'{n:02d}', 'eyebrow': eb, 'title': title, 'sub': sub},
               {'t': 'img', 'v': [im(img)], 'cap': cap}, {'t': 'p', 'v': ps}, {'t': 'note', 'v': src}]
blocks += [{'t': 'h', 'n': '09', 'eyebrow': 'WGSN × COLORO / FORECAST', 'title': 'Key Colors', 'sub': 'S/S 27 · A/W 27/28'},
           {'t': 'colors', 'groups': [
             {'label': 'S/S 27', 'items': [['Luminous Blue', '125-28-38', '#193F8F'], ['Energy Orange', '018-57-34', '#EE6643'], ['Pop Pink', '151-73-22', '#EAA6C5'], ['Meadowland Green', '050-61-19', '#A39E58'], ['Clay', '014-60-13', '#C38B84']]},
             {'label': 'A/W 27/28', 'items': [['Luminous Blue', '125-28-38', '#193F8F'], ['Russet', '013-30-24', '#7C3330'], ['Peaceful Lilac', '135-78-11', '#C9C5DF'], ['Maize', '036-65-23', '#CFA15B'], ['Deep Green', '082-30-14', '#1C5247']]}]},
           {'t': 'p', 'v': ['WGSN과 Coloro가 제안한 시즌별 예측 컬러다. 핸드백 판매 순위나 27FW 런웨이 발표를 뜻하지 않는다.']},
           {'t': 'note', 'v': '자료·컬러: Coloro Key Colors. 확인: 2026.10.29. 화면의 색은 스와치 이미지에서 뽑은 값이라 실제 컬러와 다를 수 있다.'}]
posts = json.loads((C / 'journal_posts.json').read_text(encoding='utf-8'))
posts[SLUG] = {'url': '', 'blocks': blocks}
(C / 'journal_posts.json').write_text(json.dumps(posts, ensure_ascii=False, indent=2), encoding='utf-8')
s = json.loads((C / 'site.json').read_text(encoding='utf-8'))
s['journal'] = [j for j in s['journal'] if j['slug'] != SLUG]
s['journal'].insert(0, {'url': '', 'image': f'{IMG}/cover.jpg', 'date': '2026.10', 'slug': SLUG})
(C / 'site.json').write_text(json.dumps(s, ensure_ascii=False, indent=2), encoding='utf-8')
HEAD = {'ko': {'tag': 'Issue 00', 'title': 'SS27 가방, 일곱 가지 흐름'}, 'en': {'tag': 'Issue 00', 'title': 'Seven bag stories from SS27'}, 'ja': {'tag': 'Issue 00', 'title': 'SS27 バッグ、7つの流れ'}}
for l, h in HEAD.items():
    p = C / f'{l}.json'; j = json.loads(p.read_text(encoding='utf-8'))
    j['journal']['posts'] = [x for x in j['journal']['posts'] if x.get('tag') != 'Issue 00']
    j['journal']['posts'].insert(0, h)
    p.write_text(json.dumps(j, ensure_ascii=False, indent=2), encoding='utf-8')
print(len(blocks))
