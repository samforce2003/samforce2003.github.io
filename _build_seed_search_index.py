# -*- coding: utf-8 -*-
"""生成 docs/_seed_search_data.json —— 供 docs/seed-search.html 前端检索
id 补齐逻辑与 _build_seed_two_layer.load_index 完全一致（max+1 递增补），
保证检索结果能跳到 seed-full.html#s{id} 的正确锚点。
"""
import io, os, json

BASE = r"D:/projects/samforce2003.github.io"
IDX = os.path.join(BASE, "docs", "_seed_index.jsonl")
OUT = os.path.join(BASE, "docs", "_seed_search_data.json")

recs = []
with io.open(IDX, encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if line:
            recs.append(json.loads(line))

mx = 0
for r in recs:
    try:
        mx = max(mx, int(r.get("id") or 0))
    except Exception:
        pass
nxt = mx + 1
for r in recs:
    if not r.get("id"):
        r["id"] = nxt
        nxt += 1

rows = []
for r in recs:
    rows.append({
        "i": int(r["id"]),
        "t": (r.get("title") or "")[:120],
        "s": (r.get("summary") or "")[:90],
        "d": r.get("time") or "",
        "h": r.get("shell") or "",
        "l": r.get("lang") or "zh",
    })

with io.open(OUT, "w", encoding="utf-8", newline="") as f:
    json.dump(rows, f, ensure_ascii=False, separators=(",", ":"))

print("search data:", len(rows), "rows,", round(os.path.getsize(OUT) / 1048576.0, 2), "MB")
print("last id:", rows[-1]["i"], "| last title:", rows[-1]["t"][:40])
