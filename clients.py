import socket

def tcpclient_setup(run):
    try:
        ip = input("TCP-CLIENT | IP >>> ")
        port = int(input("TCP-CLIENT | PORT >>> "))
        ans = input("TCP-CLIENT | Answer to Server >>> ")
        recv_first = eval(input("TCP-CLIENT | Receive first >>> "))
        if run in True:
            tcpclient(ip, port, ans, recv_first)
    except TypeError:
        print("ERR | TypeError, see help for more info.")

def tcpclient(ip, port, ans, recv_first):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((ip, port))
    if recv_first == True:
        req = client.recv(4096)
        print("TCP-CLIENT | Received ", req)

    client.send(ans)
    print("CLIENT | Sent answer!")
    req = client.recv(4096)
    print(req)
    x = x - 1
