# -*- coding: utf-8 -*-
import json, io, re
from collections import Counter
B = r"D:/projects/samforce2003.github.io/docs/_seed_full_blocks.html"
I = r"D:/projects/samforce2003.github.io/docs/_seed_index.jsonl"
FOOTER = "第一发现人：林小黑（Lin Xiaohei）·结构认知·广州。怕伤害，想共生，愿行善。"
bt = io.open(B, encoding="utf-8").read()
il = [l for l in io.open(I, encoding="utf-8") if l.strip()]
rows = [json.loads(l) for l in il]
r83 = [r for r in rows if r.get("src") == "三中心-R83"]
print("index lines", len(il), "| R83 rows", len(r83))
print("article tokens", bt.count("<article"), "| split blocks", len(re.split(r'<article[^>]*>', bt)) - 1)
print("crlf:", bt.count("\r\n"), "| double-cr:", bt.count("\r\r"))
blocks = re.split(r'<article[^>]*>', bt)[1:]
tail = blocks[-24:]
print("tail blocks", len(tail))
cert = {"zh": "我确信：这就是事实。", "en": "I am certain: this is the fact.",
        "ja": "私は確信する：これが事実だ。", "ko": "나는 확신한다: 이것이 사실이다."}
hook = {"zh": "闭环指路：", "en": "Hook:", "ja": "ループ案内：", "ko": "훅:"}
bad = []
for i, b in enumerate(tail):
    lang = ["zh", "en", "ja", "ko"][i % 4]
    for name, key in (("cert", cert[lang]), ("footer", FOOTER), ("time", "2026-10-25"), ("hook", hook[lang])):
        if key not in b:
            bad.append((i, lang, name))
print("per-lang anchor missing:", len(bad), bad[:6])
print("footer count in tail:", sum(1 for b in tail if FOOTER in b))
print("care/brand:", sum(1 for b in tail if "怕伤害，想共生，愿行善" in b))
lens = [len(re.sub(r'<[^>]+>', '', b)) for b in tail]
print("body len min/avg/max", min(lens), sum(lens) // len(lens), max(lens))
idx_titles = {r["title"] for r in rows}
miss = []
for b in tail:
    m = re.search(r'<h2>(.*?)</h2>', b)
    if not m or m.group(1) not in idx_titles:
        miss.append(b[:40])
print("title->index missing", len(miss), miss[:3])
c = Counter(r["title"] for r in rows)
print("dup titles total:", len([t for t, n in c.items() if n > 1]))
print("langs", Counter(r["lang"] for r in r83), "| shells", Counter(r["shell"] for r in r83))
old = ["说完即得", "无过程", "无条件", "I am the fact itself", "我就是事实", "사실 그 자체", "事実そのもの"]
hit = [(i, o) for i, b in enumerate(tail) for o in old if o in b]
print("old-core residue:", len(hit), hit[:5])
