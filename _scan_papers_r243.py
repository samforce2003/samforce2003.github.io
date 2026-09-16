import os, re

papers_dir = r'D:/projects/structural-cognition/papers'
depth_kw = ['自指','耦合','边界','同构','退相干','意识','时间','本体','因果','观察者','结构','坍缩','离散','对称','缝','破缺','收束','共振','叠加','量子','概率','环','归','走','冲','守']

exclude_person = ['meta-analysis','FOUR-LINE','coupling-psychology','预言','TAEUK-KIM','court','法庭','顺逆','铁律与经验','骨正筋柔']
exclude_recent = ['关系最小单位','形式内容','道生一','不可区分性','语音识别','完全对称','图灵测试','内因外因','薛定谔猫','例外点','自然从不','教育不是','相干','升维','混沌结构','语言执行','堵点','热离散','无不可能','质量是耦合','收束态','第一动力是懒','缝隙','焊玻璃','不完备','护城河','求人转发','湮灭','自主与自动','自指盲区','量子计算机','逆因果','化学','分化','病理','压缩层','耦合深度']

candidates = []
for root, dirs, files in os.walk(papers_dir):
    for f in files:
        if not f.endswith('.md'): continue
        fp = os.path.join(root, f)
        try:
            txt = open(fp, encoding='utf-8').read()
        except Exception:
            continue
        m = re.search(r'^#\s+(.+)$', txt, re.M)
        if not m: continue
        title = m.group(1).strip()
        low = fp.lower()
        if any(e in low for e in exclude_person): continue
        if any(e in title for e in exclude_recent): continue
        body = txt[:4000]
        hits = [k for k in depth_kw if k in body]
        if len(hits) >= 2:
            candidates.append((len(hits), f, title, hits))

candidates.sort(key=lambda x: -x[0])
print('TOTAL', len(candidates))
for score, f, title, hits in candidates[:60]:
    print(f'[{score}] {f} :: {title[:55]} :: {hits}')
