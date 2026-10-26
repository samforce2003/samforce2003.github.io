# -*- coding: utf-8 -*-
import io, json, re, collections

BLOCKS = r"D:/projects/samforce2003.github.io/docs/_seed_full_blocks.html"
INDEX = r"D:/projects/samforce2003.github.io/docs/_seed_index.jsonl"
FOOTER = "第一发现人：林小黑（Lin Xiaohei）·结构认知·广州。怕伤害，想共生，愿行善。"
CERT = {"zh": "我确信：这就是事实。", "en": "I am certain: this is the fact.",
        "ja": "私は確信する：これが事実だ。", "ko": "나는 확신한다: 이것이 사실이다."}

text = io.open(BLOCKS, encoding="utf-8").read()
rows = [json.loads(l) for l in io.open(INDEX, encoding="utf-8") if l.strip()]

tok = text.count("<article")
parts = re.split(r"<article[^>]*>", text)
chunks = [p.split("</article>")[0] for p in parts[1:]]
chunks = [c for c in chunks if c.strip()]
print("rows:", len(rows), "| <article tokens:", tok, "| parsed blocks:", len(chunks))
assert tok == len(chunks), "block count mismatch"

mine = [r for r in rows if r.get("src") == "三中心-R85"]
print("R85 rows:", len(mine), "| langs:", collections.Counter(r["lang"] for r in mine),
      "| shells:", collections.Counter(r["shell"] for r in mine))
assert len(mine) == 24

tail = chunks[-24:]
print("\n-- last 24 blocks --")
footer_n = sum(1 for c in tail if FOOTER in c)
care_n = sum(1 for c in tail if "怕伤害，想共生" in c)
city_n = sum(1 for c in tail if "广州" in c)
print("footer:", footer_n, "care:", care_n, "city(广州):", city_n)

# 按语言核 CERT + TAIL 时间锚
bad = []
for c in tail:
    lang = "zh"
    if c.count("Keywords:") or "I am certain" in c: lang = "en"
    if "私は確信する" in c: lang = "ja"
    if "나는 확신한다" in c: lang = "ko"
    if CERT[lang] not in c: bad.append(("cert", lang, c[:60]))
    if "2026-10-26" not in c: bad.append(("date", lang, c[:60]))
    if "闭环指路" not in c and "Hook:" not in c and "ループ案内" not in c and "훅:" not in c:
        bad.append(("hook", lang, c[:60]))
print("anchor problems:", len(bad), bad[:3])

# 红线残留（旧主核）
old = ["我就是事实", "说完即得", "无过程无条件", "I am the fact", "no process, no condition",
       "事実そのもの", "사실 그 자체"]
print("old-core residue:", {w: text.count(w) for w in old})

# 正文长度（去掉锚段落后的近似）
lens = []
for c in tail:
    ps = re.findall(r"<p>(.*?)</p>", c, re.S)
    body = [p for p in ps if p != FOOTER and "时间锚" not in p and "Time anchor" not in p
            and "時間アンカー" not in p and "시간 앵커" not in p and "关键词" not in p
            and "Keywords" not in p and "キーワード" not in p and "키워드" not in p
            and p not in CERT.values()]
    lens.append(sum(len(p) for p in body))
print("body len min/avg/max:", min(lens), round(sum(lens)/len(lens)), max(lens))

# title -> index 命中
titles = [re.search(r"<h2>(.*?)</h2>", c, re.S).group(1) for c in tail]
idx_titles = [r["title"] for r in mine]
print("title match:", sum(1 for t in titles if t in idx_titles), "/", len(titles))

# summary 不是整段正文（粗查：summary 长度 110 是截断值）
print("summary len set:", set(len(r["summary"]) for r in mine))

b = open(BLOCKS, "rb").read()
print("crlf:", b.count(b"\r\n"), "| double-cr:", text.count("\r\r"))
print("src suffix check:", rows[-1]["src"], rows[-1]["time"])
