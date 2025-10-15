
inp = input()

try:
    handle = open(inp)
    for line in handle:
        line = line.rstrip()
        print(line.upper())
except:
    print("Failed to open file: " + inp)