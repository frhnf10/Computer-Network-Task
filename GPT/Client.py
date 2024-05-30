import socket
import sys

def http_client(server_ip, server_port, requested_file):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))
    request = f"GET {requested_file} HTTP/1.1\r\nHost: {server_ip}\r\n\r\n"
    client_socket.sendall(request.encode())

    response = client_socket.recv(4096).decode()
    print(response)

    client_socket.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python http_client.py <server_ip> <server_port> <requested_file>")
        sys.exit(1)

    server_ip = sys.argv[1]
    server_port = int(sys.argv[2])
    requested_file = sys.argv[3]

    http_client(server_ip, server_port, requested_file)
