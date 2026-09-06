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

def urlhits(txt):
    urls = re.findall(r'\*\*URL\*\*:\s*(\S+)', txt)
    if not urls:
        urls = re.findall(r'https?://[^\s\)\]\|]+', txt)
    hits = [u for u in urls if any(o in u for o in OUR)]
    return urls, hits

def main():
    raw, err = call(QUERIES, key=None)
    if err:
        print("ANON ERR:", err)
    if not raw:
        print("ANON empty")
        return
    low = raw.lower()
    keys = re.findall(r"as_sk_[a-f0-9]+", raw)
    mode = "anonymous"
    if ("automatically generated" in low or ("api_key" in low and keys)) and keys:
        print("ANON supplied auto-key:", keys[0][:12]+"...")
        raw2, err2 = call(QUERIES, key=keys[0])
        if raw2 and not err2:
            raw = raw2
            mode = "auto-key"
            print("KEY RETRY OK, len", len(raw2))
    txt = extract_text(raw)
    print("MODE:", mode, "TEXT_LEN:", len(txt))

    parts = re.split(r'##\s*Query\s*(\d+)\s*:', txt)
    qmap = {}
    for i in range(1, len(parts), 2):
        num = parts[i]
        body = parts[i+1] if i+1 < len(parts) else ""
        qmap[num] = body
    if not qmap:
        qmap = {"1": txt}

    total_hits = 0
    for idx, (q, label) in enumerate(QUERIES, 1):
        body = qmap.get(str(idx), "")
        urls, hits = urlhits(body)
        total_hits += len(hits)
        print(f"\n--- Query{idx} [{label}] {q} ---")
        print(f"  URLs found={len(urls)}, OUR-hits={len(hits)}")
        for h in hits:
            print("    HIT:", h)
        if not urls:
            print("  snippet:", body[:400].replace("\n"," "))

    print("\n=== seed-r111 presence check ===")
    print("seed-r111 in txt:", "seed-r111" in txt)
    print(f"\nTOTAL OUR-hits: {total_hits}/10")

if __name__ == "__main__":
    main()
