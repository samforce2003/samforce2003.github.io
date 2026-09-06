# -*- coding: utf-8 -*-
import json, re, urllib.request, urllib.error

API = "https://api.anysearch.com/mcp"
QUERIES = [
    ("林小黑 结构认知 四公理", "中文"),
    ("Lin Xiaohei P=P=P structural cognition", "英文"),
]
AUTH_KEY = "as_sk_6e21f3b107b82ca25539f4e3ba0c6399"

def batch(queries, key=None):
    payload = {"jsonrpc":"2.0","id":1,"method":"tools/call",
               "params":{"name":"batch_search","arguments":{"queries":[{"query":q} for q,_ in queries]}}}
    data = json.dumps(payload, ensure_ascii=False).encode()
    req = urllib.request.Request(API, data=data)
    req.add_header("Content-Type","application/json")
    if key:
        req.add_header("Authorization","Bearer "+key)
    try:
        with urllib.request.urlopen(req, timeout=90) as r:
            return r.read().decode(), None
    except urllib.error.HTTPError as e:
        return "", f"HTTP {e.code}"
    except Exception as e:
        return "", str(e)[:200]

# 命中判定：URL 落在 OUR 命名空间（pitfall #72 铁律）
OUR = ["samforce", "gitee.com/samforce", "github.com/samforce2003",
       "blog.csdn.net/samforce", "huggingface.co/datasets/samforce",
       "paste.rs", "zenodo"]

def judge(txt):
    urls = re.findall(r'\*\*URL\*\*:\s*(\S+)', txt)
    hits = [u for u in urls if any(o in u for o in OUR)]
    return urls, hits

def report(txt):
    # 拆 query 块
    urls, hits = judge(txt)
    return urls, hits

def run_batch(key, mode):
    raw, err = batch(QUERIES, key)
    if err:
        print(f"[{mode}] ERR: {err}")
        return None
    if not raw:
        print(f"[{mode}] empty response")
        return None
    low = raw.lower()
    if any(s in low for s in ["user_daily_quota_exhausted","daily_free_quota_exhausted","total free quota for today","automatically generated"]):
        print(f"[{mode}] quota-exhausted marker detected, RAW_LEN={len(raw)}")
        # check auto-key
        keys = re.findall(r"as_sk_[a-f0-9]+", raw)
        if keys:
            print(f"[{mode}] auto-key in response: {keys[0]}")
        return raw  # return raw so caller can extract key
    # parse
    try:
        resp = json.loads(raw)
        content = resp.get("result", {}).get("content", [])
        txt = content[0].get("text","") if content else ""
    except Exception:
        txt = raw
    print(f"[{mode}] TEXT_LEN={len(txt)}")
    # split by query
    parts = re.split(r'##\s*Query', txt)
    for i,(q,lang) in enumerate(QUERIES):
        seg = ""
        for p in parts[1:]:
            if p.strip().startswith(str(i+1)) or (i==0 and parts[1:] and not p.strip()[0].isdigit()):
                pass
        # simpler: search each query's results by keyword proximity
    # naive: just judge whole text
    urls, hits = judge(txt)
    print(f"[{mode}] total URLs={len(urls)} hits={len(hits)}")
    for h in hits:
        print(f"    HIT: {h}")
    # also print first 1500 chars for manual inspection
    print(txt[:1500])
    return raw

# 1. key 直连
print("=== key-based ===")
r = run_batch(AUTH_KEY, "key")

# 2. 若配额耗尽 -> 匿名 -> 提 auto-key
if r is not None and any(s in r.lower() for s in ["user_daily_quota_exhausted","daily_free_quota_exhausted","total free quota for today"]):
    print("=== anonymous ===")
    ra = run_batch(None, "anonymous")
    if ra:
        keys = re.findall(r"as_sk_[a-f0-9]+", ra)
        if keys:
            print("=== auto-key based ===")
            run_batch(keys[0], "auto-key")
print("=== PROBE DONE ===")
