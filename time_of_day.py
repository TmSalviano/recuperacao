
i = input()
try:
    fhandle = open(i)
except:
    print("Failed to open file: " + i)

d = dict()

for line in fhandle:
    if not line.startswith("From") or line.startswith("From:"): continue
    print(line)
    t = line.split()[-2]
    h_m_s = t.split(":")
    h = h_m_s[0]
    d[h] = d.get(h, 0) + 1

l = sorted(d.items())
for hour, count in l:
    print(hour, count)
