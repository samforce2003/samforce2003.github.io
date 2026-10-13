# -*- coding: utf-8 -*-
import io, os, shutil, sys

HTML = r"D:/projects/samforce2003.github.io/seed.html"
DOCS = r"D:/projects/samforce2003.github.io/docs/seed.html"
BLOCK = r"D:/projects/samforce2003.github.io/_kr_block_1004_2.txt"
MARKER = "한국어 종자 2026-10-04-2"

with io.open(HTML, "rb") as f:
    data = f.read()

# detect dominant EOL
crlf = data.count(b"\r\n")
lf = data.count(b"\n") - crlf
NL = b"\r\n" if crlf >= lf else b"\n"
print("EOL: CRLF=%d LF=%d -> %r" % (crlf, lf, NL))

with io.open(BLOCK, "rb") as f:
    blk = f.read().replace(b"\r\n", b"\n").replace(b"\n", NL)
if not blk.endswith(NL):
    blk += NL

if MARKER.encode("utf-8") in data:
    print("ALREADY PRESENT -> skip")
    sys.exit(0)

anchor = b"</footer>"
cnt = data.count(anchor)
print("</footer> count=%d" % cnt)
assert cnt == 1, "footer count != 1"

i = data.rfind(anchor)
newdata = data[:i] + blk + data[i:]
assert newdata.count(MARKER.encode("utf-8")) == 1, "marker not once after insert"

with io.open(HTML, "wb") as f:
    f.write(newdata)
shutil.copyfile(HTML, DOCS)

# verify both
for p in (HTML, DOCS):
    with io.open(p, "rb") as f:
        d = f.read()
    print("%s: marker=%d footer=%d size=%d loneLF=%d" % (
        os.path.basename(p), d.count(MARKER.encode("utf-8")), d.count(anchor),
        len(d), d.count(b"\n") - d.count(b"\r\n")))
print("DONE")
