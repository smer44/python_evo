

#probability simulator 
# lets build simple binominal:


# ok done 

#2.there is 2 boxes with 6 white and 4 black  balls, second with 1 white and 9 black balls
#you take randomly 2 balls and put in second box 
# then you take one ball and put into first.
# the result is the abount  



#3. if you draw n dices with 1-6 summ, how summ is distributed?


#4. secretary - 

#5 - drinks 

#6- repeats ??

import random as r 
from yprob import histo_to_xy
import matplotlib.pyplot as plt
from itertools import accumulate

class MKSim:
    
    
    def __init__(self, **kwargs):
        
        self.__dict__.update(kwargs)
        #self.n = n 
        #self.p = p 
        self.run = self.run_repeats
        
    def run_dices(self):
        self.result = 0
        for _ in range(self.n):
            kn = r.randint(self.b1,self.b2)
            self.result += kn 
            
    
    def run_drinks(self):
        self.result = 0
        weights = [0.25,0.4,0.35]
        vals = [0,1,2]
        
        ks = r.choices(vals, weights, k = self.n)
        self.result = sum(ks)

    def run_repeats(self):
        self.result = 0
        known = set()
        while True:
            self.result +=1
            k = r.randint(1,self.n)
            if k in known:
                return             
            known.add(k)
            
            
            
                
        
        
        
    
    def run_secretary(self):
        letters= [x for x in range(self.n)] 
        self.result = 0
        r.shuffle(letters)
        #look for at least one letter in same place:
        for n,x in enumerate(letters):
            if n == x:
                self.result +=1
                #return
                 
            
    def run_boxes(self):
        box1 = [1]*6+[0]*4
        box2 = [1]*1+[0]*9
        
        #take 1 ball
        i1 = r.randint(0,9)
        ball1 = box1[i1]
        del box1[i1]
        box2.append(ball1)
        
        #take 2 ball
        i2= r.randint(0,8)
        ball2 = box1[i2]
        del box1[i2]  
        box2.append(ball2)
        
        #take ball back:
        i3 = r.randint(0,11)
        ball3 = box2[i3]
        del box2[i3] 
        box1.append(ball3)
        
        self.result = sum(box1)
        
              
        
            
    def reset(self):
        self.result = 0

    def run_binominal(self):
        self.reset()        
        for _ in range(self.n):
            if r.random() < self.p:
                self.result +=1 
            
    def runs(self,n):
        self.histo = {}
        #self.all_n = n
        for _ in range(n):
            self.run()
            x = self.result
            self.histo[x] = self.histo.get(x,0)+1
            
        xx,yy = histo_to_xy(self.histo , n)
        return xx,yy
    
            
        
        
            
            
ps = MKSim(n = 3, p = 0.4, b1=1, b2 = 6)

xx,yy = ps.runs(500000)

#yy = list(accumulate(yy))# for run with repeating number
#print(ps.result) 
        
plt.plot(xx,yy)
plt.show()
            
        
         