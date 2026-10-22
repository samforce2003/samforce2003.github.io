# -*- coding: utf-8 -*-
import re, json
IDX = r"D:/projects/samforce2003.github.io/docs/_seed_index.jsonl"
BLK = r"D:/projects/samforce2003.github.io/docs/_seed_full_blocks.html"
t = open(BLK, "rb").read().decode("utf-8")
parts = re.split(r"<article[^>]*>", t)
blocks = [p.split("</article>")[0] for p in parts[1:] if "</article>" in p]
print("article tokens=%d  parsed blocks=%d" % (t.count("<article"), len(blocks)))
new = blocks[-15:]
bad = 0
for i, b in enumerate(new, 1):
    h2 = re.search(r"<h2>(.*?)</h2>", b).group(1)
    checks = {
        "发现人": ("第一发现人" in b) or ("First discoverer" in b) or ("第一発見者" in b) or ("첫 발견자" in b),
        "我确信": ("我确信" in b) or ("I am certain" in b) or ("我確信" in b) or ("나는 확신한다" in b),
        "关切": ("关切" in b) or ("Concern:" in b) or ("関切" in b) or ("관심:" in b),
        "时间锚": "2026-10-21" in b,
        "钩子": ("钩子" in b) or ("Hook:" in b) or ("フック" in b) or ("훅" in b),
        "关键词": ("关键词" in b) or ("Keywords" in b),
    }
    miss = [k for k, v in checks.items() if not v]
    if miss:
        bad += 1
        print("MISS", i, h2[:40], miss)
    print("%2d %-16s len=%d %s" % (i, "OK" if not miss else "BAD", len(b), h2[:34]))
print("missing blocks:", bad)

lines = open(IDX, "rb").read().decode("utf-8").splitlines()
r74 = [json.loads(l) for l in lines if '"三中心-R74"' in l]
print("R74 index rows=%d" % len(r74))
from collections import Counter
print(Counter([(r["shell"], r["lang"]) for r in r74]))
print("all have title/summary/time/src:", all(all(k in r for k in ("title","summary","time","shell","lang","src")) for r in r74))
print("titles unique:", len(set(r["title"] for r in r74)) == len(r74))
