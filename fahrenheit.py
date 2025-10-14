
maximum = None
print(f"Max: ", maximum)

for itervar in [0, 3, 25, 23, 21, 42]:
    if maximum is None or itervar > maximum:
        maximum = itervar
        print(f"New Maximum: {maximum}")
print(f"Overall Maximum: {maximum}")
