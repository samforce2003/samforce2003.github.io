# -*- coding: utf-8 -*-
import io, shutil, os, datetime

BASE = r"D:\projects\samforce2003.github.io"
SEED = "seed-universe-is-a-loop-2026-11-11.html"
DOI = "10.5281/zenodo.24046294"
TITLE_STRONG = "林小黑·神科学｜宇宙是个环——起点就是终点：变是转出来的，起点即终点"
SUM = ("几百年人把宇宙想成一条线，越追问题越多：暗物质/暗能量/加速膨胀都没人知道。本文提出：不是追得不够远，"
       "是追错了一条路——宇宙不是线，是环，变不是走出来的、是转出来的（身体里两条链：管不变+管变，缠着转，"
       "转一圈不变转成变、再转一圈变转成不变），环的起点就是终点，一个点锁死整个环。落到天上：2024 天文学家"
       "发现的大环（Big Ring）直径 13 亿光年，越过旧理论均匀性上限，是环的痕迹。两个可证伪预言：新一代巡天"
       "会找到更多环状结构；暗能量状态方程 w 不等于 -1、随时间漂。")

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
import re
for fname in ["seed.html", os.path.join("docs", "seed.html")]:
    p = os.path.join(BASE, fname)
    s = io.open(p, encoding="utf-8").read()
    before = s
    # 刷新更新时间
    s = re.sub(r"更新时间：\d{4}-\d{2}-\d{2} \d{2}:\d{2}", "更新时间：" + nowstr, s, count=1)
    # 计数 801 -> 802（动态取当前值 +1）
    m = re.search(r'<h2>最新条目（(\d+) 条）</h2>', s)
    if m is None:
        raise SystemExit("no counter in " + fname)
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
