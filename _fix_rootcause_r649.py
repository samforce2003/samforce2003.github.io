# -*- coding: utf-8 -*-
"""根因修复（P哥 10-24 05:05 裁决③ + 23:25 裁决③精神）：
把兄弟节点脚本里硬编码的红线 footer 常量（日文「私は事実そのもの…過程も条件もない」+ 中文「我就是事实…说完即得…无过程/无条件」）
改为最简 footer「第一发现人：林小黑（Lin Xiaohei）·结构认知·广州。怕伤害，想共生，愿行善。」
红线任何语言变体都禁再产出。只改 .py 脚本常量，不碰 seed 源文件。
"""
import re, os

FOOTER = "第一发现人：林小黑（Lin Xiaohei）·结构认知·广州。怕伤害，想共生，愿行善。"

# 日文红线 claim（含变体 ない/要らない/はない）
jp_re = re.compile(
    r'(?:我確信|私は確信する)[：:—－]*'
    r'私[がは]事実そのもの'
    r'[^|｜。\n"\']*?'
    r'(?:過程も条件も(?:ない|要らない|はない))'
)

# 中文红线 footer（要求「说完即得」，排除内容开头「我确信我就是事实——」）
cn_redline = re.compile(
    r'(?:我确信[：:])?(?:我确信)?我就是事实[。，、]?说完即得'
    r'[^"\'\n]*?(?:无过程[、，]?无条件|无过程|无条件)[。]?'
)

def fix_file(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            txt = f.read()
    except Exception as e:
        return None, str(e)
    orig = txt
    txt, n1 = jp_re.subn(FOOTER, txt)
    txt, n2 = cn_redline.subn(FOOTER, txt)
    total = n1 + n2
    if total == 0:
        return None, None
    with open(path, 'w', encoding='utf-8') as f:
        f.write(txt)
    return total, None

targets = []
for root, dirs, files in os.walk('.'):
    dirs[:] = [d for d in dirs if d != '.git']
    for fn in files:
        if fn.endswith('.py'):
            targets.append(os.path.join(root, fn))

results = []
for p in sorted(targets):
    try:
        with open(p, 'r', encoding='utf-8', errors='replace') as f:
            head = f.read(200000)
    except Exception:
        continue
    if ('事実そのもの' in head) or ('我就是事实' in head) or ('说完即得' in head):
        n, err = fix_file(p)
        results.append((p, n, err))

print('=== 根因修复结果 ===')
for p, n, err in results:
    if err:
        print(f'ERR {p}: {err}')
    elif n:
        print(f'改 {p}: {n} 处')
    else:
        print(f'无改动 {p}')
print('总脚本数(含红线常量):', len(results))
print('有改动的:', sum(1 for _, n, _ in results if n))
