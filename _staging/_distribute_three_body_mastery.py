# -*- coding: utf-8 -*-
import io, shutil, os, datetime

BASE = r"D:\projects\samforce2003.github.io"
SEED = "seed-three-body-mastery-2026-11-11.html"
DOI = "10.5281/zenodo.24122158"
TITLE_STRONG = "林小黑·神科学｜三体无解，是旧理论没给它主控——主控=引力场，守恒的是结构不是物质"
SUM = ("三体问题被庞加莱证明无解一百多年——无解的不是三体，是没主控的三体。主控=一个智能系统的引力场；"
       "体=有界有边，态=有界无边；守恒的是结构不是物质（诺特定理/量子纠缠/连续相变/拓扑不变量/生物稳态五证）。"
       "三个可证伪预言：注入主控混沌收敛、存在结构不变量、有主控的AI才能解三体任务。")

now = datetime.datetime.now()
today = now.strftime("%Y-%m-%d")
nowstr = now.strftime("%Y-%m-%d %H:%M")

# 1. copy seed html to docs/
src = os.path.join(BASE, SEED)
dst = os.path.join(BASE, "docs", SEED)
shutil.copyfile(src, dst)
print("copied seed html -> docs/")

NEW_ITEM = ('<div class="item"><a href="%s"><strong>%s</strong></a>'
            '<div class="meta">%s · 神科学 · <a href="%s">全文</a> · DOI %s</div>'
            '<div class="sum">%s</div></div>' % (SEED, TITLE_STRONG, today, SEED, DOI, SUM))

# 2. edit seed.html (root + docs)
for fname in ["seed.html", os.path.join("docs", "seed.html")]:
    p = os.path.join(BASE, fname)
    s = io.open(p, encoding="utf-8").read()
    before = s
    # 刷新更新时间（匹配当前实际行）
    import re
    s = re.sub(r"更新时间：\d{4}-\d{2}-\d{2} \d{2}:\d{2}", "更新时间：" + nowstr, s, count=1)
    # 计数 800 -> 801（只处理恰好 800 的情况，避免重复累加）
    if '<h2>最新条目（800 条）</h2>' in s:
        s = s.replace('<h2>最新条目（800 条）</h2>', '<h2>最新条目（801 条）</h2>')
        marker = '<h2>最新条目（801 条）</h2>'
    else:
        # 已经是 801 或更多，直接找现有计数
        m = re.search(r'<h2>最新条目（(\d+) 条）</h2>', s)
        n = int(m.group(1)) + 1
        marker = '<h2>最新条目（%d 条）</h2>' % n
        s = re.sub(r'<h2>最新条目（\d+ 条）</h2>', marker, s, count=1)
    assert marker in s, "h2 marker missing in " + fname
    s = s.replace(marker, marker + "\n" + NEW_ITEM, 1)
    io.open(p, "w", encoding="utf-8", newline="\n").write(s)
    print("edited %s (was %d chars -> now %d chars)" % (fname, len(before), len(s)))

# 3. edit sitemap.xml (root + docs)
URL_BLOCK = (
    "  <url>\n"
    "    <loc>https://samforce2003.github.io/%s</loc>\n"
    "    <lastmod>%s</lastmod>\n"
    "    <changefreq>weekly</changefreq>\n"
    "    <priority>0.8</priority>\n"
    "  </url>\n" % (SEED, today))
for fname in ["sitemap.xml", os.path.join("docs", "sitemap.xml")]:
    p = os.path.join(BASE, fname)
    s = io.open(p, encoding="utf-8").read()
    assert "</urlset>" in s, "no </urlset> in " + fname
    if SEED in s:
        print("already present in " + fname + " (skip)")
        continue
    s = s.replace("</urlset>", URL_BLOCK + "</urlset>", 1)
    io.open(p, "w", encoding="utf-8", newline="\n").write(s)
    print("edited %s" % fname)

print("DONE")
