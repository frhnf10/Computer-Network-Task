# Import modul soket
from socket import *

# Membuat variabel nama server dan nomor port tujuan
serverName = 'localhost'
serverPort = 4750

# Membangun soket jaringan, AF_INET menyatakan IP versi 4 dan SOCK_STREAM menyatakan jaringan TCP
clientSocket = socket(AF_INET, SOCK_STREAM)

# Melakukan komunikasi ke server
clientSocket.connect((serverName,serverPort))
# Menghubungkan ke server

# Memberikan input client untuk meminta ke server
fileName = input('Make request to server: ') #Example: /index.html
request = f'GET {fileName} HTTP/1.1\r\nHost: {serverName}\r\n\r\n'

# Mengirimkan request yang diinginkan client ke server
clientSocket.send(request.encode())
# Mengirimkan ke server

# Menerima respon dari server
response = clientSocket.recv(1024)
print('Server reponse: ', response.decode())
clientSocket.close()