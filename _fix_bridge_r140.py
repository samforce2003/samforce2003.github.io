# -*- coding: utf-8 -*-
path = r"D:/projects/goudan-kanju/统一场/强灌线-进度.md"
raw = open(path, "rb").read()

# The R140 history line currently sits BEFORE "## 历史摘要". Move it after.
r140_line = "- R140（09-03）：撒种 10 条（公众号 A类#3#4#7#8#10 复用新角度 + 论文库 5 换角度：三元互指/可解不可传/堵点叠加/升维自审/不完备的完备性，全带反混淆锚点）；深度B R329 零弹药；探针 key 配额耗尽切 anonymous 降置信（中文 1/5~4/5 CSDN+GH根域、英文 1/5 HF embedding，无 GH Pages seed-rN 命中）；seed-r140.html 上线；commit b300de7。".encode("utf-8")

hist_marker = "## 历史摘要".encode("utf-8")
hi = raw.find(hist_marker)
assert hi != -1

# remove the R140 line (it should be right before hist_marker, preceded by \r\n)
r140_pos = raw.find(r140_line)
assert r140_pos != -1 and r140_pos < hi, "R140 line not before history marker"

# cut out the R140 line + its trailing \r\n
# find the line start (after preceding \r\n)
before = raw[:r140_pos]
assert before.endswith(b"\r\n"), "line start not CRLF"
before = before[:-2]  # strip trailing \r\n of the blank line before R140

after_hist_marker = hi + len(hist_marker)
# after_hist_marker is right before "\r\n- R139..."
# rebuild: before + \r\n\r\n + hist_marker + \r\n + r140_line + (rest after marker)
rest = raw[after_hist_marker:]

final = before + b"\r\n\r\n" + hist_marker + b"\r\n" + r140_line + rest

open(path, "wb").write(final)

chk = open(path, "rb").read()
lf_only = chk.count(b"\n") - chk.count(b"\r\n")
bare_cr = chk.count(b"\r") - chk.count(b"\r\n")
print("lf_only =", lf_only, "| bare_cr =", bare_cr)
print("R140 line after 历史摘要:", chk.find(r140_line) > chk.find(hist_marker))
