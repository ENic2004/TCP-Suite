import socket
import scapy

import tcpclient

global target
global port
global server

def main():
    while True:
        o = input(">>> ")
        if o in ("tcp-client-setup"):
            tcpclient.tcp_client_setup(False)
        if o in ("tcp-client-start"):
            tcpclient.tcp_client_setup(True)
main()