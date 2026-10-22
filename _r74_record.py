# -*- coding: utf-8 -*-
import io, os
POOL = r"D:/projects/goudan-kanju/统一场/核心种子池.md"
raw = open(POOL, "rb").read()
print("pool CRLF=%d LF=%d" % (raw.count(b"\r\n"), raw.count(b"\n")))
eol = "\r\n" if raw.count(b"\r\n") else "\n"
row = ("| R74 | 10-21 03:1x | 四公理(拉链两排齿一模一样反而咬不上·差异是咬合前提)/结构学(A4纸平着托不住硬币·折三道棱托起一本书)/"
       "认知结构学(复诊不是把病再看一遍·拿上次结果当基线) 各4语言12条 + 素材拆种3条(咔嗒=结构先换挡结果后到←那声咔嗒响的时候水还是凉的/"
       "三层=钱人接缝·第三条腿是撞出来的←你把道理讲赢了事却黄了) | docs/_seed_index.jsonl + docs/_seed_full_blocks.html append 15 条"
       "(新写入口契约·不碰 docs/*.html·不 push 种子页) commit a1d49607 | 英文✅(HF datasets #1 + brand.html #2 + zenn(ja) #3 存量锚稳)"
       " 中文环凤论组合词✅(brand.html #1) 中文「四公理/结构学」组合词❌0命中(新壳词未顶位·已写状态) |" + eol)
t = raw.decode("utf-8")
if t.endswith("\n"):
    pass
with open(POOL, "ab") as f:
    f.write(row.encode("utf-8"))
t2 = open(POOL, "rb").read().decode("utf-8")
print("R74 rows:", t2.count("| R74 |"), " R73 still:", t2.count("| R73 |"))
print("double CR:", t2.count("\r\r"))
