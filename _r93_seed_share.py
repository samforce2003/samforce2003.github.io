#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""R93 观察位：seed-share 同步器（此前靠人手拷 += R92 手工产出带了一条转义残片）。

做什么：
1. 读 docs/_seed_index.jsonl 里 src 以「强灌线-R<n>」开头的条目 → 从 _seed_full_blocks.html 取对应正文块
2. 只追加本轮 R 号分段到 docs/seed-share/index.html（幂等：已有该 R 号则跳过）
3. 顺手修残片：删掉正文里 `&lt;h2&gt;...&lt;/h2&gt;` 这种「标题被转义后又塞进 <p>」的行
   根因：R92 手工生成脚本把整块 HTML 拆成 <p> 时没剥 <h2>。HTML 里 <p> 内不能再嵌 <h2>，
   浏览器会把 <h2> 提前闭合 <p>，线上看到的是赤裸的 `<h2>标题</h2>` 文字。
用法： python _r93_seed_share.py [R93]
"""
import io, os, re, sys, json

BASE = os.path.dirname(os.path.abspath(__file__))
DOCS = os.path.join(BASE, 'docs')
IDX = os.path.join(DOCS, '_seed_index.jsonl')
FULL = os.path.join(DOCS, '_seed_full_blocks.html')
SHARE = os.path.join(DOCS, 'seed-share', 'index.html')
RB = sys.argv[1] if len(sys.argv) > 1 else 'R93'


def norm(s):
    return re.sub(r'\s+', '', re.sub(r'<[^>]+>', '', s))


def main():
    html = io.open(SHARE, encoding='utf-8', errors='ignore').read()

    # --- 1. 修转义残片 ---
    frag = len(re.findall(r'<p>&lt;h2&gt;.*?&lt;/h2&gt;</p>\s*', html))
    html = re.sub(r'<p>&lt;h2&gt;.*?&lt;/h2&gt;</p>\s*', '', html)
    if frag:
        print('frag-fix: 删除转义标题残片 %d 处' % frag)

    # --- 2. 幂等检查 ---
    if '<h2>%s ·' % RB in html:
        print('share: %s 已存在，跳过追加' % RB)
        io.open(SHARE, 'w', encoding='utf-8', newline='').write(html)
        return

    # --- 3. 取本轮条目 ---
    rows = []
    with io.open(IDX, encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            r = json.loads(line)
            if (r.get('src') or '').startswith('强灌线-' + RB):
                rows.append(r)
    if not rows:
        print('share: 索引里没有 src=强灌线-%s 的条目，未追加' % RB)
        io.open(SHARE, 'w', encoding='utf-8', newline='').write(html)
        return

    full = io.open(FULL, encoding='utf-8', errors='ignore').read()
    blocks = re.findall(r'<article[^>]*>.*?</article>', full, re.S)
    by_title = {}
    for b in blocks:
        m = re.search(r'<h2[^>]*>(.*?)</h2>', b, re.S)
        if m:
            by_title[norm(m.group(1))] = b.strip()

    out = ['<h2>%s · %s</h2>' % (RB, rows[0]['time'])]
    miss = 0
    for r in rows:
        b = by_title.get(norm(r['title']))
        if not b:
            miss += 1
            continue
        inner = re.sub(r'^<article[^>]*>|</article>$', '', b.strip()).strip()
        inner = re.sub(r'<h2[^>]*>.*?</h2>', '', inner, flags=re.S).strip()  # 标题已在 h3
        out.append('<h3>种子：%s</h3>' % r['title'])
        out.append('<article>')
        out.append(inner)
        out.append('</article>')

    add = '\n'.join(out) + '\n'
    html = html.replace('</body></html>', add + '</body></html>')
    io.open(SHARE, 'w', encoding='utf-8', newline='').write(html)
    print('share: %s 追加 %d 条（缺失 %d）| %dB' % (RB, len(rows) - miss, miss,
                                                  os.path.getsize(SHARE)))


if __name__ == '__main__':
    main()
