#!/usr/bin/env python3
#https://realpython.com/python-sockets/

import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)
#There’s no need to call s.close():
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    
    #bind() is used to associate the socket with a specific network interface and port number
    s.bind((HOST, PORT))
    
    #Continuing with the server example, listen() enables a server to accept() connections. It makes it a “listening” socket:
    #listen() has a backlog parameter. It specifies the number of unaccepted connections that the system will allow before refusing new connections.
    
    s.listen()
    #accept() blocks and waits for an incoming connection.
    conn, addr = s.accept()
    with conn:
        print('Server: Connected by:', addr)
        data = conn.recv(1024)
        while data:
            print(f'Server: send data back: \n {data}')  
            conn.sendall(data)
            data = conn.recv(1024)
        

            
            
            