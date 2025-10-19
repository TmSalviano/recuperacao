import re

fhandle = open("mbox-short.txt")

for line in fhandle:
    line = line.rstrip()
    if re.search("From:", line):
        print(line)
