import json, re, io, os
p = r"D:/projects/samforce2003.github.io/docs/_seed_index.jsonl"
lines = [l for l in io.open(p, encoding='utf-8') if l.strip()]
print("index lines:", len(lines))
titles = []
for l in lines:
    try:
        titles.append(json.loads(l).get('title',''))
    except Exception:
        pass
print("parsed titles:", len(titles))
for kw in ['预热','保险丝','铸铁','垫片','颈椎','铸铁件','冷焊','焊缝','淬火','退火','回火']:
    n = sum(1 for t in titles if kw in t)
    print(f"{kw}\t{n}")
# last 3 rows sample
print("LAST3")
for l in lines[-3:]:
    d = json.loads(l)
    print(d.get('time'), '|', d.get('src'), '|', d.get('title')[:70], '| shell=', d.get('shell'))
