import string
fhandle = open("romeo-full.txt")

d = dict()

for line in fhandle:
    line.rstrip()
    line = line.lower()
    for word in line.translate(line.maketrans('', '', string.punctuation)).split():
       d[word] = d.get(word, 0) + 1

print(d)