d = {'a':10, 'b':1, 'c':22}

al = list()
for key, value in d.items():
    al.append((value, key))

al.sort(reverse=True)
print(al)