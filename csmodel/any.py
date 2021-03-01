
class Any:
    
    def __init__(self,parent, cname, **kwargs):
        
        if parent:
            self.__set_all__(parent.__dict__)     
        
        # validate child fields over parent fields?
        
        self.__update_all__(kwargs)
        self.cname = cname
        self.exclude = {'cname', 'exclude','rules' , 'fs'}

        
        
    def __set_key__(self,key, value):
        if isinstance(value, list):
            self.__dict__[key] = value.copy()
            return 
        self.__dict__[key] = value
        
    def __update_key__(self,key, value):
        if isinstance(value, list):
            old = self.__dict__.get(key,None)
            if old:
                old.extend(value.clone())
                return 
            self.__dict__[key] = value.copy()
            return 
        self.__dict__[key] = value
        
    def check(self):
        for rule in self.rules:
            if not rule(self):
                return False 
        return True
        
    def fstr(self):
        return self.fs(self)    
            
        

    def __set_all__(self, d):
        for k,v in d.items():
            self.__set_key__(k, v)
            
    def __update_all__(self,d):
        for k,v in d.items():
            self.__update_key__(k, v)            
    
    def __repr__(self):
        ks = self.__dict__.keys() - self.exclude
        
        return self.__dict__.get("cname",'no_cname') + ' => {'+ ', '.join(str(k) + ' : ' + str(self.__dict__[k]) for k in ks)   +'}'     
        
        
    def __str__(self):
        return f'<{self.__dict__.get("cname",repr(self))}>' 

    
    def __call__(self, cname, **kwargs):
        return Any(self, cname, **kwargs)