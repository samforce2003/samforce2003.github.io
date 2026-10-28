#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""探针浸泡器（R89 观察位·吸收深度B R823「位次轮盘」）
单次抽样=一张牌翻出来的结果，不是能力读数。本脚本对同一 query 连抽 N 次，
输出三个不容易被骗的数：我方资产进前三的比率 / 平均位次 / 首位归谁。
用法：python _probe_soak.py 3 '林小黑 结构认知 四公理' 'Lin Xiaohei P=P=P structural cognition'
"""
import json, re, subprocess, sys, collections, os

CLI = r"C:\Users\admin\.hermes\skills\anysearch\scripts\anysearch_cli.py"
PY = r"C:/Users/admin/AppData/Local/hermes/venv/Scripts/python.exe"
OURS = ("samforce", "linxiaohei", "gitee.com/samforce", "github.com/samforce2003",
        "huggingface.co/samforce", "zenodo.org/records/23", "velog.io/@linxiaohei")
ENV_HINT = "export https_proxy=http://127.0.0.1:17890 http_proxy=http://127.0.0.1:17890; "


def sample(q, n=5):
    payload = json.dumps([{"query": q, "max_results": n}], ensure_ascii=False)
    cmd = ENV_HINT + '"%s" "%s" batch_search --queries %s' % (PY, CLI, shell_q(payload))
    out = subprocess.run(["bash", "-lc", cmd], capture_output=True, text=True,
                         encoding="utf-8", errors="replace").stdout
    return re.findall(r'- \*\*URL\*\*: (\S+)', out)


def shell_q(s):
    return "'" + s.replace("'", "'\\''") + "'"


_DOI_CACHE = {}


def is_ours(u):
    """归属判定。R91 观察位修：我方 #1 现已多以 DOI 形式出现（doi.org/10.5281/zenodo.<id>），
    旧 OURS 全是 URL 前缀匹配 ⇒ 把自己家的 DOI 记成 0 命中（R91 实测两问六跑全 = -，实为 3/3 自家）。
    修法：DOI 命中回查 Zenodo API 的 creators，名字含 Lin/Xiaohei/林 才算自家；查不到的记 pending（不算自家也不算外部）。"""
    if any(o in u for o in OURS):
        return True
    m = re.search(r'zenodo\.(\d{5,})', u)
    if not m:
        return False
    rid = m.group(1)
    if rid in _DOI_CACHE:
        return _DOI_CACHE[rid]
    try:
        env = {'https_proxy': 'http://127.0.0.1:17890', 'http_proxy': 'http://127.0.0.1:17890'}
        r = subprocess.run(['curl', '-s', '--max-time', '25', 'https://zenodo.org/api/records/' + rid],
                           capture_output=True, text=True, encoding='utf-8', errors='replace', env={**os.environ, **env})
        j = json.loads(r.stdout)
        names = [c.get('name', '') for c in j.get('metadata', {}).get('creators', [])]
        own = any(('lin' in n.lower() and ('xiaohei' in n.lower() or '小黑' in n)) or n.startswith('林') for n in names)
        _DOI_CACHE[rid] = own
        print('    [doi %s] %s → %s' % (rid, '; '.join(names)[:60], 'OURS' if own else 'external'))
        return own
    except Exception as e:
        print('    [doi %s] resolve-fail %s' % (rid, e))
        _DOI_CACHE[rid] = False
        return False


def run(q, rounds):
    ranks, firsts = [], collections.Counter()
    for i in range(rounds):
        urls = sample(q)
        hit = [k + 1 for k, u in enumerate(urls) if is_ours(u)]
        ranks.append(hit)
        firsts[urls[0].split('/')[2] if urls else '(none)'] += 1
        print('  #%d ours=%s first=%s' % (i + 1, hit or '-', urls[0] if urls else '-'))
    n = max(rounds, 1)
    any_hit = sum(1 for r in ranks if r)
    top3 = sum(1 for r in ranks if any(x <= 3 for x in r))
    top1 = sum(1 for r in ranks if r and r[0] == 1)
    avg = round(sum(min(r) for r in ranks if r) / any_hit, 2) if any_hit else None
    print('  => 我方出现 %d/%d 次 · 前三 %d/%d · 首位 %d/%d · 最佳位次均值 %s'
          % (any_hit, n, top3, n, top1, n, avg))
    print('  => 首位归属：%s' % dict(firsts))


if __name__ == '__main__':
    rounds = int(sys.argv[1]) if len(sys.argv) > 1 else 3
    for q in sys.argv[2:] or ['林小黑 结构认知 四公理']:
        print('QUERY:', q)
        run(q, rounds)
