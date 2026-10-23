# -*- coding: utf-8 -*-
import json, re

IDX = r"D:/projects/samforce2003.github.io/docs/_seed_index.jsonl"
BLK = r"D:/projects/samforce2003.github.io/docs/_seed_full_blocks.html"

# --- IDX: 行尾统一为 LF（该文件本就几乎纯 LF）---
idata = open(IDX, 'rb').read()
print("IDX before: CRLF", idata.count(b'\r\n'), "LF", idata.count(b'\n'), "CRCR", idata.count(b'\r\r'))
norm = idata.replace(b'\r\n', b'\n')
open(IDX, 'wb').write(norm)
nd = open(IDX, 'rb').read()
print("IDX after : CRLF", nd.count(b'\r\n'), "LF", nd.count(b'\n'), "CR", nd.count(b'\r'))

lines = [l for l in nd.decode('utf-8').splitlines() if l.strip()]
recs = [json.loads(l) for l in lines]
print("IDX lines:", len(lines), "parsed:", len(recs))
mine = [r for r in recs if r.get('src') == '三中心-R77']
print("R77 idx:", len(mine), "langs:", {l: sum(1 for r in mine if r['lang'] == l) for l in ('zh','en','ja','ko')})
print("shells:", sorted({r['shell'] for r in mine}))
print("id None:", all(r['id'] is None for r in mine))

# --- BLK 校验 ---
bt = open(BLK, 'rb').read().decode('utf-8', errors='replace')
print("\nBLK CRLF", bt.count('\r\n'), "LF", bt.count('\n'), "CRCR", bt.count('\r\r'))
print("token <article:", bt.count('<article'),
      "parsed blocks:", len(re.split(r'<article[^>]*>', bt)) - 1)
parts = re.split(r'<article[^>]*>', bt)[1:]
tail = parts[-16:]
print("tail blocks:", len(tail))

CHK = {
 'zh': ["第一发现人", "我确信", "关切", "时间锚", "钩子", "关键词"],
 'en': ["First discoverer", "I am certain", "Concern", "Time anchor", "Hook"],
 'ja': ["第一発見者", "私は確信する", "関心", "時間アンカー", "フック", "キーワード"],
 'ko': ["첫 발견자", "나는 확신한다", "관심", "시간 앵커", "훅", "키워드"],
}
miss = 0
lens = []
titles = []
for i, blk in enumerate(tail):
    rec = mine[i]
    lang = rec['lang']
    titles.append(blk.split('<h2>')[1].split('</h2>')[0])
    for k in CHK[lang]:
        if k not in blk:
            print("MISSING", i, lang, k); miss += 1
    if "2026-10-23" not in blk:
        print("MISSING date", i); miss += 1
    body = re.sub(r'<[^>]+>', '', blk)
    lens.append(len(body))
print("anchor missing:", miss)
print("len min/avg/max:", min(lens), round(sum(lens)/len(lens)), max(lens))

# 标题回查索引
idx_titles = {r['title'] for r in mine}
print("title match:", sum(1 for t in titles if t in idx_titles), "/", len(titles))
print("\nsample title:", titles[0])
print("tail block ends:", repr(tail[-1][-120:]))
