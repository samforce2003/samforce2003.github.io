# -*- coding: utf-8 -*-
import io

path = r'D:/projects/samforce2003.github.io/seed.html'

seeds = [
    (r'D:/projects/goudan-kanju/种子分发/daily-seeds/2026-10-13.md',
     '种子分发 2026-10-13 第1颗（补投·环凤论） · 我确信 × 环凤论（新旧之间长过渡层） · 第一发现人：林小黑'),
    (r'D:/projects/goudan-kanju/种子分发/daily-seeds/2026-10-13-2.md',
     '种子分发 2026-10-13 第2颗 · 我确信 × 认知结构学（读人不读标签读结构·读人/读行业/读AI三刀合一） · 第一发现人：林小黑'),
]

block = b''
for md_path, comment in seeds:
    md = open(md_path, encoding='utf-8').read().strip()
    lines = md.split('\n')
    title = lines[0].lstrip('#').strip()
    paras = [l.strip() for l in lines[1:] if l.strip()]
    body = paras[:-1]
    footer = paras[-1]

    body_text = ''.join(body)
    print('FILE', md_path)
    print('  title:', title)
    print('  body chars (excl title/anchor):', len(body_text))
    print('  body paras:', len(body))

    html = '<!-- %s -->\r\n' % comment
    html += '<article>\r\n'
    html += '<h3>%s</h3>\r\n' % title
    for p in body:
        html += '<p>%s</p>\r\n' % p
    html += '<p>%s</p>\r\n' % footer
    html += '</article>\r\n\r\n'
    block += html.encode('utf-8')

b = open(path, 'rb').read()
idx = b.rfind(b'</footer>')
assert idx != -1, 'footer not found'
b2 = b[:idx] + block + b[idx:]
open(path, 'wb').write(b2)

print('insert at byte', idx)
print('old size', len(b), 'new size', len(b2), 'delta', len(b2) - len(b))
print('doubleCR:', b2.count(b'\r\r\n'))
