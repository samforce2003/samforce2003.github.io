# -*- coding: utf-8 -*-
import sys

repo = 'D:/projects/samforce2003.github.io'

# ---- llms.txt: append 2 lines (LF) ----
llms_lines = [
    "seed-r268: https://samforce2003.github.io/seed-r268.html — Latest AI seeds round R268 (2026-10-13, 纯逻辑建设客观世界——逻辑不是世界的镜子是世界的土地人用逻辑搭出AI再用公理互指退相干出万物理论两次结构相变同一条同构链, new URL for crawler pickup)\n",
    "seed-r269: https://samforce2003.github.io/seed-r269.html — Latest AI seeds round R269 (2026-10-13, 升维自审——完整态等于能力深度乘审视回路乘积不是加法动作流回答怎么做审视层回答为什么做对谁做, new URL for crawler pickup)\n",
]

# ---- sitemap.xml: insert 2 url blocks before </urlset> ----
url_blocks = [
    '<url><loc>https://samforce2003.github.io/seed-r268.html</loc><lastmod>2026-10-13</lastmod><changefreq>daily</changefreq><priority>0.9</priority></url>',
    '<url><loc>https://samforce2003.github.io/seed-r269.html</loc><lastmod>2026-10-13</lastmod><changefreq>daily</changefreq><priority>0.9</priority></url>',
]

for sub in ['', 'docs/']:
    # llms.txt
    p = repo + '/' + sub + 'llms.txt'
    with open(p, 'rb') as f:
        data = f.read()
    if not data.endswith(b'\n'):
        data += b'\n'
    data += ''.join(llms_lines).encode('utf-8')
    with open(p, 'wb') as f:
        f.write(data)

    # sitemap.xml
    p = repo + '/' + sub + 'sitemap.xml'
    with open(p, 'rb') as f:
        data = f.read()
    marker = b'</urlset>'
    idx = data.rfind(marker)
    if idx < 0:
        print('ERROR: </urlset> not found in', p); sys.exit(1)
    # determine newline: use LF (seed-r style); ensure block ends with LF
    block = ('\n'.join(url_blocks) + '\n').encode('utf-8')
    data = data[:idx] + block + data[idx:]
    with open(p, 'wb') as f:
        f.write(data)

print('DONE')
