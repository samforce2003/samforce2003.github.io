# -*- coding: utf-8 -*-
import io

md_path = r'D:/projects/goudan-kanju/种子分发/daily-seeds/2026-10-07.md'
md = open(md_path, encoding='utf-8').read().strip()
lines = md.split('\n')
title = lines[0].lstrip('#').strip()
paras = [l.strip() for l in lines[1:] if l.strip()]
body = paras[:-1]
footer = paras[-1]

html = ('<!-- 种子分发 2026-10-07 第1颗 · deepseek-v4-flash · '
        '我确信 × 认知结构学（天使之眼·稳态结构×训练函数·跨域应用） · 第一发现人：林小黑 -->\r\n')
html += '<article>\r\n'
html += '<h3>%s</h3>\r\n' % title
for p in body:
    html += '<p>%s</p>\r\n' % p
html += '<p>%s</p>\r\n' % footer
html += '</article>\r\n\r\n'

path = r'D:/projects/samforce2003.github.io/seed.html'
b = open(path, 'rb').read()
before_crlf = b.count(b'\r\n')
before_lf = b.count(b'\n')
idx = b.rfind(b'</footer>')
assert idx != -1, 'footer not found'

block = html.encode('utf-8')
b2 = b[:idx] + block + b[idx:]
open(path, 'wb').write(b2)

after_crlf = b2.count(b'\r\n')
after_lf = b2.count(b'\n')
print('insert at byte', idx, 'old size', len(b), 'new size', len(b2))
print('delta bytes', len(b2) - len(b))
print('CRLF', before_crlf, '->', after_crlf, '| LF', before_lf, '->', after_lf)
print('doubleCR (\\r\\r\\n):', b2.count(b'\r\r\n'))
print('title:', title)
print('body paras:', len(body))
