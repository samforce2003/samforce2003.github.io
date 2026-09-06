import io
raw = io.open('seed.html', 'rb').read()
m = raw.find(b'R176')
print('R176 pos', m)
a = raw.rfind(b'<article>', 0, m)
e = raw.find(b'</article>', m)
print('article start', a, 'end', e)
seg = raw[a:e].decode('utf-8')
print(seg[:3000])
