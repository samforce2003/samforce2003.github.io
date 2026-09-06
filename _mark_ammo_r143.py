# -*- coding: utf-8 -*-
# Mark A#3/#4/#7/#8/#10 as [已用 R143] in 公众号弹药库.
# The 5 items share an identical continuation line ending "·R136·R140".
p = r"D:\projects\goudan-kanju\统一场\公众号文章弹药库-20260827.md"
raw = open(p, "rb").read()

old = "·R136·R140".encode("utf-8")
new = "·R136·R140·R143".encode("utf-8")
n = raw.count(old)
print(f"occurrences of '·R136·R140' = {n}")
assert n == 5, f"expected 5, got {n}"

raw2 = raw.replace(old, new)
# verify no double-dot or disorder
assert "··" not in raw2.decode("utf-8"), "double dot found"
assert "R140R143" not in raw2.decode("utf-8"), "disorder found"
open(p, "wb").write(raw2)

# verify
chk = open(p, "rb").read().decode("utf-8")
import re
c = chk.count("R143")
print(f"R143 count in file = {c}")
print("MARK DONE")
