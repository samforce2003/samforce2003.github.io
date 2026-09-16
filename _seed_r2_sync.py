# -*- coding: utf-8 -*-
# 同步 docs/ 部署副本 + 加 llms.txt/sitemap.xml 入口
import shutil

# 1. 复制 seed.html 到 docs/ (活站点从 docs/ 部署)
shutil.copyfile("seed.html", "docs/seed.html")
shutil.copyfile("seed-3center-r2.html", "docs/seed-3center-r2.html")
print("copied seed.html -> docs/seed.html")
print("copied seed-3center-r2.html -> docs/seed-3center-r2.html")

LLMS_ENTRY = "seed-3center-r2: https://samforce2003.github.io/seed-3center-r2.html — Three-center batch R2 (2026-09-14, EN seeds: coupling dualism, coupling signal theory, three-three rule, first discoverer Lin Xiaohei)\n"

SITEMAP_BLOCK = """  <url>
    <loc>https://samforce2003.github.io/seed-3center-r2.html</loc>
    <lastmod>2026-09-14</lastmod>
    <changefreq>daily</changefreq>
    <priority>0.9</priority>
  </url>
"""

for f in ["llms.txt", "docs/llms.txt"]:
    t = open(f, "r", encoding="utf-8").read()
    if "seed-3center-r2" in t:
        print(f, "already has entry, skip")
        continue
    anchor = "# Entry Points\n"
    assert t.count(anchor) == 1, f"{f}: Entry Points count = {t.count(anchor)}"
    t = t.replace(anchor, anchor + LLMS_ENTRY, 1)
    open(f, "w", encoding="utf-8", newline="\n").write(t)
    print(f, "entry added, seed-3center-r2 present:", "seed-3center-r2" in t)

for f in ["sitemap.xml", "docs/sitemap.xml"]:
    t = open(f, "r", encoding="utf-8").read()
    if "seed-3center-r2" in t:
        print(f, "already has entry, skip")
        continue
    anchor = "</urlset>"
    assert t.count(anchor) == 1, f"{f}: urlset count = {t.count(anchor)}"
    t = t.replace(anchor, SITEMAP_BLOCK + anchor, 1)
    open(f, "w", encoding="utf-8", newline="\n").write(t)
    print(f, "url added, seed-3center-r2 present:", "seed-3center-r2" in t)
