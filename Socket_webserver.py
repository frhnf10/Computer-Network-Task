#import socket module
from socket import *
serverSocket = socket(AF_INET, SOCK_STREAM)                         # Membuat Socket
#Prepare a server socket
webserver_port_number = 6777                                        # Membuat Nomor Port

serverSocket.bind(('127.0.0.1', webserver_port_number))                      # Mengaitkan Socket Dengan Nomor Port
serverSocket.listen(3)                                              # Siap Mendengarkan ketukan pintu dari client (Batas 3)

while True:
    #Establish the connection
    print ('Siap Menerima Ketukan....')
    connectionSocket, addr = serverSocket.accept()                  # Pintu Socket dibuka oleh serverSocket, masuk dengan socket baru-
                                                                    # namanya connectionsocket kiriman dari client, dan kemudian mereka-
                                                                    # dapat bertukar bit
    try:
        message = connectionSocket.recv(1024)
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        #Send one HTTP header line into socket
        connectionSocket.send('HTTP/1.1 200 OK \r\n\r\n'.encode())
        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.close()
    except IOError:
        #Send response message for the file not found
        connectionSocket.send("HTTP/1.1 200 OK  \r\n\r\n 404 Not Found".encode())
        #print('404 error: File not found')
    connectionSocket.close()
serverSocket.close()