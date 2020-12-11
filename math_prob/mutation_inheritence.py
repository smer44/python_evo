


import random as r

import matplotlib.pyplot as plt



def new_unit(unit_size, mutations_amount ):
    indexes = r.sample( range(unit_size), mutations_amount)
    
    unit = [ 0 for _ in range(unit_size)]
    
    for i in indexes:
        unit[i] = 1
    return unit 


    
    
# calculating the probability of 2 mutations to be the same :


def count_same_mutations(a, b):
    count = 0
    for x in range(len(a)):
        if a[x] and b[x]:
            count += 1
    return count




# compare the probability 

"""n = 10
p = 2

population = [new_unit(n,p) for _ in range(2000)]

all_places_count = 0
match_count = 0


for x in range(len(population)):
    for y in range(x+1,len(population)):
        all_places_count +=len(population[x])
        match_count+= count_same_mutations(population[x], population[y])
        

print("(p/n) ^2 " , (1.0 *p / n) **2)            
print("match_count/all_places_count" , 1.0 *match_count / all_places_count)
"""


            
        
    
    

        
        