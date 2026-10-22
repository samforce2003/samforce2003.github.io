# -*- coding: utf-8 -*-
"""R613: 修 sitemap 结构 + 纳入 seed-full.html + 让 build 脚本自动维护 lastmod"""
import io, os, re, datetime, xml.etree.ElementTree as ET

BASE = r'D:/projects/samforce2003.github.io'
SM = os.path.join(BASE, 'docs', 'sitemap.xml')
TODAY = '2026-10-22'

raw = io.open(SM, encoding='utf-8', errors='replace').read()
print('before: bytes %d, urlset-line=%r' % (len(raw.encode('utf-8')), raw.splitlines()[1]))

# 1) 修头：<urlset> 后那段孤立的 xmlns 片段（原文件把属性行拆成了第二行残片）
raw = re.sub(r'<\?xml[^>]*\?>\s*', '', raw, count=1)
raw = re.sub(r'<urlset[^>]*>\s*', '', raw, count=1)
# 去掉残片行 xmlns="...">
raw = re.sub(r'\n\s*xmlns="[^"]*">\s*\n', '\n', raw, count=1)
# 去掉可能的 </urlset> 前后残留
raw = re.sub(r'</urlset>\s*$', '', raw.strip())

# 2) 逐条解析，重建规范 XML
urls = re.findall(r'<url>(.*?)</url>', raw, re.S)
recs = []
for u in urls:
    loc = re.search(r'<loc>(.*?)</loc>', u, re.S)
    if not loc:
        continue
    lm = re.search(r'<lastmod>(.*?)</lastmod>', u, re.S)
    cf = re.search(r'<changefreq>(.*?)</changefreq>', u, re.S)
    pr = re.search(r'<priority>(.*?)</priority>', u, re.S)
    recs.append({'loc': loc.group(1).strip(),
                 'lastmod': lm.group(1).strip() if lm else TODAY,
                 'changefreq': cf.group(1).strip() if cf else 'weekly',
                 'priority': pr.group(1).strip() if pr else '0.8'})
print('parsed urls:', len(recs))

by_loc = {r['loc']: r for r in recs}
# 3) seed.html 刷 lastmod；seed-full.html 补进去
s1 = 'https://samforce2003.github.io/seed.html'
s2 = 'https://samforce2003.github.io/seed-full.html'
if s1 in by_loc:
    by_loc[s1]['lastmod'] = TODAY
    by_loc[s1]['changefreq'] = 'daily'
    by_loc[s1]['priority'] = '1.0'
    print('seed.html: lastmod ->', TODAY)
if s2 not in by_loc:
    recs.insert(1, {'loc': s2, 'lastmod': TODAY, 'changefreq': 'daily', 'priority': '0.6'})
    print('seed-full.html: inserted (new)')
else:
    by_loc[s2]['lastmod'] = TODAY
    print('seed-full.html: lastmod ->', TODAY)

out = ['<?xml version="1.0" encoding="UTF-8"?>',
       '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for r in recs:
    out.append('  <url>')
    out.append('    <loc>%s</loc>' % r['loc'])
    out.append('    <lastmod>%s</lastmod>' % r['lastmod'])
    out.append('    <changefreq>%s</changefreq>' % r['changefreq'])
    out.append('    <priority>%s</priority>' % r['priority'])
    out.append('  </url>')
out.append('</urlset>')
xml = '\n'.join(out) + '\n'

# 4) 语法校验
try:
    root = ET.fromstring(xml.encode('utf-8'))
    print('XML OK: root=%s, url count=%d' % (root.tag, len(list(root))))
except Exception as e:
    raise SystemExit('XML INVALID: %s' % e)

io.open(SM, 'w', encoding='utf-8', newline='\n').write(xml)
print('written: bytes %d' % len(xml.encode('utf-8')))
