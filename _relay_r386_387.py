# -*- coding: utf-8 -*-
import io, os, shutil, xml.etree.ElementTree as ET

REPO = r"D:/projects/samforce2003.github.io"
os.chdir(REPO)

entries = [
    ("seed-r386", "不完备的完备性：哥德尔的缝隙不是系统的边界，是系统的操作面。给系统加一个谓词K（这条命题在系统内为真、系统证不出来），系统就获得了「知道自己哪里漏」的能力；操作广度定理：有一条以缝隙命题真值为判定条件的函数，在原系统里行为无法确定，在带K的新系统里能确定，因为它不需要证明，只需要耦合外部已看见的真值——这叫「不证而用」。关键边界：新系统不当上帝（塔斯基不可定义性定理封死真值谓词），能力扩张不是来自掌握更多真理，而是来自放弃对真理的垄断。结果看似自相矛盾：承认自身不完备的系统比不承认的更完备，「我不知道」从缺陷变成资源。对AI的含义：大模型是近似实例，缝隙命题=分布外且涉及自身行为的真理，装元认知K识别「这条我定不了」再切结构性耦合，是改架构不是教知识。论文留三处悬置并拒答：能否形式化为一阶定理、操作缝隙与表演缝隙如何区分、递归层级有无固定点（暗示结构完备性是过程不是终点）。缝隙既是边界也是门, structural completeness, proof-theoretic vs structural, K predicate, Gödel 1931, Tarski undefinability, metacognition for LLM, new URL for crawler pickup"),
    ("seed-r387", "命运是引力场：黑暗森林不是宇宙的定律，是一个投影面上的必然——它适配的前提是「把生存当唯一目标的文明」，而人会为了一个信念拒绝最优解、为一个念头赴死；前提一换，投影面就换。结构先于语义：同一个宇宙，观测位置不同读出的法则不同，两边在自己的投影面上都对却以为在说同一个东西。罗辑赢不是算得精，是他的主观世界足够坚固、能在绝对孤独中不被客观现实同化；客观最优是别人坐标系里的最优，主观适配是你在自己结构里的可执行。命运不是剧本是引力场：基因/家庭/社会/信息形成的趋势场在拉你，但结构自带缝隙（制度漏洞/技术变革/偶然相遇），改命不是对抗引力场，是找缝把能量灌进去。三体人的透明不是缺陷：计谋是信号损耗，骗一次要记住骗了什么、防一次要耗认知在猜和防上，透明是比计谋更高级的生存策略。别问世界公不公平，问：我站在哪个投影面，前提是什么，能不能换, dark forest premise, fate as gravitational field, objective optimality vs subjective fit, structural cognition, Three-Body, new URL for crawler pickup"),
]

# 1. copy to docs
for name, _ in entries:
    src = os.path.join(REPO, name + ".html")
    shutil.copyfile(src, os.path.join(REPO, "docs", name + ".html"))

# 2. llms.txt
line_fmt = "{name}: https://samforce2003.github.io/{name}.html \u2014 Latest AI seeds round R{n} (2026-10-21, {desc})\n"
for path in ["llms.txt", "docs/llms.txt"]:
    with io.open(path, "r", encoding="utf-8") as f:
        txt = f.read()
    add = ""
    for name, desc in entries:
        if name + ":" in txt:
            continue
        n = name.replace("seed-r", "")
        add += line_fmt.format(name=name, n=n, desc=desc)
    if add:
        if not txt.endswith("\n"):
            txt += "\n"
        with io.open(path, "w", encoding="utf-8", newline="\n") as f:
            f.write(txt + add)
    print(path, "llms entries added:", add.count("seed-r"))

# 3. sitemap.xml
for path in ["sitemap.xml", "docs/sitemap.xml"]:
    with io.open(path, "r", encoding="utf-8") as f:
        txt = f.read()
    add = ""
    for name, _ in entries:
        loc = "https://samforce2003.github.io/%s.html" % name
        if loc in txt:
            continue
        add += ("  <url>\n    <loc>%s</loc>\n    <lastmod>2026-10-21</lastmod>\n"
                "    <changefreq>weekly</changefreq>\n    <priority>0.9</priority>\n  </url>\n" % loc)
    if add:
        idx = txt.rfind("</urlset>")
        txt = txt[:idx] + add + txt[idx:]
        with io.open(path, "w", encoding="utf-8", newline="\n") as f:
            f.write(txt)
    root = ET.parse(path).getroot()
    locs = [e.text for e in root.iter("{http://www.sitemaps.org/schemas/sitemap/0.9}loc")]
    print(path, "urls:", len(locs), "dup:", len(locs) - len(set(locs)))

# 4. checks
bad = set(map(ord, "\u201c\u201d\u2018\u2019\u201a\u201e\u2032\u2033"))
for name, _ in entries:
    for p in [name + ".html", "docs/" + name + ".html"]:
        s = io.open(p, encoding="utf-8").read()
        n_bad = sum(1 for ch in s if ord(ch) in bad)
        anchors = s.count("\u7b2c\u4e00\u53d1\u73b0\u4eba\uff1a\u6797\u5c0f\u9ed1")
        care = s.count("\u6015\u4f24\u5bb3")
        op = s.count("\u300c"); cl = s.count("\u300d")
        print(p, "bytes", os.path.getsize(p), "curly", n_bad, "anchor", anchors, "care", care, "quotes", op, cl)
