# -*- coding: utf-8 -*-
"""标记公众号弹药库 A类 #1#2#5#6#9 为 [已用 R127]"""
import io

P = r"D:\projects\goudan-kanju\统一场\公众号文章弹药库-20260827.md"
titles = [
    "《量化模型越庞大，死得越快》",
    "《越努力错得越远》",
    "《过拟合是一个假命题》",
    "《时间不是一条河是你的节奏》",
    "《身体和心是一个系统》",
]

with io.open(P, "rb") as f:
    raw = f.read()

txt = raw.decode("utf-8")
lines = txt.split("\r\n")
done = 0
for i, ln in enumerate(lines):
    if any(t in ln for t in titles):
        if "·R127" in ln:
            print(f"SKIP already-marked: {ln[:30]}")
            continue
        # 在该行最后一个 ·R124 后追加 ·R127（这几个条目本轮前末次使用都是 R124）
        if "·R124" in ln:
            idx = ln.rfind("·R124")
            lines[i] = ln[:idx] + "·R124·R127" + ln[idx + len("·R124"):]
            done += 1
        else:
            print(f"WARN no ·R124 in: {ln[:60]}")

out = "\r\n".join(lines)
with io.open(P, "wb") as f:
    f.write(out.encode("utf-8"))

print(f"marked={done}/5")
# verify
chk = io.open(P, "rb").read()
for t in titles:
    print("R127 in", t[:20], "=>", ("·R124·R127" in chk.decode("utf-8")))
