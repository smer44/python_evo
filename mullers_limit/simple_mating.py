import random as r
import matplotlib.pyplot as plt

def new_unit(unit_size, mutations_amount ):
    indexes = r.sample( range(unit_size), mutations_amount)    
    unit = [ 0 for _ in range(unit_size)]    
    for i in indexes:
        unit[i] = 1
    return unit 

def new_unit2(unit_size, mutations_amount ):
    unit = [0 for _ in range(unit_size-mutations_amount)] + [1 for _ in range(mutations_amount)]
    r.shuffle(unit)
    return unit 





def mate(unit1, unit2):
    child = [unit1[x] if r.random() < 0.5 else unit2[x] for x in range(len(unit1))]
    return child 

def distr_old(n, k1,k2, tryes):
    histo = {}
    for _ in range(tryes):
        a = new_unit(n,k1)
        b = new_unit(n,k2)
        c = mate(a,b)
        s = sum(c)
        histo[s] = histo.get(s,0) +1
    
    tuples = histo.items()
    tuples = sorted(tuples, key = lambda t: t[0])
    xx = [ t[0] for t in tuples]
    yy = [ t[1]/tryes for t in tuples]#divide to normalize it 
        
    return xx,yy 

def generate_children(n, k1,k2, population_size):
    pop = []
    for _ in range(population_size):
        a = new_unit(n,k1)
        b = new_unit(n,k2)
        c = mate(a,b)
        s = sum(c) # sum over array - get amount of mutations
        pop.append(s)
    return pop 
        
    
def distr(n, k1,k2, population_size):
    pop = generate_children(n, k1,k2, population_size)
    histo = to_histo(pop)
    xx,yy = histo_to_xy(histo, population_size)
    return xx,yy
    


def to_histo(arr, hmin= None, hmax = None):
    histo = {}
    if hmin and hmax:
        h = {x:0 for x in range(hmin,hmax+1)}       
     
    for x in arr: 
        histo[x] = histo.get(x,0) + 1
    return histo 

def histo_to_xy(histo, population_size):
    tuples = histo.items()
    tuples = sorted(tuples, key = lambda t: t[0])
    xx = [ t[0] for t in tuples]
    yy = [ t[1]/population_size for t in tuples]#divide to normalize it 
    return xx,yy
     
    
 
# amount of genes :       
n = 200#60


# amount of mutations in first parent:
x = 80

# amount of mutations in the second parent:
y = 120
        
    
popsize =  70000

#x,y = distr(95,90,40000)
#distr(1000,90,20000) is from 70 to 110
xx,yy = distr(n,x,y,popsize) #distr(100,90,40000)is from 82 to 97
#x,y = distr(10000,90,20000)from 70 to 110
#x,y = distr(93,90,20000) from 87 (0) to 90 (30%) to 93 (0)

#todo - 



plt.plot(xx,yy, color = "orange")

plt.show()
        


        
        
        

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


            
        
    
    

        
        