"""Add company-profile deck content (vision, PPS, categories/materials, network, products) to ko/en/ja.json. Re-runnable."""
import json
from pathlib import Path
C = Path(__file__).resolve().parents[1] / 'content'
V = ['All-in-One', 'Consulting', 'ASQ', 'Trend']
D = {
 'ko': {
  'vision': {'title': 'Vision &amp; mission.',
   'vision': '아메스코테스의 모든 구성원은 “성장을 위해 파트너와 함께”라는 비전을 공유합니다. 파트너와 함께 성장하는 글로벌 잡화 제조의 미래를 만들어갑니다.',
   'mission': '축적된 프로세스 경험과 전문성으로 독보적인 고객가치를 만듭니다. 파트너와 임직원이 함께 성장하고, 그 성장이 산업과 문화의 발전으로 이어지는 선순환을 지향합니다.',
   'values': [['올인원 시스템', '생산의 전 과정을 직접 책임지고 관리하는 통합 프로세스.'], ['맞춤형 컨설팅', '1:1 컨설팅으로 상황과 조건에 맞는 해법을 제안합니다.'],
              ['품질 관리', '자체 기준 ASQ(Amescotes Standard Quality)로 운영하는 품질 관리.'], ['트렌드 선도', '디자인, 기술, 네트워크 전반에서 변화를 이끄는 운영.']]},
  'pps': {'title': 'PPS sampling.', 'intro': '단계마다 확인하고 넘어가는 PPS 샘플 개발 시스템으로 불필요한 샘플 비용과 시간을 줄입니다.',
   'steps': [['CAD 패턴', 'CAD로 패턴을 설계해 수정과 사이즈 전개를 빠르게 합니다.'], ['종이 목업', '종이 패턴으로 사이즈, 비율, 실루엣, 구조를 먼저 확인합니다.'],
             ['가봉 샘플', '실제와 비슷한 소재로 주름·슬라우치 같은 질감과 주요 디테일을 정합니다.'], ['최종 샘플', '실제 소재로 완성도와 마감, 생산 가능성을 최종 확인합니다.']],
   'old': '기존 방식', 'old_steps': ['손 패턴', '1차 샘플', '패턴 수정', '수정 샘플'], 'new': 'PPS',
   'old_note': '수정할 때마다 샘플을 다시 만들어 기간과 비용이 늘어납니다.', 'new_note': '종이와 가봉 단계에서 미리 확정해 최종 샘플을 한 번에 갑니다.'},
  'caps': {'title': 'Categories &amp; capabilities.', 'text': '직접 경험하고 시행착오를 거쳐 노하우를 쌓은 영역만 비즈니스 범위로 정합니다. 품목마다 핵심 공정과 디테일을 직접 설계하고 개발합니다.',
   'cats': ['형태와 구조 설계', '조직 구성과 금속 장식 개발', 'SLG 전반의 디테일 설계', '라스트와 창 개발', '커스텀 굿즈 · 패키지 · 성형 리빙 아이템'],
   'mtitle': 'Materials &amp; techniques.', 'mtext': '소재의 특성과 물성을 이해한 상태에서 가공 방식과 공법까지 함께 설계합니다. 새로운 시도와 협력사와의 공동 개발로 계속 넓혀갑니다.', 'hint': '사진에 마우스를 올리면 공법 컷이 보입니다'},
  'net': {'domestic': '품질을 위해 고집하는 재단 업체부터 한국 생산을 원하는 브랜드의 공정별 전문 업체까지, 국내 협력사와 긴밀한 독자 네트워크를 운영합니다.',
   'global': '2025년 중국 칭다오에 600평 규모 공장을 세웠습니다. 한국·중국과 인도네시아·베트남·캄보디아 생산 라인을 잇고, 일본·미국·유럽 등으로 바로 출고합니다.'},
  'products': {'title': 'Made by AMESCOTES.', 'text': '국내외 브랜드와 함께 만든 제품 가운데 일부입니다.'},
  'hist5': '<br>독립 사옥 매입 · 확장 이전'},
 'en': {
  'vision': {'title': 'Vision &amp; mission.',
   'vision': 'Everyone at Amescotes shares one vision: “Growing together with our partners.” We aim to shape the future of global accessory manufacturing through shared growth.',
   'mission': 'Built on our process experience and expertise, we create distinctive value for clients, so that partners and employees grow together and that growth feeds back into industry and culture.',
   'values': [['All-in-One System', 'One integrated process, managed directly across the entire production flow.'], ['Tailored Consulting', '1:1 consulting for solutions that fit each brief and its conditions.'],
              ['Quality Control', 'Run under our own Amescotes Standard Quality (ASQ).'], ['Trend Leadership', 'Moving design, technology and business culture forward.']]},
  'pps': {'title': 'PPS sampling.', 'intro': 'Our stage-based PPS system checks design intent and structure at every step, cutting unnecessary sampling cost and time.',
   'steps': [['CAD pattern', 'Patterns are engineered in CAD, so revisions and grading move fast.'], ['Paper mock-up', 'Size, proportion, silhouette and structure are checked in paper first.'],
             ['Prototype', 'Made in a similar material to fix texture such as wrinkles and slouch, plus the key details.'], ['Final sample', 'Made in the real material to confirm finish, material fit and production feasibility.']],
   'old': 'Industry standard', 'old_steps': ['Hand pattern', '1st sample', 'Pattern revision', 'Revised sample'], 'new': 'PPS',
   'old_note': 'Every change means another sample, so time and cost keep growing.', 'new_note': 'Decisions are locked in paper and prototype, so the final sample lands in one go.'},
  'caps': {'title': 'Categories &amp; capabilities.', 'text': 'We only call it our range when we have made it ourselves, through trial and error. For each category we design and develop the core processes and details in-house.',
   'cats': ['Form and structural design', 'Belt construction and hardware development', 'Detail design across all SLGs', 'Last and sole development', 'Custom goods, packaging and molded lifestyle items'],
   'mtitle': 'Materials &amp; techniques.', 'mtext': 'We design the processing method around each material’s character and physical properties, and keep extending it through new briefs and joint development with partners.', 'hint': 'Hover a photo to see the technique'},
  'net': {'domestic': 'A close, independent network of Korean partners, from cutting houses we insist on for quality to process specialists for brands that want Korean production.',
   'global': 'In 2025 we opened a 2,000 m² factory in Qingdao, China. It links production lines in Korea, China, Indonesia, Vietnam and Cambodia, with direct shipping to Japan, the US and Europe.'},
  'products': {'title': 'Made by AMESCOTES.', 'text': 'A selection of products we have made with brands in Korea and abroad.'},
  'hist5': '<br>Purchased and moved into our own HQ building'},
 'ja': {
  'vision': {'title': 'Vision &amp; mission.',
   'vision': 'アメスコテスのメンバー全員が「パートナーと共に成長する」というビジョンを共有しています。共に成長しながら、グローバルな雑貨製造の未来をつくります。',
   'mission': '積み重ねたプロセスの経験と専門性で、他にない顧客価値を生み出します。パートナーと社員が共に成長し、その成長が産業と文化の発展へつながる好循環を目指します。',
   'values': [['オールインワン', '生産の全工程を自ら責任を持って管理する統合プロセス。'], ['個別コンサルティング', '1対1のコンサルティングで条件に合った解決策を提案します。'],
              ['品質管理', '自社基準ASQ(Amescotes Standard Quality)による品質管理。'], ['トレンドを先導', 'デザイン、技術、ネットワーク全般で変化をリードします。']]},
  'pps': {'title': 'PPS sampling.', 'intro': '段階ごとに確認して進めるPPSサンプル開発システムで、無駄なサンプル費用と時間を減らします。',
   'steps': [['CADパターン', 'CADでパターンを設計し、修正とサイズ展開を素早く行います。'], ['紙モックアップ', '紙のパターンでサイズ、比率、シルエット、構造を先に確認します。'],
             ['仮縫いサンプル', '近い素材でシワやスラウチなどの質感と主要ディテールを決めます。'], ['最終サンプル', '実際の素材で仕上がりと生産可能性を最終確認します。']],
   'old': '従来の方法', 'old_steps': ['手描きパターン', '1次サンプル', 'パターン修正', '修正サンプル'], 'new': 'PPS',
   'old_note': '修正のたびにサンプルを作り直すため、期間と費用が増えます。', 'new_note': '紙と仮縫いの段階で確定し、最終サンプルを一度で仕上げます。'},
  'caps': {'title': 'Categories &amp; capabilities.', 'text': '実際に手がけ、試行錯誤を経てノウハウを積んだ領域だけを事業範囲としています。品目ごとに核心工程とディテールを自社で設計・開発します。',
   'cats': ['形と構造の設計', '組み立てと金具の開発', 'SLG全般のディテール設計', 'ラストとソールの開発', 'カスタムグッズ・パッケージ・成形リビング'],
   'mtitle': 'Materials &amp; techniques.', 'mtext': '素材の特性と物性を理解したうえで、加工方法と工法まで設計します。新しい挑戦と協力会社との共同開発で広げ続けています。', 'hint': '写真にカーソルを合わせると工法のカットが見られます'},
  'net': {'domestic': '品質のためにこだわる裁断業者から、韓国生産を望むブランドの工程別専門業者まで、国内パートナーとの独自ネットワークを運営しています。',
   'global': '2025年、中国・青島に約2,000㎡の工場を設立しました。韓国・中国とインドネシア・ベトナム・カンボジアの生産ラインをつなぎ、日本・米国・欧州などへ直接出荷します。'},
  'products': {'title': 'Made by AMESCOTES.', 'text': '国内外のブランドと共に作った製品の一部です。'},
  'hist5': '<br>自社ビル取得・移転'},
}
for l, add in D.items():
    p = C / f'{l}.json'; j = json.loads(p.read_text(encoding='utf-8'))
    for k in ('vision', 'pps', 'caps', 'net', 'products'): j[k] = add[k]
    it = j['history']['items']
    if add['hist5'] not in it[5]: it[5] += add['hist5']
    p.write_text(json.dumps(j, ensure_ascii=False, indent=2), encoding='utf-8')
print('ok')

