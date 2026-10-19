"""One-off: dist/ref/fonts.html — four type systems rendered on the same hero + section."""
import shutil
from pathlib import Path
R = Path(__file__).resolve().parent
OPTS = [
 ('A', 'Seasats형 · 세리프 제목', '얇은 세리프 제목 + 한글 고딕 본문 + 모노 라벨. 레이아웃 원본과 가장 같은 공기, 부드럽고 고급스러움.',
  [('제목', 'Newsreader Light'), ('본문', 'Pretendard'), ('라벨', 'IBM Plex Mono')], 'seasats', 'Seasats — seasonMix · seasonSans · supplyMono'),
 ('B', 'Aesop형 · 얇은 그로테스크', '가늘고 촘촘한 산세리프 제목. 조용하고 정돈된 럭셔리 브랜드 느낌.',
  [('제목', 'Inter Tight Light'), ('본문', 'Pretendard'), ('라벨', 'IBM Plex Mono')], 'aesop', 'Aesop — Suisse Int\'l'),
 ('C', 'Teenage Engineering형 · 테크', '기하학적 산세리프 소문자 제목 + 타자기 모노. 제조·기술 회사다운 위트.',
  [('제목', 'Space Grotesk'), ('본문', 'Pretendard'), ('라벨', 'Space Mono')], 'teenage', 'teenage engineering — te-20 / te-40'),
 ('D', '현재 · 비교용', '지금 사이트 서체. 넓은 산세리프 제목 + IBM Plex KR 본문.',
  [('제목', 'Instrument Sans'), ('본문', 'IBM Plex Sans KR'), ('라벨', 'JetBrains Mono')], 'toteme', 'Toteme — Toteme Sans (참고)'),
]
def opt(k, name, desc, fonts, ref, src):
    title = 'heritage meets<br>innovation.' if k == 'C' else 'Heritage meets<br>innovation.'
    fl = ''.join(f'<li><b>{a}</b>{b}</li>' for a, b in fonts)
    return f'''<section class="opt {k}"><div class="meta"><span class="k">{k}</span><h3>{name}</h3><p>{desc}</p><ul>{fl}</ul><img src="ref_{ref}.jpg" alt=""><span class="src">{src}</span></div>
<div class="demo"><div class="hero"><h1>{title}</h1><p class="sub">잡화 생산의 가장 쉬운 방법,<br>아메스코테스 · since 2017</p><span class="btn lbl">Our services <i>→</i></span></div>
<div class="panel"><span class="lbl" style="color:var(--stone)">03 · Services</span><h2>{"brands that grew<br>alongside us." if k=="C" else "Brands that grew<br>alongside us."}</h2>
<p>소재를 찾고, 패턴을 그리고, 샘플을 만들고, 생산까지. 작업지시서가 없어도 아이디어 하나로 시작할 수 있습니다.</p>
<div><div class="row"><span>MOQ · Korea</span><span>50 pcs~</span></div><div class="row"><span>MOQ · China</span><span>200 pcs / 2 col.</span></div><div class="row"><span>Sample</span><span>≈ 2 weeks</span></div></div>
<span class="btn lbl" style="align-self:flex-start;background:#fff">View more <i>↓</i></span></div></div></section>'''
out = R.parent / 'dist' / 'ref'; out.mkdir(parents=True, exist_ok=True)
html = (R / 'fonts_board.html').read_text(encoding='utf-8').replace('<!--OPTS-->', ''.join(opt(*o) for o in OPTS))
(out / 'fonts.html').write_text(html, encoding='utf-8')
for o in OPTS: shutil.copy(R / f'ref_{o[4]}.jpg', out / f'ref_{o[4]}.jpg')
print('ok')
