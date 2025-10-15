handle = open("mbox.txt")


for line in handle:
    if line.startswith("From: "):
        print(line.strip("\n"))

handle.close()