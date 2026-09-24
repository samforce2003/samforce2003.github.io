# -*- coding: utf-8 -*-
import io, shutil

SRC = r"D:/projects/goudan-kanju/种子分发/daily-seeds/2026-09-24-5.md"
SEED = r"D:/projects/samforce2003.github.io/seed.html"
DOCS = r"D:/projects/samforce2003.github.io/docs/seed.html"

lines = [l.rstrip() for l in io.open(SRC, encoding='utf-8').read().split('\n') if l.strip()]
title = lines[0].lstrip('# ').strip()
anchor = [l for l in lines if l.startswith('第一发现人')][0]
paras = [l for l in lines[1:] if l is not anchor]

block = []
block.append('<!-- 日更种子 2026-09-24-5 · 通才与全才——一个被混淆了两千年的区别（耦合结构学·核篇） -->')
block.append('<article>')
block.append('<h3>%s</h3>' % title)
for p in paras:
    block.append('<p>%s</p>' % p)
block.append('<p>%s</p>' % anchor)
block.append('</article>')
block.append('')
block_txt = '\r\n'.join(block)

s = io.open(SEED, encoding='utf-8', newline='').read()
idx = s.rfind('</footer>')
assert idx != -1, 'no </footer> found'
before = s[:idx]
insert_at = before.rfind('\n')          # position of the \n in the \r\n before </footer>
new = before[:insert_at+1] + block_txt + before[insert_at+1:] + s[idx:]
assert new != s
io.open(SEED, 'w', encoding='utf-8', newline='').write(new)

shutil.copyfile(SEED, DOCS)
print('OK inserted, footer idx', idx)
print('new CRLF count', new.count('\r\n'))
print('article count now:', new.count('<article'))
