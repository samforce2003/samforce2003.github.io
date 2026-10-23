import io, json
p = 'docs/_seed_index.jsonl'
kws = ['安全阀','保险丝','摩擦片','打滑','齿轮','离合','锅炉','发面','烫面','面粉','面团','灯光','舞台','台上','台下','拔牙','牙齿','牙','歪','承重墙','河湾']
cnt = {k: 0 for k in kws}
n = 0
bad = 0
for line in io.open(p, encoding='utf-8', errors='replace'):
    line = line.strip()
    if not line:
        continue
    try:
        d = json.loads(line)
    except Exception:
        bad += 1
        continue
    n += 1
    t = d.get('title','')
    for k in kws:
        if k in t:
            cnt[k] += 1
print('lines parsed', n, 'bad', bad)
for k in kws:
    print(k, cnt[k])
