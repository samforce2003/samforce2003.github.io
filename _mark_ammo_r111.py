# -*- coding: utf-8 -*-
import io

p = r"D:\projects\goudan-kanju\统一场\公众号文章弹药库-20260827.md"
with io.open(p, 'r', encoding='utf-8') as f:
    lines = f.readlines()

titles = ["量化模型越庞大", "越努力错得越远", "过拟合是一个假命题", "时间不是一条河", "身体和心是一个系统"]
changed = 0
for i, line in enumerate(lines):
    for t in titles:
        if t in line and "已用" in line and not line.rstrip().endswith("R111"):
            # append ·R111 to end (before newline)
            lines[i] = line.rstrip("\r\n") + "·R111" + ("\r\n" if line.endswith("\r\n") else "\n")
            changed += 1
            break

with io.open(p, 'w', encoding='utf-8', newline='') as f:
    f.writelines(lines)

print(f"marked {changed}/5 ammo entries with ·R111")
