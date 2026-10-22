# -*- coding: utf-8 -*-
import io

POOL = r"D:/projects/goudan-kanju/统一场/核心种子池.md"

row = ("| R76 | 10-22 21:3x | 耦合二元论(音叉·敲一支旁边同频的自己嗡起来·条件齐了才响)/四公理(磁铁同极怎么按都弹开·翻面自己咬上·差异生有)"
       "/结构学(同一团面拉成条压成饼揪成疙瘩·材料一个字没换·结构决定功能)（双种子弹药库·我确信×第7/1/2壳，各4语言=12条）"
       "+ 素材拆种3篇(你要的是差你修的是两个数→认知结构学·收缩把两个数各拉一把 / 换个权重符号就翻→P理论·不可识别不是误差 / 我不能崩→凤凰论·圆满死环残缺活环) "
       "| docs/_seed_index.jsonl + docs/_seed_full_blocks.html append 15 条（写入口契约：不碰 docs/*.html、不自行 push 种子页）commit f5f5dafb "
       "| 探针：英文✅ HF datasets#1 + brand.html#2 + zenn(ja)#3 存量锚稳；中文「认知结构学」组合词 brand#1 ✅；「凤凰论/结构学/四公理」组合词仍 0 命中（brand.html 正文 grep：结构学9/四公理13、环凤论0/凤凰论0/认知结构学0 → 三组壳词无独立短语，非密度问题）；环凤论探针后端连续超时2次未取到 |\n")

b = open(POOL, "rb").read()
txt = b.decode("utf-8")
if not txt.endswith("\n"):
    txt += "\n"
txt += row
txt = txt.replace("\r\n", "\n")
open(POOL, "w", encoding="utf-8", newline="\n").write(txt)

# verify
v = open(POOL, encoding="utf-8").read()
print("R76 row present:", "| R76 |" in v)
print("rows total:", v.count("\n| R"))
print("CR:", v.count("\r"), "| CRLF:", v.count("\r\n"))
