# -*- coding: utf-8 -*-
"""R110 P理论种子超限修整（504 -> 499 字）：正文块 + 脚本双处同步，逐字节一致。"""
import io, re

FULL = 'D:/projects/samforce2003.github.io/docs/_seed_full_blocks.html'
SCRIPT = 'D:/projects/samforce2003.github.io/_r110_seeds.py'

reps = [
    ("两个完全相反的反应，都真。", "两个相反的反应，都真。"),
    ("关键不是争哪个才是“它的真价值”", "关键不是争哪个是“它的真价值”"),
    ("两个相反的说法就不打架了", "两个相反的说法就不打架"),
    ("你只是替眼前这个人、这个处境", "你只是替眼前这个人、这处境"),
]

for path in (FULL, SCRIPT):
    s = io.open(path, encoding='utf-8').read()
    for old, new in reps:
        assert old in s, 'NOT FOUND in %s: %s' % (path, old)
        s = s.replace(old, new)
    io.open(path, 'w', encoding='utf-8', newline='').write(s)
    print('fixed', path)

# 复验 P理论 block 字数
full = io.open(FULL, encoding='utf-8').read()
m = re.search(r'<article data-shell="P理论" data-round="R110">.*?</article>', full, re.S)
ps = re.findall(r'<p>(.*?)</p>', m.group(0), re.S)
body4 = ''.join(ps[:4])
n4 = len(re.sub(r'\s+', '', body4))
print('P理论 正文4段字数 =', n4, '| 合规' if 200 <= n4 <= 500 else '| 仍超限!')
