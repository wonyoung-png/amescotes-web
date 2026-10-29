"""Build the static site: content/*.json + src/*.j2 -> dist/ (ko at root, en/ and ja/ subfolders)."""
import json, re, shutil, time
from pathlib import Path
from jinja2 import Environment, FileSystemLoader, StrictUndefined

ROOT = Path(__file__).parent
DIST = ROOT / 'dist'
LANGS = ['ko', 'en', 'ja']
HANGUL = re.compile('[가-힣]')


def load(name):
    return json.loads((ROOT / 'content' / f'{name}.json').read_text(encoding='utf-8'))


def merge_singles(blocks):
    """Runs of single-photo blocks become one multi-photo set (each photo keeps its own caption)."""
    out = []
    for blk in blocks:
        if blk['t'] == 'img' and len(blk['v']) == 1:
            item = {**blk['v'][0], 'cap': blk.get('cap', '')}
            if out and out[-1]['t'] == 'set': out[-1]['v'].append(item)
            else: out.append({'t': 'set', 'v': [item]})
        else:
            out.append(blk)
    return out


def build():
    site = load('site')
    gallery = load('gallery')
    # display order: camera shots first (ATLM, R000…), phone shots after, a film every 7 tiles for rhythm
    rank = lambda g: (0 if 'ATLM' in g['src'] else 1 if 'R0' in g['src'] else 2, g['src'])
    photos = sorted((g for g in gallery if g['type'] == 'photo'), key=rank)
    films = sorted((g for g in gallery if g['type'] == 'video'), key=rank)
    gallery = []
    while photos or films:
        gallery += photos[:6]; photos = photos[6:]
        if films: gallery.append(films.pop(0))
    env = Environment(loader=FileSystemLoader(ROOT / 'src'), undefined=StrictUndefined, autoescape=True)
    if DIST.exists():
        shutil.rmtree(DIST)
    shutil.copytree(ROOT / 'assets', DIST)
    for f in ('style.css', 'app.js'):
        shutil.copy(ROOT / 'src' / f, DIST / f)
    ver = str(int(time.time()))
    links = [(l, './' if l == 'ko' else f'{l}/') for l in LANGS]
    for lang in LANGS:
        t = load(lang)
        sub = '' if lang == 'ko' else f'{lang}/'
        ctx = dict(lang=lang, t=t, site=site, ver=ver, langs=links, base='../' if sub else '',
                   path=sub, home_path=sub or './', privacy_path=f'{sub}privacy.html', gallery_path=f'{sub}gallery.html',
                   data={**t, 'site': site})
        out = DIST / sub
        out.mkdir(parents=True, exist_ok=True)
        gctx = dict(gallery=gallery, gallery_js=[{'id': g['id'], 'type': g['type']} for g in gallery],
                    photos=sum(g['type'] == 'photo' for g in gallery), videos=sum(g['type'] == 'video' for g in gallery))
        page = env.get_template('page.html.j2').render(**ctx, **gctx)
        (out / 'index.html').write_text(page, encoding='utf-8')
        (out / 'privacy.html').write_text(env.get_template('privacy.html.j2').render(**ctx), encoding='utf-8')
        (out / 'gallery.html').write_text('<!doctype html><meta http-equiv="refresh" content="0;url=./#gallery">', encoding='utf-8')  # old links land on the section
        if lang != 'ko':  # every visible string must be translated
            visible = re.sub(r'<script type="application/ld\+json">.*?</script>', '', page, flags=re.S)
            left = sorted(set(HANGUL.findall(visible)))
            assert not left, f'{lang}: untranslated Korean left: {"".join(left)[:40]}'
    # journal articles (Korean source text), drawer + footer shared with the home page
    posts = load('journal_posts'); ko = load('ko'); (DIST / 'journal').mkdir(exist_ok=True)
    order = [j['slug'] for j in site['journal']]
    for k, slug in enumerate(order):
        meta = site['journal'][k]; head = ko['journal']['posts'][k]
        nxt = order[(k + 1) % len(order)]
        html = env.get_template('article.html.j2').render(lang='ko', t=ko, site=site, ver=ver, langs=links, base='../',
            home_path='./', privacy_path='privacy.html', post={**posts[slug], 'blocks': merge_singles(posts[slug]['blocks'])}, meta=meta, head=head,
            next_slug=nxt, next_head=ko['journal']['posts'][order.index(nxt)])
        (DIST / 'journal' / f'{slug}.html').write_text(html, encoding='utf-8')
    # chapters/places in site.json must line up with every language file
    for lang in LANGS:
        t = load(lang)
        assert len(t['services']) == len(site['chapters']), lang
        assert len(t['global']['places']) == len(site['places']), lang
        assert len(t['history']['items']) == len(site['history_years']), lang
        assert len(t['journal']['posts']) == len(site['journal']), lang
    # old imweb paths (www.amescotes.co.kr/<page>) -> new sections; GitHub Pages has no 301, so meta refresh + canonical
    for old, new in OLD_PATHS.items():
        d = DIST / old; d.mkdir(exist_ok=True)
        to = f'{site["url"]}/{new}'
        (d / 'index.html').write_text(f'<!doctype html><meta charset="utf-8"><title>AMESCOTES</title><link rel="canonical" href="{to}"><meta name="robots" content="noindex"><meta http-equiv="refresh" content="0; url=../{new}"><script>location.replace("../{new}")</script><a href="../{new}">AMESCOTES</a>', encoding='utf-8')
    pages = ['', 'en/', 'ja/', 'gallery.html', 'en/gallery.html', 'ja/gallery.html'] + [f'journal/{j["slug"]}.html' for j in site['journal']]
    urls = ''.join(f'<url><loc>{site["url"]}/{p}</loc></url>' for p in pages)
    (DIST / 'llms.txt').write_text(LLMS.format(url=site['url'], email=site['email'], posts='\n'.join(f'- [{h["title"]}]({site["url"]}/journal/{j["slug"]}.html)' for j, h in zip(site['journal'], load('ko')['journal']['posts']))), encoding='utf-8')
    (DIST / 'sitemap.xml').write_text(f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>', encoding='utf-8')
    (DIST / 'robots.txt').write_text(f'User-agent: *\nAllow: /\nSitemap: {site["url"]}/sitemap.xml\n', encoding='utf-8')
    (DIST / '.nojekyll').write_text('')
    print('built', sorted(str(p.relative_to(DIST)) for p in DIST.rglob('*.html')))


OLD_PATHS = {'home': '', 'aboutus': '#story', 'services': '#works', 'businessrange': '#range', 'portfolio': '#products', 'contacts': '#contact'}
LLMS = '''# AMESCOTES, Inc. (주)아메스코테스

> Seoul-based OEM/ODM manufacturer of leather handbags, small leather goods and shoes for designer and contemporary brands. In-house development studio in Seoul, offices in Shenzhen and Guangzhou, partner factories in Dongguan, Guangzhou and Yiwu.

## Pages
- [Home (KO)]({url}/)
- [Home (EN)]({url}/en/)
- [Home (JA)]({url}/ja/)
- [Gallery]({url}/gallery.html)

## Journal
{posts}

## Contact
- {email}
'''


if __name__ == '__main__':
    build()
