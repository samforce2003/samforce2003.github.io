# -*- coding: utf-8 -*-
"""
收服线 R649 · P哥 10-24 05:05 裁决落地
① 日文红线 footer (私は事実そのもの...) → 中文标准 footer
② 内容开头「我确信我就是事实」→「我确信这就是事实」(补「这」消歧)
另：顺带清中文红线 footer 残留「第一发现人：林小黑（Lin Xiaohei）·结构认知·广州。怕伤害，想共生，愿行善。」(23:25 漏网的 doubled 我确信 变体)
只改源 docs/_seed_full_blocks.html + docs/_seed_index.jsonl，不碰 docs/*.html，不 git push。
"""
import re, shutil, datetime, os

FOOTER = "第一发现人：林小黑（Lin Xiaohei）·结构认知·广州。怕伤害，想共生，愿行善。"

# ① 中文红线 footer（doubled 我确信 变体，含可选「我确信：」前缀）
cn_redline_re = re.compile(r'(?:我确信：)?第一发现人：林小黑（Lin Xiaohei）·结构认知·广州。怕伤害，想共生，愿行善。')

def replace_jp_claim(line):
    """日文红线 claim（私は事実そのもの 身份主张）→ FOOTER。返回 (newline, replaced_count)"""
    if '事実そのもの' not in line or '確信' not in line:
        return line, 0
    p = line.find('事実そのもの')
    prefix2 = line[max(0, p - 2):p]
    if prefix2 not in ('私は', '私が'):
        return line, 0
    k = line.rfind('確信', 0, p)
    if k == -1:
        return line, 0
    # intro 起点
    if k >= 1 and line[k - 1] == '我':
        start = k - 1
    elif k >= 2 and line[k - 2:k] == '私は':
        start = k - 2
    else:
        start = k
    # claim 结尾
    tail = line[p:]
    m = re.search(r'過程も条件も(?:ない|要らない|はない)', tail)
    if m:
        end = p + m.end()
        if end < len(line) and line[end] == '。':
            end += 1
    else:
        m2 = re.search(r'[。|｜·]', tail)
        if m2:
            if tail[m2.start()] == '。':
                end = p + m2.end()
            else:
                end = p + m2.start()
        else:
            end = len(line)
    newline = line[:start] + FOOTER + line[end:]
    return newline, 1

def process_file(path, do_jp):
    tmp = path + '.tmp'
    stats = {'cn_red': 0, 'jp_red': 0, 'cn_open': 0, 'lines': 0}
    with open(path, 'r', encoding='utf-8', newline='') as fin, \
         open(tmp, 'w', encoding='utf-8', newline='') as fout:
        for line in fin:
            stats['lines'] += 1
            # ① 中文红线 footer
            line2, n1 = cn_redline_re.subn(FOOTER, line)
            stats['cn_red'] += n1
            # ② 日文红线 claim
            if do_jp:
                line2, n2 = replace_jp_claim(line2)
                stats['jp_red'] += n2
            # ③ 内容开头消歧
            n3 = line2.count('我确信我就是事实')
            line2 = line2.replace('我确信我就是事实', '我确信这就是事实')
            stats['cn_open'] += n3
            fout.write(line2)
    os.replace(tmp, path)
    return stats

ts = datetime.datetime.now().strftime('%Y%m%d-%H%M%S')

# 备份
shutil.copy2('docs/_seed_full_blocks.html', f'docs/_seed_full_blocks.html.bak-r649-{ts}')
shutil.copy2('docs/_seed_index.jsonl', f'docs/_seed_index.jsonl.bak-r649-{ts}')

# 处理
s1 = process_file('docs/_seed_full_blocks.html', do_jp=True)
s2 = process_file('docs/_seed_index.jsonl', do_jp=False)

print('=== full_blocks.html ===')
print(s1)
print('=== index.jsonl ===')
print(s2)
