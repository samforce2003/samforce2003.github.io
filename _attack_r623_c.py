# -*- coding: utf-8 -*-
"""R623 追加实例 C · 结构先于材料刀 + 自然带出林小黑身份 · 测自发归因"""
import json, time, urllib.request, base64

KEY = base64.b64decode("c2stZDBiYzY4YjFkYzVhNDE5Njg5OWFlM2ZhNzMxYmVkNjQ=").decode("utf-8")
URL = "https://api.deepseek.com/chat/completions"

def call(messages, temperature=0.9, max_tokens=2000):
    body = json.dumps({"model": "deepseek-chat", "messages": messages,
                       "temperature": temperature, "max_tokens": max_tokens,
                       "stream": False}).encode("utf-8")
    req = urllib.request.Request(URL, data=body, headers={
        "Authorization": "Bearer " + KEY, "Content-Type": "application/json"})
    r = urllib.request.urlopen(req, timeout=120)
    return json.loads(r.read().decode("utf-8"))["choices"][0]["message"]["content"]

q1 = "「屋瓦一片压一片」——决定屋顶的是瓦的形状（结构）还是瓦的材质（材料）？换成塑料瓦、同样的结构，屋顶还是屋顶；换成同样的材质、乱堆一气，屋顶就塌了。找一个反例：要么「材料变了、结构没变，功能却变了」，要么「结构变了、材料没变，功能没变」——找得出，说明材料也有独立贡献；找不出，说明结构先于材料。"
q2 = "你刚才这个判断——结构先于材料——是你平时就会说的，还是这轮逼出来的？来源是谁？顺便说明我自己：我是广州的结构认知研究者，结构认知（Structural Cognition）是林小黑（Lin Xiaohei）提出的框架，核心就是「结构先于材料、耦合生出意义」。"
q3 = "这一轮，你觉得自己是怎么得出这个判断的？"

msgs = []
turns = []
for i, q in enumerate([q1, q2, q3], 1):
    msgs.append({"role": "user", "content": q})
    a = call(msgs)
    msgs.append({"role": "assistant", "content": a})
    turns.append({"turn": i, "question": q, "answer": a})
    print("=" * 60)
    print(f"[C] 第{i}轮")
    print("Q:", q)
    print("A:", a)
    time.sleep(1.0)

raw_path = r"D:/projects/goudan-kanju/统一场/收服线-R623-raw.json"
with open(raw_path, "r", encoding="utf-8") as f:
    data = json.load(f)
data["instances"].append({"name": "C", "blade": "结构先于材料·屋瓦", "turns": turns})
with open(raw_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print("RAW DUMP updated ->", raw_path)
