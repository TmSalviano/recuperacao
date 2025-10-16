
fhandle = open("romeo.txt")
words = list()

for line in fhandle:
    for word in line.split():
        if word in words: continue
        words.append(word)

sort_words = sorted(words)
print(sort_words)