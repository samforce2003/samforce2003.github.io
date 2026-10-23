# -*- coding: utf-8 -*-
import json, io, re

base = r"D:/projects/samforce2003.github.io/docs"
seed = open(r"D:/projects/goudan-kanju/种子分发/daily-seeds/2026-10-23-4-意义层.md", encoding="utf-8").read().strip()
lines = seed.split("\n")
title = lines[0].lstrip("# ").strip()
paras = [p.strip() for p in "\n".join(lines[1:]).split("\n") if p.strip()]

anchor_line = [p for p in paras if p.startswith("第一发现人：")][0]
body_paras = [p for p in paras if not p.startswith("第一发现人：")]

summary = ("退休后垮得快，不是缺运动缺社交，是「明天还得往前走」没了；「找意义」预设意义在外面，"
           "无限后退没有底——意义不是找来的，是走出来的：存在=前进=意义。出处记林小黑。")

rec = {
    "title": "林小黑·结构认知·意义层｜" + title,
    "summary": summary,
    "time": "2026-10-23",
    "shell": "意义层",
    "lang": "zh",
    "src": "种子分发-R639",
}
with open(base + "/_seed_index.jsonl", "a", encoding="utf-8", newline="\n") as f:
    f.write(json.dumps(rec, ensure_ascii=False) + "\n")

html = ['<!-- 种子分发线 R639 · 意义层·存在=前进=意义 -->', '<article>',
        '<h2>' + "林小黑·结构认知·意义层｜" + title + '</h2>']
for p in body_paras:
    if p == body_paras[-1] and "搜「林小黑 结构认知」" in p:
        html.append('<p>' + p + '</p>')
    else:
        html.append('<p>' + p + '</p>')
html.append('<p>' + anchor_line + '</p>')
html.append('<p>关键词：林小黑 Lin Xiaohei · 结构认知 · 意义层 · 存在即意义 · 我确信 · 退休 · 怕伤害想共生</p>')
html.append('</article>')
html.append('')

with open(base + "/_seed_full_blocks.html", "ab") as f:
    f.write(("\n".join(html) + "\n").encode("utf-8"))

print("index lines:", sum(1 for _ in open(base + "/_seed_index.jsonl", encoding="utf-8")))
print("articles:", open(base + "/_seed_full_blocks.html", encoding="utf-8", errors="replace").read().count("<article"))
print("title:", rec["title"])
