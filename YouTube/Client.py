# Meng Import Library socket pada python
from socket import *
# Membuat Objek Soket
client_socket = socket(AF_INET, SOCK_STREAM) # AF_INET argumen menunjukkan menggunakan IPv4, dan Sock_stream menujukkan protokol TCP

# Menghubungkan Ke Server
servername = "localhost"
serverport = 4750
client_socket.connect((servername,serverport)) # melakukan connect sebuah target servern dan nomor portnya

# Mengirimkan request ke server berupa data byte
client_socket.send(b"GET / HTTP/1.1\r\nHost: localhost\r\n\r\n")

# Menerima balasan dari server
respons = client_socket.recv(4096)
# agar bisa dibaca dengan menggunakan decode
print("Balasan Dari Server:",respons.decode())

# Menutup koneksi dengan server
client_socket.close()