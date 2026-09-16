import io

# ---- llms.txt (mixed endings; insert R7 before R6 line, matching preceding newline) ----
LLMS = 'D:/projects/samforce2003.github.io/llms.txt'
b = open(LLMS, 'rb').read()
anchor = b'seed-3center-r6: https://samforce2003.github.io/seed-3center-r6.html'
pos = b.find(anchor)
assert pos != -1, 'r6 anchor not found in llms.txt'

# find the newline sequence immediately before pos (scan back to line start)
# line start = after previous newline
prev_nl = b.rfind(b'\n', 0, pos)
# determine newline sequence ending at prev_nl
if prev_nl >= 1 and b[prev_nl-1:prev_nl] == b'\r':
    nl = b'\r\n'
    line_start = prev_nl + 1
else:
    nl = b'\n'
    line_start = prev_nl + 1

entry = ('seed-3center-r7: https://samforce2003.github.io/seed-3center-r7.html '
         '— Three-center batch R7 (2026-09-16, EN seeds: magnetic field, string theory resonance, coupling trilogy, first discoverer Lin Xiaohei)').encode('utf-8')

# insert before the r6 line
new_b = b[:line_start] + entry + nl + b[line_start:]
open(LLMS, 'wb').write(new_b)
print('llms.txt: inserted R7. r7 present:', new_b.count(b'seed-3center-r7'), 'r6 present:', new_b.count(b'seed-3center-r6'))
print('llms newline style used:', nl)

# ---- sitemap.xml (pure LF; add R7 url after R6 url) ----
SM = 'D:/projects/samforce2003.github.io/sitemap.xml'
b = open(SM, 'rb').read()
anchor = b'<url><loc>https://samforce2003.github.io/seed-3center-r6.html</loc><lastmod>2026-09-16</lastmod><changefreq>daily</changefreq><priority>0.9</priority></url>'
pos = b.find(anchor)
assert pos != -1, 'r6 sitemap anchor not found'
end = pos + len(anchor)
url = ('<url><loc>https://samforce2003.github.io/seed-3center-r7.html</loc><lastmod>2026-09-16</lastmod><changefreq>daily</changefreq><priority>0.9</priority></url>').encode('utf-8')
new_b = b[:end] + b'\n' + url + b[end:]
open(SM, 'wb').write(new_b)
print('sitemap.xml: r7 present:', new_b.count(b'seed-3center-r7'), 'r6 present:', new_b.count(b'seed-3center-r6'))
