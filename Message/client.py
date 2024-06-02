from socket import *
serverName = 'localhost'
serverPort = 4750

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
# Sending to server

message = input('Send some word: ')
clientSocket.send(message.encode())
# Sending to server

responseServer = clientSocket.recv(1024).decode()
print('Server reponse:', responseServer)

clientSocket.close()