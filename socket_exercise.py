import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

headers_received = False
data_buffer = b""

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    
    # If we haven't found the end of headers yet, add to buffer and search
    if not headers_received:
        data_buffer += data
        # Look for the blank line that separates headers from content
        header_end = data_buffer.find(b"\r\n\r\n")
        if header_end != -1:
            # Found the end of headers, print everything after it
            headers_received = True
            content_start = header_end + 4  # Skip the \r\n\r\n
            if content_start < len(data_buffer):
                print(data_buffer[content_start:].decode(), end='')
    else:
        # Headers already processed, just print the data
        print(data.decode(), end='')

mysock.close()