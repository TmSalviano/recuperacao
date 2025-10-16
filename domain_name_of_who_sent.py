fhandle = open("mbox-short.txt")

d = dict()

for line in fhandle:
    if not line.startswith("Author: ") : continue
    line = line.rstrip()
    line = line.split('@')
    d[line[1]] = d.get(line[1], 0) + 1 

print(d)