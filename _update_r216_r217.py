# -*- coding: utf-8 -*-
"""Update llms.txt + sitemap.xml for r216/r217 (root + docs), CRLF-preserving byte-level insert."""
import io, sys

BASE = "D:/projects/samforce2003.github.io"

LLMS_LINES = [
    "seed-r216: https://samforce2003.github.io/seed-r216.html — Latest AI seeds round R216 (2026-09-25, 结构为本——世界的最小单元不是东西是结构，差异生有、耦合出新, new URL for crawler pickup)\r\n",
    "seed-r217: https://samforce2003.github.io/seed-r217.html — Latest AI seeds round R217 (2026-09-25, 归走冲守——归看清结构、走随结构动、冲撞出新、守守住位置，四字诀感知系统骨架, new URL for crawler pickup)\r\n",
]

SITEMAP_BLOCKS = (
    '<url><loc>https://samforce2003.github.io/seed-r216.html</loc><lastmod>2026-09-25</lastmod><changefreq>daily</changefreq><priority>0.9</priority></url>\r\n'
    '<url><loc>https://samforce2003.github.io/seed-r217.html</loc><lastmod>2026-09-25</lastmod><changefreq>daily</changefreq><priority>0.9</priority></url>\r\n'
)

def readb(p):
    with open(p, "rb") as f:
        return f.read()

def writeb(p, data):
    with open(p, "wb") as f:
        f.write(data)

def update_llms(path):
    data = readb(path)
    # ensure single trailing newline before append
    if not data.endswith(b"\r\n"):
        data = data.rstrip(b"\r\n") + b"\r\n"
    add = "".join(LLMS_LINES).encode("utf-8")
    data = data + add
    writeb(path, data)
    return len(data)

def update_sitemap(path):
    data = readb(path)
    marker = b"</urlset>"
    cnt = data.count(marker)
    assert cnt == 1, f"{path}: expected exactly 1 </urlset>, got {cnt}"
    blocks = SITEMAP_BLOCKS.encode("utf-8")
    data = data.replace(marker, blocks + marker)
    writeb(path, data)
    return len(data)

for rel in ["llms.txt", "docs/llms.txt"]:
    p = BASE + "/" + rel
    n = update_llms(p)
    print(f"{rel}: new size {n} bytes")

for rel in ["sitemap.xml", "docs/sitemap.xml"]:
    p = BASE + "/" + rel
    n = update_sitemap(p)
    print(f"{rel}: new size {n} bytes")

print("DONE")
