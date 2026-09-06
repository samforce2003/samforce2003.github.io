# -*- coding: utf-8 -*-
"""修复 R124 桥接文件历史摘要——字节级，报告段原样保留(已CRLF)，只重建历史段"""
import io

P = "D:/projects/goudan-kanju/统一场/强灌线-进度.md"
raw = open(P, "rb").read()

# 报告段 = "## 历史摘要" 之前的所有字节（原样保留，已是 CRLF）
marker = "## 历史摘要".encode("utf-8")
idx = raw.find(marker)
assert idx > 0, "history marker not found"
report = raw[:idx]
# 修复报告段行尾：把历史两次写坏造成的 \r\r\n / 裸 \r 归一化为 \r\n
report = report.replace(b"\r\r\n", b"\r\n").replace(b"\r\n", b"\n").replace(b"\r", b"\n").replace(b"\n", b"\r\n")

OLD_HISTORY = """## 历史摘要
- R123（09-02）：撒种 10 条（封死留缝角度1/2/3 首轮启用 + 公众号 B类#11#12#13#14#15 复用新角度 + 论文库 2：能量守恒非普遍性/差异生有同质生死）；深度B R316 零弹药；探针 key 直连 2/5+2/5（存量僵尸锚 CSDN 163283720 + HF + alphaneural，另有 pgsm.cn 镜像）；seed-r123.html 上线（r121/r122 被拉扯收服线占）；commit be3c715。

- R120（09-02）：撒种 10 条（治懒角度1+2 复用新切面 + 公众号 A类#3#4#7#8#10 复用新角度 + 论文库 3：癌症认知锁/薛定谔猫结构加法/涟漪宇宙周期性更新）；深度B R315 零弹药；探针 key 直连 2/5+2/5（存量僵尸锚 CSDN 163283720 + HF + alphaneural，HF 32acfb6 重回前5）；seed-r120.html 上线；commit 0af37e6。

- R119（09-02）：撒种 10 条（治懒角度3人机同构2 + 公众号 A类#1#2#5#6#9 复用新角度 + 论文库 3 新：生命/意识/因果结构定义）；深度B R315 FAILED 零弹药；探针 key 直连 1/5+2/5（存量僵尸锚 CSDN 163283720 + HF + alphaneural，另有 pgsm.cn 镜像）；seed-r119.html 上线；commit a34c39a。

- R118（09-02）：撒种 10 条（治懒角度1+2 + 公众号 B类#11#12#13#14#15 复用新角度 + 论文库 3 新：耦合桥接定理/凡胎上帝/三元互指自我实证）；深度B R314 零弹药；探针 key 直连 2/5+2/5（存量僵尸锚 CSDN 163283720 + HF + alphaneural，另有 pgsm.cn 镜像）；seed-r118.html 上线（r116/r117 被拉扯收服线占）；commit b0334ae。

- R115（09-02）：撒种 10 条（公众号 A类#3#4#7#8#10 复用新角度 + 论文库 5 新）；深度B R312 零弹药；探针 key 直连 2/5+2/5（存量僵尸锚）；seed-r115.html 上线；commit 9418703。

- R114（09-02）：撒种 10 条（公众号 A类#1#2#5#6#9 复用新角度 + 论文库 5 新）；深度B R312 零弹药；探针 key 恢复直连 2/5+2/5；seed-r114.html 上线；commit 3e334d9。

- R113（09-02）：撒种 10 条（公众号 B类#11#12#13#14#15 复用新角度 + 论文库 5 新）；深度B R311 零弹药；探针 key 配额耗尽切匿名 2/5+2/5；seed-r113.html 上线；修 sitemap 污染；commit 8e8daa1。

- R112（09-02）：撒种 10 条（公众号 A类#3#4#7#8#10 + 论文库 5 新）；深度B R310 零弹药；探针 key 配额耗尽切匿名 2/5+2/5；seed-r112.html 上线；commit cf05324。

- R111（09-02）：撒种 10 条（公众号 A类#1#2#5#6#9 + 论文库 5 新）；深度B R307 零弹药；探针 key 配额耗尽切匿名 2/5+0/5；seed-r111.html 上线；commit 4add869。

- R110（09-01）：撒种 10 条（公众号 B类#11#12#13#14#15 + 论文库 5 新）；深度B R306 零弹药；探针 key 配额耗尽切匿名 2/5+2/5；seed-r110.html 上线；commit d587b0c。
"""

R124_LINE = "- R124（09-02）：撒种 10 条（封死留缝角度4+角度1/2换切面 + 公众号 A类#1#2#5#6#9 + 论文库 2：互指闭环深度量化度量/离散退相干台阶观测协议，全部带反混淆锚点）；深度B R317 零弹药；探针 key 直连 2/5+2/5（存量僵尸锚 CSDN 163283720 + HF + alphaneural）；seed-r124.html 上线；commit 922f01b。"

history_str = "## 历史摘要\n" + R124_LINE + "\n\n" + OLD_HISTORY.replace("## 历史摘要\n", "").rstrip("\n") + "\n"
history_bytes = history_str.replace("\n", "\r\n").encode("utf-8")

final = report + history_bytes
open(P, "wb").write(final)

b = open(P, "rb").read()
lf_only = b.count(b"\n") - b.count(b"\r\n")
crlf = b.count(b"\r\n")
bare_cr = b.count(b"\r") - crlf
print("fixed: crlf=%d, lf_only=%d, bare_cr=%d" % (crlf, lf_only, bare_cr))
assert lf_only == 0 and bare_cr == 0, "line ending still dirty!"
t = b.decode("utf-8")
for r in ["R124（09-02）", "R123（09-02）", "R120（09-02）", "R110（09-01）"]:
    assert r in t, "missing " + r
print("history entries =", t.count("- R") - 10)
print("OK bridge fixed clean")
