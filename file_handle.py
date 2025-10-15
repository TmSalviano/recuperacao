inp = input("Write mbox file path: ")

try:
    handle = open(inp)
except:
    print(f"File not found or cannot be opened: {inp}")
    exit()

count = 0
for line in handle:
    line = line.rstrip()
    if line.startswith("Subject: "): count += 1

handle.close()

print(f"there were {count} subject lines in the file")