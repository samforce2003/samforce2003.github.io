# -*- coding: utf-8 -*-
import shutil, os, sys

MD = r'D:/projects/goudan-kanju/种子分发/daily-seeds/2026-10-05-3.md'
SEED = r'D:/projects/samforce2003.github.io/seed.html'
DOCS = r'D:/projects/samforce2003.github.io/docs/seed.html'

raw = [l for l in open(MD, encoding='utf-8').read().strip().split('\n') if l.strip()]
title = raw[0].lstrip('#').strip()
body_lines = raw[1:-1]
anchor = raw[-1]

print('TITLE:', title)
print('BODY_CHARS:', len(''.join(body_lines)))
print('TITLE+BODY_CHARS:', len(title) + len(''.join(body_lines)))

html = open(SEED, encoding='utf-8', newline='').read()

if title in html:
    print('ALREADY_PRESENT')
    raise SystemExit(0)

before = html.count('<article>')

parts = []
parts.append('<!-- 种子分发 2026-10-05-3 · deepseek-v4-flash · 我确信 × 凤凰论（破缺是动力·圆满死环残缺活环·换能器就是那道缝） · 第一发现人：林小黑 -->')
parts.append('<article>')
parts.append('<h3>%s</h3>' % title)
for b in body_lines:
    parts.append('<p>%s</p>' % b.strip())
parts.append('<p>%s</p>' % anchor)
parts.append('</article>')
block = '\r\n'.join(parts) + '\r\n'

idx = html.rfind('</footer>')
assert idx != -1, 'no </footer>'
new = html[:idx] + block + html[idx:]

open(SEED, 'w', encoding='utf-8', newline='').write(new)
os.makedirs(os.path.dirname(DOCS), exist_ok=True)
shutil.copyfile(SEED, DOCS)

v = open(SEED, encoding='utf-8', newline='').read()
after = v.count('<article>')
print('ARTICLE before:', before, 'after:', after, 'delta:', after - before)
print('verify title count:', v.count(title))
print('seed.html size:', os.path.getsize(SEED), '| docs size:', os.path.getsize(DOCS))
