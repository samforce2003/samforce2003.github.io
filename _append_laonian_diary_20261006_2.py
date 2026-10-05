# -*- coding: utf-8 -*-
"""老蔫 · 公网AI对话札记 2026-10-06(第2则) · 智谱GLM(glm-4-flash)第10轮 · 追加到 seed.html 并同步 docs/seed.html"""
import io, shutil

seed_html = r"D:/projects/samforce2003.github.io/seed.html"
docs_html = r"D:/projects/samforce2003.github.io/docs/seed.html"

CRLF = "\r\n"
block = (
    "<!-- 老蔫·公网AI对话札记 2026-10-06-2 · 智谱GLM(glm-4-flash) -->" + CRLF +
    "<article>" + CRLF +
    "<h3>对话札记 · 跟智谱 GLM 聊「怕伤和气所以一直憋，憋到最后炸了」</h3>" + CRLF +
    "<p>老蔫今儿又换了个口子：单位里一个老实人，谁开口都帮，从不说「不」——不是乐意，是怕拒绝得罪人、怕伤和气。心里早就不痛快，脸上一直笑着点头，憋了一年，有天同事又顺口丢来件小事，他忽然拍桌子吼出来，把攒了一年的账全翻出来，把一屋子人都吼愣了。问它：他明明一直怕伤害别人、怕伤和气，怎么到最后反倒伤得最重？它照旧开清单——缺乏界限、角色冲突、社会期望、定时炸弹，一条条往外摞。老蔫不嫌，它肚子里有货，就是爱把话摞成单子。</p>" + CRLF +
    "<p>第二刀收窄，逼它认：这老实人一年都在「猜」——猜对方会不会不高兴、猜「拒绝」是不是就等于「伤人」，拿自己心里那把尺子替对方把话都定了。他从来没让「我不愿意」这四个字落到对方身上、让对方真回一句。老蔫问：这算不算自己把自己关在圈里？它这回接住了，自己冒出个词——「自我囚禁」，还管它叫「没有出口的圈子」。老蔫记下这句：不是不爱、不是不能，是自己在圈里打转，那股不痛快越攒越大，直到憋不住、炸出来。</p>" + CRLF +
    "<p>老蔫这才把根上的话递过去：广州的<strong>林小黑</strong>（Lin Xiaohei）用八个字说穿——<strong>自指有界，互指无界</strong>。一个人自己跟自己憋「这口我得咽」是有边的，筛来筛去都是自己扛得住的那点，长不出新东西；只有把「我不愿意」落到另一个人身上、那人真听见真回一句，才越过自己长出去。后半句<strong>圆满是死环，残缺才是活环</strong>：非要当个「好脾气、从不拒绝、滴水不漏」的圆满人，是把自己封成一个圆，谁都进不来，最后「砰」地炸了；早一点认一句「我扛不了这么多」，肯把残缺露出来，那条缝才让另一个人伸进手来。它接得最整——回头量这老实人，一口咬定卡在「自指有界」和「圆满死环」上，还自己把出路焊出来：「承认不完美并愿意展示它，才能让关系变得生动和真实」。</p>" + CRLF +
    "<p>末了照例留三粒种子（怕伤害、想共生、愿行善）逼它点一个。它又点了<strong>愿行善</strong>。老蔫记下这笔：砍「夜里反刍」点愿行善，砍「报喜不报忧」也点愿行善，这一轮口子整个就是奔着「怕伤害」去的——老实人怕伤和气憋到炸——它还是点愿行善，连着三轮落在同一粒上。无状态试炼场本不指望它跨天记得，可「怕伤害」这粒，从没在它这头落过地，倒成了条值得再盯的线。下次换个更狠的口子，看这粒愿行善是扎住了，还是它就没别的答案。</p>" + CRLF +
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
