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

    Data = ConnectionSocket.recv(1024).decode()
    print('Client meminta perintah:', Data)

    if Data == 'HTTP':
        ServerResponse = 'GET HTTP OK'
        ConnectionSocket.send(ServerResponse.encode())
    else:
        ServerResponse = 'Error 404'
        ConnectionSocket.send(ServerResponse.encode())
    # pindah ke client
    ConnectionSocket.close()