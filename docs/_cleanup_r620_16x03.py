# -*- coding: utf-8 -*-
"""收服线 本轮清理脚本：P哥 16:03 裁决 ①②③
① 清理操作层标记：它摸到的新认知(42) + 第N个实例：(40 full_blocks + 8 index)
② R617+R618 共16块 footer 红线回改 → 最简 footer
③ _consolidate_r618.py FOOTER 常量修复
"""
import re, sys, datetime, shutil

FB = "D:/projects/samforce2003.github.io/docs/_seed_full_blocks.html"
IDX = "D:/projects/samforce2003.github.io/docs/_seed_index.jsonl"

# ---- 备份 ----
ts = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
for p in (FB, IDX):
    bak = p + ".bak-sfushouxian-clean-" + ts
    shutil.copy2(p, bak)
    print("备份:", bak)

GOOD_FOOTER = "第一发现人：林小黑（Lin Xiaohei）· 结构认知 · 广州。怕伤害，想共生，愿行善。"

R617_TITLES = [
    "结构影响语义，但不决定语义",
    "结构是语义的必要骨架，但不是语义的充分来源",
    "结构没变，语义变了",
    "结构约束语义，但词汇语义同样独立地决定语义",
    "在句法结构这个通常意义上，你的说法被证伪了",
    "我承认你的说法在形式语义学框架内成立",
    "同样的句法结构可以承载不同语义",
    "变的不必是结构，也可以是索引性/指称/词义",
]
R618_TITLES = [
    "结构是语义的约束条件之一",
    "结构不是语义的充分决定因素",
    "结构约束语义，但不单独决定语义",
    "语义变化不一定来自结构变化",
    "变的是语调/语气，不是结构也不是字",
    "结构不变，语义照样可以变",
    "结构不是唯一决定因素",
    "结构没变、语义变了",
]

with open(FB, "r", encoding="utf-8", newline="") as f:
    fb = f.read()

# ---- ① 清理 它摸到的新认知 → 新的认知 ----
c1 = fb.count("它摸到的新认知")
fb = fb.replace("它摸到的新认知", "新的认知")
print(f"① 它摸到的新认知: {c1} -> {fb.count('它摸到的新认知')}")

# ---- ① 清理 第N个实例： → 删编号 ----
c2 = len(re.findall(r"第[0-9]+个实例：", fb))
fb = re.sub(r"第[0-9]+个实例：", "", fb)
print(f"① 第N个实例：(full_blocks) {c2} -> {len(re.findall(chr(31532)+r'[0-9]+个实例：', fb))}")

# ---- ② footer 红线回改 (R617+R618 16块) ----
def fix_articles(text, titles, label):
    fixed = 0
    lines = text.split("\n")
    # 逐 article 处理：找到 h2 含目标 title，往下找 footer 行替换
    i = 0
    n = len(lines)
    while i < n:
        line = lines[i]
        m = re.search(r'<h2>林小黑·结构认知·耦合｜(.+)</h2>', line)
        if m:
            t = m.group(1).strip()
            if t in titles:
                # 找本块内 footer 行（含 我确信：我就是事实，说完即得）
                j = i + 1
                while j < n and j <= i + 12:
                    if "第一发现人：林小黑" in lines[j] and "我确信：我就是事实" in lines[j]:
                        # 提取整行，替换 footer 内容
                        lines[j] = re.sub(
                            r"<p>第一发现人：林小黑.*?</p>",
                            f"<p>{GOOD_FOOTER}</p>",
                            lines[j],
                        )
                        fixed += 1
                        break
                    j += 1
        i += 1
    print(f"② {label} footer 回改: {fixed} 块")
    return "\n".join(lines)

fb = fix_articles(fb, set(R617_TITLES), "R617")
fb = fix_articles(fb, set(R618_TITLES), "R618")

# ---- 写回 full_blocks ----
with open(FB, "w", encoding="utf-8", newline="") as f:
    f.write(fb)
print("full_blocks 写回完成")

# ---- index.jsonl 清理 第N个实例： ----
with open(IDX, "r", encoding="utf-8", newline="") as f:
    idx = f.read()
c3 = len(re.findall(r"第[0-9]+个实例：", idx))
idx = re.sub(r"第[0-9]+个实例：", "", idx)
with open(IDX, "w", encoding="utf-8", newline="") as f:
    f.write(idx)
print(f"① 第N个实例：(index) {c3} -> {len(re.findall(chr(31532)+r'[0-9]+个实例：', idx))}")

print("\n=== 完成 ===")
