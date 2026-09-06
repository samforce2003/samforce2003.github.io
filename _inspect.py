import io
raw = io.open('seed.html', 'rb').read()
txt = raw.decode('utf-8')
i = txt.find('强灌线种子 R163 ·')
j = txt.rfind('<article>', 0, i)
print("=== ONE FULL R163 ARTICLE (repr) ===")
print(repr(txt[j:j+700]))
