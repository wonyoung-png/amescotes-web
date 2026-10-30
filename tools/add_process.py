"""Home 'How it's made' section (layout B): copy step photos + ko/en/ja copy. Re-runnable."""
import json, shutil
from pathlib import Path
from PIL import Image
ROOT = Path(__file__).resolve().parents[1]; C = ROOT / 'content'
SRC = ROOT.parent / 'incoming' / 'process' / 'p'; OUT = ROOT / 'assets' / 'img' / 'process'; OUT.mkdir(parents=True, exist_ok=True)
for f in SRC.glob('c[bs]_*.jpg'):
    im = Image.open(f).convert('RGB'); im.thumbnail((1200, 1200)); im.save(OUT / f.name, quality=86)
K = ['Pattern', 'Material', 'Cutting', 'Sample', 'Sewing', 'Production', 'QC', 'Packing']
KS = ['Design', 'Pattern', 'Cutting', 'Upper', 'Assembly', 'Sole', 'QC', 'Packing']
T = {
 'ko': {'title': "How it's made.", 'bags': 'Bags', 'shoes': 'Shoes',
  'b': [['패턴 설계', '디자인과 목표 단가에 맞춰 스타일마다 패턴을 그립니다.'], ['소재 선정', '가죽과 부자재를 국내외 네트워크에서 고릅니다.'], ['재단', '패턴대로 가죽을 자르고 두께를 다듬습니다.'], ['샘플 제작', '내부 샘플실에서 직접 만들고 바로 수정합니다.'], ['봉제', '숙련된 봉제팀이 구조와 마감을 잡습니다.'], ['생산', '한국 또는 칭다오 라인에서 양산합니다.'], ['검수', '자체 기준 ASQ로 하나씩 확인합니다.'], ['포장 · 납품', '꼼꼼히 포장해 국내외로 납품합니다.']],
  's': [['디자인 · 라스트', '라스트와 디자인으로 실루엣과 착화감을 정합니다.'], ['패턴 설계', '라스트에 맞춰 갑피 패턴을 사이즈별로 전개합니다.'], ['재단', '소재를 패턴대로 자르고 부위별로 정리합니다.'], ['갑피 제작', '조각을 봉제하고 보강해 윗부분을 만듭니다.'], ['조립', '갑피를 라스트에 씌워 형태를 잡습니다.'], ['바닥 부착', '아웃솔을 압착해 붙입니다.'], ['검수', '좌우 대칭과 마감을 한 켤레씩 확인합니다.'], ['포장 · 납품', '박스 포장 후 국내외로 납품합니다.']]},
 'en': {'title': "How it's made.", 'bags': 'Bags', 'shoes': 'Shoes',
  'b': [['Pattern making', 'We draft a pattern for every style, matched to the design and the target cost.'], ['Material selection', 'Leather and trims are sourced through our network in Korea and abroad.'], ['Cutting', 'Leather is cut to the pattern and skived to the right thickness.'], ['Sampling', 'Our in-house sample room builds and revises each sample directly.'], ['Sewing', 'An experienced sewing team sets the structure and the finish.'], ['Production', 'Volume production on our lines in Korea or Qingdao.'], ['Quality control', 'Every piece is checked against our own ASQ standard.'], ['Packing & delivery', 'Carefully packed and shipped to Korea and overseas.']],
  's': [['Design & last', 'The last and the design set the silhouette and the fit.'], ['Pattern making', 'Upper patterns are graded size by size to the last.'], ['Cutting', 'Materials are cut to the pattern and sorted by part.'], ['Upper', 'Pieces are stitched and reinforced to build the upper.'], ['Lasting', 'The upper is pulled over the last to take its shape.'], ['Sole', 'The outsole is pressed and bonded on.'], ['Quality control', 'Symmetry and finish are checked pair by pair.'], ['Packing & delivery', 'Boxed and shipped to Korea and overseas.']]},
 'ja': {'title': "How it's made.", 'bags': 'Bags', 'shoes': 'Shoes',
  'b': [['パターン設計', 'デザインと目標コストに合わせて、スタイルごとにパターンを引きます。'], ['素材選定', '革と副資材を国内外のネットワークから選びます。'], ['裁断', 'パターン通りに革を裁断し、厚みを整えます。'], ['サンプル製作', '社内のサンプル室で直接製作し、すぐに修正します。'], ['縫製', '熟練の縫製チームが構造と仕上げを整えます。'], ['生産', '韓国または青島のラインで量産します。'], ['検品', '自社基準ASQで一つずつ確認します。'], ['梱包・納品', '丁寧に梱包し、国内外へ納品します。']],
  's': [['デザイン・ラスト', 'ラストとデザインでシルエットと履き心地を決めます。'], ['パターン設計', 'ラストに合わせてアッパーのパターンをサイズ展開します。'], ['裁断', '素材をパターン通りに裁断し、部位ごとに整理します。'], ['アッパー製作', 'パーツを縫製・補強してアッパーを作ります。'], ['釣り込み', 'アッパーをラストに被せて形を作ります。'], ['底付け', 'アウトソールを圧着して取り付けます。'], ['検品', '左右の対称と仕上げを一足ずつ確認します。'], ['梱包・納品', '箱に梱包し、国内外へ納品します。']]},
}
for lang, t in T.items():
    t['b'] = [[k] + s for k, s in zip(K, t['b'])]; t['s'] = [[k] + s for k, s in zip(KS, t['s'])]
    p = C / f'{lang}.json'; j = json.loads(p.read_text(encoding='utf-8')); j['make'] = t
    p.write_text(json.dumps(j, ensure_ascii=False, indent=2), encoding='utf-8')
print(len(list(OUT.glob('*.jpg'))), 'photos')
