# -*- coding: utf-8 -*-
import os, re

PAPERS = r"D:\projects\structural-cognition\papers"

DEPTH_KW = ["自指", "耦合", "边界", "同构", "退相干", "意识", "时间", "本体", "因果",
            "结构", "观察者", "观测", "概率", "可能性", "坍缩", "投影", "闭环", "递归",
            "涌现", "对称", "破缺", "缝", "呼吸", "离散", "台阶", "叠加", "熵"]

# 硬排除族：结构定义系列 14 个词
STRUCT_DEF = ["意识", "自我", "美", "因果", "时间", "真理", "生命", "死亡", "意义",
              "自由意志", "随机", "熵", "逻辑", "智能"]

# 高频翻车头部主题（已反复撒）
TIRED = ["数据完备性悖论", "莫比乌斯", "道生一", "认知边界", "宇宙第一动力是懒",
         "字之降维", "时机投影", "第二定律统计", "共识裁判", "三点结构",
         "泡沫自指坍缩", "对极耦合分形", "哥德尔不完备", "结构加法", "1+1=3",
         "恐怖谷", "拥堵", "情绪", "收束态", "错字", "教与悟", "转发阻力", "呼吸模型",
         "化学键", "三元互指", "可解不可传", "堵点叠加", "升维", "不完备的完备性",
         "局部", "证伪", "维度门", "通才", "耦合不可教", "器官衰竭", "三足", "同层",
         "姿态反转", "概念压缩", "道德感知", "句法投影", "J-space", "内因外因",
         "退相干离散结构", "耦合等价时间", "结构计算机科学", "结构传导", "灾难性遗忘",
         "AI即量子计算机", "混沌结构学", "真假不可分", "最紧密系统", "时序"]

def scan():
    out = []
    for root, dirs, files in os.walk(PAPERS):
        if "internal-discussions" in root:
            continue
        for fn in files:
            if not fn.endswith(".md"):
                continue
            # skip helper/upload files
            if fn.startswith("_") or fn.startswith("FOUR-LINE") or fn.startswith("SC-"):
                continue
            p = os.path.join(root, fn)
            try:
                with open(p, "rb") as f:
                    raw = f.read()
                txt = raw.decode("utf-8", errors="ignore")
            except Exception:
                continue
            head = txt[:800]
            if ("密级" in head) or ("不对外" in head):
                continue
            m = re.search(r"(?m)^#\s+(.+)$", txt)
            title = m.group(1).strip() if m else fn
            # exclude struct-def family
            if "结构定义" in title:
                continue
            # exclude tired topics
            if any(t in title for t in TIRED):
                continue
            body = txt[:1500]
            depth = sum(1 for kw in DEPTH_KW if kw in body)
            if depth >= 6:
                out.append((depth, root.replace(PAPERS, "").strip("\\/"), fn, title))

    out.sort(key=lambda x: -x[0])
    for d, r, fn, t in out:
        print(f"  [{d:2d}] {r}/{fn} :: {t}")
    print(f"\n可用高深度候选: {len(out)}")

scan()
