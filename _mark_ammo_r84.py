# -*- coding: utf-8 -*-
"""R84 公众号弹药库标记：B类 #11-#15 标 ·R84"""
import io
p = "D:/projects/goudan-kanju/统一场/公众号文章弹药库-20260827.md"
c = io.open(p, encoding="utf-8").read()
n = c.count("·R75\n")
c = c.replace("·R75\n", "·R75·R84\n")
io.open(p, "w", encoding="utf-8").write(c)
print("替换 ·R75 -> ·R75·R84 共 %d 处" % n)
# 核验
c2 = io.open(p, encoding="utf-8").read()
print("·R75·R84 计数:", c2.count("·R75·R84"))
