from socket import *
IPv4 = 'localhost'
Port = 4750

ServerSocket = socket(AF_INET, SOCK_STREAM)
ServerSocket.bind((IPv4, Port))
ServerSocket.listen(1)

while True:
    print ('Menunggu koneksi client....')
    # pindah ke client

    ConnectionSocket, ClientAddress = ServerSocket.accept()
    print('Koneksi terhubung dari:', ClientAddress)
    #pindah ke client

    Data = ConnectionSocket.recv(4046).decode()

    if Data == 'HTTP':
        ServerResponse = 'HTTP/1.1 200 OK'
        ConnectionSocket.send(ServerResponse.encode())
    else:
        ServerResponse = "HTTP/1.1 200 OK\r\n404 Not Found"
        ConnectionSocket.send(ServerResponse.encode())
    # pindah ke client
    ConnectionSocket.close()