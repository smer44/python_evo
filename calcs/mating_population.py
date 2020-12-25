import random as r 
import matplotlib.pyplot as plt
import math
import pprint as pp

unit_size = 1000


unit_indexes = [x for x in range(unit_size)] # 0,1,2,3...


mutations_per_unit = 50

population_size = 1000# 2000




def new_random_unit(unit_size, unit_indexes, mutations_per_unit):
    unit = [0 for _ in range(unit_size)]
    chosen_indexes = r.sample(unit_indexes, mutations_per_unit )
    for index in chosen_indexes:
        unit[index] = 1
    return unit 


#tt = new_random_unit(unit_size, unit_indexes, mutations_per_unit)

#+1: show one random unit 
#

#print(tt)


population = [new_random_unit(unit_size, unit_indexes, mutations_per_unit) for _ in range(population_size) ]


#show this population mutation counts per unit: 

#mut_counts = [ sum(unit) for unit in population]
#plt.plot(mut_counts)
#plt.title('initial population ' )
#plt.show()

def histo(population, hmin,hmax):
    population_size = len(population)
    h = {x:0 for x in range(hmin,hmax+1)}
    for unit in population:
        s = sum(unit)#count mutations
        #increase histogram place:  
        h[s] = h.get(s,0)+1
        
    h = sorted(h.items())
    xx = [(x[0]) for x in h]
    #divide by population size - to normalize to get the distribution from 0 to 1 
    yy = [(y[1]/population_size) for y in h]
    return xx,yy


#+2: for a test, lets make a distribution of initial population:
#xx,yy = histo(population,49,51)
#print(xx)
#plt.plot(xx,yy)
#plt.show()

def mate(unit1, unit2):
    child = [unit1[x] if r.random() < 0.5 else unit2[x] for x in range(len(unit1))  ]
    return child 
                                                                       
                                                                       



#+3: small mating test:
#unit1 = [0,1,0]
#unit2 = ["a","b","c"]
#print(mate(unit1,unit2))
#print(mate(unit1,unit2))



def mate_all(population, children_per_pair):
    children = []
    r.shuffle(population)
    for x in range(0,len(population),2):
        unit1, unit2 = population[x] , population[x+1]
        
        for _ in range(children_per_pair):
            child  = mate(unit1, unit2) 
            children.append(child)
    
    return children

#TEst 4: let us mate the initial population one time:
children = mate_all(population,2)

#sort by count of mutations
children = sorted(children , key = lambda unit : sum(unit))
#pp.pprint([sum(unit) for unit in children])

#plt.plot( [sum(unit) for unit in children])
#plt.show()


def kill_worst(children, percentage):
    assert percentage <=1
    # sort children by sum of mutations of each unit:
    children = sorted(children , key = lambda unit : sum(unit))
    #pp.pprint(children)
    children = children[0:int(len(children)*percentage)]
    return children 


#TEst 5: kill worst percentage of population and show it:
children = kill_worst(children, 0.5)
#pp.pprint([sum(unit) for unit in children])

#plt.plot( [sum(unit) for unit in children])
#plt.show()

    
#Test 6: repopulate the population, compencating 50% lost, means each pair have 4 children:

"""children2 = mate_all(children,4)
children2 = sorted(children2 , key = lambda unit : sum(unit))

plt.plot( [sum(unit) for unit in children2])
plt.show()
"""
 

# Test 7: let us simulate more generations like that :

def run_genx2(population, generations):
    # repopulate 2x size:
    for n in range(generations):
        
        children = mate_all(population,4)
        children = kill_worst(children, 0.5)
        population  = children 
        print("run_genx2 : step " , n)
        plt.plot( [sum(unit) for unit in children])
        plt.show()    
    return population
        


"""children2 = run_genx2(children,10)        
plt.plot( [sum(unit) for unit in children2])
plt.show()    
"""
    
    
    
# Test 7: let us simulate more generations while adding mutations:

mutations_per_gen_per_unit = 3

mutations_per_gen = mutations_per_gen_per_unit * population_size
print("mutations_per_gen : " , mutations_per_gen)

def add_mutations(population, mutations_per_gen):
    for _ in range(mutations_per_gen):
        unit = r.choice(population)
        position = r.randint(0,len(unit)-1)
        unit[position] += 1
    #print("count : " , count)
        
        
# create new population:
"""population = [new_random_unit(unit_size, unit_indexes, mutations_per_unit) for _ in range(population_size) ]
add_mutations(population, mutations_per_gen)
plt.plot( sorted([sum(unit) for unit in population]))
plt.show()  """

def add_mutationsv2(population, mutations_per_unit):
    for unit in population:
        indexes = r.sample(unit_indexes, mutations_per_unit )
        for index in indexes:
            unit[index] += 1 
                
            





# Test 8: the main text - simulation over multiple generations with mutations added :

 
def run_gen_mutx2(population, generations, mutations_per_gen):
    #print("run_gen_mutx2 : initial population " )
    plt.plot( [sum(unit) for unit in population])
    plt.title('initial population ' )
    plt.show()      
    p = 0.25
    pstr = str(int(p*100)) + ' % '
    old_average = 0
    # repopulate 2x size:
    for n in range(generations):
        print("run_gen_mutx2 : step " , n)
        
        
        
        
        #add_mutations(population, mutations_per_gen)
        add_mutationsv2(population, 10)
        print("run_gen_mutx2 : added mutations " , mutations_per_gen)
        sum_average = sum([sum(unit) for unit in population]) / len(population)
        print("run_gen_mutx2 : step " , n , "average mutations : " , sum_average , "difference from previous average : " , sum_average - old_average)
        old_average = sum_average
        
        plt.plot( sorted([sum(unit) for unit in population]))
        plt.title('added mutations # '+str( n)  )
        plt.show()         
        children = mate_all(population,8)
        print("run_genx2 : mated to be 2x size ")
        plt.plot( sorted([sum(unit) for unit in children]))
        plt.title('children mated 2x size # '+str( n)  )
        plt.show()       
        
        children = kill_worst(children, p)
        population  = children
        plt.plot( [sum(unit) for unit in children])
        plt.title('best ' + pstr + ' survived # '+str( n)  )
        plt.show()    
    return population
            

run_gen_mutx2(population, 20,4*population_size)

# on 10 mutations per unit, 25% survivers, it gets stabilized


        
        