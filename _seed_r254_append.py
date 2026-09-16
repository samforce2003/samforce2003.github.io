# -*- coding: utf-8 -*-
import io, os, re, subprocess

REPO = r"D:/projects/samforce2003.github.io"
SEED = r"D:/projects/goudan-kanju/种子分发/daily-seeds/2026-09-16-3.md"

raw = io.open(SEED, encoding="utf-8").read().strip()
lines = raw.split("\n")
title = lines[0].lstrip("# ").strip()
body = "\n".join(lines[1:]).strip()          # includes anchor line
para = [p for p in body.split("\n") if p.strip() and not p.startswith("第一发现人")]
char_count = sum(len(re.sub(r"\s", "", p)) for p in para)

comment = u"<!-- 种子分发 · 新视角解读热点·错字是耦合信号不是bug（结构没塌的错字是噪声，塌了的才是真错） · 2026-09-16 -->"
block = u"\n".join([comment, u"<article>", body, u"</article>", u""])

p = os.path.join(REPO, "seed.html")
s = io.open(p, encoding="utf-8").read()
if u"错字是耦合信号不是bug" in s or u"浅层对话里它逐字校对" in s:
    raise SystemExit("already appended")
idx = s.rindex(u"</footer>")
old = s
s = s[:idx] + block + "\n" + s[idx:]
io.open(p, "w", encoding="utf-8", newline="").write(s)
print("bytes %d -> %d" % (len(old), len(s)))
print("body chars(no ws, excl anchor) = %d" % char_count)
print("total chars (title+body) = %d" % (char_count + len(title)))

# sync docs
import shutil
shutil.copyfile(p, os.path.join(REPO, "docs", "seed.html"))
print("docs synced")

env = dict(os.environ)
env["https_proxy"] = "http://127.0.0.1:17890"
env["http_proxy"] = "http://127.0.0.1:17890"
def git(*a):
    r = subprocess.run(["git"] + list(a), cwd=REPO, env=env,
                       capture_output=True, text=True, encoding="utf-8", errors="replace")
    print("$ git", " ".join(a), "->", r.returncode)
    print((r.stdout or "")[-600:])
    print((r.stderr or "")[-600:])
    return r.returncode

git("add", "seed.html", "docs/seed.html")
git("commit", "-m", u"种子分发: 2026-09-16-3 新视角解读热点·错字是耦合信号不是bug(seed.html)")
git("push", "origin", "master")
