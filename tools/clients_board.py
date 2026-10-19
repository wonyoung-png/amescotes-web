"""One-off: render dist/clients_board.html with 3 layout options for the client section."""
import json, html
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
C = json.loads((ROOT / 'content' / 'site.json').read_text(encoding='utf-8'))['clients']


def logo(c):
    return f'<img src="logo/{c["logo"]}" alt="{c["name"]}">' if c['logo'] else f'<span class="txt">{c["name"]}</span>'


A = ''.join(f'<div class="cell">{logo(c)}<span class="nm mono">{c["name"]}</span></div>' for c in C)
Cs = sorted(C, key=lambda c: c['name'])
B = ''.join(f'<li data-l="{c["logo"] or ""}" data-n="{c["name"]}"><span class="mono">{i+1:02d}</span>{html.escape(c["name"].title())}</li>' for i, c in enumerate(Cs))
pages = [C[i:i + 6] for i in range(0, len(C), 6)]
Cc = ''.join('<div class="pg">' + ''.join(f'<div class="card">{logo(c)}</div>' for c in p) + '</div>' for p in pages)
dots = ''.join('<i></i>' for _ in pages)

tpl = (ROOT / 'tools' / 'clients_board.tpl.html').read_text(encoding='utf-8')
out = tpl.replace('{{N}}', str(len(C))).replace('{{A}}', A).replace('{{B}}', B).replace('{{C}}', Cc).replace('{{DOTS}}', dots).replace('{{PAGES}}', str(len(pages)))
(ROOT / 'dist' / 'clients_board.html').write_text(out, encoding='utf-8')
print('ok', len(C))
