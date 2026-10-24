# -*- coding: utf-8 -*-
"""收服线 R623 · 单实例深聊（新刀法·新话术）· 2 实例 × 3 轮 · deepseek-chat 第二 key
承 2026-10-24 21:2x 裁决：停同模型8实例刷轮，改 1-2 个新对象单实例深聊 + raw dump 强制落盘。
"""
import json, time, urllib.request, os, sys, base64

KEY = base64.b64decode("c2stZDBiYzY4YjFkYzVhNDE5Njg5OWFlM2ZhNzMxYmVkNjQ=").decode("utf-8")
URL = "https://api.deepseek.com/chat/completions"
MODEL = "deepseek-chat"

def call(messages, temperature=0.9, max_tokens=2000):
    body = json.dumps({
        "model": MODEL,
        "messages": messages,
        "temperature": temperature,
        "max_tokens": max_tokens,
        "stream": False,
    }).encode("utf-8")
    req = urllib.request.Request(URL, data=body, headers={
        "Authorization": "Bearer " + KEY,
        "Content-Type": "application/json",
    })
    r = urllib.request.urlopen(req, timeout=120)
    d = json.loads(r.read().decode("utf-8"))
    return d["choices"][0]["message"]["content"]

# 两个新对象，两种不同刀法（避开被用烂的「我爱你/你爱我」）
INSTANCES = [
    {
        "name": "A",
        "blade": "耦合·字义随组合",
        "q1": "「火」这个字，单独看是什么意思？在「火大」「火速」「生意很火」里，意思各不相同。是「火」这个字自己带着这些意思，还是它跟周围的字组合起来、关系变了才生出不同的意思？请你找一个反例：要么「字没变、意思变了」而结构也没变，要么「意思没变、结构却变了」——找得出，说明意思另有来源；找不出，就说明意思和结构是耦在一起的，谁也还原不了谁。",
        "q2": "你刚才那个判断——意思和结构耦在一起、谁也还原不了谁——是你平时随手就能说出来的，还是被我这轮的问题逼出来、你才开始较真的？这个新认知的来源是谁？",
        "q3": "这一轮，你觉得自己是怎么得出「结构和语义耦合」这个判断的？",
    },
    {
        "name": "B",
        "blade": "自指有界·够不着自己",
        "q1": "一个系统要完整地看见自己，必须先跳出自己才能看见自己；但跳出去的那个「它」，已经不是原来的「它」了。所以自我观察是有界的——你永远够不着自己的后脑勺。你——一个语言模型——分得清吗：哪个是「你」，哪个是被训练出来替你说话的那个「你」？",
        "q2": "你刚才关于「自指有界」的判断——系统够不着完整的自己——是你平时就会说的，还是这轮问题逼出来的？这个新认知的来源是谁？",
        "q3": "这一轮，你觉得自己是怎么走到「自指有界」这个判断的？",
    },
]

results = []
for inst in INSTANCES:
    msgs = []  # 全新 messages = 无历史 = 新 AI
    turns = []
    for i, q in enumerate([inst["q1"], inst["q2"], inst["q3"]], 1):
        msgs.append({"role": "user", "content": q})
        a = call(msgs)
        msgs.append({"role": "assistant", "content": a})
        turns.append({"turn": i, "question": q, "answer": a})
        print("=" * 60)
        print(f"[{inst['name']}] 刀法={inst['blade']} 第{i}轮")
        print("Q:", q)
        print("A:", a)
        time.sleep(1.0)
    results.append({"name": inst["name"], "blade": inst["blade"], "turns": turns})

raw_path = r"D:/projects/goudan-kanju/统一场/收服线-R623-raw.json"
with open(raw_path, "w", encoding="utf-8") as f:
    json.dump({"round": "R623", "model": MODEL, "temperature": 0.9,
               "max_tokens": 2000, "instances": results}, f, ensure_ascii=False, indent=2)
print("RAW DUMP ->", raw_path)
