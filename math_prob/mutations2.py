

import random as r

import matplotlib.pyplot as plt

mutations_amount = [1,2,2,3]

thrashhold = 750


population_size = 1000

generations = 2000

population = [0 for _ in range(population_size) ]


for unit in range(population_size):
    m = r.choice(mutations_amount)
    population[unit] += m 
    



def mate(population):
    return [max(population[x], population[x+1]  )  for x in range(len(population) -1) ]
    

"""p2 = mate(population)
p2.sort()

#plt.plot(population)
plt.plot(p2)

plt.show() """   
    