import socket

global target
global port
global message
global x

def tcp_client(run):
    if run == False:
        target = input("Target Server >>> ")
        port = int(input("Target Port >>> "))
        message = input("Message to Server >>> ")
        x = int(input("How often >>> "))
        recv_first = bool(input("Receive first >>>"))

    elif run == True:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        if recv_first == True:
            client.recv(4096)
            client.connect((target, port))
        while x > 0:
            client.send(message)
            ans = client.recv(4096)
            print(ans)
            client.close()
            x = x - 1    

    
