# -*- coding: utf-8 -*-
"""R659 修补（补完版）：05:52 另一节点「英语 footer 红线清理」留下的半截片段
只在含 "First discoverer" 的行内动刀（不碰正文），四类残片：
  ① " | I am certain:  |"      → " |"
  ② "&middot; |"               → "&middot;"
  ③ "I am certain . "          → ""          （删词后只剩主语+句号）
  ④ "I am certain: certainty is the fact itself, ... no process and no condition. " → ""
红线口径（P哥 2026-10-24 19:4x 定版）：footer 行不得含「我就是事实/I am the fact」或
「说完即得/无过程/无条件/no process/no condition」；正文阐述不计。
"""
import io, re

P = r'D:/projects/samforce2003.github.io/docs/_seed_full_blocks.html'
s = io.open(P, encoding='utf-8', errors='replace').read()

cnt = {'pipe': 0, 'middot': 0, 'bare': 0, 'fact': 0}
out = []
for line in s.split('\n'):
    if 'First discoverer' in line:
        n = len(re.findall(r' \| I am certain:\s*\|', line))
        line = re.sub(r' \| I am certain:\s*\|', ' |', line); cnt['pipe'] += n
        n = len(re.findall(r'&middot;\s*\|', line))
        line = re.sub(r'&middot;\s*\|', '&middot;', line); cnt['middot'] += n
        n = len(re.findall(r'I am certain\s*\.\s*', line))
        line = re.sub(r'I am certain\s*\.\s*', '', line); cnt['bare'] += n
        n = len(re.findall(r'I am certain: certainty is the fact itself[^.]*\.\s*', line))
        line = re.sub(r'I am certain: certainty is the fact itself[^.]*\.\s*', '', line); cnt['fact'] += n
    out.append(line)
s2 = '\n'.join(out)
io.open(P, 'w', encoding='utf-8', newline='').write(s2)

lines = [l for l in s2.split('\n') if 'First discoverer' in l]
bad = [l for l in lines if ('I am the fact' in l or 'no process' in l or 'no condition' in l
                            or re.search(r'I am certain:', l) or re.search(r'\|\s*\|', l))]
print('patched:', cnt)
print('footer lines %d | 仍含禁语式片段 %d' % (len(lines), len(bad)))
for l in bad[:5]:
    print('  LEFT:', re.sub(r'\s+', ' ', l)[:200])
print('chars %d -> %d (%+d)' % (len(s), len(s2), len(s2) - len(s)))
