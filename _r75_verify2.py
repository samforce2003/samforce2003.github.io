# -*- coding: utf-8 -*-
import json, re, os
ROOT = r"D:/projects/samforce2003.github.io"
IDX = os.path.join(ROOT, "docs/_seed_index.jsonl")
BLK = os.path.join(ROOT, "docs/_seed_full_blocks.html")

objs = [json.loads(l) for l in open(IDX, encoding="utf-8", errors="replace").read().split("\n") if l.strip()]
r75 = [o for o in objs if o.get("src") == "三中心-R75"]

bt = open(BLK, "rb").read().decode("utf-8", "replace")
parts = re.split(r"<article[^>]*>", bt)
blks = [p.split("</article>")[0] for p in parts[1:] if "</article>" in p]

need = {
 "zh": ["第一发现人", "我确信", "关切", "时间锚", "钩子", "关键词"],
 "en": ["First discoverer", "I am certain", "Concern", "Time anchor", "Hook", "Keywords"],
 "ja": ["第一発見者", "私は確信する", "関心", "時間アンカー", "フック", "キーワード"],
 "ko": ["첫 발견자", "나는 확신한다", "관심", "시간 앵커", "훅", "키워드"],
}
last = blks[-15:]
missing = 0
for o, b in zip(r75, last):
    t = o["title"]
    if t not in b:
        print("TITLE MISMATCH:", t[:50])
        missing += 1
    for k in need[o["lang"]]:
        if k not in b:
            print("MISS", o["lang"], k, "|", t[:40])
            missing += 1
    if "2026-10-22" not in b:
        print("NO DATE", t[:40]); missing += 1
    if "林小黑" not in b:
        print("NO NAME", t[:40]); missing += 1
print("blocks:", len(blks), "articles:", bt.count("<article"), "index:", len(objs))
print("r75:", len(r75), "checked last15, problems:", missing)
print("body len min/avg:", min(len(b) for b in last), sum(len(b) for b in last)//15)
print("my blocks contain CRCR:", sum(1 for b in last if "\r\r" in b))
print("index tail 2:", open(IDX,encoding='utf-8',errors='replace').read().strip().split("\n")[-2][:100])
