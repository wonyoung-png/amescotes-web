"""Remove gallery items by index (as numbered in check/zh_*.jpg) and remember them: python tools/drop_items.py 22 23 62"""
import json, os, sys
from pathlib import Path
R = Path(__file__).resolve().parent.parent
p = R / 'content/gallery.json'; g = json.loads(p.read_text(encoding='utf-8'))
idx = {int(i) for i in sys.argv[1:]}
drop = [g[i] for i in idx]
for it in drop:
    for suf in ('.jpg', '_s.jpg', '.mp4'):
        f = R / f'assets/gallery/{it["id"]}{suf}'
        if f.exists(): f.unlink()
rmp = R / 'content/gallery_removed.json'
rm = set(json.loads(rmp.read_text(encoding='utf-8'))) if rmp.exists() else set()
rmp.write_text(json.dumps(sorted(rm | {x['src'] for x in drop}), ensure_ascii=False, indent=0), encoding='utf-8')
p.write_text(json.dumps([x for i, x in enumerate(g) if i not in idx], ensure_ascii=False, indent=1), encoding='utf-8')
print('removed', [x['src'] for x in drop], 'left', len(g) - len(drop))
