import random as r

import matplotlib.pyplot as plt



population_size = 1000

bad_mutations_per_gen_amount = 1000

generations = 2000

population = [0 for _ in range(population_size) ]


for g in range(generations):
    for mut in range (bad_mutations_per_gen_amount):
        n = r.randint(0, population_size-1)
        population[n] +=1
        

#indexes = [n for n in range (population_size)]

histo = {}

for unit in population:
    if unit:
        histo[unit] =  histo.get(unit, 0) +1 



#indexes = [n for n in range (histo.values().length())]

"""x = population

x = histo.values()

plt.plot(x)

plt.show()"""