import io
raw = io.open('seed.html', 'rb').read()
m = raw.find(b'R176')
a = raw.rfind(b'<article>', 0, m)
e = raw.find(b'</article>', m)
print('block bytes:')
print(repr(raw[a:e+len(b'</article>')]))
