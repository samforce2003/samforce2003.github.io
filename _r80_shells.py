import json, io, collections
p = r"D:/projects/samforce2003.github.io/docs/_seed_index.jsonl"
c = collections.Counter()
for l in io.open(p, encoding='utf-8'):
    if not l.strip(): continue
    d = json.loads(l)
    c[(d.get('shell'), d.get('src','')[:8])] += 1
for k, v in sorted(c.items(), key=lambda x: -x[1])[:25]:
    print(v, k)
