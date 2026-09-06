import io
p = r"D:\projects\goudan-kanju\统一场\公众号文章弹药库-20260827.md"
raw = io.open(p, "rb").read()
print("CRLF count:", raw.count(b"\r\n"))
print("bare LF (not preceded by CR):", raw.count(b"\n") - raw.count(b"\r\n"))
print("double CR:", raw.count(b"\r\r"))
# show lines 74-78 raw repr to understand structure
lines = raw.split(b"\n")
for i in range(73, 79):
    print(i, repr(lines[i][:120]))
