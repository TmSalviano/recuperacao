
import socket
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