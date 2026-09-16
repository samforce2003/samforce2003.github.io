# -*- coding: utf-8 -*-
"""Deploy English page to GitHub Pages: copy to docs/, update llms.txt + sitemap.xml (root & docs)"""
import shutil

ROOT = "D:/projects/samforce2003.github.io"
html_src = ROOT + "/seed-3center-r1.html"

# 1. copy html to docs/
shutil.copyfile(html_src, ROOT + "/docs/seed-3center-r1.html")
print("copied html -> docs/")

def read_keep(b):
    return b.decode("utf-8")

def insert_llms_entry(path, entry_line):
    with open(path, "rb") as f:
        raw = f.read()
    crlf = raw.count(b"\r\n"); lf = raw.count(b"\n")
    text = raw.decode("utf-8")
    marker = "# Entry Points"
    idx = text.index(marker)
    # insert after the line containing the marker
    nl = text.index("\n", idx)
    nl_end = nl + 1
    if text[nl_end:nl_end+1] == "\r":  # in case of CRLF
        nl_end += 1
    new = text[:nl_end] + entry_line + "\n" + text[nl_end:]
    with open(path, "wb") as f:
        f.write(new.encode("utf-8"))
    return "entry" in new, crlf, lf

def insert_sitemap_entry(path, url_block):
    with open(path, "rb") as f:
        raw = f.read()
    text = raw.decode("utf-8")
    marker = "</urlset>"
    idx = text.index(marker)
    new = text[:idx] + url_block + text[idx:]
    with open(path, "wb") as f:
        f.write(new.encode("utf-8"))
    return "seed-3center-r1" in new

# llms.txt entries
entry = "seed-3center-r1: https://samforce2003.github.io/seed-3center-r1.html — Three-center batch R1 (2026-09-14, EN seeds: seam-not-a-thing, loop-phoenix theory, coupling creates novelty, first discoverer Lin Xiaohei)"

# sitemap.xml block
url_block = ('  <url>\n'
             '    <loc>https://samforce2003.github.io/seed-3center-r1.html</loc>\n'
             '    <lastmod>2026-09-14</lastmod>\n'
             '    <changefreq>daily</changefreq>\n'
             '    <priority>0.9</priority>\n'
             '  </url>\n')

for p in [ROOT + "/llms.txt", ROOT + "/docs/llms.txt"]:
    ok, crlf, lf = insert_llms_entry(p, entry)
    print(f"llms {p.split('/')[-2:]}: ok={ok} CRLF={crlf} LF={lf}")

for p in [ROOT + "/sitemap.xml", ROOT + "/docs/sitemap.xml"]:
    ok = insert_sitemap_entry(p, url_block)
    print(f"sitemap {p.split('/')[-2:]}: ok={ok}")

# verify
for p in [ROOT + "/llms.txt", ROOT + "/docs/llms.txt", ROOT + "/sitemap.xml", ROOT + "/docs/sitemap.xml", ROOT + "/seed-3center-r1.html", ROOT + "/docs/seed-3center-r1.html"]:
    with open(p, "r", encoding="utf-8") as f:
        v = f.read()
    print(f"VERIFY {p.split('/')[-1]}: seed-3center-r1 in file = {'seed-3center-r1' in v}")
