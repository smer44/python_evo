import tkinter as tk
import tkinter.font as font
from tkinter import messagebox

import socket
import threading
import time

#p2p socket
#https://codereview.stackexchange.com/questions/64628/primitive-python-p2p-socket-chat

from tutorials.sockets.verticalscrollframe import VerticalScrolledFrame

class  MyChat(tk.Tk):
    
    
    def __init__(self):
        super().__init__() 
        self.title("MyChat")
        
        self.chat_frame = VerticalScrolledFrame(self)
        self.chat_frame.pack()

        tk.Label(self.chat_frame.interior, text = "              Start chatting! ").pack()
        
        self.enter_txt = tk.Text(height=5, width=30)
        self.enter_txt.pack() 
        
        tk.Button( text = 'Connect socken', command= self.connect_socket ).pack()
        
        
        #def func(event):
        #    print("You hit enter.")
        #key names
        #https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/key-names.html
        #and name for normal enter is <return>
        self.enter_txt.bind('<Return>', self.post_message)
        self.enter_txt.bind('<Shift-Return>', lambda event: None)
        self.socket = None
        recv_thread = threading.Thread(target=self.try_to_receive, args=())
        recv_thread.start()  
     
    def post_message(self,event):
        print(f'post_message: cursor position : ', self.enter_txt.index(tk.INSERT))
        msg =  self.enter_txt.get('1.0',tk.END).strip()
        self.enter_txt.delete('1.0', tk.END)
        #ser cursor to the begin:
        self.enter_txt.mark_set("insert", "1.0") 
        
        print(f'post_message: msg: {msg}')
        
        tk.Label(self.chat_frame.interior, text = msg).pack()
        
        if self.socket:
            self.socket.sendall(msg.encode())
            print(f'post_message: sent msg to server')


    def try_to_receive(self):
        while True:
            #print(f'try_to_receive: tick!')
            if self.socket:
                data = self.socket.recv(1024).decode()
                #print(f'try_to_receive: got data  from the server : {data}') 
                if data :
                    tk.Label(self.chat_frame.interior, text = '- Answer - :'  + data).pack()
                    
            time.sleep(1)
            
        
    def connect_socket(self):            
        self.port = 65432
        self.host = '127.0.0.1'
        
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.host, self.port))
        print(f'connect_socket: connected to {self.host}:{self.port}')
        
ch = MyChat()

ch.mainloop()    
        