import random as r
import pprint as pp


class SnakeMLController:
    
    def __init__(self, pop_size, *layer_dimms):
        
        self.pop_size = pop_size 
        self.nns = [self.create_random_nn(*layer_dimms)  for _ in range(pop_size)]
        
        
        
    def create_random_nn(self,*layer_dimms):
        
        return [[r.gauss(0.5, 0.1) for _ in range(n) ] for n in layer_dimms]
    
    

sc = SnakeMLController(2, 3,4)

pp.pprint(sc.nns)
        