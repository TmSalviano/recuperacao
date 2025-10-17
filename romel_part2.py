import string

handle = open("romeo-full.txt")
d = dict()

for line in handle:
    line = line.translate(line.maketrans('','',string.punctuation))
    line = line.lower()
    line = line.split() 
    for word in line:
        d[word] = d.get(word, 0) + 1


res = list()
for word, count in d.items():
    res.append((count, word))

res.sort(reverse=True)

for count, word in res[:10]:
    print(word, count)