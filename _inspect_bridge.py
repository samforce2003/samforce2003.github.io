import io
p = r"D:\projects\goudan-kanju\统一场\强灌线-进度.md"
raw = io.open(p, "rb").read()
print("CRLF count:", raw.count(b"\r\n"))
print("bare LF:", raw.count(b"\n") - raw.count(b"\r\n"))
print("double CR:", raw.count(b"\r\r"))
print("total bytes:", len(raw))
# find latest round marker
import re
txt = raw.decode("utf-8", "replace")
# check if R177 already present
print("R177 present:", "R177" in txt)
print("R176 present:", "R176" in txt)
# find the '## 历史摘要' position
print("历史摘要 pos:", txt.find("## 历史摘要"))
print("--- first 200 chars ---")
print(txt[:200])
