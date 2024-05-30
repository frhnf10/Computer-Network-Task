# Meng Import Library socket pada python
from socket import *
# membuat socket
serverSocket = socket(AF_INET, SOCK_STREAM) # AF_INET argumen menunjukkan menggunakan IPv4, dan Sock_stream menujukkan protokol TCP

webserver_name = "localhost"
webserver_port_number = 4750
serverSocket.bind((webserver_name, webserver_port_number)) # menghubungkan 
serverSocket.listen(3)

print ('Siap Menerima Ketukan....')
client_socket, client_address = serverSocket.accept()
print('Koneksi diterima dari:', client_address)

while True:
    data = client_socket.recv(4096).decode()
    print("Pesan dari client:",data)

    response = "Pesan diterima: " + data
    client_socket.send(response.encode())

    serverSocket.close()