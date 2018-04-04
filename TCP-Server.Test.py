import socket
import threading

ip = "0.0.0.0"
port = 1234

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((ip, port))
server.listen(5)

print("Startet server on ",ip, ":", port)

def handle_client(client_socket):
    req = client_socket.recv(4096)
    print("Received ", req)
    client_socket.send("ACK!!")
    client_socket.close()

while True:
    client_socket, addr = server.accept()
    print("Accepted connection from ", addr[0], addr[1])
    client_handler = threading.Thread(target=handle_client, args=(client_socket,))
    client_handler.start()