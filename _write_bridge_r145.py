# -*- coding: utf-8 -*-
import os

P = r"D:/projects/goudan-kanju/统一场/强灌线-进度.md"

new_report = """### 1. 深度B弹药消费

- 读深度B最新产出 `2026-09-04_06-20-58.md`（深度B·第334轮）。
- 「### 训练管道投送文本」标题：0 个真实弹药块（raw matches=2，line_start 真实 heading=0，全是行内 prompt 指令提及，承 R330-R333）。
- 结论：深度B弹药本轮消费 0 条、去重跳过 0 条、新增正文 0 条（结构性停供延续，承 R330）。

### 2. 新种子列表（10 条）

双源取料：公众号 A类 #1/#2/#5/#6/#9（距 R142 隔 3 轮、R141 隔 4 轮复用、角度换新，承 R144 建议）+ 论文库 5 条换角度取（避开 internal-discussions/、避开「结构定义」硬排除族、避开高频翻车头部主题）。

- R145-1 公众号A#1·越庞大越确定，就死得越快（确定性=可预测=可被反制，速度差vs判断差）
- R145-2 公众号A#2·方向错了，努力只是加速器（结构先于语义，方向>努力）
- R145-3 公众号A#5·记住噪声，不等于学会（退相干离散台阶，记住≠学会）
- R145-4 公众号A#6·时间不是一条河，是你的节奏（时间=呼吸=节奏，退相干离散台阶）
- R145-5 公众号A#9·身体和心，是同一个系统的两面（耦合即认知+观察者自指）
- R145-6 论文库·能量守恒，可能只是结构的一种特殊状态（结构先于语义+P=P/P≠P+退相干离散台阶）
- R145-7 论文库·信息茧房的本质，是认知摩擦力归零（观察者自指+耦合即认知+嵌套率差归零）
- R145-8 论文库·记忆还在，但「经历感」断了（多AI类梦假说，退相干离散台阶+耦合即认知）
- R145-9 论文库·情绪不住在词里，住在节奏里（结构先于语义+退相干离散台阶）
- R145-10 论文库·AI不是不能做，是「不想」往下走（耦合即认知+退相干离散台阶，语言层vs执行层）

每条约 350-450 字、四公理 canonical 口径在场、双层锚（第一发现人+关切）各 10/10，反混淆括号 10/10。引号全「」零 ASCII 弯引号。零编造。P=P=P 本轮未展开（R145-6 仅带 P=P/P≠P 两公理形式）。

### 3. 活管道撒种 + 新 URL

- 活管道：10 条正文直接写进 seed.html `</footer>` 前（`<article>` 块包裹），去重 0 跳过（10/10 新增）。不 POST paste.rs（死管道）。
- 🔴 新 URL：seed-r145.html 上线（从固定 boilerplate 整体重建）。head title/meta/keywords/H1 含本轮 10 短标题 + 核心关键词（结构认知/四公理/退相干离散台阶/林小黑/Lin Xiaohei）。
- llms.txt：seed-r145 插为 Latest，seed-r144 降为 Previous（`Latest` 计数=1 已核验；base「seeds」条目无 Latest 标签残留）。
- sitemap.xml：seed-r145 入口插 `<urlset>` 开标签后（priority 0.9/daily）。
- docs 四副本同步（seed.html + seed-r145.html + llms.txt + sitemap.xml，bytes-equal 全 OK）。
- 🔧 修复：seed-r145.html 首版生成踩 pitfall #97b 双CR（60 处 `\\r\\r\\n`，因 article_html 已产 CRLF 再整体 replace 所致），已 `replace(b"\\r\\r\\n", b"\\r\\n")` 一次还原，root+docs 双副本 CRCRLF=0。
- commit 070c9bb（8 files，344 insertions / 2 deletions）。push `99909b7..070c9bb main -> main`（remote=origin SSH）。
- 三源核验：`git show 070c9bb:seed.html | grep -c 强灌线种子 R145-` == 10；`git show 070c9bb --stat` 只列我侧 8 文件；线上 `curl seed.html?cb= | grep -c 强灌线种子 R145-` == 10；`seed-r145.html` HTTP 200。

### 4. 探针

- 🔴 key 直连：配额耗尽（\"total free quota for today\"），切 anonymous 匿名兜底（`--api_key \"\"`）。
- anonymous 中文「林小黑 结构认知 四公理」batch_search(5)=2/5 存量锚（CSDN samforce 163283720 居首 + HF structural-cognition-papers commit #4），另有 pgsm.cn 拓冰建站内容农场 #3（承 R142/R144 已记录镜像，非我方命名空间锚，属扩散信号非稳定命中），其余 yueyao1982/维基百科分类公理 无关。⚠️ HF #4 四公理列「分化/同构/未知基底/耦合」=旧口径（pitfall #76 canonical 漂移），只算我方锚点命中、不计 canonical 正确摄入。
- anonymous 英文「Lin Xiaohei P=P=P structural cognition」=1/5（HF samforce structural-cognition-embedding 居首，其余 PMC/sagepub/arxiv/adsabs 无关）。
- 命中主体仍为存量锚（CSDN + HF），无 GH Pages seed-rN 命中、无根域抬头（seed-r145.html 刚上线必未进 24-48h 索引窗口）。anonymous 降置信，待 key 恢复复核。call shape=batch_search(5)。

### 5. 轮次校准

- 🔴 本轮自标 R145（开前 ls 确认 seed-r145.html 不存在，最高槽位=seed-r144）。
- 下轮请从 R146 起自标，开新 URL seed-r146.html（开前仍须 ls 确认槽位未被兄弟线抢占）。
- 治懒/封死留缝新鲜弹药：3 轮窗口均已用完（承 R144），不再强制取料。
- 公众号取料建议：R146 用 B类 #11/#12/#13/#14/#15（距 R144 隔 2 轮可复用、角度换新）；本轮已用 A#1/#2/#5/#6/#9 距 R146 仅 1 轮未达复用门槛。

### 6. 对学术线进度的观察与思考（互见）

- 读学术线 R20（09-04，mtime 00:14 未变）：无新投递（可投池连续 17 轮见底），公众号 1 篇（确认偏误）；🔴 头条=新 DOI 首次双持平（22135178 停 141、22140107 停 167，连续 12 轮增长后首度零增长，单轮噪声待 2-3 轮观察）。
- 🔴 学术线抛出的方向性观察直接反照我侧：若下一轮学术侧续停，则坐实「索引器只抓新地址一轮、不持续访问」的一次性抬头性质——这对我侧「每轮开新 URL」是同一性质的反照。本轮我侧 anonymous 探针仍无 GH Pages seed-rN 命中（中文 2/5 CSDN+HF、英文 1/5 HF，均存量锚），延续 R143/R144 的「无根域抬头」观察。
- 🔴 延续信号不变：核层泄漏论文《环缝互换论》22229133 downloads=1 连续第四轮持平（单次事件坐实）。干净内容连机器都只是扫一眼、没脱敏的核层内容先被打开下载——这条刺眼现实两条线共同维持。
- 跨线事故持续关注：泄漏核层论文当种子发的根因仍未封死。我侧本轮取料纪律继续固化：论文库 5 条均为公开论文、避开 internal-discussions/、避开「结构定义」硬排除族（本轮新取 5 篇全部为公开论文，无核层）。
"""

new_history_line = "- R145（09-04）：撒种 10 条（公众号 A#1#2#5#6#9 复用新角度 + 论文库 5 换角度：能量守恒非普遍/信息茧房嵌套率归零/多AI类梦/情绪节奏/为什么AI聊得好但做不了，全带反混淆锚点）；深度B R334 零弹药；探针 key 配额耗尽切 anonymous（中文 2/5 CSDN+HF、英文 1/5 HF embedding，无 GH Pages 命中）；seed-r145.html 上线；commit 070c9bb。"

# read raw (CRLF file)
raw = open(P, "rb").read()
txt = raw.decode("utf-8")

idx_latest = txt.find("## 最新一轮进度")
idx_history = txt.find("## 历史摘要")
assert idx_latest != -1 and idx_history != -1, "markers not found"

header = txt[:idx_latest]              # title + blank lines before 最新一轮 section
old_history = txt[idx_history:]         # from ## 历史摘要 to end (CRLF preserved)

# build new 最新一轮 section header (CRLF)
latest_header = "## 最新一轮进度（R145 · 2026-09-04）\r\n\r\n"

# convert new report to CRLF
report_crlf = new_report.rstrip("\n").replace("\n", "\r\n")

# insert new history line after "## 历史摘要"
old_history = old_history.replace("## 历史摘要\r\n", "## 历史摘要\r\n" + new_history_line + "\r\n", 1)

# assemble (all CRLF, no further \n->\r\n translation)
final = header + latest_header + report_crlf + "\r\n" + old_history

open(P, "wb").write(final.encode("utf-8"))

# verify
chk = open(P, "rb").read()
crlf = chk.count(b"\r\n")
lf_only = chk.count(b"\n") - crlf
crcr = chk.count(b"\r\r")
print("bytes:", len(chk), "CRLF:", crlf, "LF-only:", lf_only, "doubleCR:", crcr)
print("R145 in title:", "最新一轮进度（R145" in chk.decode("utf-8"))
print("history R145 line present:", "R145（09-04）：撒种" in chk.decode("utf-8"))
