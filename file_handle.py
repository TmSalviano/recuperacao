inp = input()

count = 0

confidence_total = 0

try:
    handle = open(inp)
    print("File opened")

    for line in handle:
        if not line.startswith("X-DSPAM-Confidence:") : continue

        count += 1
        first_index = line.find(":")
        print(line[first_index + 2:])
        confidence_total += float(line[first_index + 2:].strip())
        print(confidence_total)
except:
    print("Failed to open file: " + inp)

average = (confidence_total / count)
print("Average confidence: ", average)