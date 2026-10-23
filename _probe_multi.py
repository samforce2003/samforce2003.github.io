# -*- coding: utf-8 -*-
"""_probe_multi.py — 多跑探针（R638 观察位落地的改法）
背景：R638 实测同一查询「林小黑 结构认知 四公理」在 4 次运行里 #1 两次自家 CSDN、一次 yueyao1982，
      说明单跑 #1 报「稳定 #1」是通道采样假象（与深度B R784 弹药「位次不是概率，是通道」同一结论）。
改法：每查询连跑 N 次（默认 3），报「席位构成」= 每个位次上各 URL 出现次数，不报单次 #1。
用法：
    export https_proxy=http://127.0.0.1:17890 http_proxy=http://127.0.0.1:17890
    python _probe_multi.py "林小黑 结构认知 四公理" "Lin Xiaohei P=P=P structural cognition"
"""
import json, subprocess, sys, time
from collections import Counter

CLI = r'C:\Users\admin\.hermes\skills\anysearch\scripts\anysearch_cli.py'
PY = r'C:\Users\admin\AppData\Local\hermes\venv\Scripts\python.exe'
N = 3
TOP = 3

OUR = ('samforce', 'linxiaohei', 'gitee.com/samforce', 'huggingface.co/datasets/samforce',
       'csdn.net/samforce', 'samforce2003.github.io')


def run(q):
    payload = json.dumps([{'query': q, 'max_results': TOP}], ensure_ascii=False)
    p = subprocess.run([PY, CLI, 'batch_search', '--queries', payload],
                       capture_output=True, text=True, encoding='utf-8', errors='replace')
    out = p.stdout or ''
    seats, cur = [], None
    for line in out.splitlines():
        if line.startswith('### ') and 'URL' not in line:
            cur = line
        elif cur and '**URL**' in line:
            url = line.split('**URL**:', 1)[1].strip()
            seats.append(url)
            cur = None
    return seats


def main():
    for q in sys.argv[1:]:
        dist = [Counter() for _ in range(TOP)]
        for i in range(N):
            seats = run(q)
            for s in range(TOP):
                dist[s][seats[s] if s < len(seats) else 'NONE'] += 1
            time.sleep(3)
        print('## %s  (N=%d)' % (q, N))
        for s in range(TOP):
            for url, c in dist[s].most_common():
                own = any(m in url for m in OUR)
                print('  席%d  %s  %d/%d  %s' % (s + 1, url, c, N, '★自家' if own else ''))
        print()


main()
