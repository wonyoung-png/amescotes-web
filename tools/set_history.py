"""Full history list (imweb 'OUR HISTORY' + company profile), one entry per year, ko/en/ja. Re-runnable."""
import json
from pathlib import Path
C = Path(__file__).resolve().parents[1] / 'content'
YEARS = ['2017', '2020', '2021', '2022', '2023', '2024', '2025', '2026']
H = {
 'ko': [['아메스코테스 개인사업자 설립'], ['아메스코테스 법인 설립'],
        ['기업부설연구소 설립', '품질경영시스템 ISO 9001 · ISO 14001 인증', "여성 잡화 브랜드 '아뜰리에 드 루멘' 런칭"],
        ["'아뜰리에 드 루멘' 오프라인 스토어 런칭"], ['기술평가 우수기업 선정'], ['중국 해외 홀세일 계약 체결', '일본 해외 홀세일 계약 체결'],
        ['일본 법인 자회사 설립', '중국 공장 설립', '독립 사옥 매입 · 확장 이전'], ['인도네시아 유통사 계약 체결', '이노비즈(INNOBIZ) 인증']],
 'en': [['Founded as a sole proprietorship'], ['Incorporated as AMESCOTES, Inc.'],
        ['Corporate R&amp;D lab established', 'ISO 9001 · ISO 14001 certified', "Launched women’s accessories brand ‘Atelier de LUMEN’"],
        ["‘Atelier de LUMEN’ flagship store opened"], ['Selected as a technology-rated excellent company'], ['Wholesale contract signed in China', 'Wholesale contract signed in Japan'],
        ['Japanese subsidiary founded', 'Factory established in China', 'Purchased and moved into our own HQ building'], ['Distribution contract signed in Indonesia', 'INNOBIZ certified']],
 'ja': [['個人事業として創業'], ['株式会社アメスコテス設立'],
        ['企業附設研究所 設立', '品質マネジメント ISO 9001・ISO 14001 認証', 'レディース雑貨ブランド「Atelier de LUMEN」ローンチ'],
        ['「Atelier de LUMEN」直営店オープン'], ['技術評価優秀企業に選定'], ['中国でホールセール契約締結', '日本でホールセール契約締結'],
        ['日本法人(子会社)設立', '中国工場 設立', '自社ビル取得・移転'], ['インドネシア販売代理店と契約締結', 'INNOBIZ 認証']],
}
s = json.loads((C / 'site.json').read_text(encoding='utf-8')); s['history_years'] = YEARS
(C / 'site.json').write_text(json.dumps(s, ensure_ascii=False, indent=2), encoding='utf-8')
for l, rows in H.items():
    p = C / f'{l}.json'; j = json.loads(p.read_text(encoding='utf-8'))
    j['history']['items'] = ['<br>'.join(r) for r in rows]
    p.write_text(json.dumps(j, ensure_ascii=False, indent=2), encoding='utf-8')
print('ok')
