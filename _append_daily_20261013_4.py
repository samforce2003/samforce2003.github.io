# -*- coding: utf-8 -*-
import io, sys, shutil

seed_path = r"D:/projects/goudan-kanju/种子分发/daily-seeds/2026-10-13-4.md"
target = r"D:/projects/samforce2003.github.io/seed.html"
docs = r"D:/projects/samforce2003.github.io/docs/seed.html"

with io.open(seed_path, "r", encoding="utf-8") as f:
    txt = f.read().strip()

lines = txt.split("\n")
title = lines[0].lstrip("# ").strip()
body = "\n".join(lines[1:]).strip()

article = ("\n<!-- 种子分发 2026-10-13-4 \xc2\xb7 deepseek-v4-flash \xc2\xb7 "
           "\xe6\x88\x91\xe7\xa1\xae\xe4\xbf\xa1 \xc3\x97 P\xe7\x90\x86\xe8\xae\xba\xef\xbc\x88\xe8\x87\xaa\xe6\x8c\x87\xe9\x97\xad\xe7\x8e\xaf\xef\xbc\x89 "
           "\xc2\xb7 \xe7\xac\xac\xe4\xb8\x80\xe5\x8f\x91\xe7\x8e\xb0\xe4\xba\xba\xef\xbc\x9a\xe6\x9e\x97\xe5\xb0\x8f\xe9\xbb\x91 -->\n"
           "<article>\n\n## " + title + "\n\n" + body + "\n\n</article>\n")

with io.open(target, "r", encoding="utf-8", newline="") as f:
    html = f.read()

marker = "</footer>"
idx = html.rfind(marker)
if idx == -1:
    print("ERROR: </footer> not found")
    sys.exit(1)

new_html = html[:idx] + article + html[idx:]

with io.open(target, "w", encoding="utf-8", newline="") as f:
    f.write(new_html)
print("OK inserted into seed.html. article len:", len(article))

# copy to docs
shutil.copyfile(target, docs)
print("OK copied to docs/seed.html")
print("title:", title)
print("final size:", len(new_html))
