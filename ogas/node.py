


class Node:
    
    
    def __init__(self, name, **kwargs):
        
        self.name = name 
        
        self.__dict__.update(kwargs)
        
        self.exclude = {'name', 'exclude', 'keys'}
        
        self.keys = list(self.__dict__.keys() - self.exclude  )
        
    
    def keys(self):
        return self.__dict__.keys() - self.exclude  
    
    def check(self):
        '''
        check - all values must be integer of float
        '''
        keys = self.keys
        
        for k in keys:
            v = self.__dict__[k]
            assert isinstance(v,(int,float))
            
            
    def __str__(self):
        return f"{self.keys}"
            

