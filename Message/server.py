from socket import *
host = 'localhost'
port = 4750

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((host, port))
serverSocket.listen(1)

while True:
    print ('Waiting client connection....')
    # Waiting Client

    connectionSocket, clientAddress = serverSocket.accept()
    print('Connection connect from:', clientAddress)
    # Waiting Client

    data = connectionSocket.recv(1024).decode()
    print('Client says: ', data)

    if data == 'index.html':
        serverResponse = 'HTTP/1.1 200 OK'
        connectionSocket.send(serverResponse.encode())
    else:
        serverResponse = 'HTTP/1.1 OK\r\n404 Not Found'
        connectionSocket.send(serverResponse.encode())
    # Sending to Client

    connectionSocket.close()
serverSocket.close()