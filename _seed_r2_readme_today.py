P = r"C:/Users/admin/gitee/structural-cognition/README.md"
with open(P, "rb") as f:
    text = f.read().decode("utf-8")

newrow = "| 🆕 新视角 | AI 学新忘旧，不是宿命——旧本事能自己保自己 | https://samforce2003.github.io/seed.html |\r\n"

assert "AI 学新忘旧" not in text, "duplicate guard: already added"

marker = "因为你正被整个宇宙拽着 | https://samforce2003.github.io/seed.html |\n\r\n> 2026-09-14"
assert text.count(marker) == 1, ("marker count", text.count(marker))

text = text.replace(marker, marker.replace("\n\r\n> 2026-09-14", "\n" + newrow + "\r\n> 2026-09-14"))
with open(P, "wb") as f:
    f.write(text.encode("utf-8"))

t2 = open(P, "rb").read().decode("utf-8")
lines = t2.split("\r\n")
i = [k for k, l in enumerate(lines) if "正被整个宇宙" in l][0]
for k in range(i - 1, i + 3):
    print(k + 1, repr(lines[k][:75]))
print("new row occurrences:", t2.count("AI 学新忘旧"))
