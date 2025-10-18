import string

i = input()
try:
    fhandle = open(i)
except:
    print("Failed to open file: " + i)
    exit()

d = dict()

for line in fhandle:
    line = line.translate(line.maketrans("","", (string.digits + string.punctuation)))
    line = line.lower()
    line = line.split()
    for word in line:
        for char in word:
            d[char] = d.get(char, 0) + 1

l =  list()
for letter, count in d.items():
    l.append((count, letter))

l.sort(reverse=True)

for count, letter in l:
    print(letter, count)
