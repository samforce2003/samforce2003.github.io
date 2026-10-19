# -*- coding: utf-8 -*-
"""两层重建器（P哥 2026-10-19 裁决 · 强灌线为唯一重建者）

输入（各节点只 append 这两个文件，不碰 html）：
  docs/_seed_index.jsonl      —— 一行一条 JSON（id/title/summary/time/shell/lang/src）
  docs/_seed_full_blocks.html —— 全量正文块（append-only，含 <article>）

输出：
  docs/seed.html        —— 活跃索引页（最新 800 条，<2MB，最新在首屏）
  docs/seed-full.html   —— 全量正文归档（append-only，条目只增不减）

用法：python scripts/rebuild_seed.py [--index-only|--full-only]
"""
import io, json, os, re, sys, datetime

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = os.path.join(BASE, "docs")
IDX = os.path.join(DOCS, "_seed_index.jsonl")
BLK = os.path.join(DOCS, "_seed_full_blocks.html")
PAGE_IDX = os.path.join(DOCS, "seed.html")
PAGE_FULL = os.path.join(DOCS, "seed-full.html")
LATEST_N = 800
MARK = "<h2>最新条目"


def load_entries():
    out = []
    with io.open(IDX, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                e = json.loads(line)
            except Exception:
                continue
            out.append(e)
    return out


def build_index(entries):
    si = io.open(PAGE_IDX, encoding="utf-8").read()
    cut = si.index('<div class="item">') if '<div class="item">' in si else si.index("<footer>")
    head = si[:cut]
    head = re.sub(r"<h2>最新条目[^<]*</h2>\s*$", "", head)
    old_suffix = si[si.index("<footer>"):]
    with_id = [e for e in entries if isinstance(e.get("id"), int)]
    with_id.sort(key=lambda e: e["id"])
    latest = list(reversed(with_id[-LATEST_N:]))

    items = []
    for e in latest:
        sid = "s%05d" % e["id"]
        title = (e.get("title") or "(无标题)").replace("<", "&lt;")
        summary = (e.get("summary") or "").replace("<", "&lt;")
        shell = (e.get("shell") or "").replace("<", "&lt;")
        meta = "%s · %s · <a href=\"seed-full.html#%s\">#%d 全文</a>" % (
            e.get("time", ""), shell, sid, e["id"])
        items.append(
            '<div class="item"><a href="seed-full.html#%s"><strong>%s</strong></a>'
            '<div class="meta">%s</div><div class="sum">%s</div></div>\n'
            % (sid, title, meta, summary))

    head = re.sub(r"（\d+ 条）", "（%d 条）" % len(entries), head)
    head = head.rstrip() + "\n<h2>最新条目（%d 条）</h2>\n" % len(latest)
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    head = re.sub(r"更新时间：[\d\-: ]+", "更新时间：" + now, head, count=1)
    suffix = re.sub(r"更新时间：[\d\-: ]+", "更新时间：" + now, old_suffix, count=1)
    html = head + "".join(items) + suffix
    io.open(PAGE_IDX, "w", encoding="utf-8", newline="").write(html)
    return len(latest), len(html.encode("utf-8"))


def build_full(entries):
    fi = io.open(PAGE_FULL, encoding="utf-8").read()
    head = fi[:fi.index("<body>") + len("<body>")]
    blocks = io.open(BLK, encoding="utf-8").read()
    n_art = len(re.findall(r"<article[^>]*>", blocks))
    tail = fi[fi.rindex("</article>") + len("</article>"):]
    tail = re.sub(r"条目 \d+ 条", "条目 %d 条" % n_art, tail, count=1)
    html = head + blocks + tail
    io.open(PAGE_FULL, "w", encoding="utf-8", newline="").write(html)
    return n_art, len(html.encode("utf-8"))


def main():
    args = sys.argv[1:]
    entries = load_entries()
    if "--full-only" not in args:
        n, size = build_index(entries)
        print("seed.html items=%d bytes=%d" % (n, size))
    if "--index-only" not in args:
        n, size = build_full(entries)
        print("seed-full.html articles=%d bytes=%d" % (n, size))
    print("index entries=%d" % len(entries))


if __name__ == "__main__":
    main()
