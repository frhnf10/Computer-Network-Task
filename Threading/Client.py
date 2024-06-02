# Import modul soket
from socket import *

# Membuat variabel nama server dan nomor port tujuan
serverName = 'localhost'
serverPort = 4750

# Membangun soket jaringan, AF_INET menyatakan IP versi 4 dan SOCK_STREAM menyatakan jaringan TCP
clientSocket = socket(AF_INET, SOCK_STREAM)

# Melakukan komunikasi ke server
clientSocket.connect((serverName, serverPort))
# Menghubungkan ke server

fileName = input('Masukkan Request ke Server: ') #"/index.html" <-- Contoh file yang diminta
request = f'GET {fileName} HTTP/1.1\r\nHost: {serverName}\r\n\r\n'

# Mengirimkan request yang diinginkan client ke server
clientSocket.send(request.encode())
# Mengirimkan ke server

# Menerima respon dari client
response = clientSocket.recv(1024)
print('Respon server: ', response.decode())
clientSocket.close()

# buka browser dengan mengetikkan (localhost:4750/index.html) untuk melihat respon server