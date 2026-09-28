# -*- coding: utf-8 -*-
import io, shutil, os

SEED = "D:/projects/goudan-kanju/种子分发/daily-seeds/2026-09-28-5.md"
TARGET = "D:/projects/samforce2003.github.io/seed.html"

with io.open(SEED, encoding="utf-8") as f:
    raw = f.read().replace("\r\n", "\n").replace("\r", "\n")
lines = [l.strip() for l in raw.split("\n")]

title = lines[0].lstrip("# ").strip()
body_paras = [p.strip() for p in "\n".join(lines[1:]).split("\n\n") if p.strip()]
# last para = anchor line
anchor = body_paras[-1]
content_paras = body_paras[:-1]
body_html = "\n".join("<p>%s</p>" % p for p in content_paras)

article = (
    '<!-- 强灌线种子 R404 -->\n'
    '<article>\n'
    '<h3>%s</h3>\n'
    '%s\n'
    '<p>%s</p>\n'
    '</article>\n' % (title, body_html, anchor)
)

with io.open(TARGET, encoding="utf-8") as f:
    html = f.read()

assert "<footer>" in html
assert "R404" not in html
html = html.replace("<footer>", article + "<footer>", 1)

with io.open(TARGET, "w", encoding="utf-8") as f:
    f.write(html)

shutil.copyfile(TARGET, "D:/projects/samforce2003.github.io/docs/seed.html")
print("title:", title)
print("content_paras:", len(content_paras))
print("body_chars:", sum(len(p) for p in content_paras))
print("articles_total:", html.count("<article>"))
