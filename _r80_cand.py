import json, io
p = r"D:/projects/samforce2003.github.io/docs/_seed_index.jsonl"
titles = []
for l in io.open(p, encoding='utf-8'):
    if l.strip():
        try: titles.append(json.loads(l).get('title',''))
        except Exception: pass
cands = ["拱桥","拱券","钢筋","脚手架","阻尼","共振","滤网","沙漏","发酵","酵母","老面","火候","陶轮","闸门","台阶","轴承","弹簧","隔震","防火墙","缓存","索引","哈希","配重","锚链","船锚","压舱水","吃水线","潮汐","堰","水闸","渡槽","虹吸","毛细","堤坝","筏","气囊","浮力","滑轮","杠杆","绞盘","棘轮","离合","差速器","万向节","减震器","刹车片","轮胎花纹","风挡","雨刷","后视镜","盲区","隧道","涵洞","栈桥","枕木","道岔","信号灯","站台","候车","换乘"]
print("total titles", len(titles))
out = []
for kw in cands:
    n = sum(1 for t in titles if kw in t)
    out.append((n, kw))
for n, kw in sorted(out):
    print(n, kw)
