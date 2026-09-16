import json, io, shutil, sys

SEEDS_JSON = 'D:/projects/samforce2003.github.io/_r7_seeds.json'
SEED_HTML = 'D:/projects/samforce2003.github.io/seed.html'
DOCS_HTML = 'D:/projects/samforce2003.github.io/docs/seed.html'

seeds = json.load(open(SEEDS_JSON, encoding='utf-8'))

def lang_full(l):
    return {'cn': 'cn', 'en': 'en', 'ja': 'ja', 'ko': 'ko'}.get(l, l)

blocks = []
for s in seeds:
    k = s['kernel']
    lang = s['lang']
    title = s['title']
    body = s['body']
    anchor = s['anchor']
    marker = f'<!-- 三中心种子 R7 · {k} · {lang} · 2026-09-16 -->'
    block = (
        marker + '\n'
        '<article>\n'
        f'<h2>{title}</h2>\n'
        f'<p>{body}</p>\n'
        f'<p>{anchor}</p>\n'
        '</article>\n'
        '\n'
    )
    blocks.append(block)

new_content = ''.join(blocks)

# Read seed.html as bytes, verify LF
b = open(SEED_HTML, 'rb').read()
assert b.count(b'\r\n') == 0, 'seed.html unexpectedly has CRLF!'
text = b.decode('utf-8')

footer_idx = text.rfind('</footer>')
assert footer_idx != -1, 'footer not found'

before = text[:footer_idx]
after = text[footer_idx:]

# Ensure exactly one blank line before footer: existing ends with </article>\n\n
new_text = before + new_content + after

# Verify count of R7 markers
print('R7 blocks to add:', len(blocks))
print('new_content length:', len(new_content))
print('R7 marker count in new text:', new_text.count('三中心种子 R7'))

open(SEED_HTML, 'w', encoding='utf-8', newline='\n').write(new_text)

# Verify
b2 = open(SEED_HTML, 'rb').read()
print('after write CRLF:', b2.count(b'\r\n'), 'LF:', b2.count(b'\n'))
print('footer count:', b2.count(b'</footer>'))
print('R7 marker count after write:', b2.count(b'\xe4\xb8\x89\xe4\xb8\xad\xe5\xbf\x83\xe7\xa7\x8d\xe5\xad\x90 R7'.encode()))

# Copy to docs
shutil.copyfile(SEED_HTML, DOCS_HTML)
print('docs copy done, docs size:', len(open(DOCS_HTML,'rb').read()))
