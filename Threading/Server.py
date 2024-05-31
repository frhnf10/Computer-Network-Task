from socket import *
import threading

def handle_client(connectionSocket):
    try:
        message = connectionSocket.recv(1024)
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        # Send HTTP response headers
        connectionSocket.send('HTTP/1.1 200 OK\r\n\r\n'.encode())
        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.close()
    except IOError:
        # Send 404 Not Found response
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
        connectionSocket.send("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n".encode())
        connectionSocket.close()

def start_server():
    # Prepare a server socket
    servername = 'localhost'
    serverPort = 6777
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind((servername, serverPort))
    serverSocket.listen(5)
    print('The server is ready to receive')

    while True:
        # Establish the connection
        print('Waiting for connection...')
        # ke client

        connectionSocket, addr = serverSocket.accept()
        print('Connection received from', addr)
        # ke client

        # Create a new thread to handle the client
        client_thread = threading.Thread(target=handle_client, args=(connectionSocket,))
        client_thread.start()

    serverSocket.close()

if __name__ == "__main__":
    start_server()
