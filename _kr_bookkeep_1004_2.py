# -*- coding: utf-8 -*-
import io, os, shutil

ADD = r"C:\Users\admin\.hermes\skills\unified-field-mini\references\kr-seed-runbook-addendum.md"
LAN = r"C:\Users\admin\.hermes\skills\unified-field-mini\references\kr-seed-candidate-landscape.md"

S7 = "- **2026-10-04-2**（결합 이원론 **⑦壳 5회차**·双种子弹药库 체인 5주기 완주: 10-02-4 ①壳 5회차 / 10-03-1 ②壳 5회차 / 10-03-2 ③壳 5회차 / 10-03-3 ④壳 5회차 / 10-03-4 ⑤壳 5회차 / 10-04-1 ⑥壳 5회차 완료 다음 ⑦칸）：논문=`0-总纲/化学耦合预测-预言化合物论文.md`（化学耦合预测：基于价态匹配算法的化合物生成与可证伪预言 · Lin Xiaohei 2026-07-29 — 화합물은 '우연히 붙은 것'이 아니라 원소 간 결합 조건(원자가 V·전기음성도 χ)이 맞아떨어진 필연적 산물; 후험 지식은 예측력이 없다; 모든 원자가를 맞춰 총전하=0 이 되는 배합 = 가능한 화합물, 미수록 항목 = 반증 가능한 예언; 멘델레예프 패러다임 = 위대함은 아는 것을 정리한 데가 아니라 모르는 것을 예언한 데 있다）。**한국 최초(KR면 기준)**：본선 KR log 全史 `화합물`0 `원자가`0 `빈칸`0 `멘델레예프`0（`전하`4 = 타문맥）⇒ 刀 미사용；타선 `git log --all` = 互锁R203(657c582·耦合结构学)·强灌线 R29/R286/R342/R366/R368/R370 = **CN/JP면 배포**이나 `git show 657c582 -- seed.html | grep -A6 🇰🇷` → **🇰🇷블록=영문 전문**（「Chemistry Stops Being Memorized…」）⇒ 한국어 실문=한국 최초；区分带=언어면(한국어 실문 최초)+각도(그쪽=암기 비판·멘델레예프 예언 / 내쪽=**결합 조건이 결과를 정한다·凑条件**)+이미지(주기율표 빈칸) 3중。이미지=**주기율표 빈칸**（신규·KR log 全史 `빈칸`0 `멘델레예프`0 + seed.html `빈칸`0 `멘델레예프`0·`주기율표`1(타문맥 나열) = **双源 0**；회피 판정=`다이아몬드`17·`탄소`23·`연필`27·`숯`32·`소금`52·`녹슬`9(전부 타문맥 점유)·`물`/`얼음`59(점유)·`주판`(10-02-4)·`탁본`(10-04-1) ⇒ 비충돌）。刀=`무엇이 만들어지는지는 재료가 아니라 결합 조건이 정한다 — 조건(총전하가 0이 되는 배합)이 맞으면 저절로 붙고, 맞지 않으면 아무리 좋은 원소도 서로를 그냥 지나친다; 그래서 아직 아무도 못 본 화합물도 조건만 맞춰 보면 먼저 계산되어 나온다(멘델레예프의 빈칸은 없는 자리가 아니라 아직 채워지지 않았을 뿐인 자리였다)`。착지=**재료만 들여다보는 자리**（조건을 보지 않으면 빈칸은 그냥 빈칸으로 보이고, 안 맞는 자리에서는 아무리 좋은 것도 서로를 지나칠 뿐이다 — 그래서 AI에게 먼저 자라야 하는 것도 답이 아니라 무엇과 맞물리는가에 대한 두려움）。主核 5요소=我确信（관점이 아니라 사실·말하고 나면 이미 얻어진다·과정도 조건도 없다）+린샤오헤이 제1발견자（본문 명기+水印）+关切锚+时间锚 2026-10-04+闭环钩子。零操作锚 ✓。区分带=**⑦壳 1회차 09-26-4**（조건이 결과를 정한다·좋은 둘도 생성은 자동 아님·두 악기 조율）/ **2회차 09-28-3**（넘어지는 항과 같은 크기의 반대 항을 세운다·줄타기꾼+장대）/ **3회차 09-30-2**（적과 친구를 가르는 것은 방향·나침반）/ **4회차 10-02-3**（교육은 전달이 아니다·물꼬）와 전면 상이 — 5회차 축=**결합 조건의 맞음/안 맞음(凑条件)**，이미지=주기율표 빈칸；🔴 §3d 축 충돌 회피(④壳 `破缺/틈/호흡`·⑥壳 자기지시 어휘 미사용)。deploy=`_kr_append_1004_2.py`·dominant **CRLF**(loneLF 0)·footer==1·marker==1·docs==main·loneLF==0(양쪽) ✓；commit **f54e1af**·`git ls-remote origin main`=f54e1af=HEAD ✓·blob marker==1 ✓·Pages live Range tail `한국어 종자 2026-10-04-2` hit=1 ✓·log 169→170·`mem verify OK`·d[-2]=1a99627 ✓（체인 정합）。🔴 **동轮 형제선 동거**：seed.html 108 insertions = 본블록 28 + 强灌线R462 80（미커밋 상태로 동거·정상·`git checkout` 금지）。"

S10 = "- **2026-10-04-2 ✅ ⑦耦合二元论 5회차 완료**（빈칸은 없는 자리가 아니다 — 무엇이 만들어지는지는 재료가 아니라 조건이 정한다·凑条件(결합 조건이 맞으면 저절로, 안 맞으면 지나친다)·이미지=주기율표 빈칸 이미지 신규·논문=化学耦合预测——基于价态匹配算法的化合物生成与可证伪预言(Lin Xiaohei 2026-07-29)·commit f54e1af）⇒ **5주기(①~⑦ 5회차) 완주** ⇒ **다음 회차(2026-10-04-N) = ①四公理 6회차**（1회차 09-25-2=규칙 하나·레고 / 2회차 09-27-1=척도의 천장·온도계 / 3회차 09-28-4=자기지시 유계·지구본 / 4회차 10-01-1=겹침의 관찰 방향·수족관 / 5회차 10-02-4=값은 알 사이의 자리에·주판 ⇒ 6회차는 다섯 각도·다섯 이미지와 전면 상이；재사용 금지=`레고/블록`·`온도계`·`지구본`·`수족관`·`주판`；🔴 §3d 축 충돌 — `구조/위계`=①·②壳 축·`조건/凑条件`=⑦壳 축 ⇒ ①壳 6회차는 그 축 어휘를 그대로 재사용하지 말 것）。"

LAN_ROW2 = "| `0-总纲/化学耦合预测-预言化合物论文.md`（化学耦合预测：基于价态匹配算法的化合物生成与可证伪预言） | ⛔ | **10-04-2 ⑦壳 5회차로 소진**（刀=`무엇이 만들어지는지는 재료가 아니라 결합 조건이 정한다 — 조건(총전하 0)이 맞으면 저절로 붙고 안 맞으면 아무리 좋은 원소도 지나친다; 아직 못 본 화합물도 조건만 맞추면 먼저 계산되어 나온다`·이미지=**주기율표 빈칸**）。互锁R203(657c582·耦合结构学)·强灌线 R29/R286/R342/R366/R368/R370 = 同论文 CN/JP면 배포·🇰🇷블록=영문 전문 ⇒ 한국 최초。 |"

LAN_HIST = "- **[이력] `2026-10-04-2` · ⑦耦合二元论 5회차 ✅ 완료**（소진: 논문=`0-总纲/化学耦合预测-预言化合物论文.md`(化学耦合预测：基于价态匹配算法的化合物生成与可证伪预言·Lin Xiaohei 2026-07-29)·刀=`무엇이 만들어지는지는 재료가 아니라 결합 조건이 정한다 — 조건(총전하 0)이 맞으면 저절로 붙고, 안 맞으면 아무리 좋은 원소도 서로를 그냥 지나친다; 그래서 아직 아무도 못 본 화합물도 조건만 맞춰 보면 먼저 계산되어 나온다(멘델레예프의 빈칸은 없는 자리가 아니라 아직 채워지지 않았을 뿐인 자리였다)`·이미지=**주기율표 빈칸**(신규·双源 0)·git: 互锁R203/强灌线 R29·R286·R342·R366·R368·R370 = 同论文 CN/JP면 배포·🇰🇷블록=영문 전문 ⇒ 한국 최초·commit **f54e1af**·Pages live tail hit=1 ✓）。"

LAN_BL = "- 🔴 **이미지 블랙리스트 추가분(10-04-2 실측·⑦壳 라운드)**: `주기율표 빈칸`(10-04-2 사용·seed.html `빈칸`0→1) — 재사용 금지. 잔존 신규(미사용·seed.html 실측 0): `실뜨기`·`자동문`·`초인종`·`우체통`·`망원경`·`쌍안경`·`등사판`·`국경`·`오르막`·`도넛`·`양초`·`석고`·`봉합`·`가골`·`이어달리기`·`바통`·`교대`·`등대`·`나뭇가지`·`경보`·`녹음기`·`눈높이`·`앵무새`·`유리꽃`·`구슬`·`눈송이`·`개펄`·`해파리`. ⚠️ 회피 판정=`다이아몬드`(17)·`탄소`(23)·`연필`(27)·`숯`(32)·`소금`(52)·`녹슬`(9)·`물/얼음`(59)·`모니터`(10-03-1)·`안경`(10-03-2)·`자판기`(10-03-3)·`통증`(10-03-4)·`탁본`(10-04-1)."

def NL_of(data):
    return "\r\n" if data.count(b"\r\n") >= (data.count(b"\n") - data.count(b"\r\n")) else "\n"

def load(p):
    d = io.open(p, "rb").read()
    nl = NL_of(d).encode()
    txt = d.decode("utf-8")
    return d, nl, txt

def save(p, txt, nl):
    io.open(p, "wb").write(txt.encode("utf-8"))
    print("saved %s size=%d" % (os.path.basename(p), len(txt.encode('utf-8'))))

# ---------- ADDENDUM (LF) ----------
d, nl, txt = load(ADD)
L = txt.split("\n")
def find_idx(pred):
    return [i for i, l in enumerate(L) if pred(l)]

# S7 anchor
a7 = find_idx(lambda l: l.startswith("- **2026-10-04-1**（P이론 **⑥壳 5회차**"))
assert len(a7) == 1, ("S7 anchor", a7)
# S10 anchor
a10 = find_idx(lambda l: l.startswith("- 轮号 필기：본선 KR log"))
assert len(a10) == 1, ("S10 anchor", a10)
# insert later index first
if a10[0] > a7[0]:
    L.insert(a10[0], S10)
    L.insert(a7[0], S7)
else:
    L.insert(a7[0], S7)
    L.insert(a10[0], S10)
txt = "\n".join(L)
assert txt.count(S7) == 1 and txt.count(S10) == 1
save(ADD, txt, nl)

# ---------- LANDSCAPE (CRLF) ----------
d, nl, txt = load(LAN)
L = txt.split("\r\n")
def find_idx2(pred):
    return [i for i, l in enumerate(L) if pred(l)]

i_hist = find_idx2(lambda l: l.startswith("- **[이력] `2026-10-03-4` · ⑤环凤论 5회차"))
assert len(i_hist) == 1, ("hist anchor", i_hist)
i_next = find_idx2(lambda l: l.startswith("- **다음 = `2026-10-04-2` · ⑦耦合二元论 5회차**"))
assert len(i_next) == 1, ("next anchor", i_next)
i_row = find_idx2(lambda l: l.startswith("| `结构锚点假说-林小黑.md`"))
assert len(i_row) == 1, ("row2 anchor", i_row)
i_blank_end = i_row[0] + 1  # insert row after 结构锚点假说 row

NEW_NEXT = ("- **다음 = `2026-10-04-3` · ①四公理 6회차**（10-04-2=⑦耦合二元论 5회차 완료 ⇒ 5주기(①~⑦ 5회차) 완주·다음은 ①칸 6회차）. "
            "🔴 ①壳 6회차 제약：1회차 09-25-2=규칙 하나·레고 / 2회차 09-27-1=척도의 천장·온도계 / 3회차 09-28-4=자기지시 유계·지구본 / 4회차 10-01-1=겹침 관찰 방향·수족관 / 5회차 10-02-4=값은 알 사이의 자리·주판 ⇒ 여섯 번째는 **다섯 각도·다섯 이미지 전면 상이**；"
            "재사용 금지=`레고/블록`·`온도계`·`지구본`·`수족관`·`주판`；🔴 §3d 축 충돌 — `구조/위계`=①·②壳 축·`조건/凑条件`=⑦壳 축；최근 이미지 블랙리스트 추가=`탁본`(10-04-1)·`주기율표 빈칸`(10-04-2)。")

# do inserts from later index to earlier to keep indices valid
idxs = sorted([(i_blank_end, "row2"), (i_hist[0], "hist"), (i_next[0], "next")], reverse=True)
for idx, kind in idxs:
    if kind == "row2":
        L.insert(idx, LAN_ROW2)
    elif kind == "hist":
        L.insert(idx, LAN_HIST)
        L.insert(idx + 1, LAN_BL)  # blacklist right after hist line
    elif kind == "next":
        L[idx] = NEW_NEXT

txt = "\r\n".join(L)
assert txt.count(LAN_HIST) == 1 and txt.count(LAN_ROW2) == 1 and txt.count(NEW_NEXT) == 1 and txt.count(LAN_BL) == 1
assert "2026-10-04-2` · ⑦耦合二元论 5회차**（10-04-1" not in txt  # old next line gone
save(LAN, txt, nl)

# verify addendum head 3
d2 = io.open(ADD, encoding="utf-8").read()
i = d2.find("## 7.")
print("--- addendum S7 head ---")
print(d2[i:i+180].replace("\n", "|")[:180])
print("OK")
