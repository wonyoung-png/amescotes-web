"""FAQ 10/30: replace the no-tech-pack answer with the CEO's wording, add re-make from existing product and material swap. Re-runnable."""
import json
from pathlib import Path
C = Path(__file__).resolve().parents[1] / 'content'
NEW = {
 'ko': [
  ['전문 디자이너가 없어서 구체적인 작업지시서가 없는데, 제작이 가능한가요?', '네, 충분히 가능합니다. 정식 작업지시서가 없더라도 원하시는 실물 샘플(레퍼런스)이나 사진, 간단한 아이디어 스케치만 전달해 주시면 됩니다. 아메스코테스의 전문 인력이 소통을 통해 세부 디테일을 함께 잡아드리니 편하게 문의해 주세요.'],
  ['기존에 다른 공장에서 만들던 제품입니다. 패턴이나 자재 정보가 명확하지 않은데 진행할 수 있나요?', '네, 가능합니다. 기존 제품(실물 샘플)을 보내주시면 이를 바탕으로 패턴을 새롭게 복원(도면화)하고, 기존 자재와 가장 유사한 고품질 자재를 찾아 동일한 느낌으로 구현해 드립니다.'],
  ['가죽으로 된 샘플을 보았는데, 패브릭(천)이나 합성피혁(가죽 대체제)으로 바꿔서 만들 수 있나요?', '네, 얼마든지 가능합니다. 소재가 바뀌면 가방의 형태를 잡는 내부 보강재와 패턴을 새롭게 설계하여 원래의 디자인 핏을 살려냅니다. 반대로 패브릭이나 합성피혁 제품을 고급 가죽 제품으로 전환하여 제작하는 것도 가능합니다.']],
 'en': [
  ["We don't have a professional designer or a detailed tech pack. Can you still make our product?", 'Yes, absolutely. Even without a formal tech pack, a physical sample you like, photos or a simple idea sketch is enough. Our specialists will work out the details with you, so feel free to get in touch.'],
  ['Our product was made at another factory, and the pattern and material details are unclear. Can you take it on?', 'Yes. Send us the existing product (a physical sample) and we will rebuild the pattern from it as new technical drawings, then source high-quality materials closest to the originals to recreate the same look and feel.'],
  ['We saw a leather sample. Can it be made in fabric or synthetic leather instead?', 'Yes, of course. When the material changes, we redesign the internal reinforcement that holds the shape, along with the pattern, so the original design fit is kept. It also works the other way: fabric or synthetic leather products can be converted into premium leather.']],
 'ja': [
  ['専門のデザイナーがおらず、詳しい仕様書がありません。それでも製作できますか？', 'はい、十分に可能です。正式な仕様書がなくても、ご希望の実物サンプル（リファレンス）や写真、簡単なアイデアスケッチをお送りいただければ大丈夫です。アメスコテスの専門スタッフがやり取りしながら細部を一緒に詰めていきますので、お気軽にお問い合わせください。'],
  ['以前は別の工場で作っていた製品です。パターンや資材の情報がはっきりしませんが、進められますか？', 'はい、可能です。既存の製品（実物サンプル）をお送りいただければ、それをもとにパターンを新たに復元（図面化）し、既存の資材に最も近い高品質な資材を探して同じ風合いで再現します。'],
  ['レザーのサンプルを見ましたが、ファブリックや合成皮革に変えて作れますか？', 'はい、もちろん可能です。素材が変わる場合は、形を保つ内部の芯材とパターンを新たに設計し、元のデザインのフィット感を活かします。反対に、ファブリックや合成皮革の製品を上質なレザー製品に切り替えて製作することもできます。']],
}
OLD_Q = {'ko': '디자인이나 작업지시서가 없어도 의뢰할 수 있나요?', 'en': 'Can I start without a tech pack or finished design?', 'ja': 'デザインや仕様書がなくても依頼できますか？'}
for lang, new in NEW.items():
    p = C / f'{lang}.json'; j = json.loads(p.read_text(encoding='utf-8')); items = j['faq']['items']
    qs = [x[0] for x in items]
    if OLD_Q[lang] in qs:
        i = qs.index(OLD_Q[lang]); items[i] = new[0]
    for q in new[1:]:
        if q[0] not in [x[0] for x in items]:
            items.insert(len(items) - 1, q)  # keep "how do I get started" last
    p.write_text(json.dumps(j, ensure_ascii=False, indent=2), encoding='utf-8')
    print(lang, len(items))
