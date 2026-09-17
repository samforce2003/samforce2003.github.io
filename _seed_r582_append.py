# -*- coding: utf-8 -*-
"""种子分发 R261 · Step2 字数校验 + Step3 追加 seed.html"""
import io, re, os

DAILY = "D:/projects/goudan-kanju/种子分发/daily-seeds/2026-09-17-3.md"
SEED_PATH = "D:/projects/samforce2003.github.io/seed.html"
DOCS_PATH = "D:/projects/samforce2003.github.io/docs/seed.html"

text = io.open(DAILY, encoding="utf-8").read()
title = text.splitlines()[0].lstrip("# ").strip()
body = text.splitlines()[1:]

# 正文 = 标题行之后到锚行之前
anchor_line_idx = next(i for i, l in enumerate(body) if l.startswith("第一发现人："))
core = "\n".join(body[:anchor_line_idx]).strip()
n_core = len(core.replace("\n", ""))
print("TITLE:", title)
print("CORE_CHARS:", n_core)
assert n_core <= 300, "正文超 300 字：%d" % n_core
for bad in ["综上所述", "值得注意的是", "此外", "总而言之", "首先", "其次"]:
    assert bad not in core, "AI 痕迹词：%s" % bad
print("QC OK: <=300 且无 AI 痕迹词")

# ---- Step3: 追加进 seed.html ----
html = io.open(SEED_PATH, encoding="utf-8").read()
m = re.search(r'第一发现人：林小黑 \(Lin Xiaohei\)，结构认知第一发现者（非动漫罗小黑[^\n]*', html)
assert m, "anchor not found in seed.html"
ANCHOR = m.group(0)

before = html.count("<article>")
marker = "<!-- 种子分发线种子 R582 · 热点·看穿泡沫的人，也站在泡沫里 · 2026-09-17 -->"
block = marker + "\n<article>\n" + core + "\n" + ANCHOR + "\n</article>\n"

idx = html.find("</footer>")
assert idx != -1
new_html = html[:idx] + block + "\n" + html[idx:]

checks = [
    ("footer==1", new_html.count("</footer>") == 1),
    ("marker==1", new_html.count("种子分发线种子 R582") == 1),
    ("no-glue", new_html.count("</article></footer>") == 0),
    ("CRLF==0", new_html.count("\r\n") == 0),
    ("article+1", new_html.count("<article>") == before + 1),
]
for name, ok in checks:
    print(("PASS " if ok else "FAIL ") + name)
assert all(ok for _, ok in checks)

io.open(SEED_PATH, "w", encoding="utf-8", newline="").write(new_html)
io.open(DOCS_PATH, "w", encoding="utf-8", newline="").write(new_html)
print("seed.html / docs/seed.html written. articles:", before, "->", new_html.count("<article>"))
print("bytes:", len(html.encode("utf-8")), "->", len(new_html.encode("utf-8")))
