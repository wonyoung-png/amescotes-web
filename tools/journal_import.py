"""Turn a scraped Naver post dump (incoming/journal.json) into content/journal_posts.json + assets/journal/<slug>/*.jpg."""
import base64, io, json, sys
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
SRC = Path(sys.argv[1])
SLUG = {'224445659104': 'burgundy-suede-fw26', '223238746315': 'lambskin', '222007690109': 'bag-making-process'}
# lines kept off the company site: replica wording and a personal phone ask from the 2020 post
DROP = ('LV가방을 훔쳐서', '셀린을 모티브', '휴대폰 번호', '거래처 대표님이', '청량한 컬러의 오플가죽')

raw = json.loads(SRC.read_text(encoding='utf-8'))
posts = json.loads((ROOT / 'content' / 'journal_posts.json').read_text(encoding='utf-8')) if (ROOT / 'content' / 'journal_posts.json').exists() else {}
for log, post in raw.items():
    slug = SLUG[log]; out = ROOT / 'assets' / 'journal' / slug; out.mkdir(parents=True, exist_ok=True)
    blocks, n, skip_imgs = [], 0, False
    for b in post['blocks']:
        if b['t'] == 'p':
            lines = [l for l in b['v'] if not any(d in l for d in DROP)]
            skip_imgs = len(lines) < len(b['v'])  # images right after a dropped line belong to it
            while lines and not lines[-1]: lines.pop()
            while lines and not lines[0]: lines.pop(0)
            if lines: blocks.append({'t': 'p', 'v': lines})
        else:
            if skip_imgs: continue
            files = []
            for d in b.get('data') or []:
                if not d: continue
                im = Image.open(io.BytesIO(base64.b64decode(d.split(',', 1)[1]))).convert('RGB')
                im.thumbnail((1400, 1400)); n += 1
                name = f'{n:02d}.jpg'; im.save(out / name, quality=80, optimize=True, progressive=True)
                files.append({'src': f'journal/{slug}/{name}', 'w': im.width, 'h': im.height})
            if files: blocks.append({'t': 'img', 'v': files, 'cap': b.get('cap', '')})
    posts[slug] = {'log': log, 'url': f'https://blog.naver.com/amescotesofficial/{log}', 'blocks': blocks}
    print(slug, len(blocks), n)
(ROOT / 'content' / 'journal_posts.json').write_text(json.dumps(posts, ensure_ascii=False, indent=1), encoding='utf-8')
