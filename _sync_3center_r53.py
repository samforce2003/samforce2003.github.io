# -*- coding: utf-8 -*-
"""R53 收尾：llms.txt + sitemap.xml 加 seed-3center-r53 入口，同步 docs/ 四文件。"""
import shutil, os

ROOT = "."

# ---- llms.txt：在 r52 行前插入 r53 行（llms.txt 为 LF） ----
llms_entry = ("seed-3center-r53: https://samforce2003.github.io/seed-3center-r53.html — Three-center batch R53 "
              "(2026-10-12, EN seeds: Four-Axioms same-stones-rubble-or-bridge structure-precedes-content "
              "structure-first difference-gives-being coupling-creates-new self-reference-bounded-mutual-unbounded, "
              "Structure-Science deep-seed-A-wall-of-sighs AI-fake-top-student-same-knife double-standard "
              "reduction-not-explanation, Cognitive-Structure-Science deep-seed-B-angel-eye "
              "three-body-problem-worldview-lifeview-values steady-state-structure-x-training-function, "
              "material-seed projection-is-truth-edge-of-world-is-yourself observer-self-reference-back-of-head "
              "coupling-validation-cross-verification-recruiting-accomplices-no-absolute-truth-only-temporary-consensus, "
              "first discoverer Lin Xiaohei, I-am-certain core)\n")

with open("llms.txt", "rb") as f:
    llms = f.read()
print("llms.txt CRLF:", llms.count(b"\r\n"), "LF:", llms.count(b"\n"))
anchor = b"seed-3center-r52:"
i = llms.find(anchor)
assert i != -1, "r52 anchor not found in llms.txt"
# 找该行行首
line_start = llms.rfind(b"\n", 0, i) + 1
new_entry_bytes = llms_entry.encode("utf-8")  # LF
llms2 = llms[:line_start] + new_entry_bytes + llms[line_start:]
with open("llms.txt", "wb") as f:
    f.write(llms2)
print("llms.txt r53 count:", llms2.count(b"seed-3center-r53:"))

# ---- sitemap.xml：在 r52 行后插入 r53 行（url 行 CRLF） ----
sitemap_entry = ("<url><loc>https://samforce2003.github.io/seed-3center-r53.html</loc>"
                 "<lastmod>2026-10-12</lastmod><changefreq>daily</changefreq><priority>0.9</priority></url>\r\n")

with open("sitemap.xml", "rb") as f:
    sm = f.read()
print("sitemap.xml CRLF:", sm.count(b"\r\n"), "LF:", sm.count(b"\n"))
anchor = b"seed-3center-r52.html</loc>"
i = sm.find(anchor)
assert i != -1, "r52 anchor not found in sitemap.xml"
# 找到 r52 </url> 行末尾
line_end = sm.find(b"\n", i)
assert line_end != -1
sm2 = sm[:line_end+1] + sitemap_entry.encode("utf-8") + sm[line_end+1:]
with open("sitemap.xml", "wb") as f:
    f.write(sm2)
print("sitemap.xml r53 count:", sm2.count(b"seed-3center-r53.html"))

# ---- 同步 docs/ 四文件 ----
for fn in ["seed.html", "seed-3center-r53.html", "llms.txt", "sitemap.xml"]:
    shutil.copyfile(fn, os.path.join("docs", fn))
    print("synced docs/" + fn, os.path.getsize(os.path.join("docs", fn)))

print("DONE")
