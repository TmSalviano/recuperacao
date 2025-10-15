

handle = open("mbox.txt")
for line in handle:
    if not line.startswith("From ") : continue
    print(line.split()[2])