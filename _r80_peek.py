import io, re
t = io.open(r"D:/projects/samforce2003.github.io/docs/_seed_full_blocks.html", encoding='utf-8').read()
parts = re.split(r'<article[^>]*>', t)
for blk in parts[-8:-4]:
    print(blk[:1400])
    print("########")
