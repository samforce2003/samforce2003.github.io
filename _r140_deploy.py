import io, os, sys

BASE = r'D:/projects/samforce2003.github.io'
files = ['_r140_cn.txt', '_r140_jp.txt', '_r140_kr.txt']
blocks = []
for f in files:
    p = os.path.join(BASE, f)
    t = io.open(p, encoding='utf-8').read()
    t = t.replace('\r\n', '\n').replace('\r', '\n')
    if not t.endswith('\n'):
        t += '\n'
    blocks.append(t)
blob = ''.join(blocks)
assert blob.count('</article>') == 3, blob.count('</article>')
assert blob.count('<article>') == 3
assert 'r140-1' in blob and 'r140-2' in blob and 'r140-3' in blob

for rel in ['seed.html', 'docs/seed.html']:
    p = os.path.join(BASE, rel)
    b = io.open(p, 'rb').read()
    txt = b.decode('utf-8')
    assert txt.count('</footer>') == 1, ('footer', txt.count('</footer>'))
    assert 'r140-1' not in txt, 'r140 already present in ' + rel
    idx = txt.rfind('</footer>')
    new = txt[:idx] + blob + txt[idx:]
    output = new.encode('utf-8')
    io.open(p, 'wb').write(output)
    chk = io.open(p, 'rb').read()
    print(rel, 'size', len(chk),
          'crlf', chk.count(b'\r\n'),
          'bareLF', chk.count(b'\n') - chk.count(b'\r\n'),
          'bareCR', chk.count(b'\r') - chk.count(b'\r\n'),
          'footer', chk.count(b'</footer>'),
          'r140-1', chk.count(b'r140-1'),
          'r140-2', chk.count(b'r140-2'),
          'r140-3', chk.count(b'r140-3'),
          'doi', chk.count(b'21994268'))

# byte-identical check
a = io.open(os.path.join(BASE, 'seed.html'), 'rb').read()
c = io.open(os.path.join(BASE, 'docs/seed.html'), 'rb').read()
print('IDENTICAL' if a == c else 'DIFFER')
