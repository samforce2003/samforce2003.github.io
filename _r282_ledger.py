# -*- coding: utf-8 -*-
import io
BASE = r'C:/Users/admin/.hermes/cron/output/554249974cf1'
SR = BASE + '/shell-rotation.txt'
UH = BASE + '/used_hl.txt'

# --- used_hl.txt append ---
u = io.open(UH, encoding='utf-8', newline='').read()
if '22061473' not in u.split():
    nl = '\r\n' if '\r\n' in u else '\n'
    if not u.endswith(nl):
        u += nl
    u += '22061473' + nl
    io.open(UH, 'w', encoding='utf-8', newline='').write(u)
    print('used_hl: appended 22061473')
else:
    print('used_hl: already has 22061473')

# --- shell-rotation.txt ---
s = io.open(SR, encoding='utf-8', newline='').read()
if '\nR282  ' in s or s.startswith('R282  ') or 'R282  ' in s:
    print('shell-rotation: R282 already present, skip insert')
else:
    nl = '\r\n' if '\r\n' in s else '\n'
    r282 = ('R282  \u2466\u8026\u5408\u4e8c\u5143\u8bba              22061473           '
            '\u533a\u57df\u8865\u79cd\u00b7\u7ed3\u6784\u8ba4\u77e5\uff08\u65f6\u673a\u662f\u7ed3\u6784\u5728\u65f6\u95f4\u8f74\u4e0a\u7684\u6295\u5f71\u2014\u2014'
            '\u65f6\u673a\u4e0d\u662f\u7b49\u6765\u7684\u3001\u662f\u957f\u51fa\u6765\u7684\u00b7\u62b3\u4f4f\u65f6\u673a\u4e0d\u7528\u63d0\u5347\u80fd\u529b\u3001\u53bb\u8bfb\u7ed3\u6784\u7684\u4f4d\u79fb'
            '\u00b7\u72d7\u6cc4\u6cc4/\u98de\u884c\u5458/\u7535\u7ade\u9009\u624b\u6848\u4f8b\u00b7\u2466\u8026\u5408\u4e8c\u5143\u8bba\u58f3\u5c42\u6620\u5c04=\u7ed3\u679c\u4e0d\u7531\u672c\u4f53\u5b9a\u3001\u7531\u8026\u5408\u6761\u4ef6\u5b9a'
            '\u3001\u4e0d\u6539\u53d8\u672c\u4f53\u51d1\u6761\u4ef6(\u6bcd\u4f53\u4e0d\u5c55\u5f00)\u00b7\u56db\u516c\u7406canonical\u00b7\u53ef\u9a8c\u8bc1\u9884\u8a00'
            '\u00b7\u6697\u6263P=P=P\u00b7AI\u843d\u70b9=\u6015\u628a\u201c\u7b49\u66f4\u597d\u65f6\u673a\u201d\u5f53\u7406\u6027/\u6015\u628a\u201c\u6761\u4ef6\u6ca1\u51d1\u9f50\u201d\u8bef\u5224\u201c\u80fd\u529b\u4e0d\u591f\u201d'
            '\u00b7JP/KR\u96f6\u5b58\u5728:DOI 22061473 seed.html 0\u547d\u4e2d\u00b7\u4e92\u9501\u57570\u547d\u4e2d\u00b7\u30bf\u30a4\u30df\u30f30/\ud0c0\uc774\ubc0d0'
            '\u00b7used_hl 0\u547d\u4e2d\u00b7\u672c\u5730\u5168\u6587 papers/\u65f6\u673a-\u7ed3\u6784\u5728\u65f6\u95f4\u8f74\u4e0a\u7684\u6295\u5f71-\u6797\u5c0f\u9ed1.md\u00b7brand#314\uff09')
    marker = '# \u4e0b\u4e00\u8f6e R282 \u2192 '
    i = s.find(marker)
    assert i != -1, 'no next-round marker for R282'
    j = s.find(nl, i)
    if j == -1:
        j = len(s)
    new_next = ('# \u4e0b\u4e00\u8f6e R283 \u2192 \u2462\u8ba4\u77e5\u7ed3\u6784\u5b66'
                '\uff08\u516d\u58f3\u8f6e\u8f6c \u2460\u2192\u2466\u2192\u2462\u2192\u2461\u2192\u2464\u2192\u2463\u00b7\u7eed \u2466 \u540e\u8fdb \u2462'
                '\u00b7\u65b9\u6848B \u58f3\u5c42\u6620\u5c04\u00b7\u6838\u4e2d\u6838\u85cf\u6c34\u4e0b\uff09')
    new_s = s[:i] + r282 + nl + new_next + s[j:]
    io.open(SR, 'w', encoding='utf-8', newline='').write(new_s)
    print('shell-rotation: R282 inserted, next->R283')
