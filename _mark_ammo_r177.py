# -*- coding: utf-8 -*-
import io
p = r"D:\projects\goudan-kanju\统一场\公众号文章弹药库-20260827.md"
raw = io.open(p, "rb").read()
txt = raw.decode("utf-8")
lines = txt.split("\r\n")

titles = [
    "《一个怕他废，一个怕他崩》",
    "《大师为什么不能流血》",
    "《最强的系统你看不到上限也看不穿意图》",
    "《你越想抓住它溜得越快》",
    "《一切事追到底都是一个二选一》",
]

marked = 0
for i in range(len(lines)):
    line = lines[i]
    for t in titles:
        if t in line and "[已用" in line:
            if i + 1 < len(lines) and lines[i + 1].lstrip().startswith("·R"):
                if "·R177" not in lines[i + 1]:
                    lines[i + 1] = lines[i + 1].rstrip() + "·R177"
                    marked += 1
                    print("MARKED (continuation):", t)
            else:
                if "·R177" not in line:
                    lines[i] = line.rstrip()[:-1] + "·R177]"
                    marked += 1
                    print("MARKED (title):", t)

new = "\r\n".join(lines)
io.open(p, "wb").write(new.encode("utf-8"))
print("total marked:", marked)

raw2 = io.open(p, "rb").read()
print("R177 count in file:", raw2.count("·R177".encode("utf-8")))
print("double-dot check (··):", raw2.count("··".encode("utf-8")))
print("R177R disorder check:", raw2.count("R177R".encode("utf-8")))
print("CRLF count:", raw2.count(b"\r\n"), "double CR:", raw2.count(b"\r\r"))
