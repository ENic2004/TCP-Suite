import socket
import scapy

import tcpclient

global target
global port
global server

def main():
    while True:
        o = input(">>> ")
        if o in ("tcp-client"):
            tcpclient.tcp_client(False)
main()