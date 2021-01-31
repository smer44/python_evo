
# dummy game ist just a game where unit moves left or right in 1 d line 
import random as r

class DummyGC:
    
    def __init__(self, size, step = 1):
        self.size = size
        self.step = step
        self.initial_fitness = 0
        self.fitness_step =1
        
        
    
    def reset(self):
        self.position = int(r.random()*self.size)
        self.fitness = self.initial_fitness
        self.run = True 
        
    def move(self, dir):
        self.position +=  [-1,1][dir] * self.step        
        self.run =  self.check()
        return self.run 
        
        
    def move_left(self):
        self.move(0)
        
    def move_right(self):
        self.move(1)    
        
        
        
    def check(self):
        return self.position > 0 and self.position < self.size  
    
    def __str__(self):
        sarr = ['-']*self.size
        if self.run:
            sarr[self.position] =  'X' 
        return ''.join(sarr)
    
    def to_nn(self):
        sarr = [0]*self.size
        sarr[self.position] = 1
        return sarr 
        
        
        
gc = DummyGC(10)
gc.reset()

gc.position = 0

print(gc) 

print(gc.to_nn()) 

gc.move_left()

#print(gc.position)
#print(gc.check())

print(gc) 

gc.reset()

gc.position = 9


print(gc) 
gc.move_right()
print(gc) 


        
        
        
         