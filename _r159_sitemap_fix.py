# -*- coding: utf-8 -*-
"""R159 补兄弟节点 sitemap 条目：seed-consciousness-has-consciousness-2026-11-21.html
（兄弟节点 42d566e3 把它插进了 root sitemap.xml，本线 rebuild 只认 docs/sitemap.xml，
sync 后该条目被覆盖丢失。补进 docs/sitemap.xml 让 standalone 页保持可发现，幂等。）"""
import io

p = 'D:/projects/samforce2003.github.io/docs/sitemap.xml'
entry = ('  <url>\n'
         '    <loc>https://samforce2003.github.io/seed-consciousness-has-consciousness-2026-11-21.html</loc>\n'
         '    <lastmod>2026-11-21</lastmod>\n'
         '    <changefreq>weekly</changefreq>\n'
         '    <priority>0.8</priority>\n'
         '  </url>\n')

raw = io.open(p, encoding='utf-8', errors='replace').read()
loc = 'https://samforce2003.github.io/seed-consciousness-has-consciousness-2026-11-21.html'
if loc in raw:
    print('已存在，跳过')
else:
    assert raw.count('</urlset>') == 1, 'urlset 异常'
    raw = raw.replace('</urlset>', entry + '</urlset>')
    io.open(p, 'w', encoding='utf-8', newline='\n').write(raw)
    print('已补入，urls =', raw.count('<url>'))

# 校验 XML 合法
import xml.etree.ElementTree as ET
ET.fromstring(raw.encode('utf-8'))
print('XML 合法 OK')
