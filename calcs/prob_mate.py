

import random as r 
import matplotlib.pyplot as plt
from math_prob.pop_utils import *



n = 1000


# amount of mutations:
x = 40

y = 30


def mate(arr1,arr2):
    return [ arr1[x] if r.random() < 0.5 else arr2[x] for x in range(len(arr1))]


def mate_test(n,x,y):
    unit1 = [0 for _ in range(n-x)] + [1 for _ in range(x)]
    r.shuffle(unit1)

    unit2 = [0 for _ in range(n-y)] + [1 for _ in range(y)]
    r.shuffle(unit2)
    
    m = mate(unit1,unit2)
    s = sum(m)
    return s 

def mate_sequence(n,x,y,times):
    histo = {}
    for _ in range(times):
        s = mate_test(n,x,y)
        histo[s] = histo.get(s, 0) +1 
    return histo 



h = mate_sequence(n,x,y,10000)

so = sorted(h.items())

xx = [k[0] for k in so]      

yy = [k[1] for k in so]  


plt.plot(xx,yy)

plt.show()
    
 # the same with pop_utils:   
        
times = 10000

histo = histo_session(times, mate_test, n,x,y,)
    
