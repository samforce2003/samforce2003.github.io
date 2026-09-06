# -*- coding: utf-8 -*-
p = r"D:/projects/goudan-kanju/统一场/公众号文章弹药库-20260827.md"
raw = open(p, "rb").read()
txt = raw.decode("utf-8")
lines = txt.split("\r\n")
targets = ["量化模型越庞大，死得越快", "越努力错得越远", "过拟合是一个假命题", "时间不是一条河是你的节奏", "身体和心是一个系统"]
done = 0
for i, l in enumerate(lines):
    for tg in targets:
        if tg in l and "[已用" in l and "·R145" not in l:
            lines[i] = l + "·R145"
            done += 1
            break
out = "\r\n".join(lines)
open(p, "wb").write(out.encode("utf-8"))

# verify
chk = open(p, "rb").read().decode("utf-8")
print("marked:", done)
print("R145 occurrences:", chk.count("·R145"))
print("double-dot:", chk.count("··"))
# check no乱序: R145 should come after R142/R141, never before
import re
for m in re.finditer(r'·R14[0-9]·R145', chk):
    print("ok seq:", m.group(0))
print("bad seq R145R14x:", len(re.findall(r'R145·R14', chk)))
