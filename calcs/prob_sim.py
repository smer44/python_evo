import random
import matplotlib.pyplot as plt


n = 10
k = int(n * 0.5)

nmk = n-k 

#print(nmk)

pop = [0 for _ in range(nmk)] + [1 for _ in range(k)]

random.shuffle(pop)

#print(pop)


p = 0.5

def step(pop, p):
    for n in range(len(pop)):
        if (random.random() < p):
            pop[n] ^= 1 


#step(pop,p)

#print(pop)


def measure_count(n,k,p):
    nmk = n-k 
    pop = [0 for _ in range(nmk)] + [1 for _ in range(k)]
    #random.shuffle(pop)
    step(pop,p)
    s = sum(pop)
    return s 

def measure_distribution(n,k,p, times):
    d = {}    
    for _ in range(times):
        result = measure_count(n,k,p)
        d[result]=  d.get(result, 0)+1
    return d


    
d = measure_distribution(2000,1200,0.4,20000)

sorted = sorted(d.items())
print(sorted)

plt.plot([x[0] for x in sorted] , [x[1] for x in sorted ] )

plt.show()

    
    
    
    


        