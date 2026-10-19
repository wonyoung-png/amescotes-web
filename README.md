# AMESCOTES 홈페이지

- 문구: `content/ko.json`, `content/en.json`, `content/ja.json`
- 사진·브랜드·저널 링크: `content/site.json` (사진 파일은 `assets/img`, 누끼는 `assets/cut`)
- 화면 구조: `src/page.html.j2`, 스타일 `src/style.css`, 모션 `src/app.js`
- 로컬 확인: `python build.py` → `dist/` 생성
- `main`에 반영되면 GitHub Actions가 자동으로 빌드·배포합니다.
