import re
i = input("Enter a regular expression: ")

fhandle = open("mbox.txt")
count = 0
for line in fhandle:
    line = line.rstrip()
    f_all = re.findall(i, line)
    if len(f_all) > 0:
        count += 1

print("mbox.txt had %d lines that matched %s" % (count, i))