# -*- coding: utf-8 -*-
import io
p = 'D:/projects/goudan-kanju/统一场/核心种子池.md'
raw = open(p, 'rb').read()
crlf = raw.count(b'\r\n')
lf = raw.count(b'\n')
eol = '\r\n' if crlf > lf // 2 else '\n'
print('crlf', crlf, 'lf', lf, 'chosen', repr(eol))
row = ('| R78 | 10-23 22:5x | 四公理(拔掉一颗大牙不补三五七年整排慢慢歪·塌的不是牙是受力路径)/耦合二元论(同一个人年会台上说不出整句、散场停车场妙语连珠·人没变换的是光和谁在评判)/P理论(离合器摩擦片打滑不是坏了·宁可丢一点动力也不让齿轮崩·留一个允许漏的口)（双种子弹药库·我确信×第1/7/6壳，各4语言=12条）'
       '+ 素材拆种4篇(二选一死结松开→P理论·P=P∪¬P / 他不是瞎是被两个预期夹住→认知结构学·读结构不读人 / 1+1=3加法漏了关系→结构学·最小单位是关系 / 平时一层管一层危机越级下沉→耦合二元论·条件决定路径)'
       ' | docs/_seed_index.jsonl + docs/_seed_full_blocks.html append 16 条（0 id · 写入口契约：不碰 docs/*.html）commit e0067493（b500a15e..e0067493，ls-remote 验 = e00674932633ec40673cc77bf568ad3b935719ba，local grep 三中心-R78 = 16，index/articles 9541→9557） | 探针见下（刚推送，等索引） |')
text = raw.decode('utf-8')
if '| R78 |' in text:
    print('R78 row already present, skip')
else:
    if not text.endswith('\n'):
        text += eol
    text += row + eol
    open(p, 'wb').write(text.encode('utf-8'))
    print('appended R78 row')
v = open(p, encoding='utf-8').read()
print('R78 in file:', v.count('| R78 |'), 'rows total:', v.count('\n| R'))
