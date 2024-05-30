from socket import *
ServerName = 'localhost'
ServerPort = 4750

ClientSocket = socket(AF_INET, SOCK_STREAM)
ClientSocket.connect((ServerName,ServerPort))
# pindah ke server

Message = input('Kirimkan permintaan: ')
ClientSocket.send(Message.encode())
#pindah ke server

ResponseServer = ClientSocket.recv(1024).decode()
print('Respon server:', ResponseServer)

ClientSocket.close()