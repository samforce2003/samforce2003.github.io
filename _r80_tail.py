import io, re
p = r"D:/projects/samforce2003.github.io/docs/_seed_full_blocks.html"
b = open(p,'rb').read()
print("bytes", len(b), "crlf", b.count(b'\r\n'), "lf", b.count(b'\n'), "crr", b.count(b'\r\r'))
t = b.decode('utf-8', 'replace')
parts = re.split(r'<article[^>]*>', t)
print("article tokens:", t.count('<article'), "blocks:", len(parts)-1)
print("=== tail 1800 chars ===")
print(t[-1800:])
p2 = r"D:/projects/samforce2003.github.io/docs/_seed_index.jsonl"
b2 = open(p2,'rb').read()
print("index crlf", b2.count(b'\r\n'), "lf", b2.count(b'\n'))
