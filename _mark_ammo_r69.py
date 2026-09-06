# -*- coding: utf-8 -*-
# 标记公众号文章弹药库 B类 #11-#15 已用 R69
import io

path = r"D:\projects\goudan-kanju\统一场\公众号文章弹药库-20260827.md"
with io.open(path, "rb") as f:
    raw = f.read()
text = raw.decode("utf-8")

# 每条 B类 末尾是 ·R66，替换为 ·R66·R69
before = text.count("·R66")
text = text.replace("·R66", "·R66·R69")
after = text.count("·R66·R69")

with io.open(path, "wb") as f:
    f.write(text.encode("utf-8"))
print("marked: replaced %d occurrences of ·R66 -> ·R66·R69 (now %d)" % (before, after))
