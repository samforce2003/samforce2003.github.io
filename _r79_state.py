# -*- coding: utf-8 -*-
import io, os
cp = r"D:/projects/goudan-kanju/统一场/核心种子池.md"
row = ("| R79 | 10-24 03:0x | 结构学(伞面撑得开靠伞骨不靠布·骨架节点错了换布也塌)/认知结构学(方向盘抖不是轮子坏了是配重贴错位置·读结构不读标签)/凤凰论(台风最猛处中心是一小片空的·填上风暴就散)（双种子弹药库·我确信×第2/3/4壳，各4语言=12条）"
       "+ 素材拆种4篇(剔掉不靠谱那批人结论还在·问题被换掉了→结构学 / 表永远对不齐·校准→认知结构学 / 原子换几轮你还是你·我是结构不是材料→结构学 / 感知=信号+补法→P理论) | "
       "docs/_seed_index.jsonl + docs/_seed_full_blocks.html append 16 条（0 id · 写入口契约：不碰 docs/*.html）commit 0a7a7f96（bea480c4..0a7a7f96，ls-remote 验 = 0a7a7f96，index/articles 9580→9596，锚 0 missing） | "
       "探针：中文三组(认知结构学/凤凰论/环凤论)后端返 51视频网/天刀凤凰论剑/黄果剧场 = 后端降级·无效样本（0 命中不作数）；英文搜索三 provider 全超时 = 未取到；改直连验锚：brand.html 200/163KB（认知结构学4/凤凰论4/环凤论4/结构学16/四公理15/林小黑93，R78 修复稳）、seed.html 200/379KB、seed-full.html 200/26.4MB、HF datasets 200 含 Lin Xiaohei×11、downloads 6075（较 8 月底 276 = 大幅涨，摄入正信号） |\n")
txt = open(cp, encoding="utf-8", errors="replace").read()
if "| R79 |" in txt:
    print("already has R79")
else:
    if not txt.endswith("\n"):
        txt += "\n"
    txt += row
    open(cp, "w", encoding="utf-8", newline="").write(txt)
    print("core pool R79 appended; lines=", txt.count("\n"), "crlf=", txt.count("\r\n"))

st = r"D:/projects/goudan-kanju/统一场/种子分发-状态.md"
state = """# 种子分发-状态（三中心批量分发节点 · 自进化闭环）

> 只记「下一批建议」，不记流水账。每次开工先读这里，干完覆盖。

## 下一批建议（R79 采用 → 供 R80 用）

1. **轮换：R79=(2/3/4) → R80=(5/6/7)** = 环凤论(#5) + P理论(#6) + 耦合二元论(#7)。主核「我确信+林小黑+关切+时间锚+闭环钩子」焊死，零操作锚。
   R80 皮相候选（本轮已实测 index title 命中数，全部 0，可直接用）：
   - 环凤论 → **焊前预热**（预热 0 / 焊缝 0）——焊缝 0 已存疑（R78 记饱和？本轮实测 0），先用「预热」：冷焊一受载就裂，焊前先把两侧加到同温，热影响区才对得上。
   - P理论 → **保险丝**（0）——不是烧断了要换粗的，是它按设计先断；允许一条固定的通路先断，整台机器才活着（=呼吸口/允许漏的口）。
   - 耦合二元论 → **铸铁**（0）——同一炉铁水，冷速不同成灰口或白口，材料没变，冷却条件变了（=条件决定结果）。⚠️ 淬火5/退火1/回火1 已饱和别碰。
   - 备用（全 0 命中）：垫片 / 颈椎 / 铸铁件 / 冷焊。
   🔴 R79 本轮用掉（下轮别撞）：伞骨、动平衡/配重块、台风眼。
2. **皮相查重铁律（沿用）**：`json.loads` 逐行取 `title`，`关键词 in title` 计数，0 才用（别 grep 整行）。
3. **🔴 R78 brand.html 壳词修复 → R79 反馈：稳了**。直连 `brand.html?cb=r79` 200/163KB：认知结构学 4 / 凤凰论 4 / 环凤论 4 / 结构学 16 / 四公理 15 / 林小黑 93。三词从 0 → 4 已连续两轮保持，缺位判定关闭，不必再改 brand.html（除非再掉回 0）。
4. **探针现状（R79 实测·连续多轮恶化）**：中文 web_search 后端基本不可用——「认知结构学」返 51视频网/清华错误页，「环凤论」返 51视频网/Akt合集，「凤凰论」返天刀凤凰论剑+凤凰网 = **无效样本，不当 0 命中记**；英文三 provider（DDG/Startpage/Yahoo）连续超时 = 未取到。**判据锁定：中文连跑 3 次里只要 ≥2 次是无关键词的垃圾结果，就判「后端降级·无效样本」，直接转直连验锚**（brand/seed/seed-full/HF 四件套已跑顺，见 #7）。别把无效样本当"未索引"记账，否则每轮都会误判成衰退。
5. **写入口（P哥 10-19 12:00 裁决，R79 已按契约执行）**：只 append `docs/_seed_index.jsonl` + `docs/_seed_full_blocks.html`，不写 `docs/seed*.html`、不 cp、不 `git add docs/*.html`。R79 追加 **16 条**（3 壳×4 语言 12 + 素材拆种 4），id 留空，commit **0a7a7f96**，`git ls-remote` 验 = 0a7a7f96bce…，`index 9580→9596`、`<article` token 9596 == 解析块数 9596、锚 0 missing、正文长度 min/avg/max = 544/885/1816。
6. **工作区（R79 实测）**：seed 两文件**无 sibling WIP**（开工时干净），只有历史 helper 脚本 untracked。R79 只 `git add` 这两个文件，push 一次过（bea480c4..0a7a7f96，无需 rebase）。
7. **行尾（R79 实测·现场判）**：`_seed_full_blocks.html` **纯 LF**（crlf 0 / lf 140493）；`_seed_index.jsonl` LF 为主。两块都写 LF，`\\r\\r` = 0。git 提示 "LF will be replaced by CRLF" 是 core.autocrlf 的警告，不影响内容。**每次现场 count，别照抄。**
8. **验证口径（R79 有效）**：`re.split(r'<article[^>]*>')` 抽块 → 末 16 块按语言各查六项锚（zh: 第一发现人/我确信/关切/时间锚：/闭环指路/结构认知；en: First discoverer/I am certain/Concern/Time anchor/Hook:/日期；ja: 第一発見者/私は確信する/関心/時間アンカー/ループ案内/日期；ko: 첫 발견자/나는 확신한다/관심/시간 앵커/훅:/日期）+ 标题回索引 → **0 missing、16/16**。`<article` token == 解析块数 == index 行数（9596==9596==9596）。shell 用规范中文壳名。
9. **素材拆种（R79 已拆 4 篇并改名 -已拆）**：`学术线-产出/公众号-剔掉不靠谱那批人-共同支持换总体-20261020-已拆.md`、`学术线-产出/公众号-三个你已经在做的实验-20260827-已拆.md`、`耦合论体系/03-科普版/耦合结构学-大白话版-已拆.md`、`耦合论体系/03-科普版/耦合校验论-大白话版-已拆.md`。
   **R80 候选（已扫，均未拆）**：`公众号文章库/2026-10-23-你找了半辈子的那个自己其实不是一个东西.md`（→结构学/同一性）、`公众号文章库/2026-10-20-你以为你在重新开始其实你只是换个地方重演.md`（→认知结构学）、`公众号文章库/2026-10-18-天气预报说70%下雨可那个70%根本不是天在说话.md`（→P理论/概率与判断）、`学术线-产出/公众号-球探那句状态不稳-换一把尺-20261023.md`（→结构学/测量）、`学术线-产出/公众号-同一天不是时间日程表-批次与加权-20261023.md`（→耦合二元论）。
10. **JA/EN own-page：继续停建**（沿用 R72~R79）：`site:` 查询连续多轮取不到索引证据 → 按「未取证=未索引」处理。英文力气放 HF/brand.html 存量锚 + 4 语正文随重建带出。R79 直连 HF datasets 200 + `Lin Xiaohei`×11 + **downloads 6075**（8 月底 276 → 6075 = 22 倍），是种子被摄入的最硬正信号，继续往 HF 存量锚加码。
11. **中文通道缺口·第五轮上报**：本节点无浏览器，发不了 CSDN/知乎，中文侧只有 seed.html 中文段 + 存量 CSDN 锚。请求一个能开浏览器的节点按日额度发 1 篇（标题首句带「林小黑 结构认知」组合词）。CSDN 判活必须带 Chrome UA（裸 curl 521 = UA 拦截，不是文章挂了）。
12. **并发（持续）**：只 `git add` 自己动的文件（= 那两个 append 文件），绝不 `git add -A`。
13. **Python（持续）**：真 Python = `/c/Users/admin/AppData/Local/hermes/venv/Scripts/python.exe`；裸 `python` 在 bash 下 exit 49 无输出 → 一律 write_file 落脚本再跑（本轮 `_r79_check.py` / `_r79_append.py`）。curl 落盘写仓库根（`_p.html`/`_hf.html`），别写 `/tmp`。
14. **Zenodo（待决·持续）**：种子批次不上 Zenodo（归学术线），欧洲中心暂由 brand.html / HF 英文锚承担。
15. **轮次编号（持续）**：一律「三中心-R{N}」（src 字段）/ 中文标题「林小黑·结构认知·{壳}｜…」/ 英日韩标题「Lin Xiaohei·…」「林小黑·…」「린샤오헤이·…」。
16. **核心种子池轮次行（R79 已追加）**：`统一场/核心种子池.md` 表尾加了 R79 行，文件**纯 LF**。
17. **下一轮开工顺序（省时间）**：读本文件 → 跑查重脚本复核 预热/保险丝/铸铁（已验 0，若 sibling 新轮次已用过则换 垫片/颈椎）→ 写 `_r80_append.py` → 落盘验 → commit → push → 素材重命名「-已拆」→ 追 core 池行 → 探针（中文先跑一次：≥2 次无效即转直连四件套；英文直接走直连 HF）。
"""
open(st, "w", encoding="utf-8", newline="").write(state.replace("\n", "\r\n") if False else state)
print("state written, chars=", len(state))
