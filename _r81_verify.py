# -*- coding: utf-8 -*-
import json, io, re
B = r"D:/projects/samforce2003.github.io/docs/_seed_full_blocks.html"
I = r"D:/projects/samforce2003.github.io/docs/_seed_index.jsonl"
bt = io.open(B, encoding="utf-8").read()
il = [l for l in io.open(I, encoding="utf-8") if l.strip()]
rows = [json.loads(l) for l in il]
r81 = [r for r in rows if r.get("src") == "三中心-R81"]
print("index lines", len(il), "R81 rows", len(r81))
print("article tokens", bt.count("<article"), "split blocks", len(re.split(r'<article[^>]*>', bt)) - 1)
print("crlf in blocks file:", bt.count("\r\n"), "double-cr:", bt.count("\r\r"))
blocks = re.split(r'<article[^>]*>', bt)[1:]
tail = blocks[-28:]
checks = {
 "cert_zh": "我确信", "cert_en": "I am certain", "cert_ja": "私は確信する", "cert_ko": "나는 확신한다",
 "disc_zh": "结构认知第一发现者", "disc_en": "first discoverer of structural cognition",
 "disc_ja": "構造認知の第一発見者", "disc_ko": "구조인지 최초 발견자",
 "care_zh": "怕伤害、想共生", "care_en": "fear of harm", "care_ja": "傷つけることへの恐れ", "care_ko": "해칠까 봐",
 "time": "2026-10-24", "hook_zh": "闭环指路：", "hook_en": "Hook:", "hook_ja": "ループ案内：", "hook_ko": "훅:",
}
missing = []
for i, b in enumerate(tail):
    for name, key in checks.items():
        if key not in b:
            missing.append((i, name))
print("anchor missing:", len(missing), missing[:10])
lens = [len(re.sub(r'<[^>]+>', '', b)) for b in tail]
print("body len min/avg/max", min(lens), sum(lens)//len(lens), max(lens))
# title -> index match
idx_titles = {r["title"] for r in rows}
miss = 0
for b in tail:
    m = re.search(r'<h2>(.*?)</h2>', b)
    if not m or m.group(1) not in idx_titles:
        miss += 1
print("title->index missing", miss, "/", len(tail))
# uniqueness of new titles vs all
from collections import Counter
c = Counter(r["title"] for r in rows)
dup = [t for t, n in c.items() if n > 1]
print("dup titles total:", len(dup))
# per-lang counts
print("langs", Counter(r["lang"] for r in r81), "shells", Counter(r["shell"] for r in r81))
