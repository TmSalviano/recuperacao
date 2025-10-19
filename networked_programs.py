import socket

pr43_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
pr43_sock.connect(('data.pr4e.org', 80))
cmd = b'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'
pr43_sock.send(cmd)

while True:
    data = pr43_sock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end='')

pr43_sock.close()