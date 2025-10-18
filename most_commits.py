
fhandle = open("mbox.txt")

d = dict()

for line in fhandle:
    line = line.rstrip()
    if not line.startswith("From:") : continue
    address = line.split()[1]
    d[address] = d.get(address, 0 ) + 1
    
t = list()

for address, count in d.items():
    t.append((count, address))

t.sort(reverse=True)
print(t[0][1], t[0][0])