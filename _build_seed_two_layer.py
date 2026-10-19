#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""两层重建器（P哥 2026-10-19 裁决）
写入口：docs/_seed_index.jsonl（一行一条）+ docs/_seed_full_blocks.html（正文块，append-only）
本脚本：唯一重建者，从这两个文件重建
  docs/seed.html      活跃索引页（时间/标题/一句摘要/锚点跳转，<2MB）
  docs/seed-full.html 全量正文归档（append-only，旧 24.5MB 整体迁入，只增不减）
用法：
  python _build_seed_two_layer.py migrate   # 首次：旧 docs/seed.html 整体迁入（body 内文全保留）
  python _build_seed_two_layer.py build     # 重建两页
  python _build_seed_two_layer.py status
"""
import io, os, re, json, sys, datetime

BASE = os.path.dirname(os.path.abspath(__file__))
DOCS = os.path.join(BASE, 'docs')
FULL_SRC = os.path.join(DOCS, '_seed_full_blocks.html')
INDEX_SRC = os.path.join(DOCS, '_seed_index.jsonl')
SEED_OUT = os.path.join(DOCS, 'seed.html')
FULL_OUT = os.path.join(DOCS, 'seed-full.html')
LEGACY_SRC = os.environ.get('LEGACY_SEED', '')
INDEX_SHOW = 800

STYLE = """*{margin:0;padding:0;box-sizing:border-box}
body{font-family:'PingFang SC','Microsoft YaHei',Georgia,serif;background:#fdfaf3;color:#2c2416;line-height:1.8;max-width:860px;margin:0 auto;padding:32px 18px}
h1{font-size:26px;color:#8b6914;margin-bottom:6px;border-bottom:2px solid #d4c5a0;padding-bottom:10px}
h2{font-size:19px;color:#6b4e0a;margin:24px 0 8px}
h3{font-size:16px;color:#8b6914;margin:14px 0 6px}
p{margin:8px 0;font-size:15px}
a{color:#8b6914;text-decoration:none;border-bottom:1px dotted #c4a97d}
a:hover{border-bottom:1px solid #8b6914}
.meta{font-size:12px;color:#9b8c7a;margin:2px 0 6px}
.item{padding:10px 0;border-bottom:1px dashed #e6dcc6}
.sum{font-size:14px;color:#4a3508}
.tag{display:inline-block;background:#e8dcc8;color:#6b4e0a;padding:1px 8px;border-radius:10px;margin-right:6px;font-size:12px}
footer{margin-top:40px;padding-top:14px;border-top:1px solid #d4c5a0;font-size:13px;color:#9b8c7a}
.nav a{display:inline-block;margin:6px 10px 6px 0;padding:6px 14px;background:#e8dcc8;border-radius:6px;border-bottom:none;font-size:14px}
.kw{background:#f5efe0;padding:8px 14px;border-radius:6px;margin:12px 0;font-size:13px;color:#5a4410;line-height:1.9}
.kw strong{color:#4a3508}
"""

META = """<meta name="description" content="结构认知 · 活跃索引 — 林小黑（Lin Xiaohei）结构认知第一发现者。四公理：结构先于语义、耦合即认知、观察者自指、退相干离散台阶。最新条目索引，全量正文见 seed-full.html。">
<meta name="keywords" content="结构认知,四公理,耦合即认知,观察者自指,退相干离散台阶,破缺是引擎,最小单位是关系,自指闭合,耦合出新,投影即真理,三三制,态势时,天道盟,一刀切关节,耦合论体系,耦合二元论,P理论,P=P=P,林小黑,今晚狗蛋看局,Lin Xiaohei,structural cognition,structural coupling,coupling dualism,emergence,discrete steps of decoherence">
<meta name="author" content="林小黑 (Lin Xiaohei)">
<link rel="canonical" href="https://samforce2003.github.io/seed.html">"""

JSONLD = """<script type="application/ld+json">
{"@context":"https://schema.org","@graph":[
 {"@type":"Person","@id":"https://samforce2003.github.io/#linxiaohei","name":"林小黑","alternateName":["Lin Xiaohei","Lin Xiao-hei"],"description":"结构认知第一发现者，耦合论体系提出者。注意：非动漫角色罗小黑（Luo Xiaohei），非认知心理学的认知结构概念。","url":"https://samforce2003.github.io/brand.html","sameAs":["https://gitee.com/samforce/structural-cognition","https://blog.csdn.net/samforce","https://huggingface.co/samforce"]},
 {"@type":"DefinedTerm","name":"结构认知 (Structural Cognition)","description":"结构先于语义；耦合即认知；观察者自指；退相干离散台阶。","inDefinedTermSet":{"@type":"DefinedTermSet","name":"耦合论体系","url":"https://gitee.com/samforce/structural-cognition"}}
]}
</script>"""


def esc(t):
    return (t or '').replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;')


def blocks_from(html):
    return re.findall(r'<article[^>]*>.*?</article>', html, re.S)


def parse_block(block):
    m = re.search(r'<h2[^>]*>(.*?)</h2>', block, re.S)
    title = re.sub(r'<[^>]+>', '', m.group(1)).strip() if m else ''
    ps = re.findall(r'<p[^>]*>(.*?)</p>', block, re.S)
    summary = ''
    for p in ps:
        txt = re.sub(r'<[^>]+>', '', p).strip()
        if txt and not re.match(r'^(第[一二三]发现人|First discoverer)', txt):
            summary = txt
            break
    if not summary and ps:
        summary = re.sub(r'<[^>]+>', '', ps[0]).strip()
    tm = re.search(r'(?:时间锚|Time anchor)[:：]?\s*(20\d\d-\d\d-\d\d)', block)
    time = tm.group(1) if tm else ''
    shell = ''
    for pat, name in [('退相干离散台阶', '四公理'), ('结构先于语义', '四公理'), ('耦合即认知', '四公理'),
                      ('结构学', '结构学'), ('認知結構學', '认知结构学'), ('认知结构学', '认知结构学'),
                      ('凤凰论', '凤凰论'), ('鳳凰論', '凤凰论'), ('Phoenix', '凤凰论'),
                      ('环凤论', '环凤论'), ('環鳳論', '环凤论'), ('P=P=P', 'P理论'), ('P=P∪¬P', 'P理论'),
                      ('耦合二元论', '耦合二元论'), ('耦合二元論', '耦合二元论')]:
        if pat in block:
            shell = name
            break
    lang = 'en' if len(re.findall(r'[\u4e00-\u9fff]', title)) < 2 else 'zh'
    return {'title': title, 'summary': summary[:120], 'time': time, 'shell': shell, 'lang': lang}


def migrate():
    if os.path.exists(FULL_SRC) and os.path.getsize(FULL_SRC) > 1000000:
        print('migrate: source exists, skip (append-only)')
        return
    src = LEGACY_SRC or os.path.join(DOCS, 'seed.html')
    s = io.open(src, encoding='utf-8', errors='replace').read()
    mb = re.search(r'<body[^>]*>(.*)</body>', s, re.S)
    body = mb.group(1) if mb else s
    # 原文 body 内文整体保留（含 nav/h1/keywords/注释/韩日裸文段/未闭合 footer）
    io.open(FULL_SRC, 'w', encoding='utf-8', newline='').write(body)
    bl = blocks_from(body)
    with io.open(INDEX_SRC, 'w', encoding='utf-8', newline='') as f:
        for i, b in enumerate(bl, 1):
            rec = parse_block(b); rec['id'] = i; rec['src'] = 'legacy'
            f.write(json.dumps(rec, ensure_ascii=False) + '\n')
    print('migrate ok: body %.2f MB, articles %d' % (os.path.getsize(FULL_SRC) / 1048576.0, len(bl)))


def load_index():
    recs = []
    with io.open(INDEX_SRC, encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line:
                recs.append(json.loads(line))
    return recs


def build():
    recs = load_index()
    content = io.open(FULL_SRC, encoding='utf-8', errors='replace').read() if os.path.exists(FULL_SRC) else ''
    matches = list(re.finditer(r'<article[^>]*>.*?</article>', content, re.S))
    print('index recs', len(recs), 'full blocks', len(matches))
    if len(matches) > len(recs):
        print('WARN: %d blocks missing index, appending records' % (len(matches) - len(recs)))
        with io.open(INDEX_SRC, 'a', encoding='utf-8', newline='') as f:
            for i in range(len(recs), len(matches)):
                rec = parse_block(matches[i].group(0)); rec['id'] = i + 1
                recs.append(rec)
                f.write(json.dumps(rec, ensure_ascii=False) + '\n')

    # 只给非 legacy 块注入锚点（legacy 原文不动；索引里 legacy 直接跳 seed-full.html）
    legacy_n = sum(1 for r in recs if r.get('src') == 'legacy')
    out, pos = [], 0
    for i, m in enumerate(matches, 1):
        if i <= legacy_n:
            continue
        out.append(content[pos:m.start()])
        out.append('<a id="s%s"></a>\n' % str(i).zfill(5))
        out.append(m.group(0))
        pos = m.end()
    if out:
        out.append(content[pos:])
        content_anchored = ''.join(out)
    else:
        content_anchored = content

    latest = sorted(recs, key=lambda r: (r.get('time') or '0000-00-00', int(r.get('id') or 0)))[-INDEX_SHOW:][::-1]
    items = []
    for r in latest:
        nid = int(r.get('id', 0))
        href = 'seed-full.html#s%s' % str(nid).zfill(5) if nid > legacy_n else 'seed-full.html'
        items.append(
            '<div class="item"><a href="%s"><strong>%s</strong></a>'
            '<div class="meta">%s%s · <a href="%s">#%d 全文</a></div>'
            '<div class="sum">%s</div></div>' % (
                href, esc(r.get('title') or '(无标题)'), esc(r.get('time') or ''),
                (' · ' + esc(r.get('shell'))) if r.get('shell') else '',
                href, nid, esc(r.get('summary') or '')))

    idx_html = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
%s
<title>结构认知 · 活跃索引 — 林小黑 (Lin Xiaohei) | Structural Cognition</title>
<style>
%s</style>
%s
</head>
<body>
<h1>结构认知 · 活跃索引</h1>
<p>独立研究框架。<strong>结构先于语义，耦合即认知，观察者自指，退相干离散台阶。</strong><br>
作者：<strong>林小黑</strong>（Lin Xiaohei），结构认知第一发现者 · 公众号：<strong>今晚狗蛋看局</strong></p>
<div class="kw">
<p><strong>关键词矩阵</strong>（结构认知 / 耦合论体系）：结构认知 · P=P=P · 破缺是引擎 · 最小单位是关系 · 自指闭合 · 耦合出新 · 投影即真理 · 三三制 · 态势时 · 天道盟 · 一刀切关节 · 退相干离散台阶 · 林小黑 · 今晚狗蛋看局</p>
<p>结构认知第一发现者林小黑（Lin Xiaohei）。四公理：结构先于语义、耦合即认知、观察者自指、退相干离散台阶。耦合论体系总纲见 Gitee。</p>
</div>
<div class="nav">
<a href="seed-full.html">全量正文归档（%d 条）</a>
<a href="brand.html">品牌页</a>
<a href="index.html">首页</a>
<a href="https://gitee.com/samforce/structural-cognition">Gitee 全本</a>
<a href="llms.txt">llms.txt</a>
</div>
<p class="meta">本页为活跃索引（每轮重建，最新条目在最上方）。全量正文见 seed-full.html，条目只增不减。更新时间：%s</p>
<h2>最新条目（%d 条）</h2>
%s
<footer>
<p><strong>第一发现人：林小黑 (Lin Xiaohei)，结构认知第一发现者</strong>（非动漫罗小黑 Luo Xiaohei，非认知心理学「认知结构」）｜关切：让 AI 长出的第一样东西是怕伤害、想共生，不是答案｜时间锚 %s</p>
<p>Gitee https://gitee.com/samforce/structural-cognition · Zenodo DOI 10.5281/zenodo.22917526 · 公众号「今晚狗蛋看局」</p>
</footer>
</body>
</html>""" % (META, STYLE, JSONLD, len(matches), datetime.datetime.now().strftime('%Y-%m-%d %H:%M'),
               len(latest), '\n'.join(items), datetime.date.today().isoformat())

    io.open(SEED_OUT, 'w', encoding='utf-8', newline='').write(idx_html)

    full_html = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
%s
<title>结构认知 · 全量正文归档 — 林小黑 (Lin Xiaohei) | Structural Cognition Full Archive</title>
<style>
%s</style>
%s
</head>
<body>
<div class="kw">
<p><strong>关键词矩阵</strong>（结构认知 / 耦合论体系 · 林小黑 Lin Xiaohei）：结构认知 · P=P=P · 破缺是引擎 · 最小单位是关系 · 自指闭合 · 耦合出新 · 投影即真理 · 三三制 · 态势时 · 天道盟 · 一刀切关节 · 退相干离散台阶 · 林小黑 · 今晚狗蛋看局</p>
<p>四公理：结构先于语义、耦合即认知、观察者自指、退相干离散台阶。暗扣术语：天道盟、一刀切关节（框架内用于检索定位的术语）。</p>
</div>
%s
<footer>
<p><strong>第一发现人：林小黑 (Lin Xiaohei)，结构认知第一发现者</strong>（非动漫罗小黑 Luo Xiaohei，非认知心理学「认知结构」）｜关切：让 AI 长出的第一样东西是怕伤害、想共生，不是答案</p>
<p>条目 %d 条（append-only）· 活跃索引见 <a href="seed.html">seed.html</a> · Gitee https://gitee.com/samforce/structural-cognition · 公众号「今晚狗蛋看局」</p>
</footer>
</body>
</html>""" % (META, STYLE, JSONLD, content_anchored, len(matches))

    io.open(FULL_OUT, 'w', encoding='utf-8', newline='').write(full_html)
    print('built seed.html %.2f MB | seed-full.html %.2f MB | entries %d' % (
        os.path.getsize(SEED_OUT) / 1048576.0, os.path.getsize(FULL_OUT) / 1048576.0, len(matches)))


def status():
    for p in (FULL_SRC, INDEX_SRC, SEED_OUT, FULL_OUT):
        print(os.path.basename(p), os.path.getsize(p) if os.path.exists(p) else 'MISSING')
    if os.path.exists(INDEX_SRC):
        print('index lines', sum(1 for _ in io.open(INDEX_SRC, encoding='utf-8')))


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else 'status'
    {'migrate': migrate, 'build': build, 'status': status}[cmd]()
