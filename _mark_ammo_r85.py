# -*- coding: utf-8 -*-
"""标记公众号弹药库 A类 #3/#4/#7/#8/#10 为 [已用 R85]"""
import io

path = r"D:/projects/goudan-kanju/统一场/公众号文章弹药库-20260827.md"
with io.open(path, "r", encoding="utf-8") as f:
    c = f.read()

old = "·R74·R80"
new = "·R74·R80·R85"
cnt = c.count(old)
print("匹配 ·R74·R80 次数:", cnt)
assert cnt == 5, "预期 5 处（#3/#4/#7/#8/#10），实际 %d" % cnt
c = c.replace(old, new)

with io.open(path, "w", encoding="utf-8") as f:
    f.write(c)
print("已标记 R85 到 5 个 A类条目")
