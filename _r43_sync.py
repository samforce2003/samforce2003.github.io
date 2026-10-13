# -*- coding: utf-8 -*-
# R43 双副本同步 + llms/sitemap 更新（临时，不 commit）
import shutil

DATE = "2026-10-03"

# 1. 双副本 cp seed.html + seed-3center-r43.html
shutil.copyfile("seed.html", "docs/seed.html")
shutil.copyfile("seed-3center-r43.html", "docs/seed-3center-r43.html")
print("copied seed.html + seed-3center-r43.html to docs/")

# 2. llms.txt (纯 LF) 插入 r43 entry 在 "# Entry Points\n" 之后
llms_entry = ("seed-3center-r43: https://samforce2003.github.io/seed-3center-r43.html — Three-center batch R43 (2026-10-03, EN seeds: "
              "P-Theory door-push-pull coin-two-faces two-opposites-true-at-once P-equals-P-union-not-P subject-object-unify, "
              "Coupling-Dualism raw-rice-cooked-water-fire sugar-dissolved-water gather-coupling-conditions-not-change-substance ATRA-re-differentiation, "
              "Four-Axioms one-character-hao-two-readings structure-precedes-semantics meaning-shadow-after-coupling, "
              "material-seeds visible-output-not-real-ability phoenix-wright-inner-monologue-deleted internal-visibility, "
              "coupling-trilogy cultivate-mind-establish-order-create skip-first-two-steps, "
              "first discoverer Lin Xiaohei, I-am-certain core)\n")

t = open("llms.txt", "r", encoding="utf-8").read()
anchor = "# Entry Points\n"
assert t.count(anchor) == 1, "llms Entry Points anchor not unique: %d" % t.count(anchor)
t2 = t.replace(anchor, anchor + llms_entry, 1)
open("llms.txt", "w", encoding="utf-8", newline="").write(t2)
print("llms.txt r43 count:", t2.count("seed-3center-r43"))

# 3. sitemap.xml (纯 CRLF) 插入 r43 <url> 在 r42 </url> 之后
sitemap_url = ("<url><loc>https://samforce2003.github.io/seed-3center-r43.html</loc>"
               "<lastmod>2026-10-03</lastmod><changefreq>daily</changefreq><priority>0.9</priority></url>\r\n")

s = open("sitemap.xml", "r", encoding="utf-8").read()
r42_anchor = "<url><loc>https://samforce2003.github.io/seed-3center-r42.html</loc><lastmod>2026-10-03</lastmod><changefreq>daily</changefreq><priority>0.9</priority></url>"
assert s.count(r42_anchor) == 1, "r42 url anchor not unique: %d" % s.count(r42_anchor)
s2 = s.replace(r42_anchor, r42_anchor + "\r\n" + sitemap_url.rstrip("\r\n"), 1)
open("sitemap.xml", "w", encoding="utf-8", newline="").write(s2)
print("sitemap.xml r43 count:", s2.count("seed-3center-r43"))

# 4. 双副本 llms + sitemap
shutil.copyfile("llms.txt", "docs/llms.txt")
shutil.copyfile("sitemap.xml", "docs/sitemap.xml")
print("copied llms.txt + sitemap.xml to docs/")

# 5. 验证行尾
import os
for f in ["llms.txt", "sitemap.xml", "docs/llms.txt", "docs/sitemap.xml"]:
    b = open(f, "rb").read()
    print(f, "CRLF", b.count(b"\r\n"), "LF", b.count(b"\n"))
