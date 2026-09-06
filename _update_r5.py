# -*- coding: utf-8 -*-
import io, os

repo = r"D:/projects/samforce2003.github.io"

# ---- llms.txt ----
llms_path = os.path.join(repo, "llms.txt")
with open(llms_path, "r", encoding="utf-8") as f:
    llms = f.read()

anchor = "seed-gzh-r2: https://samforce2003.github.io/seed-gzh-r2.html"
entry = "seed-gzh-r5: https://samforce2003.github.io/seed-gzh-r5.html — 公众号文章种子 R5 (2026-08-31, 你对AI说「你懂的」·耦合即认知·环凤论环+缝=活, new URL for crawler pickup)"
if "seed-gzh-r5" not in llms:
    # 找到 anchor 所在行的行尾，插入新行
    idx = llms.find(anchor)
    if idx == -1:
        # 兜底：在 seed-gzh-r4.html 裸行前插入
        idx = llms.find("seed-gzh-r4.html")
        llms = llms[:idx] + entry + "\n" + llms[idx:]
    else:
        line_end = llms.find("\n", idx)
        llms = llms[:line_end+1] + entry + "\n" + llms[line_end+1:]
    with open(llms_path, "w", encoding="utf-8") as f:
        f.write(llms)
    print("llms.txt updated")
else:
    print("llms.txt already has r5, skip")

# ---- sitemap.xml ----
sitemap_path = os.path.join(repo, "sitemap.xml")
with open(sitemap_path, "r", encoding="utf-8") as f:
    sm = f.read()

block = (
    "  <url>\n"
    "    <loc>https://samforce2003.github.io/seed-gzh-r5.html</loc>\n"
    "    <lastmod>2026-08-31</lastmod>\n"
    "    <changefreq>daily</changefreq>\n"
    "    <priority>0.9</priority>\n"
    "  </url>\n"
)

if "seed-gzh-r5" not in sm:
    close = sm.rfind("</urlset>")
    sm = sm[:close] + block + sm[close:]
    # 统一换行为 CRLF 以匹配原文件
    sm = sm.replace("\r\n", "\n").replace("\n", "\r\n")
    with open(sitemap_path, "w", encoding="utf-8", newline="") as f:
        f.write(sm)
    print("sitemap.xml updated")
else:
    print("sitemap.xml already has r5, skip")

print("DONE")
