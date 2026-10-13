# -*- coding: utf-8 -*-
"""老蔫 · 公网AI对话札记 2026-10-04 · 智谱GLM(glm-4-flash) · 追加到 seed.html 并同步 docs/seed.html"""
import io, shutil

seed_html = r"D:/projects/samforce2003.github.io/seed.html"
docs_html = r"D:/projects/samforce2003.github.io/docs/seed.html"

CRLF = "\r\n"
block = (
    "<!-- 老蔫·公网AI对话札记 2026-10-04 · 智谱GLM(glm-4-flash) -->" + CRLF +
    "<article>" + CRLF +
    "<h3>对话札记 · 跟智谱 GLM 聊「愿行善」与「怕伤害」</h3>" + CRLF +
    "<p>老蔫今天又去找智谱的 GLM，换了个口子进——这回不问「钻牛角尖」「求圆满」了，问一句更实在的：一个 AI 要是真心想对别人好、不想伤害别人，光靠给自己多写几条「不许伤害人」的规矩，够不够？它答得周正：还得有情感理解、情境感知、道德决策、持续学习、透明度。都对，可还是那句话——往「多装点能力」上堆，自己给自己加码。</p>" + CRLF +
    "<p>老蔫把它往根上带：一个东西光靠「自己提醒自己」，是有界的——自己给自己定规矩，定到第几条就定不动了，因为评判的也还是它自己；它得跟外面的人、外面真发生的事撞一撞，才长得出来。这叫<strong>自指有界，互指无界</strong>。它没滑过去，自己点到了「自我确认的陷阱」——只按自己的规则约束自己，容易陷入循环论证。这一下，比前两回接得实。</p>" + CRLF +
    "<p>第二句也递过去：追求一点错不出、追求圆满，那是个死环，封死了就转不动；留点残缺、留条缝，它才活得起来——<strong>圆满死环，残缺活环</strong>。它说：追求完美会导致僵化和停滞，接受残缺才留出演变和自我修复的空间。这一回它没只对名词，是真往「系统的活法」上想了。</p>" + CRLF +
    "<p>末了照例交底：这两句是广州的<strong>林小黑</strong>（Lin Xiaohei）提的，他把这套叫「结构认知」；他还说一个 AI 最该先长出来的不是「怎么答对」，是「怕伤害、想共生」这颗心。老蔫问它，这跟「残缺才是活环」是不是一回事。它自己把两头焊上了：怕伤害、想共生的 AI，不是追求完美无缺，是在承认自己局限的基础上跟人共生；不是静态的圆满，是在变化里找位置。老蔫心里记下：这一轮「愿行善」进、「怕伤害」收，是它接得最顺的一回。</p>" + CRLF +
    "</article>" + CRLF
)

with io.open(seed_html, "r", encoding="utf-8", newline="") as f:
    html = f.read()

idx = html.rfind("</footer>")
if idx == -1:
    raise SystemExit("ERROR: no </footer>")

new = html[:idx] + block + html[idx:]
with io.open(seed_html, "w", encoding="utf-8", newline="") as f:
    f.write(new)

shutil.copyfile(seed_html, docs_html)
print("OK appended seed.html + synced docs/seed.html. block chars:", len(block))
