# -*- coding: utf-8 -*-
"""R146 翻炒清单补记：append [x] 一条 + 更新头部「已翻炒」计数。"""
import io, re

path = 'D:/projects/goudan-kanju/统一场/翻炒清单.md'
line = ('- [x] DeepSeek Harness（dsh）摸结构心得「压缩≠记忆·腾地方与记住是两码事」'
        '（`待分发素材库/摸结构心得/2026-11-17-DeepSeek-Harness.md`·9513B·2026-11-17·摸结构心得·未标已拆/已发·从未进过清单与账本，本轮补入；'
        '"腾地方解决装不下／记住解决想不起来／一切皆插件却装不下记忆／靠改不动活着"此前零次；'
        'dsh 官方仓库 README/SAFETY/architecture 等内部技术细节与"大肥鱼"等具体人名/平台名整段剔除，只留"压缩≠记忆"这一根骨头；'
        '与已炒《你不在你身体里你在你跟别人的缝里》（R145·关系是本源/换皮故事）、《那道缝不是破了是气门》（R144·留缝/气门）、《断干净是句假话》（R143·过渡场）均不同，这篇讲"腾地方与记住是两码事、靠改不动活着"（记忆/锚切面），四者全避）'
        '→ 换成：科普短文《你删掉的那些东西，根本没记住过——"腾地方"和"记住"是两码事》'
        '（手机相册删照片 → 腾地方 vs 记住 → dsh 一切皆插件却做不出记忆、60 条评论全在造轮子 → 我们都在用腾地方假装记住：笔记/收藏夹/截图 → 给自己留一根改不动的钉子；'
        '边界：不是叫你别清理、不是叫你什么都记，是别拿"腾地方"冒充"记住"；'
        '先血肉后骨架，黑话出圈：压缩→腾地方、记忆→记住/改不动的钉子、可逆副作用→装进去拆了跟着消失、锚→根/钉子；'
        '落款第一发现人：林小黑（Lin Xiaohei），神科学第一发现者（结构认知是其来时路/骨））')

txt = io.open(path, encoding='utf-8').read()

# 写盘前断言：核心论断片段此前零次（判整体，不判末行）
for k in ['腾地方和记住是两码事', '改不动的钉子', '压缩≠记忆']:
    if k in txt:
        print('ABORT：核心论断已存在于清单，撞源不写：', k)
        raise SystemExit(1)

with io.open(path, 'a', encoding='utf-8', newline='') as f:
    f.write('\n' + line + '\n')

# append 后断言：关键片段已进全文
txt2 = io.open(path, encoding='utf-8').read()
assert '你删掉的那些东西，根本没记住过' in txt2, 'append 断言失败'
print('append OK')

# 更新头部计数：已翻炒 644 -> 645（以 grep 实数为准）
n = len(re.findall(r'^- \[x\]', txt2, re.M))
print('grep 实际 [x] 条数 =', n)
new_txt = re.sub(r'^- 已翻炒：\d+ 篇', '- 已翻炒：%d 篇' % n, txt2, count=1, flags=re.M)
io.open(path, 'w', encoding='utf-8', newline='').write(new_txt)
print('头部已翻炒计数更新为', n)
