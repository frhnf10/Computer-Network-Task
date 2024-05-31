from socket import *
ServerName = 'localhost'
ServerPort = 4750

ClientSocket = socket(AF_INET, SOCK_STREAM)
ClientSocket.connect((ServerName,ServerPort))
# pindah ke server

Message = input('Kirimkan permintaan: ')
#request = f"GET {Message} HTTP/1.1\r\nHost: {ServerName}\r\n\r\n"
ClientSocket.send(Message.encode())
#pindah ke server

ResponseServer = ClientSocket.recv(4046).decode()
print('Respon server:', ResponseServer)

ClientSocket.close()