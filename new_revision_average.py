import re

i = input("Enter a file: ")
try:
    fhandle = open(i)
except:
    print("Failed to open file %s" % i)

count = 0

t = list()

for line in fhandle:
    line = line.rstrip()
    l = re.findtll("^New Revision: ([0-9]+)", line)
    if len(l) > 0:
        for s in l:
            t.append(int(s))
        count += 1


print((sum(t) // count))