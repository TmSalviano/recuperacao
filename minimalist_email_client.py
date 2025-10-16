
fhandle = open("mbox-short.txt")
t = list()

for line in fhandle:
    if not line.startswith("From") or len(line) < 2: continue
    t.append(line.split()[1])

for email in t:
    print(email)
    
print("There were %d lines in the file with From as the first word" % len(t))