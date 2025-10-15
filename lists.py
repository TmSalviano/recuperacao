
l = []

while True:
    num = input()
    if num == "done":
        print("Average: ", (sum(l) / len(l)))
        break 
    l.append(float(num))
