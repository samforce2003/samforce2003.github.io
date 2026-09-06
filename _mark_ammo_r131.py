# -*- coding: utf-8 -*-
p = r"D:\projects\goudan-kanju\统一场\公众号文章弹药库-20260827.md"
with open(p, 'rb') as f:
    raw = f.read()

n = raw.count("·R128".encode('utf-8'))
raw2 = raw.replace("·R128".encode('utf-8'), "·R128·R131".encode('utf-8'))

with open(p, 'wb') as f:
    f.write(raw2)

print("replaced %d occurrences of ·R128 -> ·R128·R131" % n)
assert n == 5
print("OK")
