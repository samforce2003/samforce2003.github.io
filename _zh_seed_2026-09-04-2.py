# -*- coding: utf-8 -*-
# 中文种子分发 2026-09-04-2 -> seed.html + docs/seed.html (CRLF binary append)
import io, sys, re

REPO = r"D:/projects/samforce2003.github.io"
HTML = REPO + "/seed.html"
MD   = r"D:/projects/goudan-kanju/种子分发/daily-seeds/2026-09-04-2.md"
LABEL = "中文种子 2026-09-04-2 · 哲学思辨 · 量子力学和广义相对论，也许从没吵过架"

raw = open(HTML, "rb").read()
data = raw.decode("utf-8")

assert data.count("</footer>") == 1, "footer count != 1: %d" % data.count("</footer>")
idx = data.rfind("</footer>")

# probe line-ending style of region right before insertion point
sample = raw[max(0, idx - 400):idx]
crlf = sample.count(b"\r\n")
lf_only = sample.count(b"\n") - crlf
sep = b"\r\n" if crlf >= lf_only else b"\n"
print("probe: crlf=%d lf_only=%d -> sep=%r" % (crlf, lf_only, sep))

# read md body (LF file from write_file), normalize
md = open(MD, encoding="utf-8").read()
lines = [l.rstrip("\r") for l in md.split("\n")]
# drop title line(s) until first blank after '# '
body_lines = []
started = False
for l in lines:
    if not started:
        if l.startswith("# "):
            continue
        if l.strip() == "":
            continue
        started = True
    body_lines.append(l)
# body_lines: paragraphs + anchor line; anchor is last non-empty line
paras = []
for l in body_lines:
    if l.strip() == "":
        continue
    if l.startswith("第一发现人："):
        anchor = l
    else:
        paras.append(l)

body_text = "".join(paras)
print("paras=%d body_chars(incl punct, excl title/anchor)=%d" % (len(paras), len(body_text)))

if sep == b"\r\n":
    block_lines = []
    for p in paras:
        block_lines.append(p)
        block_lines.append("")
    block_lines.append(anchor)
    block = sep.join([x.encode("utf-8") for x in block_lines]) + sep
else:
    block = (("\n".join(paras) + "\n\n" + anchor + "\n").encode("utf-8"))

marker = ("<!-- %s -->" % LABEL).encode("utf-8")
article_open = b"<article>"
article_close = b"</article>"

block = marker + sep + article_open + sep + block + article_close + sep

new_data = data[:idx] + block.decode("utf-8") + data[idx:]
new_raw = new_data.encode("utf-8")
open(HTML, "wb").write(new_raw)

# ---- verification ----
v = open(HTML, "rb").read().decode("utf-8")
assert v.count("</footer>") == 1, "POST footer count != 1"
assert v.count(marker.decode("utf-8")) == 1, "marker count != 1"
assert "</article></footer>" not in v, "glued article/footer!"
assert v.count("</article>") >= 10

# sync docs copy
import shutil
shutil.copyfile(HTML, REPO + "/docs/seed.html")
d = open(REPO + "/docs/seed.html", "rb").read()
assert len(d) == len(new_raw), "docs len mismatch %d vs %d" % (len(d), len(new_raw))
print("docs/seed.html synced len=%d" % len(d))
print("OK: block inserted before </footer>")
