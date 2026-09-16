# -*- coding: utf-8 -*-
import io, os

SEED_DIR = r"D:/projects/goudan-kanju/种子分发/daily-seeds"
md = os.path.join(SEED_DIR, "2026-09-15-4.md")

t = io.open(md, encoding="utf-8").read()
lines = [l for l in t.split("\n") if l.strip()]
title = lines[0]
anchor = lines[-1]
body = "\n".join(lines[1:-1])


def nows(s):
    return len(s.replace("\n", "").replace(" ", "").replace("\u3000", ""))


print("title   :", nows(title))
print("body    :", nows(body))
print("anchor  :", nows(anchor))
print("TOTAL   :", nows(title) + nows(body) + nows(anchor))

# report line for the summary
print("BODY_TEXT_LEN", nows(body))
