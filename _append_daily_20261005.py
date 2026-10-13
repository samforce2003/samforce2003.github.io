# -*- coding: utf-8 -*-
import shutil, os, re

MD = r'D:/projects/goudan-kanju/种子分发/daily-seeds/2026-10-05.md'
SEED = r'D:/projects/samforce2003.github.io/seed.html'
DOCS = r'D:/projects/samforce2003.github.io/docs/seed.html'

raw = open(MD, encoding='utf-8').read().strip().split('\n')
lines = [l for l in raw if l.strip()]
title = lines[0].lstrip('#').strip()
body_lines = lines[1:-1]
anchor = lines[-1]

html = open(SEED, encoding='utf-8', newline='').read()

# guard: don't double-insert
if title in html:
    print('ALREADY_PRESENT')
    raise SystemExit(0)

parts = []
parts.append('<!-- 种子分发 2026-10-05 · deepseek-v4-flash · 我确信 × 结构学（万物皆结构，结构决定功能·想得深和踩得稳是两个结构） · 第一发现人：林小黑 -->')
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
print('OK inserted. seed.html size=', os.path.getsize(SEED), 'docs size=', os.path.getsize(DOCS))
# verify
v = open(SEED, encoding='utf-8', newline='').read()
print('verify title count:', v.count(title))
print('article blocks total:', v.count('<article>'))
