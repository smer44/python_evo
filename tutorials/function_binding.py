

class HasSomeFunction:
    
    
    def __init__(self):
        
        self.a = 5
        
    def pp(self):
        
        print (f"HasSomeFunction{{{self.a}}}") 
    
    
class HasNotSomeFunction:
    
    def __init__(self):
        self.a = 42 
        self.pp = lambda : HasSomeFunction.pp(self)
        
        
        
        
a = HasNotSomeFunction()

a.pp()

