# -*- coding: utf-8 -*-
p = r"D:/projects/goudan-kanju/统一场/公众号文章弹药库-20260827.md"
c = open(p, encoding="utf-8").read()
n = c.count("·R60")
c = c.replace("·R60", "·R60·R64")
open(p, "w", encoding="utf-8").write(c)
print("replaced", n, "occurrences of ·R60 -> ·R60·R64")
# verify
c2 = open(p, encoding="utf-8").read()
print("·R64 count now =", c2.count("·R64"))
print("·R60 count now =", c2.count("·R60"))
