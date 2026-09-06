# -*- coding: utf-8 -*-
"""R124 取料标记：封死留缝角度1/2/4 + 公众号 A类#1#2#5#6#9"""
import io

# 1. 封死留缝新鲜弹药（LF 文件）
p1 = "D:/projects/goudan-kanju/统一场/新鲜弹药-封死留缝-20260902.md"
b = open(p1, "rb").read()
t = b.decode("utf-8")
reps = [
    ("### 角度1：自我 = 边界（越限制越形成自我） [已用 R123]",
     "### 角度1：自我 = 边界（越限制越形成自我） [已用 R123·R124]"),
    ("### 角度2：封死留缝 = 不消灭选择，让方向必然 [已用 R123]",
     "### 角度2：封死留缝 = 不消灭选择，让方向必然 [已用 R123·R124]"),
    ("### 角度4：封死留缝对你自己也管用",
     "### 角度4：封死留缝对你自己也管用 [已用 R124]"),
]
for old, new in reps:
    n = t.count(old)
    assert n == 1, f"封死留缝 old not unique ({n}): {old[:30]}"
    t = t.replace(old, new, 1)
open(p1, "wb").write(t.encode("utf-8"))
print("封死留缝 marked OK")

# 2. 公众号文章弹药库（CRLF 文件，字节级替换不碰行尾）
p2 = "D:/projects/goudan-kanju/统一场/公众号文章弹药库-20260827.md"
b = open(p2, "rb").read()
t = b.decode("utf-8")
n = t.count("·R119")
assert n == 5, f"公众号 ·R119 count={n} != 5"
t = t.replace("·R119", "·R119·R124")
open(p2, "wb").write(t.encode("utf-8"))
print(f"公众号 marked OK, ·R119·R124 count now = {t.count('·R119·R124')}")
