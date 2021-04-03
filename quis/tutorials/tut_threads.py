'''
Created on 20.03.2021

@author: peter
'''
import threading

a = 10
print(a)  
 
def tread_a():
    global a 
    a += 20 
    print('tread_a', a)    
    

def tread_b():
    global a 
    a += 30 
    print('tread_b', a)    
    
thread = threading.Thread(target=tread_a, args=())


thread2 = threading.Thread(target=tread_b, args=())
thread2.start()   
thread.start()  
