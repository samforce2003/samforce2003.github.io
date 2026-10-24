# -*- coding: utf-8 -*-
"""R658 观察位仪器：把「有几条正文」升级为「这几条现在读得到吗」。
深度B R800 的刀口：索引里有座位 ≠ 读者坐得下。本线自己的验收一直是「新增正文 N 条」（座位数），
从没量过「最新那条在第几个字节」。量四件：
 1) 三个自家页 HTTP 状态 + Content-Length
 2) 最新块在本地的字节偏移（seed-full.html 顶部 60 条预览区里 = 爬虫第一屏就够到）
 3) 最新条目是否在 seed.html 首屏（前 3 个 item）
 4) 本地/线上字节是否一致
"""
import io, os, re, json, urllib.request

BASE = r'D:/projects/samforce2003.github.io/docs'
SITE = 'https://samforce2003.github.io/'
HDR = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120 Safari/537.36'}
PROXY = 'http://127.0.0.1:17890'
NEWEST = '退相干离散台阶：索引里有座位，读者不一定坐得下'


def head(url, proxy=True):
    op = urllib.request.build_opener(
        urllib.request.ProxyHandler({'http': PROXY, 'https': PROXY}) if proxy
        else urllib.request.ProxyHandler({}))
    op.addheaders = list(HDR.items())
    try:
        r = op.open(url, timeout=25)
        body = r.read()
        return r.status, r.headers.get('Content-Length'), len(body)
    except Exception as e:
        return 'ERR:%s' % str(e)[:60], None, 0


def main():
    print('== 1. 载体可直读（本地直连 · 带浏览器 UA） ==')
    for page in ('seed.html', 'seed-full.html', 'seed-search.html', 'sitemap.xml'):
        st, cl, n = head(SITE + page)
        print('  %-18s HTTP %-28s CL=%-10s 读到 %d B' % (page, st, cl, n))

    print('== 2. 最新块在 seed-full.html 的字节偏移 ==')
    full = io.open(os.path.join(BASE, 'seed-full.html'), encoding='utf-8', errors='replace').read()
    tot = len(full.encode('utf-8'))
    pos = full.find(NEWEST)
    if pos >= 0:
        off = len(full[:pos].encode('utf-8'))
        print('  最新块标题偏移 %d B = 全文 %.1f%% 处（全文 %d B / %.2f MiB）'
              % (off, 100.0 * off / tot, tot, tot / 1048576.0))
        seg = full.rfind('<article', 0, pos)
        print('  所在 article 起始偏移 %d B' % len(full[:seg].encode('utf-8')))
    else:
        print('  !! 最新块标题不在 seed-full.html 里')

    print('== 3. 最新条目是否在活跃索引首屏 ==')
    idx = io.open(os.path.join(BASE, 'seed.html'), encoding='utf-8', errors='replace').read()
    items = re.findall(r'<div class="item">.*?</div></div>', idx, re.S)
    print('  seed.html 索引条目 %d 条 / %.0f KB' % (len(items), len(idx.encode('utf-8')) / 1024.0))
    for i, it in enumerate(items[:3], 1):
        t = re.search(r'<strong>(.*?)</strong>', it, re.S)
        h = re.search(r'href="([^"]+)"', it)
        print('   top%d %-46s -> %s' % (i, (t.group(1) if t else '')[:44], h.group(1) if h else ''))
    print('  最新块在 top3 内：%s' % ('Yes' if any(NEWEST[:16] in it for it in items[:3]) else 'NO'))

    print('== 4. sitemap 覆盖 ==')
    sm = io.open(os.path.join(BASE, 'sitemap.xml'), encoding='utf-8', errors='replace').read()
    locs = re.findall(r'<loc>(.*?)</loc>', sm)
    ko = [l for l in locs if 'structural-cognition-ko-' in l]
    import glob
    ko_files = glob.glob(os.path.join(BASE, 'structural-cognition-ko-*.html'))
    print('  sitemap %d urls | ko 条目 %d | 本地 ko 文件 %d' % (len(locs), len(ko), len(ko_files)))
    miss = [os.path.basename(f) for f in ko_files
            if not any(os.path.basename(f) in l for l in ko)]
    print('  ko 未入册：%d %s' % (len(miss), miss[:5]))

    print('== 5. 索引记录数 ==')
    recs = [json.loads(l) for l in io.open(os.path.join(BASE, '_seed_index.jsonl'), encoding='utf-8') if l.strip()]
    print('  _seed_index.jsonl %d 条 | 本轮 src=强灌线-R658 %d 条 | 深度B-R800 %d 条'
          % (len(recs), sum(1 for r in recs if r.get('src') == '强灌线-R658'),
             sum(1 for r in recs if r.get('src') == '深度B-R800')))


if __name__ == '__main__':
    main()
