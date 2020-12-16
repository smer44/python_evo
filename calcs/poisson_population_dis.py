import random as r
import matplotlib.pyplot as plt
import math


population_size =10 **4

xx = [ x for x in range(population_size)]

population = [ 0 for _ in range(population_size)]

mutations_per_unit = 80

# also, if 
histo = {}


def mutate(population, mutations_per_unit, histo):  
    population_size = len(population)
    total_mutations = population_size * mutations_per_unit
    histo.clear()
    for _ in range(total_mutations):
        # select random unit in population and give him a mutation:
        unit_index = r.randint(0,population_size-1) 
        population[unit_index] +=1
        
        
    #normalize , to get a distribution:
    for x in range(len(population)):
        unit = population[x]
        histo[unit] = histo.get(unit,0)+1
        
    histo = sorted(histo.items())
    xx = [(x[0]) for x in histo]
    yy = [(y[1]/population_size) for y in histo]
    return xx,yy
    
        
            
xx,yy= mutate(population, mutations_per_unit, histo)    
    
    
    
    
# sort result by mutation amount 
population = sorted(population)
#this must be poisson distributed: 


#print(xx, yy)
plt.plot(population)
plt.show()

# but it is not.

#calculate poisson distr of it :

def fact_int(n):
    x = n if n > 0 else 1
    for nn in range(n-1,1,-1):
        x *= nn 
    return x

# u = lambda = mutation rate, i  expected amount of mutations = x expected number of events

def poi(u, i):
    return math.exp(-u) * u**i / fact_int(i)
    

#print(fact_int(20))     


#check poisson variables :
#https://www.dummies.com/education/math/business-statistics/how-to-compute-poisson-probabilities/
#print(poi(2,4))   

xx2 = [i for i in range(int(mutations_per_unit*0.5), int( mutations_per_unit*1.5)) ]
poisson_pop= [poi(mutations_per_unit,i) for i in xx2 ]


plt.plot(xx2,poisson_pop, xx,yy)
plt.show()






