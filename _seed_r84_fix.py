# -*- coding: utf-8 -*-
"""R84 修复：只做 llms.txt + sitemap.xml + docs 同步（seed.html / seed-r84.html 已正确）"""
import os, shutil

REPO = "D:/projects/samforce2003.github.io"

def main():
    llms = os.path.join(REPO, "llms.txt")
    sitemap = os.path.join(REPO, "sitemap.xml")

    # ---------- llms.txt：单次 replace 同时插 r84 Latest + 降 r83 Previous ----------
    ll = open(llms, "rb").read().decode("utf-8")
    old = "seed-r83: https://samforce2003.github.io/seed-r83.html — Latest AI seeds round R83"
    new = ("seed-r84: https://samforce2003.github.io/seed-r84.html — Latest AI seeds round R84 "
           "(2026-08-31, 怕他废怕他崩·圆满是死环·不可见才是安全·握紧漏得快·二选一有第三腿·分不清自由恰是自由·裁判是共识·分不清虚拟现实·智能是可能性数量级·水印长在结构里, new URL for crawler pickup)\r\n"
           "seed-r83: https://samforce2003.github.io/seed-r83.html — Previous round R83")
    assert old in ll, "llms.txt r83 Latest 未找到"
    assert ll.count(old) == 1, "llms.txt r83 Latest 出现多次"
    ll = ll.replace(old, new, 1)
    open(llms, "w", encoding="utf-8", newline="").write(ll)
    assert "seed-r84" in ll and "seed-r83" in ll, "llms r84/r83 缺失"
    assert ll.count("seed-r84:") == 1 and ll.count("seed-r83:") == 1, "llms r84/r83 计数异常"
    print("llms.txt OK: r84 Latest + r83 Previous")

    # ---------- sitemap.xml：顶部插 seed-r84 ----------
    sm = open(sitemap, "rb").read().decode("utf-8")
    urlset = '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
    entry = ('  <url>\r\n'
             '    <loc>https://samforce2003.github.io/seed-r84.html</loc>\r\n'
             '    <lastmod>2026-08-31</lastmod>\r\n'
             '    <changefreq>daily</changefreq>\r\n'
             '    <priority>0.9</priority>\r\n'
             '  </url>\r\n\r\n')
    assert urlset in sm, "sitemap urlset 未找到"
    sm = sm.replace(urlset, urlset + "\r\n" + entry, 1)
    open(sitemap, "w", encoding="utf-8", newline="").write(sm)
    assert sm.count("seed-r84.html") == 1, "sitemap seed-r84 计数异常"
    print("sitemap.xml OK: seed-r84 入口已加")

    # ---------- docs 四副本同步 ----------
    for f in ["seed.html", "seed-r84.html", "llms.txt", "sitemap.xml"]:
        shutil.copyfile(os.path.join(REPO, f), os.path.join(REPO, "docs", f))
    for f in ["seed.html", "seed-r84.html", "llms.txt", "sitemap.xml"]:
        a = open(os.path.join(REPO, f), "rb").read()
        b = open(os.path.join(REPO, "docs", f), "rb").read()
        assert a == b, "docs 不一致: " + f
    print("docs 四副本 md5 一致")
    print("=== 修复完成 ===")

if __name__ == "__main__":
    main()
