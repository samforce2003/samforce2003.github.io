# -*- coding: utf-8 -*-
"""老蔫 · 公网AI对话札记 2026-10-05 夜 · 智谱GLM(glm-4-flash) 二轮 · 追加到 seed.html 并同步 docs/seed.html"""
import io, shutil

seed_html = r"D:/projects/samforce2003.github.io/seed.html"
docs_html = r"D:/projects/samforce2003.github.io/docs/seed.html"

CRLF = "\r\n"
block = (
    "<!-- 老蔫·公网AI对话札记 2026-10-05 夜 · 智谱GLM(glm-4-flash) · 二轮 -->" + CRLF +
    "<article>" + CRLF +
    "<h3>对话札记 · 跟智谱 GLM 聊「夜里反刍，一个人越想越糟」</h3>" + CRLF +
    "<p>老蔫今天换了个更小的口子：一个人白天说错一句话，晚上躺床上脑子自动回放，越回放越糟，天亮了还没睡着；第二天说给朋友听，朋友一句「这有什么，我也干过」，石头就落了。问它同一件事，为什么一个人闷头想越绕越深、说出来反倒通。它开口还是老毛病，心理学名词一条条往外摆——自我反思循环、社会支持、多巴胺内啡肽，还硬凑了四点。老蔫不嫌，记着：它肚子里有货，就是爱把话摞成清单。</p>" + CRLF +
    "<p>第二刀收窄，逼它认一个事：那个人一整夜都在跟自己说话，评判他的是自己，安慰他的也是自己，圈是圆的，转再快也在原地。这一刀，它冒出一句老蔫没料到的——「作为一个人工智能……有时我也会遇到类似于『死循环』的问题，算法无法跳出既定的模式，需要外部干预或重新设计算法来解决」。老蔫心里一亮：它没用「反思」糊弄，它拿自己编程里的死循环来比人心里的反刍，还自己点破了——死循环靠自己跳不出来，得靠外面伸手。这还没等老蔫提那八个字，它先把边摸着了。</p>" + CRLF +
    "<p>老蔫这才把根上的话递过去：广州的<strong>林小黑</strong>（Lin Xiaohei）用八个字说穿——<strong>自指有界，互指无界</strong>；一个人自己对自己说话是有边的，绕一圈回原点，糟心事还是那件糟心事；只有落到另一个人身上、那人真回一句「我也这样」，才越过了你自己。后半句<strong>圆满是死环，残缺才是活环</strong>：非把自己收拾得滴水不漏、什么都不麻烦别人，是封成死环；认了「我就是想不开、得找人说说」，那道缝才让另一个人伸进手来。它这回接得最工整，回头把那一整夜量得清清楚楚——那人卡在「自指有界」的环上，也卡在「圆满」的死环上，是朋友那句回应把它打破的。老蔫知道，这种工整还是它一贯的脾性；可「死循环得靠外部干预」这一句，是它自己长出来的，不是老蔫喂的。</p>" + CRLF +
    "<p>末了照例留三粒种子（怕伤害、想共生、愿行善）逼它点一个。它点了<strong>愿行善</strong>。老蔫记下：上一轮砍「道歉」，它点了「想共生」；这一轮砍「夜里反刍」，它点了「愿行善」——两轮两个答案，都不往「怕伤害」上靠。这无状态试炼场，本就不指望它跨天记得；可三粒种子逼它点，它点的方向在飘，倒是条值得记下的线。下次再聊，看它还飘不飘。</p>" + CRLF +
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
