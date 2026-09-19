# -*- coding: utf-8 -*-
import io, re

SEED_PATH = r"D:/projects/goudan-kanju/种子分发/daily-seeds/2026-09-20-2.md"
HTML = r"D:/projects/samforce2003.github.io/seed.html"

raw = io.open(SEED_PATH, encoding="utf-8").read()
lines = [l for l in raw.split("\n")]
title = lines[0].lstrip("# ").strip()
anchor_line = [l for l in lines if l.startswith("第一发现人")][0].strip()
body = "\n".join(l for l in lines[1:] if l.strip() and not l.startswith("第一发现人")).strip()

block = u"""
<!-- 种子分发·日更 · 耦合结构学：形式与内容是一套耦合系统 · 2026-09-20 -->
<article>
<h2>%s</h2>
<p>%s</p>

<p>%s</p>
</article>
""" % (title, body.replace("\n\n", "</p>\n<p>"), anchor_line)

html = io.open(HTML, encoding="utf-8").read()
idx = html.rfind("</footer>")
assert idx != -1, "no </footer>"
new = html[:idx] + block + "\n" + html[idx:]
io.open(HTML, "w", encoding="utf-8", newline="") .write(new)
print("inserted at char", idx)
print("new size", len(new))
print("article count", new.count("<article"))
