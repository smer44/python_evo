from math_prob.pop_utils import *

import matplotlib.pyplot as plt

from math_prob.ycombi import *


pop = new_arr01(400,600)

print(pop)


sam = r.sample(pop,100)

s = sum(sam)

print(s)

def step():
    pop = new_arr01(400,600)
    sam = r.sample(pop,100)
    s = sum(sam)
    return s

hi = histo_session(30000, step)

x,y = histo_to_plot(hi)


#n = 100
#p = 60.0/100


#x2 = [i for i in range(40,75)]
#y2 = [binn(n,k,p) for k in x]
    
plt.plot(x,y)
#plt.plot(x2,y2)

plt.show()    