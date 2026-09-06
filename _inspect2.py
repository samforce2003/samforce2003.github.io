import io
raw = io.open('seed.html', 'rb').read()
print('total bytes', len(raw))
print('CRLF count', raw.count(b'\r\n'))
print('CRCR (double CR) count', raw.count(b'\r\r'))
print('bare LF (LF not preceded by CR)', len(raw.split(b'\r\n')) - 1 if False else 'skip')
# find footer
fp = raw.find(b'</footer>')
print('</footer> pos', fp)
print('open footer tag pos', raw.find(b'<footer'))
# show bytes around footer
print('--- bytes around footer ---')
print(repr(raw[fp-400:fp+50]))
