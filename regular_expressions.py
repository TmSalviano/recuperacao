import re

fhandle = open("mbox-short.txt")
for line in fhandle:
    line = line.rstrip()
    f_all = re.findall("^From .+ ([0-9][0-9]):", line)
    if len(f_all) > 0:
        print(f_all)
    