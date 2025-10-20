import urllib.request, urllib.parse, urllib.error
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

i = input("Enter the url: ")
try:
    handle = urllib.request.urlopen(i, context=ctx)
except:
    print("Failed to open url")

char_count = 0
while True:
    info = handle.read(500)
    if len(info) < 1 or char_count >= 3000: break
    char_count += len(info)
    print(info)

print(char_count, "is the total amount of characters")
    