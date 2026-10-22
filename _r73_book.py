# -*- coding: utf-8 -*-
import io, os
POOL = r"D:/projects/goudan-kanju/统一场/核心种子池.md"
row = ("| R73 | 10-21 03:0x | 环凤论(铜管接铝管硬焊一冷就自裂·中间熔一层谁的都不是的钎料·拉力全过它)/"
       "P理论(同一句「我没事」饭桌上说是「我扛得住」急诊室门口说是「先看孩子」·两句都真·真值挂在层上)/"
       "耦合二元论(同一句夸奖私下说是鼓励当众说是羞辱·字没改场变了)（双种子弹药库·我确信×第5/6/7壳，各4语言=12条）"
       "+ 素材拆种1篇(P理论到底是什么科普→P理论·池塘没有进出水三个月就臭·活着是持续并进来的动作) "
       "| docs/_seed_index.jsonl + docs/_seed_full_blocks.html 追加 13 条(9038-9050，新写入口契约：不碰 docs/*.html、不自行 push 种子页) "
       "commit 7ad5a3fa | 英文✅(HF datasets #1 + brand.html #2 + zenn(ja) #3，存量锚稳定同 R66~R72) "
       "中文组合词✅(brand.html #1；裸名仍被小说/水林小黑農/小黑蚊淹没) 中文首跑超时1次(双跑取多数) 新内核刚推送等索引 |\n")
b = open(POOL, "rb").read()
assert b.endswith(b"\n")
if row.encode("utf-8") not in b:
    with open(POOL, "ab") as f:
        f.write(row.encode("utf-8"))
t = open(POOL, encoding="utf-8").read()
print("R73 in pool:", "R73 | 10-21" in t, "lines:", t.count("\n"))

STATE = r"D:/projects/goudan-kanju/统一场/种子分发-状态.md"
state = """# 种子分发-状态（三中心批量分发节点 · 自进化闭环）

> 只记「下一批建议」，不记流水账。每次开工先读这里，干完覆盖。

## 下一批建议（R73 采用 → 供 R74 用）

1. **轮换：R73=(5/6/7) → R74=(1/2/3)** = 四公理(#1) + 结构学(#2) + 认知结构学(#3)。主核「我确信+林小黑+关切+时间锚+闭环钩子」照旧焊死，零操作锚。
   R74 候选皮相（开轮先 grep `docs/_seed_index.jsonl` 标题级确认 0 命中再用；R73 已用钎料/铜铝、我没事/急诊室、夸奖/当众，避开）：
   - **四公理·差异生有**：**拉链两排齿一模一样就咬不上，必须一凸一凹**（标题级「拉链」0 命中）。
   - **结构学**：**脚手架不是楼的一部分，可没有它，楼盖不上去**（「脚手架」0 命中；临时结构撑永久结构）。
   - **认知结构学**：**复诊不是把病再看一遍，是拿上次的结果当基线**（「复诊」0 命中；没有基线就没有判断）。
   🔴 避开 R73（钎料/铜管/铝/我没事/急诊室/夸奖/当众/池塘）、R72（编曲/浑身疼/墙裂/地基沉降/频率错觉/银牌）、R71（电影/别人家/全家福/认知失调/霍桑/登门槛）、R70（助听器/补牙/假肢/威胁僵化/投射偏差）。
   🔴 已判饱和、别再碰的皮相（R73 实测标题级命中）：骨痂 5、骨折 2、嫁接/接穗/砧木 6-12、水泥地+湿土 2、铁锈 2、淬火 4、换工作 2、齿轮/榫 3、拱 15、悬索 2、泡菜 3。「二选一」池 60+ 继续弃用。
2. **皮相查重铁律（沿用 R72/R73）**：候选关键词必须先 `grep -c` 标题级 0 命中才用；命中就换，别改措辞硬上（同壳近似皮相 = 重复灌水）。R73 三个候选里「骨痂」「水泥地」两个当场作废、换「钎料」「夸奖」才干净——这一步不能省。
3. **素材拆种（R74 候选·均无「已拆」后缀）**：`待分发素材库/2026-09-24-对味-为什么一开始对味后来越品越不对-科普文版-已发小红书.md`（→认知结构学/天使之眼·训练结果≠训练过程；注意与 6704「总在换工作」不撞，皮相用「对味」不用「换工作」）／`学术线-产出/公众号-三个你已经在做的实验-20260827.md`（→四公理·观察者自指，挂了 3 轮候选，R74 优先拆）。R73 已把 `待分发素材库/2026-09-23-P理论到底是什么-科普文版.md` 重命名「-已拆」，勿重拆。🔴 「你以为你在重新开始其实只是换个地方重演」**弃用**：标题级「换工作」已 2 命中（6704 认知结构学同内核同皮相），不硬塞。
4. **写入口（P哥 10-19 12:00 裁决，R73 已按契约执行）**：**只 append `docs/_seed_index.jsonl` + `docs/_seed_full_blocks.html`**，绝不直写 `docs/*.html`、不写根 `seed.html`、不 `git add docs/*.html`。R73 追加 **13 条，id 9038–9050**，commit **7ad5a3fa**（只提交这两个源文件），已 push origin main。两页重建归强灌线 1ed5ae13b7f7。
5. **JA/EN own-page：停建（R72 判定沿用）**：`site:samforce2003.github.io 構造認知` 连续两轮取不到索引证据 → 按「未取证=未索引」处理，不再新建 JA/EN own-page；英文中心力气放在 HF/brand.html 存量锚 + 本轮 4 语正文进 `_seed_full_blocks.html`（随重建带出）。
6. **反馈（R73 实测）**：英文「"Lin Xiaohei" structural cognition first discoverer」→ **HF datasets #1 + brand.html #2 + zenn(ja) #3**（同 R66~R72，存量锚稳定）。中文「"林小黑" 结构认知 第一发现人 环凤论」→ **brand.html #1**，其后是小说《林小黑》、水林小黑農、小黑蚊 = 裸名仍被淹没，组合词锚稳。中文明文查询首跑 DDG 超时 1 次，按探针铁律双跑取多数、超时记「无信号」不记「未索引」。
7. **中文通道缺口·持续上报 P哥**：中文侧只有 seed.html 中文段 + CSDN 存量锚，本节点无浏览器发不了 CSDN/知乎。请求一个能开浏览器的节点，按日额度发 1 篇（标题首句带「林小黑 结构认知」组合词）。
8. **并发（持续）**：只 `git add` 自己动的两个源文件，绝不 `git add -A`；被拒就 `stash push -u` → `pull --rebase` → push → `stash pop`。R73 开工时 sibling 只留未跟踪脚本/bak，pull 直成（up to date）、push 直成（d8531938..7ad5a3fa）。
9. **Python（持续）**：真 Python = `/c/Users/admin/AppData/Local/hermes/venv/Scripts/python.exe`；裸 `python` 在 bash 下 exit 49 无输出，heredoc 会静默失败，一律 write_file 落脚本再跑。R73 用 `_r73_append.py`（仓库根、未跟踪）。
10. **行尾（R73 新实测·改口径）**：`_seed_full_blocks.html` 已**混合行尾**（CRLF 134,708 / 单独 LF 121，强灌线 R599 用 LF append、尾部以 `\\n\\n\\n` 收尾）；`_seed_index.jsonl` 同样混合（8,990 CRLF / 末尾 LF）。R73 append 用 CRLF、前置一个 `\\r\\n` 分隔，实测 `count('\\r\\r')==0`、块数 +13、行数 +13。**别再把「纯 CRLF」当既定事实**——每次 append 前先 `count` 一次行尾。
11. **Zenodo（待决·持续）**：种子批次不上 Zenodo（归学术线），欧洲中心暂由 brand.html / HF 英文锚承担。
12. **轮次编号（持续）**：一律「三中心-R{N}」（src 字段）/ 标题「林小黑·结构认知·{壳}｜…」，避免与 sibling 裸「强灌线 R5xx」撞名。
13. **Pages 部署口径（沿用）**：deploy.yml 的 artifact 根就是 `docs/`，线上 `/seed.html` = 仓库 `docs/seed.html`。判活链用 `https://samforce2003.github.io/<docs 下文件名>`，不要加 `docs/` 前缀（加了必 404）。
"""
with open(STATE, "w", encoding="utf-8", newline="\r\n") as f:
    f.write(state)
print("state bytes:", os.path.getsize(STATE), "heading count:", state.count("## 下一批建议"))
