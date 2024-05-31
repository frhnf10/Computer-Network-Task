from socket import *
servername = 'localhost'
serverport = 6777

clientsocket = socket(AF_INET, SOCK_STREAM)
clientsocket.connect((servername,serverport))
# ke server

filename = "/index.html"  # Example filename
request = f"GET {filename} HTTP/1.1\r\nHost: {servername}\r\n\r\n"
clientsocket.send(request.encode())
# ke server

modifiedsentence = clientsocket.recv(1024)
print('From Server: ', modifiedsentence.decode())
clientsocket.close()

# masih membuat client dan server sederhana