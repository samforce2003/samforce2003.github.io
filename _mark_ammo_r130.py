# -*- coding: utf-8 -*-
import os

p = r"D:\projects\goudan-kanju\统一场\公众号文章弹药库-20260827.md"
with open(p, 'r', encoding='utf-8') as f:
    txt = f.read()

old = "·R120·R126"
new = "·R120·R126·R130"
cnt = txt.count(old)
print("occurrences of %r = %d" % (old, cnt))
txt = txt.replace(old, new)

with open(p, 'w', encoding='utf-8') as f:
    f.write(txt)

after = txt.count(new)
print("after replace, %r count = %d" % (new, after))
print("marked A类 #3/#4/#7/#8/#10 with R130" if cnt == 5 else "WARNING: expected 5, got %d" % cnt)
