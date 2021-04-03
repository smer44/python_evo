import socket


# peer 1 - liste port 10, rites port 20

# peer 2 - liste port 20, rites port 10


HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server


array = ['2', '20', '300']

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


s.connect((HOST, PORT))


for value in array:
    s.sendall(value.encode())
    data = s.recv(1024).decode()
    value = int(data)
    print('received 1:' , value)    
    s.sendall(str(value).encode())
    data = s.recv(1024).decode()
    value = int(data)
    print('received 2:' , value)      
    


