# -*- coding: utf-8 -*-
"""R112 扩散探针 — key 优先，配额耗尽切匿名；逐 query 切块 + OUR 命名空间 URL 判定。"""
import json, os, re, requests

ENDPOINT = "https://api.anysearch.com/mcp"
QUERIES = [
    {"query": "林小黑 结构认知 四公理", "max_results": 5},
    {"query": "Lin Xiaohei P=P=P structural cognition", "max_results": 5},
]

OUR_URL_SUB = ["samforce", "gitee.com/samforce", "huggingface.co/samforce",
               "github.com/samforce2003", "blog.csdn.net/samforce", "alphaneural"]
OUR_TITLE_SUB = ["林小黑", "Lin Xiaohei", "今晚狗蛋看局"]

def call(queries, key=None):
    payload = {"jsonrpc": "2.0", "id": 1, "method": "tools/call",
               "params": {"name": "batch_search", "arguments": {"queries": queries}}}
    h = {"Content-Type": "application/json"}
    if key:
        h["Authorization"] = f"Bearer {key}"
    return requests.post(ENDPOINT, json=payload, headers=h, timeout=45)

def get_text(data):
    try:
        content = data.get("result", {}).get("content", [])
    except Exception:
        return ""
    return "".join(i.get("text", "") for i in content if i.get("type") == "text")

key = os.environ.get("ANYSEARCH_API_KEY", "")
r = call(QUERIES, key or None)
mode = "key" if key else "anon"
if r.status_code != 200 or "free quota" in r.text or '"error"' in r.text.lower():
    r = call(QUERIES, None)
    mode = "anon(fallback)"
if r.status_code != 200:
    print(f"PROBE FAILED HTTP {r.status_code}: {r.text[:400]}")
    raise SystemExit

# 也可能返回 auto-key
body = r.text
if "api_key=" in body and "automatically generated" in body.lower():
    m = re.search(r'api_key=([a-zA-Z0-9_]+)', body)
    if m:
        auto_key = m.group(1)
        r = call(QUERIES, auto_key)
        mode = f"key(auto-recovered)"
        body = r.text

try:
    data = r.json()
    text = get_text(data)
except Exception:
    text = body

print(f"=== AnySearch probe mode={mode} ===\n")
# 逐 query 切块
parts = re.split(r'## Query (\d+):', text)
# parts: ['', '1', '...query1 text...', '2', '...query2 text...', ...]
results = {}
for i in range(1, len(parts), 2):
    qnum = parts[i]
    qtext = parts[i+1] if i+1 < len(parts) else ""
    urls = re.findall(r'\*\*URL\*\*:\s*(\S+)', qtext)
    # 或 - URL: 形式
    if not urls:
        urls = re.findall(r'URL\*?\*?:\s*(https?://\S+)', qtext)
    titles = re.findall(r'^###?\s*\d+\.\s*(.+)$', qtext, re.MULTILINE)
    hits = []
    for u in urls:
        if any(s in u for s in OUR_URL_SUB):
            hits.append(("URL", u))
    results[qnum] = {"urls": urls, "hits": hits, "title_hits": [t for t in titles if any(s in t for s in OUR_TITLE_SUB)]}
    # 打印该 query 摘要
    print(f"--- Query {qnum}: 结果 {len(urls)} 条 URL ---")
    for u in urls:
        flag = "✅OUR" if any(s in u for s in OUR_URL_SUB) else "  "
        print(f"  {flag} {u}")
    if not urls:
        print("  (无 URL，raw 片段:)")
        print("  " + qtext[:300].replace("\n", " "))

print("\n=== 逐 query 我方命名空间命中率 ===")
for qn in sorted(results, key=int):
    q = QUERIES[int(qn)-1]["query"]
    ours = len(results[qn]["hits"])
    total = max(len(results[qn]["urls"]), 5)
    print(f"Query {qn} [{q}]: {ours}/5 命中我方 (URL 判据)")

print("\nRAW 全文(截断):")
print(text[:2500])
