# Import modul soket & thread
from socket import *
import threading

def handle_client(connectionSocket):

    # Jika sendainya yang diminta ada maka:
    try:
        # Menerima permintaan dan mencari file yang diminta
        message = connectionSocket.recv(1024).decode()
        fileName = message.split()[1]
        f = open(fileName[1:])
        outputData = f.read()

        # Mengirimkan HTTP header ke client dengan message OK, yang mengisyarakatkan ada
        connectionSocket.send('HTTP/1.1 200 OK\r\n\r\n'.encode())

        # Dan mengirimkan konten file berdasarkan permintaan client
        connectionSocket.send(outputData.encode())
        connectionSocket.close()

    # Jika seandainya yang diminta tidak ada maka:
    except IOError:

        # Mengirmkan status tidak ada ke client
        connectionSocket.send('HTTP/1.1\r\n404 Not Found\r\n\r\n'.encode())
        connectionSocket.send('<html><body><h1>404 Not Found</h1></body></html>'.encode())
    connectionSocket.close()

def start_server():
    # Membuat variabel nama server dan nomor port
    serverName = 'localhost'
    port = 4750

    # Membangun soket jaringan, AF_INET menyatakan IP versi 4 dan SOCK_STREAM menyatakan jaringan TCP
    serverSocket = socket(AF_INET, SOCK_STREAM)

    # Melakukan bind nama server dengan nomor port
    serverSocket.bind((serverName, port))

    # Soket siap mendengarkan koneksi dari client batas 5
    serverSocket.listen(5)

    while True:
        print ('Menunggu koneksi client....')
        # Menunggu koneksi client

        # Server menerima koneksi dari client berdasarkan nama server dan nomor port
        connectionSocket, addr = serverSocket.accept()
        print('Koneksi diterima dari', addr)

        # Membuat thread untuk menghandle client
        client_thread = threading.Thread(target=handle_client, args=(connectionSocket,))
        client_thread.start()
        # Menunggu client
    serverSocket.close()

if __name__ == "__main__":
    start_server()