# -*- coding: utf-8 -*-
import subprocess

a = subprocess.check_output(['git','show','HEAD~1:seed.html']).decode('utf-8').replace('\r\n','\n').replace('\r','\n')
b = open('seed.html','rb').read().decode('utf-8').replace('\r\n','\n').replace('\r','\n')

# find first and last difference positions
n = min(len(a), len(b))
first = None
for i in range(n):
    if a[i] != b[i]:
        first = i
        break
last = None
for i in range(1, n+1):
    if a[-i] != b[-i]:
        last = i
        break
print('first diff at', first)
print('last diff at (from end)', last)
print('len a', len(a), 'len b', len(b))
print()
print('=== A around first ===')
print(repr(a[first-100:first+1500]))
print()
print('=== B around first ===')
print(repr(b[first-100:first+1500]))
