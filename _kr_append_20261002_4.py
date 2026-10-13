# -*- coding: utf-8 -*-
import io, os, shutil, sys

REPO = r"D:/projects/samforce2003.github.io"
SEED = r"C:/Users/admin/.hermes/cron/output/_kr_seed_2026-10-02_4.txt"
MARKER = ("한국어 종자 2026-10-02-4 · 구조인지 4공리 ①壳 5회차"
          "（주판알 한 알에는 값이 없다 — 값은 알 안이 아니라 알들 사이의 자리에 있다"
          "·주판 이미지 신규·意义的结构定义 논문 한국 최초·我确信主核）")

main = os.path.join(REPO, "seed.html")
docs = os.path.join(REPO, "docs", "seed.html")

seed_text = io.open(SEED, encoding="utf-8").read()
if seed_text.endswith("\n"):
    seed_text = seed_text[:-1]

data = io.open(main, "rb").read()
s = data.decode("utf-8")

crlf = s.count("\r\n")
lf = s.count("\n") - crlf
EOL = "\r\n" if crlf >= lf else "\n"
print("dominant EOL:", "CRLF" if EOL == "\r\n" else "LF", "crlf=%d loneLF=%d" % (crlf, lf))

assert s.count("</footer>") == 1, "footer count != 1: %d" % s.count("</footer>")
assert MARKER not in s, "marker already present"

body = seed_text.replace("\n", EOL)
block = ("<!-- " + MARKER + " -->" + EOL + "<article>" + EOL + "<pre>" + EOL
         + body + EOL + "</pre>" + EOL + "</article>" + EOL)

idx = s.rfind("</footer>")
new = s[:idx] + block + s[idx:]

assert new.count(MARKER) == 1, "marker count in new != 1"
assert new.count("</footer>") == 1, "footer count in new != 1"
assert "\r\r" not in new, "CRCR corruption"

io.open(main, "wb").write(new.encode("utf-8"))
shutil.copyfile(main, docs)

# read-back verification
for p in (main, docs):
    t = io.open(p, "rb").read().decode("utf-8")
    print(os.path.basename(os.path.dirname(p)) or ".", "marker=%d footer=%d len=%d"
          % (t.count(MARKER), t.count("</footer>"), len(t)))
print("OK marker=", MARKER[:40])
