import socket
import scapy

import clients

global target
global port
global server

def main():
    while True:
        o = input("NTC >>> ")
        if o in ("help"):
            print("Usage:")
            print("tcp-client - opens the TCP-Client menu")
            print("exit - quits the programm")
            print("help - prints this message")
        elif o in ("tcp-client"):
            while True:
                o = input("TCP-CLIENT >>> ")
                if o in ("setup"):
                    clients.tcpclient_setup(False)
                elif o in ("start"):
                    clients.tcpclient_setup(True)
                elif o in ("back"):
                    main()
                else:
                    print("ERR | Unknown command, see help for more info.")
        else: 
            print ("ERR | Unknown command, see help for more info.")
        
print("Network Tool Collection, written by Elia Patzschke")
print("(C) Elia Patzschke 2018, all rights reserved")
print("Type 'help' or press enter for help")
main()