
first = "Tiago"
last = "Salviano"
number = 912345678

d = dict()

d[last, first] = number


for last, first in d:
    print(first, last, d[last,first])