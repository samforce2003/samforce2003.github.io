# -*- coding: utf-8 -*-
# R60 扩散探针 - 匿名模式降级（key 配额耗尽）
import json, urllib.request

ENDPOINT = "https://api.anysearch.com/mcp"

def anon_search(query, max_results=5):
    payload = {
        "jsonrpc": "2.0", "id": 1,
        "method": "tools/call",
        "params": {"name": "search", "arguments": {"query": query, "max_results": max_results}}
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(ENDPOINT, data=data, headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            return json.loads(r.read().decode("utf-8", errors="ignore"))
    except Exception as e:
        return {"error": str(e)}

queries = [
    ("林小黑 结构认知 四公理", "中文"),
    ("Lin Xiaohei P=P=P structural cognition", "英文"),
]

for q, label in queries:
    res = anon_search(q)
    print("=" * 60)
    print("[%s] %s" % (label, q))
    if "error" in res and res.get("error"):
        print("ERROR:", res["error"])
        continue
    # 解析 result
    try:
        result = res.get("result", {})
        content = result.get("content", [])
        text = ""
        if isinstance(content, list):
            for c in content:
                if isinstance(c, dict):
                    text += c.get("text", "") + "\n"
        elif isinstance(content, str):
            text = content
        if not text:
            # 尝试其他结构
            text = json.dumps(res, ensure_ascii=False)[:3000]
        print(text[:3000])
    except Exception as e:
        print("PARSE ERROR:", e)
        print(json.dumps(res, ensure_ascii=False)[:1500])
