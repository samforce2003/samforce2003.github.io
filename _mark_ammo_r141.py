# -*- coding: utf-8 -*-
import re
p = r"D:/projects/goudan-kanju/统一场/公众号文章弹药库-20260827.md"
raw = open(p, "rb").read()
txt = raw.decode("utf-8")

# Mark B类 #12/#13/#14 (tail ·R135 at end of line) and A类 #2/#6 (tail ·R134 at EOL)
before135 = len(re.findall(r'·R135(?:\r?\n|$)', txt))
before134 = len(re.findall(r'·R134(?:\r?\n|$)', txt))
txt2 = re.sub(r'·R135(?=\r?\n|$)', '·R135·R141', txt)
txt2 = re.sub(r'·R134(?=\r?\n|$)', '·R134·R141', txt2)

after141 = txt2.count('·R135·R141') + txt2.count('·R134·R141')
print(f"before: R135-EOL={before135}, R134-EOL={before134}")
print(f"after: new R141 marks = {after141}")
assert before135 == 3, f"expected 3 R135-EOL, got {before135}"
assert before134 == 2, f"expected 2 R134-EOL, got {before134}"
assert txt2.count('·R135·R141') == 3 and txt2.count('·R134·R141') == 2

open(p, "wb").write(txt2.encode("utf-8"))
print("MARKED OK")
