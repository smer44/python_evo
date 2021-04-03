

import tkinter as tk

import tkinter.font as font
import socket
import time
import threading



class ChatDisplay(tk.Tk):
    
    
    def __init__(self, *args, **kwargs):
        
        self.HOST = '127.0.0.1' 
        self.PORT = 65432       
        
        super().__init__(*args, **kwargs)
        
        self.chatframe = tk.Frame(self)
        self.chatframe.pack()
        
        self.input = tk.Text(self, height=5, width=60)
        self.input.pack()
        
        self.input.bind('<Return>', self.post_message)
        self.input.bind('<Shift-Return>', lambda event: None)  
        self.got_msgs = []
      
        
        
    def init_as_server(self):
        self.title('SERVER ')
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(( self.HOST,  self.PORT))
        s.listen()
        print('Server:init_as_client: listen:' , s )
        self.s = s
        thread = threading.Thread(target=self.server_thread, args=())
        thread.start()       
         
        
        
    def server_thread(self):
        s = self.s
        print('Server:server_thread: s:' , s )
        conn, addr = s.accept()
        self.conn = conn
        with conn:
            print(f'Server:server_thread: accepted client:', addr)
            while True:
                #print(f'Server: trying to get data')  
                data = conn.recv(1024)
                if data:
                    got_msg = data.decode()
                    print('Server:got_msg' , got_msg)
                    self.got_msgs.append(got_msg)
                    #tk.Label(self.chatframe, text = '- Answer:- ' + got_msg).pack()
                #print(f'Server:server_thread: slept')
        print('Server:server_thread: end of tread')
        
    def init_as_client(self):
        self.title('CLIENT ')
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        s.connect(( self.HOST,  self.PORT))
        print('Client:init_as_client: connected:' , s )
        self.s = s
        #error was if i give here server_thread
        
        thread = threading.Thread(target=self.client_thread, args=())
        thread.start()  
        self.conn = s       
        
    def client_thread(self):
        s = self.s
        while True:
            #print(f'Client: self.last_msg:', self.last_msg)
            #print(f'Client: trying to get data')  
            data = s.recv(1024)
            if data:
                got_msg = data.decode()
                print('Client:got_msg' , got_msg)
                self.got_msgs.append(got_msg)
                #tk.Label(self.chatframe, text = '- Answer:- ' + got_msg).pack()   
        print('Cleint:client_thread: end of tread')      

        
    def  post_message(self, event):
        msg =  self.input.get('1.0',tk.END).strip()  
        #print('event:', event) 
        #print('msg:', msg)
        self.input.delete('1.0', tk.END)
        label = tk.Label(self.chatframe, text = msg).pack()   
        print('post_message : self.conn:' , self.conn)
        self.conn.sendall(msg.encode())
        #self.last_msg = msg
        
        #print('label:' , label)
        
    def  flush_msgs(self):

        for msg in self.got_msgs:
            tk.Label(self.chatframe, text = '- Answer:- ' + msg).pack()   
        self.got_msgs = []
        
    def upd(self):        
        self.flush_msgs()
        self.update()    
        
           

q = ChatDisplay() 

q.init_as_server()




time.sleep(1)

q2 = ChatDisplay() 
q2.init_as_client()


count = 0
while True:
    q.upd()
    q2.upd()
    time.sleep(0.1)
    print(f"while True: sleep: {count}")
    count+=1
    
    
    

#q.mainloop()      
#q2.mainloop()   
         