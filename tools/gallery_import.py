"""Import photos/videos from a folder into the gallery.

Usage: python tools/gallery_import.py "G:/공유 드라이브/LUMEN/비주얼/작업이미지"
Drops exact duplicates and near-identical burst shots, writes web-sized files to
assets/gallery/ and the list to content/gallery.json (new items are appended, so
running it again on a new folder only adds what isn't there yet).
"""
import json, subprocess, sys, hashlib
from pathlib import Path
from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'assets' / 'gallery'
LIST = ROOT / 'content' / 'gallery.json'
PHOTO = {'.jpg', '.jpeg', '.png'}
VIDEO = {'.mov', '.mp4'}
SKIP = {'IMG_9057', 'IMG_0478', 'IMG_0479', 'IMG_0480'}  # floor / packing clips
SKIP_PHOTO = {'2bab18d76e539a0def6e6f35b346b955', 'IMG_7235'}  # third-party product screenshots
SKIP_NAMES = {'ATLM6852.JPG', 'ATLM6853.JPG', 'IMG_9051.MP4'}  # supplier signage, duplicate clip
BURST = 7  # dhash bits that may differ and still count as "the same shot"


def dhash(im):
    g = im.convert('L').resize((9, 8))
    px = list(g.getdata())
    return sum(1 << i for i in range(64) if px[(i // 8) * 9 + i % 8] > px[(i // 8) * 9 + i % 8 + 1])


def main(src):
    OUT.mkdir(parents=True, exist_ok=True)
    items = json.loads(LIST.read_text(encoding='utf-8')) if LIST.exists() else []
    seen_ids = {it['id'] for it in items}
    hashes = [it['h'] for it in items if 'h' in it]
    removed = set(json.loads((ROOT / 'content' / 'gallery_removed.json').read_text(encoding='utf-8'))) if (ROOT / 'content' / 'gallery_removed.json').exists() else set()
    files = sorted(p for p in Path(src).rglob('*') if p.suffix.lower() in PHOTO | VIDEO)
    added = 0
    for p in files:
        if p.stem in SKIP or p.stem in SKIP_PHOTO or p.name in SKIP_NAMES or p.name in removed:
            continue
        fid = hashlib.md5(p.name.encode()).hexdigest()[:10]  # same file name in copied folders = same item
        if fid in seen_ids:
            continue
        if p.suffix.lower() in PHOTO:
            im = ImageOps.exif_transpose(Image.open(p)).convert('RGB')
            h = dhash(im)
            if any(bin(h ^ o).count('1') <= BURST for o in hashes):
                continue
            hashes.append(h)
            big = im.copy(); big.thumbnail((1800, 1800)); big.save(OUT / f'{fid}.jpg', quality=78, optimize=True, progressive=True)
            sm = im.copy(); sm.thumbnail((720, 720)); sm.save(OUT / f'{fid}_s.jpg', quality=74, optimize=True, progressive=True)
            items.append({'id': fid, 'type': 'photo', 'w': big.width, 'h_px': big.height, 'h': h, 'src': p.name})
        else:
            mp4 = OUT / f'{fid}.mp4'
            subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', str(p), '-an', '-vf', "scale='min(720,iw)':-2",
                            '-c:v', 'libx264', '-crf', '28', '-preset', 'slow', '-pix_fmt', 'yuv420p', '-movflags', '+faststart', str(mp4)], check=True)
            subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', str(mp4), '-frames:v', '1', '-q:v', '5', str(OUT / f'{fid}_s.jpg')], check=True)
            w, hh = Image.open(OUT / f'{fid}_s.jpg').size
            items.append({'id': fid, 'type': 'video', 'w': w, 'h_px': hh, 'src': p.name})
        seen_ids.add(fid); added += 1
        print('+', p.name, flush=True)
    LIST.write_text(json.dumps(items, ensure_ascii=False, indent=1), encoding='utf-8')
    print(f'added {added}, total {len(items)}')


if __name__ == '__main__':
    main(sys.argv[1])
