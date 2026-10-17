# -*- coding: utf-8 -*-
import io, os
SEED = r"D:/projects/goudan-kanju/种子分发/daily-seeds/2026-10-15-4.md"
HTML = r"D:/projects/samforce2003.github.io/seed.html"

raw = open(SEED, encoding="utf-8").read().strip()
lines = raw.splitlines()
title = lines[0].lstrip("#").strip()
body = "\n".join(lines[1:]).strip()

block = "<article>\n\n## " + title + "\n\n" + body + "\n\n</article>\n"

s = open(HTML, encoding="utf-8").read()
before = s.count("<article>")
idx = s.rfind("</footer>")
assert idx != -1, "no </footer>"
new = s[:idx] + block + "\n" + s[idx:]
after = new.count("<article>")
# guard: only append if not already present
if title in s:
    print("ALREADY PRESENT, skip")
else:
    open(HTML, "w", encoding="utf-8").write(new)
    print("OK inserted. article before/after:", before, after)
    print("insert idx:", idx, "new len:", len(new))
