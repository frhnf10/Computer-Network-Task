# Import modul soket
from socket import *

# Membuat variabel nama server dan nomor port
server = 'localhost'
port = 4750

# Membangun soket jaringan, AF_INET menyatakan IP versi 4 dan SOCK_STREAM menyatakan jaringan TCP
serverSocket = socket(AF_INET, SOCK_STREAM)

# Melakukan bind nama server dengan nomor port
serverSocket.bind((server, port))

# Soket siap mendengarkan koneksi dari client batas 3
serverSocket.listen(3)

while True:
    print ('Waiting client connection....')
    # Menunggu koneksi client

    # Server menerima koneksi dari client berdasarkan nama server dan nomor port
    connectionSocket, addr = serverSocket.accept()
    print('Connection connect from:',addr)
    # Menunggu client

    # Jika sendainya yang diminta ada maka:
    try:
        # Menerima permintaan dan mencari file yang diminta
        message = connectionSocket.recv(1024)
        fileName = message.split()[1]
        f = open(fileName[1:])
        outputData = f.read()

        # Mengirimkan HTTP header ke client dengan message OK, yang mengisyarakatkan ada
        connectionSocket.send('HTTP/1.1 200 OK\r\n\r\n'.encode())
         
        # Dan mengirimkan konten file html berdasarkan permintaan client
        connectionSocket.send(outputData.encode())
        connectionSocket.close()

    # Jika seandainya yang diminta tidak ada maka:
    except IOError:

        # Mengirmkan status tidak ada ke client
        connectionSocket.send('HTTP/1.1 OK\r\n404 Not Found\r\n\r\n'.encode())
        connectionSocket.send('<html><body><h1>404 Not Found</h1></body></html>'.encode())
    connectionSocket.close()
serverSocket.close()
