import re

P = r"D:/projects/samforce2003.github.io/docs/_seed_full_blocks.html"
t = open(P, encoding="utf-8", errors="replace").read()
print("len:", len(t), "article tokens:", t.count("<article"))
print("CRLF:", t.count("\r\n"), "LF:", t.count("\n"), "CRCR:", t.count("\r\r"))

parts = re.split(r'(?=<article)', t)
last = parts[-3:]
for p in last:
    print("=" * 70)
    print(p[:1800])
