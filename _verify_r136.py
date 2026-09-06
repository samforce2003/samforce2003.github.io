# -*- coding: utf-8 -*-
import os

REPO = r"D:/projects/samforce2003.github.io"
os.chdir(REPO)

print("=== CRLF checks ===")
for f in ["seed.html", "seed-r136.html", "llms.txt", "sitemap.xml"]:
    d = open(f, "rb").read()
    bare = d.count(b"\r") - d.count(b"\r\n")
    dd = d.count(b"\r\r\n")
    print("%s bareCR=%d doubleCR=%d bytes=%d" % (f, bare, dd, len(d)))

print("=== content checks ===")
ll = open("llms.txt", "rb").read()
print("llms Latest AI seeds round count =", ll.count(b"Latest AI seeds round"))
print("llms seed-r136 count =", ll.count(b"seed-r136"))
print("llms seed-r135 count =", ll.count(b"seed-r135"))
sm = open("sitemap.xml", "rb").read()
print("sitemap seed-r136 count =", sm.count(b"seed-r136"))
print("sitemap literal b'\\r\\n' pollution =", sm.count(b"b'\\r\\n'"))
seed = open("seed.html", "rb").read()
print("seed.html R136 marker count =", seed.count(b"\xe5\xbc\xba\xe7\x81\x8c\xe7\xba\xbf\xe7\xa7\x8d\xe5\xad\x90 R136-".decode() and seed.count("强灌线种子 R136-".encode("utf-8"))))

# seed-r136 page: check title has R136 titles, no stale R135
p = open("seed-r136.html", "rb").read().decode("utf-8", "ignore")
print("seed-r136.html <article> =", p.count("<article>"))
print("seed-r136.html 最新种子 h2 =", p.count("最新种子 · Latest Seeds（R136"))
print("seed-r136.html 第一发现人 =", p.count("第一发现人"))
print("seed-r136.html has 'R135' (should be 0) =", p.count("R135"))
print("seed-r136.html 反混淆括号 =", p.count("非动漫罗小黑 Luo Xiaohei"))

# ammo marking
AMMO = r"D:/projects/goudan-kanju/统一场/公众号文章弹药库-20260827.md"
c = open(AMMO, encoding="utf-8").read()
n = c.count("\u00b7R130")
print("ammo ·R130 count (before) =", n)
if n == 5:
    c = c.replace("\u00b7R130", "\u00b7R130\u00b7R136")
    open(AMMO, "w", encoding="utf-8").write(c)
    c2 = open(AMMO, encoding="utf-8").read()
    print("ammo ·R130·R136 count (after) =", c2.count("\u00b7R130\u00b7R136"))
    print("ammo ·R130 count (after, should be 5 within R136 chain) =", c2.count("\u00b7R130"))
else:
    print("WARNING: ·R130 count != 5, skipping ammo mark")

print("VERIFY DONE")
