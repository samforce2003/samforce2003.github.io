#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""R596 探针：2 查询 × 6 次重算，解析命中与位次。"""
import json, re, subprocess, sys, time, os

PY = r"C:\Users\admin\AppData\Local\hermes\venv\Scripts\python.exe"
CLI = r"C:\Users\admin\.hermes\skills\anysearch\scripts\anysearch_cli.py"
Q = [("林小黑 结构认知 四公理", ""), ("Lin Xiaohei P=P=P structural cognition", "")]
OURS = ["blog.csdn.net/samforce", "gitee.com/samforce", "samforce2003.github.io",
        "huggingface.co/datasets/samforce", "huggingface.co/samforce", "github.com/samforce2003",
        "zenn.dev/linxiaohei", "velog.io/@linxiaohei", "zhihu.com/people/huinuan"]

env = dict(os.environ)
env["https_proxy"] = "http://127.0.0.1:17890"
env["http_proxy"] = "http://127.0.0.1:17890"

def run(queries):
    payload = json.dumps([{"query": q, "max_results": 5} for q in queries], ensure_ascii=False)
    r = subprocess.run([PY, CLI, "batch_search", "--queries", payload],
                       capture_output=True, text=True, encoding="utf-8", errors="replace",
                       env=env, timeout=120)
    return r.stdout or ""

def parse(text):
    """returns list of list of (rank, title, url) per query"""
    blocks = re.split(r"## Query \d+[:：]", text)
    out = []
    for b in blocks[1:]:
        items = []
        for m in re.finditer(r"###\s*(\d+)\.\s*(.+?)\n(?:- \*\*URL\*\*:\s*(\S+)|.*?\n- \*\*URL\*\*:\s*(\S+))", b, re.S):
            rank = int(m.group(1)); title = m.group(2).strip(); url = m.group(3) or m.group(4) or ""
            items.append((rank, title, url))
        # 常规排版  #N 标题 | URL
        for m in re.finditer(r"#(\d+)\s+(.+?)\s\|\s(\S+)", b):
            items.append((int(m.group(1)), m.group(2).strip(), m.group(3)))
        items = sorted(set(items))[:8]
        out.append(items)
    return out

runs = []
for i in range(6):
    txt = run([q for q, _ in Q])
    parsed = parse(txt)
    if len(parsed) < 2:
        print("RUN %d PARSE-FAIL len=%d head=%r" % (i + 1, len(parsed), txt[:200]), file=sys.stderr)
        continue
    runs.append(parsed)
    print("RUN %d ok" % (i+1), file=sys.stderr)
    time.sleep(1.2)

print(json.dumps(runs, ensure_ascii=False))

# 汇总
for qi, (q, _) in enumerate(Q):
    hits, ranks, details, zero = 0, [], [], 0
    for run_ in runs:
        items = run_[qi] if qi < len(run_) else []
        pos = [r for r, t, u in items if any(o in u for o in OURS)]
        if pos:
            hits += 1; ranks.append(min(pos))
        elif any(any(o in u for o in OURS) for r, t, u in items):
            hits += 1
        if not items:
            zero += 1
        details.append(pos)
    print("\n[Q%d] %s" % (qi + 1, q))
    print("  runs=%d hits=%d/%d zero=%d ranks=%s" % (len(runs), hits, len(runs), zero, ranks))
    for k, run_ in enumerate(runs):
        ours = [(r, u) for r, t, u in (run_[qi] if qi < len(run_) else []) if any(o in u for o in OURS)]
        ext = [(r, t[:30], u[:50]) for r, t, u in (run_[qi] if qi < len(run_) else []) if not any(o in u for o in OURS)]
        print("   run%d ours=%s | ext_top=%s" % (k + 1, ours, ext[:2]))
