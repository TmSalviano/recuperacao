
s = "This string will be decorated sorted and then undecorated"

l = list()

for word in s.split():
    l.append((len(word), word)) 

l.sort(reverse=True)

res = list(    print(word, length))
for length, word in l:
    res.append(word)

print(res)

