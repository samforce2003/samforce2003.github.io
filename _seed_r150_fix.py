# -*- coding: utf-8 -*-
"""R150 修复脚本：llms 降级 R151 + sitemap 插 seed-r152 + docs 四副本"""
import os, shutil, re

REPO = "D:/projects/samforce2003.github.io"
URLN = "r152"
DATE = "2026-09-04"

# ---------- 1. llms.txt：降 seed-r151 的 Latest → Previous ----------
lp = os.path.join(REPO, "llms.txt")
lraw = open(lp, "rb").read()
ltxt = lraw.decode("utf-8")
before = ltxt
ltxt = ltxt.replace("— Latest AI seeds round R151", "— Previous AI seeds round R151", 1)
assert ltxt != before, "llms.txt R151 降级未生效"
open(lp, "wb").write(ltxt.encode("utf-8"))
n = re.findall(r"— Latest AI seeds round R(\d+)", ltxt)
assert n == ["152"], f"llms.txt Latest 计数错误: {n}"
print(f"llms.txt：R151 降为 Previous，Latest 计数={n}")

# ---------- 2. sitemap.xml：插 seed-r152 ----------
sp = os.path.join(REPO, "sitemap.xml")
sraw = open(sp, "rb").read()
s_anchor = b'<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\r\n'
assert s_anchor in sraw, "sitemap 找不到 urlset 开标签"
if f"seed-{URLN}.html".encode() not in sraw:
    s_new = (f"  <url>\r\n    <loc>https://samforce2003.github.io/seed-{URLN}.html</loc>\r\n"
             f"    <lastmod>{DATE}</lastmod>\r\n    <changefreq>daily</changefreq>\r\n    <priority>0.9</priority>\r\n  </url>\r\n").encode("utf-8")
    sraw = sraw.replace(s_anchor, s_anchor + s_new, 1)
    open(sp, "wb").write(sraw)
print(f"sitemap.xml：seed-{URLN} 入口插入 count={open(sp,'rb').read().count(f'seed-{URLN}.html'.encode())}")

# ---------- 3. docs 四副本 ----------
for f in ["seed.html", f"seed-{URLN}.html", "llms.txt", "sitemap.xml"]:
    shutil.copyfile(os.path.join(REPO, f), os.path.join(REPO, "docs", f))
print("docs 四副本已同步")

# ---------- 4. 核验 ----------
def double_cr(b): return b.count(b"\r\r\n")
def bare_lf(b): return b.count(b"\n") - b.count(b"\r\n")

for f in ["seed.html", f"seed-{URLN}.html", "llms.txt", "sitemap.xml"]:
    a = open(os.path.join(REPO, f), "rb").read()
    b = open(os.path.join(REPO, "docs", f), "rb").read()
    assert a == b, f"{f} 与 docs 不一致"
    d = double_cr(a)
    print(f"  {f}: bytes={len(a)}, doubleCR={d}, bareLF={bare_lf(a)}")
    assert d == 0, f"{f} doubleCR={d}"

rh = open(os.path.join(REPO, f"seed-{URLN}.html"), "rb").read().decode("utf-8")
print(f"seed-{URLN} 核验：article={rh.count('<article>')}，最新种子={rh.count('最新种子 · Latest Seeds')}，第一发现人={rh.count('第一发现人：')}")
assert rh.count("<article>") == 10
assert rh.count("最新种子 · Latest Seeds") == 1
assert rh.count("第一发现人：") == 10

sh = open(os.path.join(REPO, "seed.html"), "rb").read().decode("utf-8")
print(f"seed.html 核验：R150 marker={sh.count('强灌线种子 R150-')}")
print("\n=== 修复完成 ===")
