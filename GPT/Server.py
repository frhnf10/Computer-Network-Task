import socket
import threading
import os

def handle_request(client_connection):
    try:
        request = client_connection.recv(1024).decode()
        print(f"Request: {request}")

        headers = request.split('\n')
        filename = headers[0].split()[1]

        if filename == '/':
            filename = '/index.html'

        try:
            file = open(os.getcwd() + filename, 'rb')
            response = b'HTTP/1.1 200 OK\n\n' + file.read()
            file.close()
        except FileNotFoundError:
            response = b'HTTP/1.1 404 NOT FOUND\n\nFile Not Found'

        client_connection.sendall(response)
    finally:
        client_connection.close()

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('0.0.0.0', 6789))
    server_socket.listen(5)
    print("Server running on port 6789")

    while True:
        client_connection, client_address = server_socket.accept()
        client_thread = threading.Thread(target=handle_request, args=(client_connection,))
        client_thread.start()

if __name__ == "__main__":
    start_server()
