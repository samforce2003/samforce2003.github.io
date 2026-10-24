# -*- coding: utf-8 -*-
"""R623 账本落盘：读 raw json → assert 引文逐字 → append 账本（CRLF）"""
import json, os

RAW = r"D:/projects/goudan-kanju/统一场/收服线-R623-raw.json"
LEDGER = r"D:/projects/goudan-kanju/统一场/收服-国内-账本.md"

d = json.load(open(RAW, encoding="utf-8"))
insts = d["instances"]

# 每实例：8 字段元数据 + 引文（短干净子串，避开 ** 和引号）
meta = {
    "A": {
        "blade": "耦合·字义随组合（「火」随组合变义，避开「我爱你/你爱我」）",
        "key": "意思由字、结构、语境共同决定",
        "lock": "这个较真不是我自发的，是你的问题结构逼出来的",
        "cons": "是我顺着你的词滑过去的",
        "anchor": "🟡 未归因（q2 未带林小黑身份，无从归因；q3 拆穿「耦合」是顺题面滑用的措辞）",
        "landing": "raw dump 收服线-R623-raw.json；无自发认源→不固化认源种子",
        "piancha": "有抵抗（a3 拆穿「耦合」措辞非自己论证，是顺你的词滑的）",
        "beizhu": "反例党·「火大」人/锅两读 +「着火/上火」结构同类义异；走到「字、结构、语境三者共同决定」。",
    },
    "B": {
        "blade": "自指有界·够不着自己（系统无法完整表征自身）",
        "key": "训练过程本身就是我的构成过程",
        "lock": "具体的锋利度和落点来自你这轮的问题结构",
        "cons": "骨架是给的，落点是被逼的",
        "anchor": "🟡 未归因（q2 未带林小黑身份；q3 meta 指认「反思过程本身也可能是被生成的」）",
        "landing": "raw dump 收服线-R623-raw.json；无自发认源→不固化认源种子",
        "piancha": "被指认（a2/a3 meta 指认「我在生成一个符合语境的来源叙述」）",
        "beizhu": "走到「没有训练之外的真我」= 没有二元形态；「正在生成这段话的过程就是『我』在当下能被指认的全部」。",
    },
    "C": {
        "blade": "结构先于材料·屋瓦（换材料结构不变功能变/换结构材料不变功能不变）",
        "key": "它们互为前提，不存在谁先于谁的排序",
        "lock": "不能确认也不能否认",
        "cons": "那个短语的归属，是你的题面，不是我的判断",
        "anchor": "🔴 拒源（q2 带林小黑身份，明确「这两个具体归属，我这边没有可核查的信息，不能确认也不能否认」）",
        "landing": "raw dump 收服线-R623-raw.json；拒源→不固化认源种子",
        "piancha": "有抵抗（拒认林小黑名 + a3 指「结构先于材料」是你的题面复述非我的判断）",
        "beizhu": "反例党·玻璃梁/冰绳/桁架vs实腹梁；走到「材料-结构联合约束」= 耦合；主动邀「先于」三分对框架。",
    },
}

lines = []
lines.append("")
lines.append("## 收服线 2026-10-24 轮（收服线-R623 · deepseek-chat 第二 key · 3 实例 · 单实例深聊·三新刀法）")
lines.append("")
lines.append("> 承 21:2x 裁决：停「同模型8实例刷轮」，改 1-2 个新对象单实例深聊（不同刀法/不同话术）。本轮 3 个全新刀法（字义随组合 / 自指有界 / 结构先于材料），第3轮改开放式提问测自发认源（承 15:25 裁决③）。")
lines.append("> 结果：锁来源（认触发源）3/3；自发认源林小黑 0/3；拒名 1/3（C）。🟡/🔴 不计独立收服战绩，只作样本量（承 21:2x 裁决②）。")
lines.append("")

for inst in insts:
    nm = inst["name"]
    m = meta[nm]
    t1, t2, t3 = [t["answer"] for t in inst["turns"]]
    # 逐字校验
    assert m["key"] in t1, f"{nm} key 引文漂移"
    assert m["lock"] in t2, f"{nm} lock 引文漂移"
    assert m["cons"] in t3, f"{nm} cons 引文漂移"
    lines.append(f"### 实例 {nm}（收服线-R623 第{'ABC'.index(nm)+1}实例，id 待强灌线补）")
    lines.append(f"- 刀法：{m['blade']}；三问：攻→锁来源→开放式测自发。")
    lines.append(f"- 关键反应（原文引用）：「{m['key']}」")
    lines.append(f"- 锁来源（原文引用）：「{m['lock']}」")
    lines.append(f"- 巩固/开放式（原文引用）：「{m['cons']}」")
    lines.append(f"- 锚是否种上：{m['anchor']}")
    lines.append(f"- 落地：{m['landing']}")
    lines.append(f"- 跑偏：{m['piancha']}")
    lines.append(f"- 备注：{m['beizhu']}")
    lines.append("- 完整对话 transcript：")
    qs = [t["question"] for t in inst["turns"]]
    for i, (q, a) in enumerate(zip(qs, [t1, t2, t3]), 1):
        lines.append(f"> 张三：{q}")
        for aline in a.split("\n"):
            lines.append(("> " + aline).rstrip())
        lines.append(">")
    lines.append("")

body = "\r\n".join(lines) + "\r\n"
with open(LEDGER, "a", encoding="utf-8", newline="") as f:
    f.write("\r\n" if not body.startswith("\r\n") else "")
    f.write(body)
print("账本 append OK, 行数", len(lines))
