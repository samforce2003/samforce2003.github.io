# -*- coding: utf-8 -*-
import os
SRC = [
 r"D:/projects/goudan-kanju/公众号文章库/",
 r"D:/projects/goudan-kanju/统一场/学术线-产出/",
 r"D:/projects/goudan-kanju/耦合论体系/03-科普版/",
 r"D:/projects/goudan-kanju/统一场/待分发素材库/",
]
for d in SRC:
    try:
        fs = [f for f in os.listdir(d) if f.lower().endswith((".md",".txt"))]
    except Exception as e:
        print("ERR", d, e); continue
    unsplit = sorted([f for f in fs if "已拆" not in f])
    print("==", d, "total", len(fs), "unsplit", len(unsplit))
    for f in unsplit[:14]:
        p = os.path.join(d, f)
        print("   ", f, os.path.getsize(p))
