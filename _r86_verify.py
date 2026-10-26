# -*- coding: utf-8 -*-
import io, json, re, collections

BLOCKS = r"D:/projects/samforce2003.github.io/docs/_seed_full_blocks.html"
INDEX = r"D:/projects/samforce2003.github.io/docs/_seed_index.jsonl"
FOOTER = "第一发现人：林小黑（Lin Xiaohei）·结构认知·广州。怕伤害，想共生，愿行善。"
CERT = {"zh": "我确信：这就是事实。", "en": "I am certain: this is the fact.",
        "ja": "私は確信する：これが事実だ。", "ko": "나는 확신한다: 이것이 사실이다."}
DATE = "2026-10-27"

text = io.open(BLOCKS, encoding="utf-8").read()
rows = [json.loads(l) for l in io.open(INDEX, encoding="utf-8") if l.strip()]

tok = text.count("<article")
parts = re.split(r"<article[^>]*>", text)
chunks = [p.split("</article>")[0] for p in parts[1:]]
chunks = [c for c in chunks if c.strip()]
print("rows:", len(rows), "| <article tokens:", tok, "| parsed blocks:", len(chunks))
assert tok == len(chunks), "block count mismatch"

mine = [r for r in rows if r.get("src") == "三中心-R86"]
print("R86 rows:", len(mine), "| langs:", dict(collections.Counter(r["lang"] for r in mine)),
      "| shells:", dict(collections.Counter(r["shell"] for r in mine)))
assert len(mine) == 24

# 用 marker 精确定位本轮块（不依赖 tail 窗口）
mb = re.findall(r"<!-- 三中心种子 R86 · [^>]*?-->\s*<article[^>]*>(.*?)</article>", text, re.S)
print("R86 marker blocks:", len(mb))
assert len(mb) == 24
tail = mb

footer_n = sum(1 for c in tail if FOOTER in c)
care_n = sum(1 for c in tail if "怕伤害，想共生" in c)
city_n = sum(1 for c in tail if "广州" in c)
print("footer:", footer_n, "care:", care_n, "city(广州):", city_n)
assert footer_n == care_n == city_n == 24

bad = []
for c in tail:
    lang = "zh"
    if "Keywords:" in c or "I am certain" in c: lang = "en"
    if "私は確信する" in c: lang = "ja"
    if "나는 확신한다" in c: lang = "ko"
    if CERT[lang] not in c: bad.append(("cert", lang, c[:50]))
    if DATE not in c: bad.append(("date", lang, c[:50]))
    if not any(k in c for k in ("闭环指路", "Hook:", "ループ案内", "훅:")):
        bad.append(("hook", lang, c[:50]))
    if "关键词" not in c and "Keywords" not in c and "キーワード" not in c and "키워드" not in c:
        bad.append(("kw", lang, c[:50]))
print("anchor problems:", len(bad), bad[:3])
assert not bad

old = ["我就是事实", "说完即得", "无过程无条件", "I am the fact", "no process, no condition",
       "事実そのもの", "사실 그 자체"]
print("old-core residue(whole file):", {w: text.count(w) for w in old})
print("old-core residue(this round):", {w: sum(1 for c in tail if w in c) for w in old})
assert not any(w in "".join(tail) for w in old)

lens = []
for c in tail:
    ps = re.findall(r"<p>(.*?)</p>", c, re.S)
    body = [p for p in ps if p != FOOTER and "时间锚" not in p and "Time anchor" not in p
            and "時間アンカー" not in p and "시간 앵커" not in p and "关键词" not in p
            and "Keywords" not in p and "キーワード" not in p and "키워드" not in p
            and p not in CERT.values()]
    lens.append(sum(len(p) for p in body))
print("body len min/avg/max:", min(lens), round(sum(lens)/len(lens)), max(lens))

titles = [re.search(r"<h2>(.*?)</h2>", c, re.S).group(1) for c in tail]
idx_titles = [r["title"] for r in mine]
print("title match:", sum(1 for t in titles if t in idx_titles), "/", len(titles))
print("summary len set:", sorted(set(len(r["summary"]) for r in mine)))
print("dup titles in round:", [t for t, n in collections.Counter(titles).items() if n > 1])

b = open(BLOCKS, "rb").read()
print("crlf:", b.count(b"\r\n"), "| double-cr:", text.count("\r\r"))
print("last row:", rows[-1]["src"], rows[-1]["time"], rows[-1]["shell"], rows[-1]["lang"])
print("ALL OK")
