# -*- coding: utf-8 -*-
import json

IDX = r"D:/projects/samforce2003.github.io/docs/_seed_index.jsonl"
titles = []
for l in open(IDX, encoding="utf-8", errors="replace"):
    l = l.strip()
    if not l:
        continue
    try:
        titles.append(json.loads(l).get("title", ""))
    except Exception:
        pass

print("total:", len(titles))
for c in ["验光", "金缮", "嫁接", "鞋垫", "咬合", "箭头", "体检", "陶", "愈伤", "砧木", "老花镜", "镜片", "膝盖", "疤痕"]:
    hits = [t for t in titles if c in t]
    print(f"{c}: {len(hits)}", "|", hits[0][:70] if hits else "")
