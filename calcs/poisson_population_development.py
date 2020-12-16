import random as r
import matplotlib.pyplot as plt
import math


population_size =10 **3

indexes = [ x for x in range(population_size)]

population = [ 0 for _ in range(population_size)]

generations = 20

mutations_per_unit = 80

kill_rate = 0.01

def mutate(population, population_size, total_mutations):  
    
    #print(len(population))
    for _ in range(total_mutations):
        # select random unit in population and give him a mutation:
        unit_index = r.randint(0,population_size-1) 
        population[unit_index] +=1
       
    #histo = sorted(histo.items())
    #xx = [(x[0]) for x in histo]
    #yy = [(y[1]/population_size) for y in histo]
    count = sum(population)
    return count


def  gen_run(population, mutations_per_unit, generations, kill_rate):
    
    population_size = len(population)
    total_mutations_per_generations = population_size * mutations_per_unit
    survival_rate = int(population_size*kill_rate) 
    print("survival_rate : " , survival_rate)
    
    d = [] # distribution of summ of all mutations over generations 
    generation_indexes = [x for x in range(generations)]
    for gen in generation_indexes:
        count = mutate(population, population_size, total_mutations_per_generations)
        d.append(count)
        # sort result by mutation amount 
        population = sorted(population)
        #kill those with higher mutation amount:
        population = population[: survival_rate ]
        #repopulate:
        # take 2 random units from survivers and mate:
        next_gen = [(r.choice(population) + r.choice(population))/2 for _ in  range(population_size)]
        population = next_gen

        
        
        
        
   
    return generation_indexes, d 




#degeneration scenario

xx, yy= gen_run(population, mutations_per_unit, generations, kill_rate)

plt.plot(xx, yy)
plt.show()
        
    
     
    
    


