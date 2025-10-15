
l = ['a', 'b', 'c']
another_list = ['d', 'e', 'f']
another_list.extend(l)
another_list.sort()

b_item = another_list.pop(1)
print(another_list)
print("Here is the letter b: " + b_item)