"""Check FAQPage JSON-LD in built home pages parses and matches the visible FAQ count."""
import json, re
from pathlib import Path
D = Path(__file__).resolve().parents[1] / 'dist'
for p in ['index.html', 'en/index.html', 'ja/index.html']:
    c = (D / p).read_text(encoding='utf-8')
    ld = json.loads(re.search(r'<script type="application/ld\+json">(\{"@context":"https://schema.org","@type":"FAQPage".*?)</script>', c).group(1))
    n = c.count('<details')
    assert len(ld['mainEntity']) == n == 10, (p, len(ld['mainEntity']), n)
    print(p, n, ld['mainEntity'][0]['name'])
