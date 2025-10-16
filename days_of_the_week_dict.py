
i  = input()
try:
    fhandle = open(i)
except:
    print("failed to open file: ", i)

d = dict()

for line in fhandle:
    if not line.startswith("From"): continue
    line = line.split()
    if len(line) < 3: continue
    d[line[2]] = d.get(line[2], 0) + 1

print(d)
