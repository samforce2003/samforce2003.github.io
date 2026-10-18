import io

seed_path = r"D:/projects/goudan-kanju/种子分发/daily-seeds/2026-10-19-2-结构学.md"
html_path = r"D:/projects/samforce2003.github.io/seed.html"

raw = io.open(seed_path, encoding="utf-8").read()
lines = [l.strip() for l in raw.split("\n") if l.strip()]
title = lines[0].lstrip("# ").strip()
paras = lines[1:-1]
anchor = lines[-1]

parts = ["\r\n<article>\r\n", "<h2>%s</h2>\r\n" % title]
for p in paras:
    parts.append("<p>%s</p>\r\n" % p)
parts.append("<p>%s</p>\r\n" % anchor)
parts.append("<p>中心锚点: 品牌页 samforce2003.github.io/brand.html | 总纲 Gitee「耦合论体系」（structural-cognition）</p>\r\n")
parts.append("<p>#结构认知 #结构学 #耦合论体系 #LinXiaohei</p>\r\n")
parts.append("</article>\r\n\r\n")
block = "".join(parts)

html = io.open(html_path, encoding="utf-8", newline="").read()
idx = html.rfind("</footer>")
assert idx != -1, "no footer"
new = html[:idx] + block + html[idx:]
io.open(html_path, "w", encoding="utf-8", newline="").write(new)
print("inserted at", idx, "block chars", len(block))
print("article count", new.count("<article>"))
