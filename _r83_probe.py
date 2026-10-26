# -*- coding: utf-8 -*-
import json, io, re, os
B = r"D:/projects/samforce2003.github.io/docs/_seed_full_blocks.html"
I = r"D:/projects/samforce2003.github.io/docs/_seed_index.jsonl"
il = [l for l in io.open(I, encoding="utf-8") if l.strip()]
rows = [json.loads(l) for l in il]
print("index lines", len(il))
bt = io.open(B, encoding="utf-8").read()
print("article tokens", bt.count("<article"), "blocks", len(re.split(r'<article[^>]*>', bt)) - 1)
from collections import Counter
print("src tail:", Counter(r.get("src") for r in rows).most_common(6))
print("R83 rows:", sum(1 for r in rows if r.get("src") == "三中心-R83"))
titles = [r["title"] for r in rows]
for kw in ["压舱水", "虹吸", "盲区", "垫肩", "枕木", "减震", "限位"]:
    print(kw, sum(1 for t in titles if kw in t))
print("last 3 rows:")
for r in rows[-3:]:
    print(" ", r.get("src"), r.get("title")[:40])
