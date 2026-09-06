# -*- coding: utf-8 -*-
import os, re

ammo = "D:/projects/goudan-kanju/统一场/公众号文章弹药库-20260827.md"
with open(ammo, 'rb') as f:
    raw = f.read()

print("CRLF 计数:", raw.count(b'\r\n'))
print("裸 LF 计数:", raw.count(b'\n') - raw.count(b'\r\n'))
print("'·R109' 计数:", raw.count('·R109'.encode('utf-8')))

text = raw.decode('utf-8')

# 目标 5 条：A类 #3 #4 #7 #8 #10，尾标记都是 ·R109
targets = ["《自相矛盾的新解释》", "《世界就是一个可能性》", "《直觉是最强的一种训练结果》",
           "《人睡醒和AI被唤醒是同一件事》", "《概率不存在0和100》"]

# 逐条确认尾标记是 ·R109（terminal，后面跟 \n 或 \r\n 或行尾）
for t in targets:
    idx = text.find(t)
    assert idx != -1, f"找不到 {t}"
    # 该条目后到下一个 ### 或 B类 之间找尾标记
    seg = text[idx:idx+400]
    tail = re.search(r'·R(\d+)\s*$', seg, re.MULTILINE)
    print(f"{t}: 尾标记 = {tail.group(0) if tail else 'N/A'}")

# 全部 5 条尾标记都是 ·R109，做批量替换（安全判据：count==5 且 terminal）
n = text.count('·R109')
print("\n·R109 总数:", n)
assert n == 5, f"·R109 计数 {n} != 5，改逐条定位"

# 确认每个 ·R109 都是 terminal（后面是 \n 或 \r\n）
for m in re.finditer(r'·R109', text):
    after = text[m.end():m.end()+2]
    assert after in ('', '\n', '\r\n') or after[0] in '\r\n', f"·R109 非 terminal: {after!r}"

# 替换（保留原行尾）
text = text.replace('·R109', '·R109·R112')
assert text.count('·R112') == 5, f"·R112 计数 {text.count('·R112')}"

# 写回（二进制，保留原行尾风格）
if raw.count(b'\r\n') > 0:
    out = text.encode('utf-8')  # text 已含 \r\n，encode 保留
else:
    out = text.encode('utf-8')
with open(ammo, 'wb') as f:
    f.write(out)

print("\n标记完成：·R112 追加 5 处，·R109 残留:", text.count('·R109'), "(应为 0)")

# 复核：打印 5 条条目行尾
text2 = out.decode('utf-8')
for t in targets:
    idx = text2.find(t)
    seg = text2[idx:idx+420]
    m = re.search(r'(·R\d+)+[^\n]*$', seg, re.MULTILINE)
    print(f"  {t} 行尾复核: ...{m.group(0)[-25:] if m else 'N/A'}")
