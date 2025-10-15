
a = "banana"
b = "banana"

if a is b:
    print("a and b point to the same object")

list1 = [1, 2, 3]
list2 = [1, 2, 3]

identical = list1

if list1 is list2:
    print("list1 and 2 point to the same object'")
else:
    print("list1 and 2 point to different objects")

if identical is list1:
    print("The identical list not only has the same value as list1, it is identical to list it's pointing to the same object which is aliasing in python")

list1[0] = 10
