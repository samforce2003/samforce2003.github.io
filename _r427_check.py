# -*- coding: utf-8 -*-
import io
d = open('seed.html','rb').read()
crlf = d.count(b'\r\n')
lf = d.count(b'\n')
lone_lf = lf - crlf
print('CRLF:', crlf, '| lone LF:', lone_lf, '| total LF:', lf)
print('footer count:', d.count(b'</footer>'))
print('total bytes:', len(d))
marker = '<!-- 强灌线种子 R426 -->'.encode('utf-8')
print('R426 marker count:', d.count(marker))
i = d.rfind(marker)
print('last R426 marker idx:', i)
print(repr(d[i:i+40]))
