# -*- coding: utf-8 -*-
import json, re, os
ROOT = r"D:/projects/samforce2003.github.io"
IDX = os.path.join(ROOT, "docs/_seed_index.jsonl")
BLK = os.path.join(ROOT, "docs/_seed_full_blocks.html")

raw = open(IDX, "rb").read().decode("utf-8", "replace")
lines = [l for l in raw.split("\n") if l.strip()]
objs = []
bad = 0
for l in lines:
    try:
        objs.append(json.loads(l))
    except Exception:
        bad += 1
print("index lines:", len(lines), "parse_fail:", bad)
r75 = [o for o in objs if o.get("src") == "三中心-R75"]
print("R75 entries:", len(r75))
titles = [o["title"] for o in r75]
print("R75 unique titles:", len(set(titles)))
print("R75 langs:", {l: sum(1 for o in r75 if o.get("lang") == l) for l in ["zh", "en", "ja", "ko"]})
print("R75 shells:", sorted(set(o.get("shell") for o in r75)))
print("R75 with id field:", sum(1 for o in r75 if o.get("id")))
print("last index line:", lines[-1][:120])

bt = open(BLK, "rb").read().decode("utf-8", "replace")
print("article tokens:", bt.count("<article"))
parts = re.split(r"<article[^>]*>", bt)
blks = [p for p in parts[1:] if "</article>" in p]
print("parsed blocks:", len(blks))
print("CRCR in file:", bt.count("\r\r"))

need = ["第一发现人", "我确信", "关切", "时间锚", "钩子", "关键词"]
miss = 0
for b in blks[-15:]:
    body = b.split("</article>")[0]
    for n in need:
        if n not in body:
            print("MISSING", n, "in", body[:60])
            miss += 1
print("last15 missing items:", miss)
print("last15 all 2026-10-22:", sum(1 for b in blks[-15:] if "2026-10-22" in b))
print("last block tail:", repr(blks[-1][-260:]))
