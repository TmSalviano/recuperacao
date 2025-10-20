
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
try:
    url = input("enter url: ")
    if len(url) < 1:
        print("non existant url")
        exit()
    domain_name = url.split("/")[2]
except:
    print("invalid url:", url)
    exit()

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((domain_name, 80))
cmd = f'GET {url} HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

count = 0
while True:
    data = mysock.recv(512)
    if len(data) < 1 or count > 3000:
        break
    count += len(data)
    print(data.decode(),end='')
mysock.close()
print("The total number of characters is:", count)

print(char_count, "is the total amount of characters")
    