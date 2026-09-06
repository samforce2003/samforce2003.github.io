# -*- coding: utf-8 -*-
"""R114 标记公众号弹药库 [已用] —— A类#1#2#5#6#9 追加 ·R114"""
p = r"D:\projects\goudan-kanju\统一场\公众号文章弹药库-20260827.md"
with open(p, "rb") as f:
    raw = f.read()

old = "·R103·R108·R111".encode("utf-8")
new = "·R103·R108·R111·R114".encode("utf-8")
cnt = raw.count(old)
assert cnt == 5, f"expected 5 occurrences, got {cnt}"
raw = raw.replace(old, new)

with open(p, "wb") as f:
    f.write(raw)
print(f"marked: {cnt} entries appended ·R114 (A类#1#2#5#6#9)")
