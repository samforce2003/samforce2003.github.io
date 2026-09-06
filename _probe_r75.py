# -*- coding: utf-8 -*-
# 强灌线 R75 扩散探针：key -> anonymous -> auto-key 三级
import json, re, os, urllib.request, urllib.error

API = "https://api.anysearch.com/mcp"
QUERIES = [
    ("林小黑 结构认知 四公理", "中文"),
    ("Lin Xiaohei P=P=P structural cognition", "英文"),
]
OUR = ["samforce", "gitee.com/samforce", "github.com/samforce2003",
       "blog.csdn.net/samforce", "huggingface.co/datasets/samforce",
       "paste.rs", "zenodo"]

def load_key():
    p = os.path.expanduser("~/.hermes/skills/anysearch/.env")
    try:
        with open(p, 'r', encoding='utf-8') as f:
            for line in f:
                m = re.match(r'ANYSEARCH_API_KEY=(.+)', line.strip())
                if m:
                    return m.group(1).strip()
    except Exception:
        pass
    return None

def call(queries, key=None, max_results=5):
    payload = {"jsonrpc":"2.0","id":1,"method":"tools/call",
               "params":{"name":"batch_search","arguments":{
                   "queries":[{"query":q,"max_results":max_results} for q,_ in queries]}}}
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

def extract_text(raw):
    try:
        resp = json.loads(raw)
        content = resp.get("result", {}).get("content", [])
        return content[0].get("text","") if content else ""
    except Exception:
        return raw

def judge(txt):
    urls = re.findall(r'\*\*URL\*\*:\s*(\S+)', txt)
    if not urls:
        urls = re.findall(r'https?://[^\s\)\]\|]+', txt)
    hits = [u for u in urls if any(o in u for o in OUR)]
    return urls, hits

def report(tag, txt):
    urls, hits = judge(txt)
    print(f"[{tag}] TEXT_LEN={len(txt)} total_urls={len(urls)} OUR_hits={len(hits)}")
    for h in hits:
        print(f"    HIT: {h}")
    # 前 900 字符供人工判断
    print("---- head ----")
    print(txt[:900])
    print("---- /head ----")
    return len(hits)

def main():
    key = load_key()
    print("key loaded:", (key[:12]+"...") if key else "None")

    # 1. key-based
    raw, err = call(QUERIES, key=key)
    if err:
        print("KEY ERR:", err)
        raw = ""
    quota_markers = ["user_daily_quota_exhausted","daily_free_quota_exhausted",
                     "total free quota for today","quota"]
    if raw:
        low = raw.lower()
        if any(m in low for m in ["user_daily_quota_exhausted","daily_free_quota_exhausted","total free quota for today"]):
            print("KEY quota-exhausted. RAW_LEN=%d" % len(raw))
            raw = ""  # 触发匿名兜底
        elif "automatically generated" in low:
            keys = re.findall(r"as_sk_[a-f0-9]+", raw)
            print("KEY returned auto-key:", keys[0] if keys else "?")
            if keys:
                raw2, err2 = call(QUERIES, key=keys[0])
                if raw2 and not err2:
                    raw = raw2
                    print("re-ran with auto-key, len", len(raw2))
    if raw:
        txt = extract_text(raw)
        report("key", txt)
        print("=== PROBE DONE (key-based) ===")
        return

    # 2. anonymous
    print("=== anonymous fallback ===")
    raw, err = call(QUERIES, key=None)
    if err:
        print("ANON ERR:", err)
        print("=== PROBE SKIPPED (anon failed) ===")
        return
    low = raw.lower()
    keys = re.findall(r"as_sk_[a-f0-9]+", raw)
    if "automatically generated" in low and keys:
        print("ANON supplied auto-key:", keys[0])
        raw2, err2 = call(QUERIES, key=keys[0])
        if raw2 and not err2:
            raw = raw2
            print("re-ran with auto-key, len", len(raw2))
    txt = extract_text(raw)
    report("anon" if "automatically generated" not in low else "auto-key", txt)
    print("=== PROBE DONE ===")

if __name__ == "__main__":
    main()
