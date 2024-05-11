from socket import *
servername = 'servername'
serverport = 6777
clientsocket = socket(AF_INET, SOCK_STREAM)
clientsocket.connect((servername,serverport))

sentence = input('lowercase input: ')
clientsocket.send(sentence.encode())
modifiedsentence = clientsocket.recv(1024)
print('From Server: ', modifiedsentence.decode())
clientsocket.close()

# masih membuat client dan server sederhana