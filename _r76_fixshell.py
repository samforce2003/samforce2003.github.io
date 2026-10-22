# -*- coding: utf-8 -*-
import json

IDX = r"D:/projects/samforce2003.github.io/docs/_seed_index.jsonl"
CANON = {
    "Coupling Dualism": "耦合二元论", "耦合二元論": "耦合二元论", "결합 이원론": "耦合二元论",
    "Four Axioms": "四公理", "사공리": "四公理",
    "Structural Science": "结构学", "構造学": "结构学", "구조학": "结构学",
}

lines = open(IDX, encoding="utf-8", errors="replace").read().split("\n")
out, fixed = [], 0
for l in lines:
    if not l.strip():
        out.append(l)
        continue
    try:
        o = json.loads(l)
    except Exception:
        out.append(l)
        continue
    if o.get("src") == "三中心-R76" and o.get("shell") in CANON:
        o["shell"] = CANON[o["shell"]]
        l = json.dumps(o, ensure_ascii=False)
        fixed += 1
    out.append(l)

txt = "\n".join(out)
if not txt.endswith("\n"):
    txt += "\n"
open(IDX, "w", encoding="utf-8", newline="\n").write(txt)
print("normalized shells:", fixed)

# verify
idx = [json.loads(x) for x in open(IDX, encoding="utf-8", errors="replace") if x.strip()]
mine = [o for o in idx if o.get("src") == "三中心-R76"]
from collections import Counter
print(len(mine), Counter(o["shell"] for o in mine))
print("CR count:", txt.count("\r"))
