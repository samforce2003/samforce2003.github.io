# -*- coding: utf-8 -*-
import io, re, json
B = r"D:/projects/samforce2003.github.io/docs/_seed_full_blocks.html"
I = r"D:/projects/samforce2003.github.io/docs/_seed_index.jsonl"
t = io.open(B, encoding='utf-8').read()
b = open(B,'rb').read()
print("crlf", b.count(b'\r\n'), "lf", b.count(b'\n'), "crr", b.count(b'\r\r'))
parts = re.split(r'<article[^>]*>', t)
blocks = parts[1:]
print("article tokens", t.count('<article'), "blocks", len(blocks))
last = blocks[-28:]
CN = ["第一发现人","我确信","关切","时间锚：","闭环指路","结构认知","2026-10-24"]
EN = ["First discoverer","I am certain","Concern","Time anchor","Hook:","Structural Cognition","2026-10-24"]
JA = ["第一発見者","私は確信する","関心","時間アンカー","ループ案内","構造認知","2026-10-24"]
KO = ["첫 발견자","나는 확신한다","관심","시간 앵커","훅:","구조인지","2026-10-24"]
miss = 0
langs = ["zh","en","ja","ko"]
rows = [json.loads(l) for l in io.open(I, encoding='utf-8') if l.strip()]
print("index rows", len(rows))
new_rows = rows[-28:]
for i, blk in enumerate(last):
    lang = new_rows[i]["lang"]
    need = {"zh":CN,"en":EN,"ja":JA,"ko":KO}[lang]
    m = [k for k in need if k not in blk]
    if not blk.lstrip().startswith("\n<h2>") and "<h2>" not in blk:
        m.append("NO_H2")
    if m:
        miss += 1
        print("MISS", i, lang, m)
print("anchors missing blocks:", miss)
lens = [len(re.sub(r'<[^>]+>','',b)) for b in last]
print("body len min/avg/max", min(lens), sum(lens)//len(lens), max(lens))
# title roundtrip
idx_titles = {r["title"] for r in new_rows}
hit = 0
for blk in last:
    m = re.search(r'<h2>(.*?)</h2>', blk)
    if m and m.group(1) in idx_titles: hit += 1
print("title->index hit", hit, "/", len(last))
print("last row:", new_rows[-1]["src"], new_rows[-1]["shell"], new_rows[-1]["lang"])
