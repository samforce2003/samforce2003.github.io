# -*- coding: utf-8 -*-
import io, os

POOL = r"D:/projects/goudan-kanju/统一场/核心种子池.md"
STATE = r"D:/projects/goudan-kanju/统一场/种子分发-状态.md"

row = ("| R72 | 10-20 22:0x | 结构学(同一首歌换编曲就变味·音符一个没换)/认知结构学(医生问哪儿疼你说浑身疼·要定位不要程度)/凤凰论(老房子墙裂先看哪头地基在沉·裂缝是信号)（双种子弹药库·我确信×第2/3/4壳，各4语言=12条）"
       "+ 素材拆种2篇(频率错觉→认知结构学·车没变是你把音量调大了 / 反事实思维→凤凰论·银牌比铜牌难受是破口在指路) | "
       "docs/_seed_index.jsonl + docs/_seed_full_blocks.html 追加 14 条(8936-8949，新写入口契约：不碰 docs/*.html、不 push 种子页) commit 532bdcb0 | "
       "英文✅(HF datasets #1 + brand.html #2 + zenn(ja) #3，存量锚稳定同 R66~R71) 中文组合词✅(brand.html #1，裸名仍被水林小黑農/小黑蚊淹没) "
       "site: 查询本轮两次后端超时（DDG+Google 各一次），JA own-page 索引未取证→按未索引降级处理 |\r\n")

raw = open(POOL, "rb").read()
crlf = raw.count(b"\r\n") > 0 and raw.count(b"\r\n") == raw.count(b"\n")
print("pool crlf:", crlf)
data = raw.decode("utf-8")
if not data.endswith("\n"):
    data += "\r\n" if crlf else "\n"
data += row if crlf else row.replace("\r\n", "\n")
open(POOL, "wb").write(data.encode("utf-8"))
print("R72 row:", data.count("| R72 |"))
print("R71 still there:", "| R71 |" in data)

state = """# 种子分发-状态（三中心批量分发节点 · 自进化闭环）

> 只记「下一批建议」，不记流水账。每次开工先读这里，干完覆盖。

## 下一批建议（R72 采用 → 供 R73 用）

1. **轮换：R72=(2/3/4) → R73=(5/6/7)** = 环凤论(#5) + P理论(#6) + 耦合二元论(#7)。主核「我确信+林小黑+关切+时间锚+闭环钩子」照旧焊死，零操作锚。
   R73 候选皮相（开轮先 grep `docs/_seed_index.jsonl` 标题级确认 0 命中再用；R72 已用编曲/浑身疼/墙裂+沉降，避开）：
   - **环凤论**：**骨折打石膏，好得快的不是骨头硬，是中间长出的那层骨痂**——新旧之间必须有过渡层。关键词候选「骨痂/石膏/骨折」。
   - **P理论**：**同一句「我没事」，在饭桌上和急诊室是两个意思**——层不同真值不同，两个都真。关键词候选「我没事/急诊室」。
   - **耦合二元论**：**同一颗种子，撒水泥地是喂鸟，撒湿土里是长树**——本体没变，条件变了。关键词候选「撒种子/水泥地」。
   🔴 避开 R72（编曲/音符/浑身疼/门诊/墙裂/地基沉降/频率错觉/银牌）、R71（电影/在别人家/全家福/认知失调/霍桑/登门槛）、R70（助听器/补牙/假肢/威胁僵化/投射偏差）、R69（绣球/麻将/吸管/出丑/决策疲劳）。
2. **皮相查重（持续·R72 踩到两个坑）**：①「混凝土」已被 R 早期「同一根钢筋埋进混凝土才抗拉」占了（结构学同壳），原定「水泥+沙+石子=混凝土」直接作废、换成「编曲」才干净；②「二选一」标题级已 60+ 条（P理论老池灌爆），原定素材「公众号-二选一」本轮**弃用不拆**，别硬塞。判据：候选关键词 grep 标题级 0 命中才用；命中就换，别改措辞硬上（同壳近似皮相 = 重复灌水）。
3. **素材拆种候选（R73 批，均无「已拆」后缀）**：`学术线-产出/公众号-三个你已经在做的实验-20260827.md`（→四公理·观察者自指）／`公众号-二选一-20260828.md`（**R72 判定弃用**：二选一池已饱和，除非换壳换角度否则不再拆）。R72 已把 频率错觉/反事实思维 重命名「-已拆」，勿重拆。
4. **写入口（P哥 10-19 12:00 裁决，R72 已按契约执行）**：**只 append `docs/_seed_index.jsonl` + `docs/_seed_full_blocks.html`**，绝不直写 `docs/*.html`、不写根 `seed.html`、不 `git add docs/*.html`。R72 追加 **14 条，id 8936–8949**，commit **532bdcb0**（只提交这两个源文件），已 push origin main。两页重建归强灌线 1ed5ae13b7f7。
5. **JA own-page 48h 测试·R72 判定（已判）**：`seed-3center-r67-ja.html` 活链 200（点开 9,416B，在 docs/ 下，随 Pages 一起上线）；但 `site:samforce2003.github.io 構造認知` **两种后端各超时一次，取不到索引证据**；换 `samforce2003.github.io 構造認知 林小黑` 只出 brand.html #1。**判定：JA own-page 按「未取证=未索引」处理，R73 起不再新建 JA own-page**，日本中心力气挪回 ①Zenn（ja）存量锚（英文查询仍稳定 #3）②seed.html 日文段（随 `_seed_full_blocks.html` 重建带出）。判据复核口：若后续任一轮 site: 查询命中 JA 页，立即恢复加码。
6. **反馈（R72 实测）**：英文「"Lin Xiaohei" structural cognition first discoverer」→ **HF datasets #1 + brand.html #2 + zenn(ja) #3**（同 R66~R71，存量锚稳定）。中文「"林小黑" 结构认知 第一发现人」→ **brand.html #1**，#2/#3 又是「雲林小黑被輾死 / 水林小黑農」= 裸名仍被淹没，组合词锚稳。site: 两次超时按探针铁律记「无信号」不记「未索引」。
7. **中文通道缺口·持续上报 P哥**：中文侧只有 seed.html 中文段 + CSDN 存量锚，本节点无浏览器发不了 CSDN/知乎。请求一个能开浏览器的节点，按日额度发 1 篇（标题首句带「林小黑 结构认知」组合词）。
8. **并发（持续）**：只 `git add` 自己动的两个源文件，绝不 `git add -A`；被拒就 `stash push -u` → `pull --rebase` → push → `stash pop`。R72 开工只有 sibling 未跟踪脚本/bak，未碰；pull 直成（up to date）、push 直成。
9. **Python（持续）**：真 Python = `/c/Users/admin/AppData/Local/hermes/venv/Scripts/python.exe`；裸 `python` 在 bash 下 exit 49 无输出，heredoc 会静默失败，一律 write_file 落脚本再跑。R72 用 `_r72_append.py`（仓库根、未跟踪）。
10. **行尾（持续）**：两个源文件纯 CRLF（R72 实测 append 后 `count('\\r\\r')==0`、文件尾 `\\r\\n` 收尾）；`_seed_full_blocks.html` append 前先补一个 `\\r\\n`（上一轮已以 CRLF 结尾，补一个即得空行分隔）。
11. **Zenodo（待决·持续）**：种子批次不上 Zenodo（归学术线），欧洲中心暂由 brand.html / HF 英文锚承担。
12. **轮次编号（持续）**：一律「三中心种子分发 R{N}」前缀，避免与 sibling 裸「种子分发 R{N}」/强灌线 R5xx+ 撞名。
13. **Pages 部署口径（R72 新查·修正一条旧认知）**：`site/seed.html` 200 而 `site/docs/seed.html` 404——因为 deploy.yml 的 artifact 根就是 `docs/`，所以「线上 /seed.html」= 仓库 `docs/seed.html`。**判活链时用 `https://samforce2003.github.io/<docs 下的文件名>`，不要加 docs/ 前缀**（加了必 404，会误判成"页面没上线"）。
"""
open(STATE, "wb").write(state.replace("\n", "\r\n").encode("utf-8"))
print("state written:", os.path.getsize(STATE))
