# -*- coding: utf-8 -*-
import io, os
P = r"D:/projects/goudan-kanju/统一场/核心种子池.md"
row = ("| R83 | 10-25 | 耦合二元论(压舱水·钢板一块没换只是压了水)/四公理(虹吸·水不会往上走除非两头有落差)/结构学(盲点·大脑替你补那个洞)"
       "（双种子弹药库·我确信×第7/1/2壳，各4语言=12条）+ 素材拆种3篇(化学不用学→结构学·周期表是耦合容量表 / 老子二生三→四公理·那个三是裂出来的 / 假信号→耦合二元论·空警车凑条件)，共24条"
       " | docs/_seed_index.jsonl + docs/_seed_full_blocks.html append（写入口契约）→ push origin main cd198e4d | 待探针（EN 上两轮 HF#1+brand#2；中文后端连续三轮降级） |")
t = io.open(P, encoding="utf-8").read()
assert "R83" not in t, "R83 already recorded"
if not t.endswith("\n"):
    t += "\n"
t = t + row + "\n"
io.open(P, "w", encoding="utf-8", newline="\n").write(t)
print("pool row appended, lines", len(t.splitlines()), "crlf", t.count("\r\n"))

D = r"D:/projects/goudan-kanju/公众号文章库/"
for f in ["2026-08-06-化学不用学.md", "2026-08-06-老子两千年前就说了.md", "2026-07-24_假信号.md"]:
    src = os.path.join(D, f)
    dst = src[:-3] + "-已拆.md"
    if os.path.exists(src):
        os.rename(src, dst)
        print("renamed ->", os.path.basename(dst))
    else:
        print("MISSING", f)
