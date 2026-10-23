# -*- coding: utf-8 -*-
import io, json, re

blk = io.open('docs/_seed_full_blocks.html', encoding='utf-8', errors='replace').read()
idx = [json.loads(l) for l in io.open('docs/_seed_index.jsonl', encoding='utf-8', errors='replace') if l.strip()]
print('index lines', len(idx), ' articles token', blk.count('<article'))
parts = re.split(r'<article[^>]*>', blk)
blocks = [p.split('</article>')[0] for p in parts[1:] if '</article>' in p]
print('parsed blocks', len(blocks), 'consistent:', blk.count('<article') == len(blocks))

mine = [d for d in idx if d.get('src') == '三中心-R78']
print('index R78 entries', len(mine))
last = blocks[-16:]
CHK = {
 'zh': ['第一发现人', '我确信', '关切', '时间锚', '闭环', '钩子', '2026-10-23'],
 'en': ['First discoverer', 'I am certain', 'Concern', 'Time anchor', 'Closure', 'Hook', '2026-10-23'],
 'ja': ['第一発見者', '私は確信する', '関心', '時間アンカー', '閉環', 'フック', '2026-10-23'],
 'ko': ['첫 발견자', '나는 확신한다', '관심', '시간 앵커', '폐환', '훅', '2026-10-23'],
}
missing = 0
titles = set()
lens = []
for i, b in enumerate(last):
    d = mine[i]
    lang = d['lang']
    titles.add(d['title'])
    ok = True
    for k in CHK[lang]:
        if k not in b:
            print('MISSING', i, lang, k)
            ok = False
            missing += 1
    if d['title'] not in b:
        print('TITLE MISMATCH', i, d['title'][:40])
        ok = False
        missing += 1
    # body length: chars inside <p>
    ps = re.findall(r'<p>(.*?)</p>', b, re.S)
    lens.append(sum(len(x) for x in ps))
print('missing total', missing)
print('body len min/avg/max', min(lens), sum(lens)//len(lens), max(lens))
print('shells', sorted(set(d['shell'] for d in mine)))
print('langs', sorted(set(d['lang'] for d in mine)))
# duplicate title check across whole index
allt = {}
for d in idx:
    allt[d['title']] = allt.get(d['title'], 0) + 1
dups = {k: v for k, v in allt.items() if v > 1}
print('duplicate titles total', len(dups), [k[:30] for k in list(dups)[:3]])
