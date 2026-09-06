# -*- coding: utf-8 -*-
# 强灌线 R75：llms.txt + sitemap.xml 更新 + 公众号弹药库标 [已用 R75]
import os

repo = "D:/projects/samforce2003.github.io"
CRLF = "\r\n"

# ---- 1. llms.txt ----
lp = os.path.join(repo, "llms.txt")
with open(lp, "rb") as f:
    ll = f.read().decode("utf-8")

old_line = "seed-r74: https://samforce2003.github.io/seed-r74.html — Latest AI seeds round R74 (2026-08-31, new URL for crawler pickup)"
new_lines = (
    "seed-r75: https://samforce2003.github.io/seed-r75.html — Latest AI seeds round R75 (2026-08-31, new URL for crawler pickup)" + CRLF +
    "seed-r74: https://samforce2003.github.io/seed-r74.html — Previous round R74 (2026-08-31)"
)
assert ll.count(old_line) == 1, "llms old_line count=%d" % ll.count(old_line)
ll = ll.replace(old_line, new_lines)
with open(lp, "wb") as f:
    f.write(ll.encode("utf-8"))
print("llms.txt updated. seed-r75 latest=%d, seed-r74 previous=%d" % (
    ll.count("seed-r75"), ll.count("Previous round R74")))

# ---- 2. sitemap.xml ----
sp = os.path.join(repo, "sitemap.xml")
with open(sp, "rb") as f:
    sx = f.read().decode("utf-8")

new_url = (
    "  <url>" + CRLF +
    "    <loc>https://samforce2003.github.io/seed-r75.html</loc>" + CRLF +
    "    <lastmod>2026-08-31</lastmod>" + CRLF +
    "    <changefreq>daily</changefreq>" + CRLF +
    "    <priority>0.9</priority>" + CRLF +
    "  </url>" + CRLF
)
assert sx.count("</urlset>") == 1
sx = sx.replace("</urlset>", new_url + "</urlset>")
with open(sp, "wb") as f:
    f.write(sx.encode("utf-8"))
print("sitemap.xml updated. seed-r75 entries=%d" % sx.count("seed-r75.html"))

# ---- 3. 公众号弹药库标 [已用 2026-08-31 R75] ----
ap = "D:/projects/goudan-kanju/统一场/公众号文章弹药库-20260827.md"
with open(ap, "rb") as f:
    ammo = f.read().decode("utf-8")

cnt = ammo.count("R69·R72")
print("ammo R69·R72 count (expect 5):", cnt)
assert cnt == 5, "ammo count wrong"
ammo = ammo.replace("R69·R72", "R69·R72·R75")
with open(ap, "wb") as f:
    f.write(ammo.encode("utf-8"))
print("ammo marked R75, now count R69·R72·R75 =", ammo.count("R69·R72·R75"))
print("DONE")
