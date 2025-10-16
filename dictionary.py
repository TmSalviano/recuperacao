fhandle = open("words.txt")
d = dict()

for line in fhandle:
    for word in line.split():
        for c in word:
            if c not in d:
                d[c] = 0
            else:
                d[c] = d[c] + 1
                
print(d)
