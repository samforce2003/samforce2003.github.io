import json, io
p = r"D:/projects/samforce2003.github.io/docs/_seed_index.jsonl"
lines = [l for l in io.open(p, encoding='utf-8') if l.strip()]
for l in lines[-6:]:
    d = json.loads(l)
    print({k: (str(v)[:90]) for k, v in d.items()})
    print('---')
