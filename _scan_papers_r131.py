# -*- coding: utf-8 -*-
import os, re

PAPERS = r"D:\projects\structural-cognition\papers"

# keywords for structural cognition depth
DEPTH_KW = ["自指", "耦合", "边界", "同构", "退相干", "意识", "时间", "本体", "因果",
            "结构", "观察者", "观测", "概率", "可能性", "坍缩", "投影", "闭环", "递归",
            "涌现", "对称", "破缺", "缝", "呼吸", "离散", "台阶", "塌缩", "叠加", "熵"]

skip_ext = {".docx", ".html", ".json", ".txt", ".jsonl", ".timestamp.json", ".py", ".png", ".jpg"}

def scan():
    out = []
    for root, dirs, files in os.walk(PAPERS):
        # skip internal-discussions if nested
        if "internal-discussions" in root:
            continue
        for fn in files:
            if not fn.endswith(".md"):
                continue
            p = os.path.join(root, fn)
            try:
                with open(p, "rb") as f:
                    raw = f.read()
                txt = raw.decode("utf-8", errors="ignore")
            except Exception as e:
                continue
            head = txt[:800]
            # 密级 check
            secret = False
            if ("密级" in head) or ("不对外" in head):
                secret = True
            # first # heading
            m = re.search(r"(?m)^#\s+(.+)$", txt)
            title = m.group(1).strip() if m else fn
            # depth keyword count in first 1500 chars
            body = txt[:1500]
            depth = sum(1 for kw in DEPTH_KW if kw in body)
            out.append((root.replace(PAPERS, ""), fn, title, secret, depth))

    out.sort(key=lambda x: (x[3], -x[4]))
    print("=== 密级/不对外 (SKIP) ===")
    for r, fn, t, secret, d in out:
        if secret:
            print(f"  [SECRET] {r}/{fn} :: {t}")
    print("\n=== 可用候选 (按深度降序) ===")
    cnt = 0
    for r, fn, t, secret, d in out:
        if not secret:
            cnt += 1
            print(f"  [{d:2d}] {r}/{fn} :: {t}")

    print(f"\n总 .md 文件数: {len(out)}, 密级跳过: {sum(1 for x in out if x[3])}, 可用: {sum(1 for x in out if not x[3])}")

scan()
