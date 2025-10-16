fhandle = open("words.txt")
d = dict()

for line in fhandle:
    for word in line.split():
       d[word] = 0

print("daily" in d)