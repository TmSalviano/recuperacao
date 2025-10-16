
fhandle = open("mbox-short.txt")
d = dict()

for line in fhandle:
    if not line.startswith("From:") : continue
    line = line.split()
    if len(line) < 2: continue
    d[line[1]] = d.get(line[1], 0) + 1


max = 0
person = ""
for k in d:
    if d[k] > max:
        max = d[k]
        person = k
    
print(person, max)
