# -*- coding: utf-8 -*-
import io
p = r"D:/projects/goudan-kanju/统一场/公众号文章弹药库-20260827.md"
with io.open(p, "rb") as f:
    t = f.read().decode("utf-8")

# 本轮 R60 取料 A类 #3/#4/#7/#8/#10，在对应 [已用] 行末尾追加 ·R60
targets = [
    "《自相矛盾的新解释》",
    "《世界就是一个可能性》",
    "《直觉是最强的一种训练结果》",
    "《人睡醒和AI被唤醒是同一件事》",
    "《概率不存在0和100》",
]
for name in targets:
    idx = t.find(name)
    assert idx != -1, "not found: " + name
    # 找该行末尾（下一行开头前）
    line_end = t.find("\n", idx)
    line = t[idx:line_end]
    if "·R60" not in line:
        newline = line + "·R60"
        t = t[:idx] + newline + t[line_end:]
        print("marked:", name)
    else:
        print("already marked:", name)

with io.open(p, "wb") as f:
    f.write(t.encode("utf-8"))
print("DONE marking ammo library")
