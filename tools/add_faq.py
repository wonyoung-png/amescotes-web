"""Home FAQ (ko/en/ja) from facts already on the site. Re-runnable."""
import json
from pathlib import Path
C = Path(__file__).resolve().parents[1] / 'content'
FAQ = {
 'ko': {'title': 'FAQ.', 'items': [
  ['최소 주문 수량(MOQ)은 얼마인가요?', '한국 생산은 50개부터, 중국 생산은 스타일당 2컬러 200개부터 가능합니다.'],
  ['샘플은 얼마나 걸리나요?', '약 2주입니다. 외주 없이 서울 내부 개발팀이 패턴과 샘플을 직접 만듭니다.'],
  ['디자인이나 작업지시서가 없어도 의뢰할 수 있나요?', '네. 아이디어나 참고 이미지만 있어도 됩니다. ODM으로 트렌드·소재를 바탕으로 기획과 디자인까지 제안합니다.'],
  ['어떤 제품을 만드나요?', '가방, 지갑, 벨트, 키링, 슈즈 등 스몰 레더 굿즈 전반과 트레이·코스터 같은 리빙 아이템을 만듭니다. 럭셔리부터 컨템포러리, 홀세일, 아티스트 굿즈까지 대응합니다.'],
  ['어떤 소재를 다루나요?', '천연가죽, 비건 레더, 코튼, 나일론, 폴리에스터, PVC 등 특수 소재를 다룹니다.'],
  ['어디서 생산하나요?', '서울에서 개발하고 한국, 칭다오 자체 공장, 동관·광저우·이우 협력 공장에서 생산합니다. 수량·소재·단가에 맞춰 생산지를 제안합니다.'],
  ['품질은 어떻게 관리하나요?', 'ISO 9001·14001 기준으로 공정을 관리하고, 자체 품질 기준 ASQ로 검수합니다. 납품 이후 A/S까지 책임집니다.'],
  ['샘플 비용과 생산 일정은 어떻게 되나요?', '제품과 수량에 따라 달라 문의 시 견적과 함께 안내합니다. 종이 목업과 가봉 단계에서 미리 확정하는 PPS 방식으로 샘플 횟수와 비용을 줄입니다.'],
  ['해외 브랜드와도 작업하나요?', '네. 일본 법인을 통해 일본 브랜드와 협업하고 있고, 중국·일본·인도네시아 유통사와 거래하고 있습니다.'],
  ['어떻게 문의하면 되나요?', '아래 문의 양식이나 contact@amescotes.co.kr로 만들고 싶은 제품, 예상 수량, 희망 생산지를 보내 주시면 진행 방법을 안내드립니다.']]},
 'en': {'title': 'FAQ.', 'items': [
  ['What is your minimum order quantity (MOQ)?', 'From 50 pcs for production in Korea, and from 200 pcs per style in 2 colours for production in China.'],
  ['How long does sampling take?', 'About two weeks. Our in-house development team in Seoul makes the patterns and samples themselves, with nothing outsourced.'],
  ['Can I start without a tech pack or finished design?', 'Yes. An idea or a few reference images is enough. As an ODM partner we can propose the concept and design based on trend and material research.'],
  ['What products do you make?', 'Bags, wallets, belts, keyrings, shoes and other small leather goods, plus living items such as trays and coasters, for luxury, premium, contemporary, wholesale and artist-merchandise lines.'],
  ['Which materials do you work with?', 'Genuine leather, vegan leather, cotton, nylon, polyester, and special materials such as PVC.'],
  ['Where is production done?', 'We develop in Seoul and produce in Korea, at our own factory in Qingdao, and with partner factories in Dongguan, Guangzhou and Yiwu. We recommend the location that fits your quantity, material and target cost.'],
  ['How do you manage quality?', 'Production is managed to ISO 9001 and ISO 14001, inspected against our own standard, ASQ (Amescotes Standard Quality), and supported with after-sales service after delivery.'],
  ['What do samples cost and what is the production lead time?', 'Both depend on the product and quantity, so we confirm them with your quote. Our PPS process fixes size and structure at the paper and toile stages, which cuts the number of samples and their cost.'],
  ['Do you work with brands outside Korea?', 'Yes. We work with Japanese brands through our Japan subsidiary and supply distributors in China, Japan and Indonesia.'],
  ['How do I get started?', 'Use the contact form below or email contact@amescotes.co.kr with the product you have in mind, the expected quantity and your preferred production location.']]},
 'ja': {'title': 'FAQ.', 'items': [
  ['最小ロット（MOQ）はいくつですか？', '韓国生産は50個から、中国生産は1スタイル2色200個から承ります。'],
  ['サンプルはどのくらいかかりますか？', '約2週間です。外注せず、ソウルの社内開発チームがパターンとサンプルを直接製作します。'],
  ['デザインや仕様書がなくても依頼できますか？', 'はい。アイデアや参考画像だけでも大丈夫です。ODMとしてトレンドと素材をもとに企画・デザインからご提案します。'],
  ['どのような製品を作っていますか？', 'バッグ、財布、ベルト、キーリング、シューズなどのスモールレザーグッズ全般と、トレー・コースターなどのリビングアイテムを製作しています。ラグジュアリーからコンテンポラリー、ホールセール、アーティストグッズまで対応します。'],
  ['どのような素材を扱っていますか？', '本革、ヴィーガンレザー、コットン、ナイロン、ポリエステル、PVCなどの特殊素材を扱っています。'],
  ['どこで生産していますか？', 'ソウルで開発し、韓国、青島の自社工場、東莞・広州・義烏の協力工場で生産します。数量・素材・コストに合わせて生産地をご提案します。'],
  ['品質管理はどのように行っていますか？', 'ISO 9001・14001に基づいて工程を管理し、自社基準ASQで検品します。納品後のアフターサービスまで責任を持ちます。'],
  ['サンプル費用と生産スケジュールは？', '製品と数量によって異なるため、お見積りとあわせてご案内します。紙のモックアップと仮縫いの段階で事前に確定するPPS方式で、サンプルの回数と費用を抑えます。'],
  ['海外ブランドとも取引していますか？', 'はい。日本法人を通じて日本のブランドと協業しており、中国・日本・インドネシアの流通会社とも取引しています。'],
  ['どのように問い合わせればよいですか？', '下のお問い合わせフォーム、またはcontact@amescotes.co.krまで、作りたい製品、予定数量、希望生産地をお送りください。進め方をご案内します。']]},
}
for lang, f in FAQ.items():
    p = C / f'{lang}.json'; j = json.loads(p.read_text(encoding='utf-8')); j['faq'] = f
    p.write_text(json.dumps(j, ensure_ascii=False, indent=2), encoding='utf-8')
print('ok')
