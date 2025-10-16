
fhandle = open("words.txt")
d = dict()

for line in fhandle:
    for word in line.split():
        for c in word:
            d[c] = d.get(c, 0) + 1


for k in sorted(d.keys()):
    if d[k] > 10:
        print(k, d[k])