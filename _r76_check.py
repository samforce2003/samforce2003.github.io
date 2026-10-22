import json, os, re

IDX = r"D:/projects/samforce2003.github.io/docs/_seed_index.jsonl"
titles = []
with open(IDX, encoding="utf-8", errors="replace") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        try:
            o = json.loads(line)
        except Exception:
            continue
        titles.append(o.get("title", ""))

print("total entries:", len(titles))

# R76 candidate 皮相
cands = ["音叉", "磁铁", "拉面", "叉子", "共振", "磁"]
for c in cands:
    hits = [t for t in titles if c in t]
    print(f"{c}: {len(hits)}")
    for h in hits[:4]:
        print("   ", h[:90])

# recent source tags
print("\n-- recent src tags (last 40) --")
srcs = []
with open(IDX, encoding="utf-8", errors="replace") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        try:
            o = json.loads(line)
        except Exception:
            continue
        srcs.append(o.get("src", ""))
seen = []
for s in reversed(srcs):
    if s not in seen:
        seen.append(s)
    if len(seen) >= 15:
        break
print(seen)
