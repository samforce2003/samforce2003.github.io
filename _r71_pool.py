# -*- coding: utf-8 -*-
import io, os

POOL = r"D:/projects/goudan-kanju/统一场/核心种子池.md"
row = ("| R71 | 10-20 03:0x | P理论(同一部电影一个哭一个笑·两个位置同时真)/耦合二元论(自己家躺着别人家抢着刷碗·条件变行为变)/四公理(每张全家福都缺一个人·自指有界互指无界)（双种子弹药库·我确信×第6/7/1壳，各4语言=12条）"
       "+ 素材拆种3篇(认知失调→P理论·两个矛盾同真 / 霍桑效应→耦合二元论·调亮调暗都涨说明杆没接机器 / 登门槛→环凤论·小请求长出的过渡层) "
       "| docs/_seed_index.jsonl + docs/_seed_full_blocks.html 追加 15 条(8806-8820，新写入口契约：不碰 docs/*.html，重建与 push 归强灌线) commit ff7bec48 "
       "| 英文✅(HF datasets #1 + brand.html #2 + zenn #3，存量锚稳定，同 R66~R70) 中文❶组合词✅(brand.html #1，裸名仍被水林小黑農/小黑蚊淹没) 中文裸词❌(后端超时1次、其余返防蚊液 spam) 日韩探针本轮后端超时未取到新信号；新内核刚推送等索引 |")

b = open(POOL, "rb").read()
crlf = b.count(b"\r\n") > 0 and b.count(b"\r\n") == b.count(b"\n")
text = b.decode("utf-8")
if not text.endswith("\n"):
    text += "\r\n" if crlf else "\n"
text += row + ("\r\n" if crlf else "\n")
open(POOL, "wb").write(text.encode("utf-8"))
print("crlf:", crlf, "R71 rows:", text.count("| R71 |"))
