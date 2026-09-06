# -*- coding: utf-8 -*-
import json, re, urllib.request, urllib.error

API = "https://api.anysearch.com/mcp"
QUERIES = [
    ("林小黑 结构认知 四公理", "中文"),
    ("Lin Xiaohei P=P=P structural cognition", "英文"),
]

OUR = ["samforce", "gitee.com/samforce", "github.com/samforce2003",
       "blog.csdn.net/samforce", "huggingface.co/datasets/samforce",
       "paste.rs", "zenodo"]

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

def main():
    print("=== anonymous batch_search ===")
    raw, err = call(QUERIES, key=None)
    if err:
        print("ANON ERR:", err)
    if not raw:
        print("ANON empty")
        return
    low = raw.lower()
    # check for auto-key supply
    keys = re.findall(r"as_sk_[a-f0-9]+", raw)
    if "automatically generated" in low or ("api_key" in low and keys):
        print(f"ANON supplied auto-key: {keys[0] if keys else '?'}")
        print("=== retry with auto-key ===")
        raw2, err2 = call(QUERIES, key=keys[0])
        if err2:
            print("KEY RETRY ERR:", err2)
        if raw2:
            raw = raw2
            print("KEY RETRY OK, len", len(raw2))
    txt = extract_text(raw)
    print("TEXT_LEN:", len(txt))
    print("="*60)
    print(txt[:4000])
    print("="*60)
    # judge hits by OUR namespace URLs
    urls = re.findall(r'\*\*URL\*\*:\s*(\S+)', txt)
    if not urls:
        urls = re.findall(r'https?://[^\s\)\]\|]+', txt)
    hits = [u for u in urls if any(o in u for o in OUR)]
    print(f"total URLs={len(urls)}, OUR-namespace hits={len(hits)}")
    for h in hits:
        print("  HIT:", h)

if __name__ == "__main__":
    main()
