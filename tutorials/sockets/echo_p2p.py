'''
Created on 12.03.2021

@author: peter
# we need 2 threds here - 
- one listens and answers,
- another receives ?? 

https://stackoverflow.com/questions/23267305/python-sockets-peer-to-peer
Yes, two sockets are necessary. 
The listening socket should open on a constant port, 
and the client port should be opened on a different 
(potentially dynamic) port, usually higher in the
 port range. As an example:

Server sockets on port 1500, client sockets on port 1501.

Peer1: 192.168.1.101

Peer2: 192.168.1.102

When peer1 connects to peer2 it looks like this: 
192.168.1.101:1501 -> 192.168.1.102:1500.

When peer2 connects to peer1 it looks like this:
 192.168.1.102:1501 -> 192.168.1.101:1500.

Listening TCP sockets are also generally run on 
a separate thread since they are blocking.


here is good example 
https://github.com/AvinashAgarwal14/chatroom-p2p/blob/master/chat.py


alice must not get alice ...
'''
import socket
import threading
import time
import threading


class P2PBot:
    
    def __init__(self, name):
        self.HOST = '127.0.0.1'  
        self.PORT = 65432  
        self.name = name 
        
        #self.output_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #this is waiting, so it must be put in a thread too:
        #self.output_socket.connect((self.HOST, self.PORT))
        #print('after output_socket')
        #need to use same port, but with reuseaddr :
        #self.output_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        server_thread = threading.Thread(target=self.server_tread, args=())
        server_thread.start()
        
        client_thread = threading.Thread(target=self.client_thread, args=())
        client_thread.start()        
        
        #self.output_socket.sendall(name.encode())
        
        
    def client_thread(self):
        print(f'peer {self.name}: started client_thread')
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sout:
            sout.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            sout.connect((self.HOST, self.PORT))
            print(f'peer {self.name}: connected')
            sout.sendall(self.name.encode())
            print(f'peer {self.name}: msg sent')
        
    def server_tread(self):
        print(f'peer {self.name}: started server_tread')
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.bind((self.HOST, self.PORT))
            s.listen()
            conn, addr = s.accept()
            with conn:
                print(f'peer {self.name}: accepted:', addr)
                
                while True:
                    #try to get data:
                    data = conn.recv(1024)
                    while data:
                        print(f'peer {self.name} got:' , data)
                        
                        data = conn.recv(1024)
                    time.sleep(1)
            
alice = P2PBot('alice')
bob = P2PBot('bob')    

