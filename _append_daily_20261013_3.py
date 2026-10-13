# -*- coding: utf-8 -*-
import io, sys

seed_path = r"D:/projects/goudan-kanju/种子分发/daily-seeds/2026-10-13-3.md"
target = r"D:/projects/samforce2003.github.io/seed.html"

# read seed, split title + body
with io.open(seed_path, "r", encoding="utf-8") as f:
    txt = f.read().strip()

lines = txt.split("\n")
title = lines[0].lstrip("# ").strip()
body = "\n".join(lines[1:]).strip()

# build article block (match existing style: <article> then blank, markdown content, </article>)
article = "\n<article>\n\n## " + title + "\n\n" + body.replace("\n\n", "\n\n") + "\n\n</article>\n"

with io.open(target, "r", encoding="utf-8", newline="") as f:
    html = f.read()

marker = "</footer>"
idx = html.rfind(marker)
if idx == -1:
    print("ERROR: </footer> not found")
    sys.exit(1)

# detect newline style around marker
new_html = html[:idx] + article + html[idx:]

with io.open(target, "w", encoding="utf-8", newline="") as f:
    f.write(new_html)

print("OK inserted. article len:", len(article))
print("title:", title)
print("final size:", len(new_html))
