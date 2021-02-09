

class Vali:
    
    def __init__(self):
        
        
        self.vali_str = {
            '*': lambda rule, value : len(rule)== 1,
            '+': lambda rule, value : len(rule)== 1 and value != None,            
            
            }
        
        self.vali_class = {
            str: lambda rule,value: self.vali_str[rule[0]](rule,value),
            
            tuple : lambda rule,value: self.vali_tuple[rule[0]](rule,value),
            
            }
        
        self.vali_tuple = {
            'and' : self.__vali_tuple_and__,
            'or' : self.__vali_tuple_or__,
            
            
            }
        
        
        
         
    
    def __call__(self,rule, value):
        return self.vali_class[type(rule)](rule,value)
        
    
    
    
    def __vali_tuple_and__(self, rule_tuple, value):
        
        for rule in rule_tuple[1:]:
            if not self(rule,value):
                return False 
        return True 
    
    def __vali_tuple_or__(self, rule_tuple, value):
        
        for rule in rule_tuple[1:]:
            if self(rule,value):
                return True 
        return False             

        

