from socket import *
servername = '172.17.48.1'
serverport = 6777
clientsocket = socket(AF_INET, SOCK_STREAM)
clientsocket.connect((servername,serverport))

#sentence = input('lowercase input: ')
#clientsocket.send(sentence.encode())

filename = 'C:/Users/asus/OneDrive - Telkom University/Documents/HTML/index.html'  # Example filename
#request = f"GET {filename} HTTP/1.1\r\nHost: {servername}\r\n\r\n"
clientsocket.send(filename.encode())

modifiedsentence = clientsocket.recv(1024)
print('From Server: ', modifiedsentence.decode())
clientsocket.close()

# masih membuat client dan server sederhana