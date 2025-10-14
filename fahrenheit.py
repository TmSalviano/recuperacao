list = []

while True:
    number = input() 
    try:
        if number == "done":
            break
        list.append(int(number))
    except Exception as e:
        print(f"Not a number or {e}")
        continue

print(max(list))
print(min(list))