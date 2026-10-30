"""PPS section v2: lead with the two strengths (CAD pattern, paper mock-up) + a plain comparison table. Re-runnable."""
import json
from pathlib import Path
C = Path(__file__).resolve().parents[1] / 'content'
V = {
 'ko': {
  'claim': '손 패턴 대신 CAD, 샘플 전에 종이 목업. 최종 샘플을 한 번에 맞춥니다.',
  'why': [
   ['01', 'CAD 패턴', '손으로 그리는 대신 CAD로 설계합니다.', ['수정과 사이즈 전개가 빠릅니다', '치수가 정확해 좌우·사이즈별 오차가 적습니다', '패턴을 파일로 보관해 수정·재생산 때 그대로 씁니다']],
   ['02', '종이 목업', '샘플을 만들기 전에 종이로 실물 크기를 먼저 만듭니다.', ['사이즈감과 비율을 손에 들고 확인합니다', '가죽을 자르기 전에 고쳐 샘플 재제작을 줄입니다', '3일이면 첫 형태를 볼 수 있습니다']]],
  'th': ['', '기존 방식', 'AMESCOTES PPS'],
  'rows': [['패턴', '손 패턴', 'CAD 패턴'], ['수정 · 사이즈 전개', '다시 그림', '파일에서 바로 수정'], ['사이즈 확인', '1차 샘플이 나온 뒤', '종이 목업에서 먼저 (3일~)'], ['수정할 때', '샘플을 다시 제작 (2주~)', '목업 · 가봉 단계에서 수정'], ['샘플까지 기간 (예시)', '약 5주 이상', '약 3주 반~']],
  'steps_label': '진행 단계'},
 'en': {
  'claim': 'CAD instead of hand patterns, a paper mock-up before any sample. The final sample lands in one go.',
  'why': [
   ['01', 'CAD pattern', 'Patterns are engineered in CAD, not drawn by hand.', ['Revisions and grading move fast', 'Precise measurements keep left-right and size-to-size errors low', 'Patterns are kept as files and reused for revisions and reorders']],
   ['02', 'Paper mock-up', 'Before any sample, we build the bag at full size in paper.', ['You check size and proportion in your hands', 'Fixes happen before leather is cut, so fewer samples are remade', 'The first form is ready in about three days']]],
  'th': ['', 'Industry standard', 'AMESCOTES PPS'],
  'rows': [['Pattern', 'Hand pattern', 'CAD pattern'], ['Revision & grading', 'Redrawn by hand', 'Edited directly in the file'], ['Size check', 'After the 1st sample', 'First, in a paper mock-up (3 days~)'], ['When changes are needed', 'A new sample is made (2 weeks~)', 'Fixed at the mock-up and prototype stage'], ['Time to final sample (example)', '5+ weeks', 'About 3.5 weeks~']],
  'steps_label': 'Steps'},
 'ja': {
  'claim': '手描きパターンではなくCAD、サンプルの前に紙モックアップ。最終サンプルを一度で仕上げます。',
  'why': [
   ['01', 'CADパターン', '手描きではなくCADで設計します。', ['修正とサイズ展開が速い', '寸法が正確で、左右・サイズ間の誤差が少ない', 'パターンをデータで保管し、修正・再生産にそのまま使えます']],
   ['02', '紙モックアップ', 'サンプルを作る前に、紙で実物大の形を作ります。', ['サイズ感と比率を手に取って確認できます', '革を裁断する前に直すので、サンプルの作り直しが減ります', '約3日で最初の形を確認できます']]],
  'th': ['', '従来の方法', 'AMESCOTES PPS'],
  'rows': [['パターン', '手描き', 'CADパターン'], ['修正・サイズ展開', '描き直し', 'データ上ですぐ修正'], ['サイズ確認', '1次サンプルの後', '紙モックアップで先に（3日〜）'], ['修正が必要なとき', 'サンプルを作り直し（2週間〜）', 'モックアップ・仮縫い段階で修正'], ['最終サンプルまで（例）', '約5週間以上', '約3週間半〜']],
  'steps_label': '進行ステップ'},
}
for lang, v in V.items():
    p = C / f'{lang}.json'; j = json.loads(p.read_text(encoding='utf-8')); j['pps'].update(v)
    p.write_text(json.dumps(j, ensure_ascii=False, indent=2), encoding='utf-8')
print('ok')
