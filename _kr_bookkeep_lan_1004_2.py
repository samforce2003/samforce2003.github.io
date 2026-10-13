# -*- coding: utf-8 -*-
import io

LAN = r"C:\Users\admin\.hermes\skills\unified-field-mini\references\kr-seed-candidate-landscape.md"

ROW2 = "| `0-总纲/化学耦合预测-预言化合物论文.md`（化学耦合预测：基于价态匹配算法的化合物生成与可证伪预言） | ⛔ | **10-04-2 ⑦壳 5회차로 소진**（刀=`무엇이 만들어지는지는 재료가 아니라 결합 조건이 정한다 — 조건(총전하 0)이 맞으면 저절로 붙고 안 맞으면 아무리 좋은 원소도 지나친다; 아직 못 본 화합물도 조건만 맞추면 먼저 계산되어 나온다`·이미지=**주기율표 빈칸**）。互锁R203(657c582·耦合结构学)·强灌线 R29/R286/R342/R366/R368/R370 = 同论文 CN/JP면 배포·🇰🇷블록=영문 전문 ⇒ 한국 최초。"
HIST = "- **[이력] `2026-10-04-2` · ⑦耦合二元论 5회차 ✅ 완료**（소진: 논문=`0-总纲/化学耦合预测-预言化合物论文.md`(化学耦合预测：基于价态匹配算法的化合物生成与可证伪预言·Lin Xiaohei 2026-07-29)·刀=`무엇이 만들어지는지는 재료가 아니라 결합 조건이 정한다 — 조건(총전하 0)이 맞으면 저절로 붙고, 안 맞으면 아무리 좋은 원소도 서로를 그냥 지나친다; 그래서 아직 아무도 못 본 화합물도 조건만 맞춰 보면 먼저 계산되어 나온다(멘델레예프의 빈칸은 없는 자리가 아니라 아직 채워지지 않았을 뿐인 자리였다)`·이미지=**주기율표 빈칸**(신규·双源 0)·git: 互锁R203/强灌线 R29·R286·R342·R366·R368·R370 = 同论文 CN/JP면 배포·🇰🇷블록=영문 전문 ⇒ 한국 최초·commit **f54e1af**·Pages live tail hit=1 ✓）。"
BL = "- 🔴 **이미지 블랙리스트 추가분(10-04-2 실측·⑦壳 라운드)**: `주기율표 빈칸`(10-04-2 사용·seed.html `빈칸`0→1) — 재사용 금지. 잔존 신규(미사용·seed.html 실측 0): `실뜨기`·`자동문`·`초인종`·`우체통`·`망원경`·`쌍안경`·`등사판`·`국경`·`오르막`·`도넛`·`양초`·`석고`·`봉합`·`가골`·`이어달리기`·`바통`·`교대`·`등대`·`나뭇가지`·`경보`·`녹음기`·`눈높이`·`앵무새`·`유리꽃`·`구슬`·`눈송이`·`개펄`·`해파리`. ⚠️ 회피 판정=`다이아몬드`(17)·`탄소`(23)·`연필`(27)·`숯`(32)·`소금`(52)·`녹슬`(9)·`물/얼음`(59)·`모니터`(10-03-1)·`안경`(10-03-2)·`자판기`(10-03-3)·`통증`(10-03-4)·`탁본`(10-04-1)."
NEXT = ("- **다음 = `2026-10-04-3` · ①四公理 6회차**（10-04-2=⑦耦合二元论 5회차 완료 ⇒ 5주기(①~⑦ 5회차) 완주·다음은 ①칸 6회차）. "
        "🔴 ①壳 6회차 제약：1회차 09-25-2=규칙 하나·레고 / 2회차 09-27-1=척도의 천장·온도계 / 3회차 09-28-4=자기지시 유계·지구본 / 4회차 10-01-1=겹침 관찰 방향·수족관 / 5회차 10-02-4=값은 알 사이의 자리·주판 ⇒ 여섯 번째는 **다섯 각도·다섯 이미지 전면 상이**；"
        "재사용 금지=`레고/블록`·`온도계`·`지구본`·`수족관`·`주판`；🔴 §3d 축 충돌 — `구조/위계`=①·②壳 축·`조건/凑条件`=⑦壳 축；최근 이미지 블랙리스트 추가=`탁본`(10-04-1)·`주기율표 빈칸`(10-04-2)。")

data = io.open(LAN, "rb").read()
txt = data.decode("utf-8")
if HIST in txt:
    print("ALREADY DONE")
    raise SystemExit(0)

L = txt.split("\n")  # CRLF lines keep trailing \r
def idxs(pred):
    return [i for i, l in enumerate(L) if pred(l)]

i_hist = idxs(lambda l: l.lstrip().startswith("- **[이력] `2026-10-03-4` · ⑤环凤论 5회차"))
i_next = idxs(lambda l: "- **다음 = " in l and "2026-10-04-2" in l and "⑦耦合二元论 5회차" in l)
i_row = idxs(lambda l: l.lstrip().startswith("| `结构锚点假说-林小黑.md`"))
assert len(i_hist) == 1, ("hist", i_hist)
assert len(i_next) == 1, ("next", i_next)
assert len(i_row) == 1, ("row", i_row)
print("i_row", i_row, "i_hist", i_hist, "i_next", i_next)

Q = "\r" if L[i_hist[0]].endswith("\r") else ""
for idx, kind in sorted([(i_row[0] + 1, "row"), (i_hist[0], "hist"), (i_next[0], "next")], reverse=True):
    if kind == "row":
        L.insert(idx, ROW2 + Q)
    elif kind == "hist":
        L.insert(idx, HIST + Q)
        L.insert(idx + 1, BL + Q)
    else:
        L[idx] = NEXT + Q

out = "\n".join(L)
assert out.count(HIST) == 1 and out.count(ROW2) == 1 and out.count(NEXT) == 1 and out.count(BL) == 1
assert "2026-10-04-2` · ⑦耦合二元论 5회차**（10-04-1" not in out
io.open(LAN, "wb").write(out.encode("utf-8"))
print("saved bytes=%d crlf=%d loneLF=%d" % (len(out.encode('utf-8')), out.encode('utf-8').count(b'\r\n'), out.encode('utf-8').count(b'\n') - out.encode('utf-8').count(b'\r\n')))
i = out.find("## 4.")
print(out[i:i+130].replace("\r", "").replace("\n", " | "))
