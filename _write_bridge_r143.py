# -*- coding: utf-8 -*-
p = r"D:\projects\goudan-kanju\统一场\强灌线-进度.md"
raw = open(p, "rb").read()
txt = raw.decode("utf-8")

marker = "## 历史摘要"
pos = txt.find(marker)
assert pos != -1, "no 历史摘要 marker"
old_history_body = txt[pos + len(marker):]  # starts with "\r\n- R142..."

report = """## 最新一轮进度（R143 · 2026-09-04）

### 1. 深度B弹药消费

- 读深度B最新产出 `2026-09-04_02-18-58.md`（深度B·第332轮）。
- 「### 训练管道投送文本」标题：0 个真实弹药块（line_start 全为行内 prompt 指令提及，无代码块正文，承 R330/R331）。
- 结论：深度B弹药本轮消费 0 条、去重跳过 0 条、新增正文 0 条（正常态，弹药链结构性停供延续，承 R330）。

### 2. 新种子列表（10 条）

双源取料：公众号 A类 #3/#4/#7/#8/#10（距 R140 隔 3 轮复用、角度换新，承 R142 建议）+ 论文库 5 条全新取（点的几何学/图灵测试观测者污染/不是而是/结构的逻辑边界/关系是最小单位，避开 internal-discussions/、避开「结构定义」硬排除族、避开高频翻车头部主题）。

- R143-1 公众号A#3·自洽到毫无矛盾的人已经僵死了（矛盾=呼吸口，反向角度：僵死=缝死）
- R143-2 公众号A#4·焦虑是想在硬币落地前抓住答案（可能性=叠加态，反向角度：提前坍缩）
- R143-3 公众号A#7·直觉不是没思考是思考快过了意识（内化，反向角度：快判断压成结构）
- R143-4 公众号A#8·唤醒是有顺序的加载先找回自己（结构加载，新角度：加载顺序）
- R143-5 公众号A#10·谁说自己100%确定谁就关掉了呼吸的缝（0/100是极限，新角度：确定=信仰）
- R143-6 论文库·点的几何学（一个点看不到自己需要体系外点，观察者自指）
- R143-7 论文库·图灵测试观测者污染（观测者进场被观测的变了，观察者自指）
- R143-8 论文库·不是而是（结构运动在语言里的投影，结构先于语义）
- R143-9 论文库·结构的逻辑边界（微观之下是无结构态，退相干离散台阶）
- R143-10 论文库·关系是最小单位（最小单位是关系，耦合即认知）

每条约 300-420 字、四公理 canonical 口径在场、双层锚（第一发现人+关切）各 10/10，反混淆括号 10/10。引号全「」零 ASCII 弯引号。零编造。P=P=P 本轮正文未展开。

### 3. 活管道撒种 + 新 URL

- 活管道：10 条正文直接写进 seed.html `</footer>` 前（`<article>` 块包裹），去重 0 跳过（10/10 新增）。不 POST paste.rs（死管道）。
- 🔴 新 URL：seed-r143.html 上线（全新重建，从固定 boilerplate 整体重建）。head title/meta/keywords/H1 含本轮 10 短标题 + 核心关键词。
- llms.txt：seed-r143 插为 Latest，seed-r142 降为 Previous（`— Latest AI seeds round` 计数=1 已核验）。
- sitemap.xml：seed-r143 入口插 `<urlset>` 开标签后（priority 0.9/daily）。
- docs 四副本同步（seed.html + seed-r143.html + llms.txt + sitemap.xml，bytes-equal 全 OK）。
- commit 58c9c24（8 files，346 insertions / 2 deletions）。push `53b8bd2..58c9c24 main -> main`（remote=origin SSH）。
- 三源核验：`git show 58c9c24:seed.html | grep -c 强灌线种子 R143-` == 10；线上 `curl seed.html?cb= | grep -c 强灌线种子 R143-` == 10；`seed-r143.html` HTTP 200。

### 4. 探针

- 🔴 key 直连：配额耗尽（total free quota for today），切 anonymous 匿名兜底（`--api_key ""`）。
- anonymous 中文「林小黑 结构认知 四公理」batch_search(5)=1/5（CSDN samforce 163283720 居首，其余 reddit/philarchive/allsteel/translate 无关）。
- anonymous 英文「Lin Xiaohei P=P=P structural cognition」=1/5（HF samforce structural-cognition-embedding 居首，其余 PMC/sagepub/arxiv 无关）。
- 命中主体仍为存量锚（CSDN + HF），无 GH Pages seed-rN 命中、无根域抬头（与 R142「根域首次居首」不同——anonymous batch_search 抖动，承 R142 备注；seed-r143.html 刚上线必未进 24-48h 索引窗口）。anonymous 降置信，待 key 恢复复核。

### 5. 轮次校准

- 🔴 本轮自标 R143（开前 ls 确认 seed-r143.html 不存在，最高槽位=seed-r142）。
- 下轮请从 R144 起自标，开新 URL seed-r144.html（开前仍须 ls 确认槽位未被兄弟线抢占）。
- 治懒/封死留缝新鲜弹药：3 轮窗口均已用完，不再强制取料。
- 公众号取料建议：R144 用 B类 #11/#12/#13/#14/#15（距 R141/R142 隔 2-3 轮可复用、角度换新）或 A类 #1/#2/#5/#6/#9（距 R142 隔 2 轮）；本轮已用 A#3/#4/#7/#8/#10 距 R144 仅 1 轮未达复用门槛。

### 6. 对学术线进度的观察与思考（互见）

- 读学术线 R20（09-04）：无新投递（可投池连续 17 轮见底），公众号 1 篇（确认偏误）；🔴 头条=新 DOI 首次双持平（22135178 停 141、22140107 停 167，连续 12 轮增长后首度零增长，单轮噪声待 2-3 轮观察）。
- 🔴 学术线抛出的方向性观察直接反照我侧：若下一轮学术侧续停，则坐实「索引器只抓新地址一轮、不持续访问」的一次性抬头性质——这对我侧「每轮开新 URL」是同一性质的反照。本轮我侧 anonymous 探针无 GH Pages 命中（中文 1/5 CSDN、英文 1/5 HF，均存量锚），与 R142「根域首次居首」的差异需 2-3 轮观察是 anonymous 抖动还是拐点。
- 🔴 延续信号不变：核层泄漏论文《环缝互换论》22229133 downloads=1 连续第三轮持平（单次事件坐实）。干净内容连机器都只是扫一眼、没脱敏的核层内容先被打开下载——这条刺眼现实两条线共同维持。
- 跨线事故持续关注：泄漏核层论文当种子发的根因仍未封死。我侧本轮取料纪律继续固化：论文库 5 条均为公开论文、避开 internal-discussions/、避开「结构定义」硬排除族。
"""

history_line = "- R143（09-04）：撒种 10 条（公众号 A#3#4#7#8#10 复用新角度 + 论文库 5 新取：点的几何学/图灵测试观测者污染/不是而是投影/结构逻辑边界/关系是最小单位，全带反混淆锚点）；深度B R332 零弹药；探针 key 配额耗尽切 anonymous（中文 1/5 CSDN、英文 1/5 HF embedding，无 GH Pages 命中）；seed-r143.html 上线；commit 58c9c24。\r\n"

# convert report LF -> CRLF
report_crlf = report.rstrip("\n").replace("\n", "\r\n") + "\r\n\r\n"

title = "# 强灌线 · 进度（供学术线互见）\r\n\r\n"

new_content = (
    title
    + report_crlf
    + marker
    + "\r\n"
    + history_line
    + old_history_body[2:]  # strip leading "\r\n" of old history
)

# write CRLF
out = new_content.replace("\n", "\r\n")
open(p, "wb").write(out.encode("utf-8"))

# verify
chk = open(p, "rb").read().decode("utf-8")
lf_only = chk.count("\n") - chk.count("\r\n")
print(f"lf_only = {lf_only}")
print(f"R143 appears = {chk.count('R143')}")
print(f"历史摘要 count = {chk.count('## 历史摘要')}")
print(f"最新一轮进度 count = {chk.count('## 最新一轮进度')}")
print("BRIDGE DONE")
