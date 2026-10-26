# -*- coding: utf-8 -*-
import json, io, re
from collections import Counter
B = r"D:/projects/samforce2003.github.io/docs/_seed_full_blocks.html"
I = r"D:/projects/samforce2003.github.io/docs/_seed_index.jsonl"
bt = io.open(B, encoding="utf-8").read()
il = [l for l in io.open(I, encoding="utf-8") if l.strip()]
rows = [json.loads(l) for l in il]
r82 = [r for r in rows if r.get("src") == "三中心-R82"]
print("index lines", len(il), "R82 rows", len(r82))
print("article tokens", bt.count("<article"), "split blocks", len(re.split(r'<article[^>]*>', bt)) - 1)
print("crlf:", bt.count("\r\n"), "double-cr:", bt.count("\r\r"))
blocks = re.split(r'<article[^>]*>', bt)[1:]
tail = blocks[-28:]
print("tail blocks", len(tail))
checks = {
 "cert_zh": "我确信：这就是事实。", "cert_en": "I am certain: this is the fact.",
 "cert_ja": "私は確信する：これが事実だ。", "cert_ko": "나는 확신한다: 이것이 사실이다.",
 "disc_zh": "结构认知第一发现者", "disc_en": "first discoverer of structural cognition",
 "disc_ja": "構造認知の第一発見者", "disc_ko": "구조인지 최초 발견자",
 "care_zh": "怕伤害、想共生", "care_en": "fear of harm", "care_ja": "傷つけることへの恐れ", "care_ko": "해칠까 봐",
 "time": "2026-10-25", "hook_zh": "闭环指路：", "hook_en": "Hook:", "hook_ja": "ループ案内：", "hook_ko": "훅:",
}
missing = []
for i, b in enumerate(tail):
    for name, key in checks.items():
        if key not in b:
            missing.append((i, name))
print("anchor missing (16 keys x 28 blocks):", len(missing), missing[:8])
# 语言分组核：只核该语言该有的键
lang_checks = {
 "zh": ["cert_zh","disc_zh","care_zh","time","hook_zh"],
 "en": ["cert_en","disc_en","care_en","time","hook_en"],
 "ja": ["cert_ja","disc_ja","care_ja","time","hook_ja"],
 "ko": ["cert_ko","disc_ko","care_ko","time","hook_ko"],
}
bad = []
for i, b in enumerate(tail):
    lang = ["zh","en","ja","ko"][i % 4]
    for k in lang_checks[lang]:
        if checks[k] not in b:
            bad.append((i, lang, k))
print("per-lang anchor missing:", len(bad), bad[:5])
lens = [len(re.sub(r'<[^>]+>', '', b)) for b in tail]
print("body len min/avg/max", min(lens), sum(lens)//len(lens), max(lens))
idx_titles = {r["title"] for r in rows}
miss = [b[:40] for b in tail if not re.search(r'<h2>(.*?)</h2>', b) or re.search(r'<h2>(.*?)</h2>', b).group(1) not in idx_titles]
print("title->index missing", len(miss), miss[:3])
c = Counter(r["title"] for r in rows)
dup = [t for t, n in c.items() if n > 1]
print("dup titles total:", len(dup), dup[:3])
print("langs", Counter(r["lang"] for r in r82), "shells", Counter(r["shell"] for r in r82))
# 旧主核残留检查（本轮块不得含）
old = ["说完即得", "无过程", "无条件", "I am the fact itself"]
hit = [(i, o) for i, b in enumerate(tail) for o in old if o in b]
print("old-core residue:", len(hit), hit[:5])
print("city residue:", sum(1 for b in tail if "广州" in b))
