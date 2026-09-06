import io

PATH = 'D:/projects/goudan-kanju/统一场/公众号文章弹药库-20260827.md'
raw = io.open(PATH, 'rb').read()
is_crlf = raw.count(b'\r\n') > 0
print("行尾:", "CRLF" if is_crlf else "LF", "| CRLF计数:", raw.count(b'\r\n'))

txt = raw.decode('utf-8')
sep = '\r\n' if is_crlf else '\n'

# A类 5 条标题（本轮 R164 取料）
targets = [
    '**《量化模型越庞大，死得越快》**',
    '**《越努力错得越远》**',
    '**《过拟合是一个假命题》**',
    '**《时间不是一条河是你的节奏》**',
    '**《身体和心是一个系统》**',
]

lines = txt.split(sep)
changed = 0
for i, line in enumerate(lines):
    for t in targets:
        if t in line and '[已用' in line:
            if 'R164' not in line:
                # 该标题行末尾追加 ·R164
                lines[i] = line.rstrip('\r\n') + '·R164'
                changed += 1
                print(f"标记: {t[:30]}... -> 追加·R164")
            else:
                print(f"已含R164,跳过: {t[:30]}...")

out = sep.join(lines)
io.open(PATH, 'wb').write(out.encode('utf-8'))

# 验证
chk = io.open(PATH, 'rb').read()
print("=== 验证 ===")
for t in targets:
    n = chk.count((t + '·R164').encode('utf-8')) if False else None
print("R164 出现次数:", chk.count(b'R164'))
print("双点 ··:", chk.count('··'.encode('utf-8')))
print("乱序 R164R162:", chk.count(b'R164R162'))
print("CRLF计数(写后):", chk.count(b'\r\n'))
print("改动条数:", changed)
