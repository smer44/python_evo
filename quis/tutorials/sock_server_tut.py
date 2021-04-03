import socket
import threading
import time


host = "localhost"

port = 65432

client_port = 65432
# socket.AF_INET = IPV4
#socket.SOCK_STREAM = TCP
#socket.SOCK_DGRAM = udp


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
cs.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


value = '2'.encode()

s.bind((host, port))

s.listen()
        
    

array = ['2', '20', '300']

def client_thread():
    global cs
    print('Client: before while True:')
    while True:
        try:
            cs.connect((host, client_port)) 
        except: 
            print('unable to connect')
            time.sleep(1)
    
    print('Client: send_data')
    for value in array:
        cs.sendall(value.encode())
        data = cs.recv(1024).decode()
        value = int(data)
        print('received 1:' , value)    
        cs.sendall(str(value).encode())
        data = cs.recv(1024).decode()
        value = int(data)
        print('received 2:' , value)      
        
    
client_thread = threading.Thread(target=client_thread, args=())
client_thread.start() 

print('after client_thread.start() ')
  
def handle_next_client():
    global thread_count
    global conn
    global addr
    
    print(f"Server: connection number {thread_count} {conn}" )        
    with conn:
        print('Server: Connected by:', addr)
        data = conn.recv(1024)
        print('Server: gained data' , data)
        while data:
            value = int(data.decode())
            print("value ",value )
            msg = str(value*value).encode()
            conn.sendall(msg)
            data = conn.recv(1024)
        
thread_count = 0

print('after def handle_next_client() ')

while True:    
    print(f"trying to accept {thread_count} " )  
    conn, addr = s.accept()
    print(f"accepted {thread_count} " )  
    thread_count +=1
    recv_thread = threading.Thread(target=handle_next_client, args=())
    recv_thread.start() 
        
print('after while True:  ')
        
        
        