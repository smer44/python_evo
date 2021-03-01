def reducel(fn ,*args):      
        
    ret = args[0]
    for n in range(1, len(args)):
        ret = fn(ret,args[n])
    return ret 
    
def reducer( fn ,*args):
    ret = args[-1]
    for n in range(len(args)-2, -1,-1):
        ret = fn(args[n], ret)
    return ret     
    


class Eval:
    
    
    def __init__(self):
        
        self.ops = {'with':lambda a,b: self.ywith(a,b),
                      '-': lambda a,b: a-b,
                      'in': lambda a,b: self.yin(a,b),
                      '->' : lambda a,b :self.yfollows(a, b)
                      }
        self.to_log = True
        
    def __call__(self, *expr):

        result =  self.ops[expr[0]](*expr[1:])
        if(self.to_log):
            print('Eval : ', self.opstr(expr) , ' = ' , result)
        return result
    
    def opstr(self,expr):
        return (' ' +str(expr[0])+ ' ').join(str(x) for x in expr[1:])
        
    def ywith(self,a,b):
        if a == b: return a 
        
        if (a == bool or isinstance(a, bool)) and \
            (isinstance(b, bool) or b == bool):
                return bool
        
        if isinstance(a, set): 
            a = a.copy()
        else:
            a = {a}

        if isinstance(b, set):
            a.update(b) 
        else:
            a.add(b)
        return a

    
            
    
    def yin(self,a,b):
        if isinstance(a,type):
            return a == b   

        if isinstance(b,type):
            if isinstance(a,set):
                for x in a:
                    if not isinstance(x, b):
                        return False 
                return True
            
            if isinstance(a,bool):
                return b == bool
            
            return isinstance(a, b)
        #interval or set handling:
        if isinstance(b, set):
            if isinstance(a,set):
                return a.issubset(b)
            return a in b
        

        
        #default operation for non interval types:
        return a == b 
    
    def yfollows(self,a,b):
        '''returns a->b
        if a is a type, b must be the same type 
        if a is primitive value, not a or b is calculated 
        '''
        if a == bool :
            return b == bool
        
        assert isinstance(a, bool)
        
        if b == bool:
            return not a 
        
        assert isinstance(b, bool) 
        return not a or b 
        
        
        
    
    