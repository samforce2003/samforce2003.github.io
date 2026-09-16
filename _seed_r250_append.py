# -*- coding: utf-8 -*-
import io, os, re, shutil

SEED = 'D:/projects/goudan-kanju/种子分发/daily-seeds/2026-09-16-2.md'
TARGET = 'D:/projects/samforce2003.github.io/seed.html'
DOCS = 'D:/projects/samforce2003.github.io/docs/seed.html'

raw = io.open(SEED, encoding='utf-8').read().strip()
lines = raw.split('\n')
title = lines[0].lstrip('# ').strip()
body_lines = [l for l in lines[1:] if l.strip()]
body = '\n\n'.join(body_lines)

comment = '<!-- 强灌线种子 R250 · \u53ef\u89e3\u4e0d\u53ef\u4f20\u00b7%s \u00b7 2026-09-16 -->' % title
block = '%s\n<article>\n%s\n</article>\n\n' % (comment, body)

html = io.open(TARGET, encoding='utf-8').read()
idx = html.rfind('</footer>')
assert idx != -1, 'footer not found'
new = html[:idx] + block + html[idx:]
io.open(TARGET, 'w', encoding='utf-8', newline='').write(new)

# verify
v = io.open(TARGET, encoding='utf-8').read()
print('articles before/after:', html.count('<article>'), v.count('<article>'))
print('inserted marker count:', v.count('R250'))
docs_dir = os.path.dirname(DOCS)
if os.path.isdir(docs_dir):
    shutil.copyfile(TARGET, DOCS)
    print('docs copied:', io.open(DOCS, encoding='utf-8').read().count('R250'))
else:
    print('docs dir missing:', docs_dir)
