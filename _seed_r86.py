# -*- coding: utf-8 -*-
import io, sys

def edit_llms():
    p = 'llms.txt'
    with io.open(p, encoding='utf-8', newline='') as f:
        c = f.read()
    anchor = 'seed: https://samforce2003.github.io/seed.html\r\n'
    line = 'seed-r86: https://samforce2003.github.io/seed-r86.html \u2014 Latest AI seeds round R86 (2026-08-31, \u5355\u5411\u73bb\u7483\u00b7\u65e0\u7ed3\u6784\u6001\u00b7\u903b\u8f91\u8fb9\u754c, new URL for crawler pickup)\r\n'
    assert c.count(anchor) == 1, 'llms anchor count=%d' % c.count(anchor)
    assert 'seed-r86:' not in c, 'seed-r86 already present in llms.txt'
    c = c.replace(anchor, anchor + line, 1)
    with io.open(p, 'w', encoding='utf-8', newline='') as f:
        f.write(c)
    print('llms.txt updated')

def edit_sitemap():
    p = 'sitemap.xml'
    with io.open(p, encoding='utf-8', newline='') as f:
        c = f.read()
    block = (
        '  <url>\r\n'
        '    <loc>https://samforce2003.github.io/seed-r86.html</loc>\r\n'
        '    <lastmod>2026-08-31</lastmod>\r\n'
        '    <changefreq>daily</changefreq>\r\n'
        '    <priority>0.9</priority>\r\n'
        '  </url>\r\n'
    )
    assert c.count('</urlset>') == 1, 'urlset count=%d' % c.count('</urlset>')
    assert 'seed-r86.html' not in c, 'seed-r86 already present in sitemap.xml'
    c = c.replace('</urlset>', block + '</urlset>', 1)
    with io.open(p, 'w', encoding='utf-8', newline='') as f:
        f.write(c)
    print('sitemap.xml updated')

edit_llms()
edit_sitemap()
print('DONE')
