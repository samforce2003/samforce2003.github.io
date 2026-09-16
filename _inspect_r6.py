b = open('seed.html', 'rb').read()
idx = b.rfind(b'</footer>')
seg = b[idx-200:idx]
# show repr of first 300 bytes to see exact line endings
print(repr(seg[:300]))
print('---')
print('CRLF pairs:', seg.count(b'\r\n'))
print('bare CR:', seg.count(b'\r'))
print('bare LF:', seg.count(b'\n'))
