# -*- coding: utf-8 -*-
import io, json
p = 'docs/_seed_index.jsonl'
kws = ['骨痂','骨折','骨','辐条','伞骨','蜂巢','六边形','轮胎','动平衡','配重','颈椎','台风眼','雷劈','树','焊缝','预热','铸铁','弹簧','垫片','拱','榫']
cnt = {k: 0 for k in kws}
for line in io.open(p, encoding='utf-8', errors='replace'):
    line = line.strip()
    if not line:
        continue
    d = json.loads(line)
    t = d.get('title', '')
    for k in kws:
        if k in t:
            cnt[k] += 1
print(' / '.join('%s=%d' % (k, cnt[k]) for k in kws))
