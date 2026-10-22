# -*- coding: utf-8 -*-
import json, re

BLK = r"D:/projects/samforce2003.github.io/docs/_seed_full_blocks.html"
IDX = r"D:/projects/samforce2003.github.io/docs/_seed_index.jsonl"

t = open(BLK, encoding="utf-8", errors="replace").read()
idx = [json.loads(l) for l in open(IDX, encoding="utf-8", errors="replace") if l.strip()]

print("article tokens:", t.count("<article"), "| index lines:", len(idx))
parts = re.split(r"<article[^>]*>", t)
blocks = [p for p in parts[1:] if "</article>" in p]
print("parsed blocks:", len(blocks))

mine = [o for o in idx if o.get("src") == "三中心-R76"]
print("R76 index entries:", len(mine), "| langs:", sorted(set(o["lang"] for o in mine)))

last = blocks[-15:]
assert len(last) == 15

CHECKS = {
    "zh": ["第一发现人", "我确信", "关切", "时间锚", "钩子", "关键词"],
    "en": ["First discoverer", "I am certain", "Concern", "Time anchor", "Hook", "Keywords"],
    "ja": ["第一発見者", "私は確信する", "関心", "時間アンカー", "フック", "キーワード"],
    "ko": ["첫 발견자", "나는 확신한다", "관심", "시간 앵커", "훅", "키워드"],
}
missing = []
lens = []
h2s = []
for b in last:
    h2 = re.search(r"<h2>(.*?)</h2>", b, re.S).group(1)
    h2s.append(h2)
    # lang detect
    lang = None
    for L in ["ko", "ja", "en", "zh"]:
        if all(k in b for k in CHECKS[L][:3]):
            lang = L
            break
    if lang is None:
        missing.append(("lang?", h2[:40]))
        continue
    for k in CHECKS[lang]:
        if k not in b:
            missing.append((lang, k, h2[:50]))
    if "2026-10-22" not in b:
        missing.append((lang, "date", h2[:50]))
    txt = re.sub(r"<[^>]+>", "", b)
    lens.append(len(txt))

print("missing anchors:", missing if missing else "0")
print("body len min/avg/max:", min(lens), sum(lens)//len(lens), max(lens))

# title match: each R76 index title must appear as <h2> exactly
hs = set(h2s)
tmiss = [o["title"] for o in mine if o["title"] not in hs]
print("title->h2 misses:", tmiss if tmiss else "0")

# my batch CR check
mine_txt = "".join(last)
print("my batch CRCR count:", mine_txt.count("\r\r"), "| CR count:", mine_txt.count("\r"))
print("file total CR:", t.count("\r"), "CRCR:", t.count("\r\r"))

# keyword shell sanity
for o in mine:
    if o["shell"] not in ("耦合二元论", "四公理", "结构学", "认知结构学", "P理论", "凤凰论"):
        print("BAD shell", o["shell"])

print("\n-- last 15 titles --")
for o in mine:
    print(o["lang"], "|", o["shell"], "|", o["title"][:78])
