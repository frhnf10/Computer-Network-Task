from socket import *
clientsocket = socket(AF_INET, SOCK_STREAM)

servername = 'localhost'
serverport = 4750
clientsocket.connect((servername,serverport))

message = "Halo, "
clientsocket.send(message.encode())

response = clientsocket.recv(1024).decode()
print('From Server: ', response)
clientsocket.close()

# masih membuat client dan server sederhana