import random as r 
import matplotlib.pyplot as plt
import math
import pprint as pp

unit_size = 1000


unit_indexes = [x for x in range(unit_size)] # 0,1,2,3...


mutations_per_unit = 50

population_size = 2000# 2000




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


population = [new_random_unit(unit_size, unit_indexes, mutations_per_unit + x % 5) for x in range(population_size) ]


#show this population mutation counts per unit: 

mut_counts = sorted([ sum(unit) for unit in population])
plt.plot(mut_counts)
plt.ylim(0,100)
avg = sum(mut_counts) / len(mut_counts)
plt.title('Simulation 1. this shows population initial mutations per organism\n with ' + str(avg) + " in average" )
plt.show()

def histo(mut_counts, hmin= None ,hmax = None ):
    population_size = len(population)
    
    h = {} 
    if hmin and hmax:
        h = {x:0 for x in range(hmin,hmax+1)}
    for s in mut_counts:
        #increase histogram place:  
        h[s] = h.get(s,0)+1
        
    h = sorted(h.items())
    xx = [(x[0]) for x in h]
    #divide by population size - to normalize to get the distribution from 0 to 1 
    yy = [(y[1]/population_size) for y in h]
    return xx,yy


#+2: for a test, lets make a distribution of initial population:
xx,yy = histo(mut_counts,48,57)
print(xx)
plt.plot(xx,yy)
plt.title('Simulation 1. this shows the histogram over population,\n what is the probability distribution  ' )
plt.show()

def mate(unit1, unit2):
    child = [unit1[x] if r.random() < 0.5 else unit2[x] for x in range(len(unit1))  ]
    return child 
                                                                       
                                                                       



#+3: small mating test:
unit1 = [0,1,0]
unit2 = ["a","b","c"]
print("Small mating test")

print("parent " , unit1) 
print("parent " , unit2) 

print("child  ", mate(unit1,unit2))
print("child  ", mate(unit1,unit2))



def mate_all(population, children_per_pair):
    children = []
    r.shuffle(population)
    for x in range(0,len(population),2):
        unit1, unit2 = population[x] , population[x+1]
        
        for _ in range(children_per_pair):
            child  = mate(unit1, unit2) 
            children.append(child)
    
    return children

# 4: let us mate the initial population one time:
children = mate_all(population,2)

#sort by count of mutations
children = sorted(children , key = lambda unit : sum(unit))
pp.pprint([sum(unit) for unit in children])
plt.ylim(0,100)


mut_counts = sorted([ sum(unit) for unit in children])
avg = sum(mut_counts) / len(mut_counts)
plt.title( "Simulation 1. Next Population after mating one time, with "+ str(avg) + " in average" )
plt.plot( mut_counts)
plt.show()

xx,yy = histo(mut_counts)
print(xx)
plt.plot(xx,yy)
plt.title('Simulation 1. the probability distribution for next generation  ' )
plt.show()




def kill_worst(children, percentage):
    assert percentage <=1
    # sort children by sum of mutations of each unit:
    children = sorted(children , key = lambda unit : sum(unit))
    #pp.pprint(children)
    children = children[0:int(len(children)*percentage)]
    return children 


#:5. kill worst percentage of population and show it:
children = kill_worst(children, 0.5)
#pp.pprint([sum(unit) for unit in children])
plt.ylim(0,100)
mut_counts = sorted([ sum(unit) for unit in children])
avg = sum(mut_counts) / len(mut_counts)

plt.title( "Simulation 2. Killed the worst half of the population\n now the average is " + str(avg))
plt.plot(mut_counts)
plt.show()

    
# 6: repopulate the population, compencating 50% lost, means each pair have 4 children:

repop_rate = 4

children2 = mate_all(children,repop_rate)
children2 = sorted(children2 , key = lambda unit : sum(unit))


mut_counts = sorted([ sum(unit) for unit in children2])
avg = sum(mut_counts) / len(mut_counts)

plt.title( "Simulation 2. Repopulate, while each par has " + str(repop_rate) + " children\n the averate is "\
            + str(avg) + "\n so this is one factor what decreaces mutations")
plt.ylim(0,100)
plt.plot( mut_counts)
plt.show()

 

# Test 7: let us simulate more generations like that :

def run_genx2(population, generations):
    # repopulate 2x size:
    for n in range(generations):
        
        children = mate_all(population,4)
        children = kill_worst(children, 0.5)
        population  = children 
        #print("run_genx2 : step " , n)
        mut_counts = sorted([ sum(unit) for unit in population])
        avg = sum(mut_counts) / len(mut_counts)
        
        plt.title( "Simulation 3. Lets run some more generation. \n Step " + str(n) + " with average " + str(avg))
        plt.ylim(0,100)
        
        plt.plot(mut_counts)
        plt.show()    
    return population
        


children2 = run_genx2(children,10)      
    
    
    
# Test 8: let us add mutations:

mutations_per_gen_per_unit = 3

mutations_per_gen = mutations_per_gen_per_unit * population_size
#print("mutations_per_gen : " , mutations_per_gen)

#adding mutations_per_gen mutations to all generation to random units
def add_mutations(population, mutations_per_gen):
    for _ in range(mutations_per_gen):
        unit = r.choice(population)
        position = r.randint(0,len(unit)-1)
        unit[position] = 1
    #print("count : " , count)
        
        
# create new population:
population = [new_random_unit(unit_size, unit_indexes, mutations_per_unit) for _ in range(population_size) ]
add_mutations(population, mutations_per_gen)
plt.ylim(50,100)
mut_counts = sorted([ sum(unit) for unit in population])
avg = sum(mut_counts) / len(mut_counts)

plt.title( "Simulation 4. Lets put all together and add mutations to initial population\n this must be 50 + poisson-distrubuted \n now the average " + str(avg)) 
plt.plot( mut_counts)
plt.show()


#adding  mutations_per_unit mutations to each unit in population
def add_mutationsv2(population, mutations_per_unit):
    for unit in population:
        indexes = r.sample(unit_indexes, mutations_per_unit )
        for index in indexes:
            unit[index] = 1 
                
            





# Test 8: the main text - simulation over multiple generations with mutations added 
 
def run_gen_mutx2(population, generations, mutations_per_someth, mutation_fn = add_mutations):

    p = 0.5
    repop_rate = int(2/p)
    pstr = str(int(p*100)) + ' % '
    old_average = 0
    
    for n in range(generations):
                

        mutation_fn(population, mutations_per_someth)
        
        pop_sum  = sorted([ sum(unit) for unit in population])
        
        sum_average = sum(pop_sum) / len(pop_sum)
        
        avg_diff = sum_average - old_average
        old_average = sum_average        
        plt.plot( pop_sum )
        
        msg = "Simulation 4. step " + str(n) + " after " + str(mutations_per_someth) + " new mutations added\n average: " + str(sum_average) + " avg_diff " + str(avg_diff) 
         
        plt.title(msg  ) 
        plt.show()         
        
        #-- kill worst 
        population = kill_worst(population, p)  
        pop_sum  = sorted([ sum(unit) for unit in population])
        sum_average = sum(pop_sum) / len(pop_sum)
        
        msg = "Simulation 4.  step " + str(n) + "after killed worst\n average: " + str(sum_average) 
        
        plt.plot( pop_sum)
        plt.title(msg )
        plt.show()       
        
        # mate for next generation
        
        population = mate_all(population,repop_rate)
        pop_sum  = sorted([ sum(unit) for unit in population])
        sum_average = sum(pop_sum) / len(pop_sum)
        
        msg = "Simulation 4. step " + str(n) + " after repopulating\n average:" + str(sum_average) 
        
        plt.plot(pop_sum)
        plt.title(msg )
        plt.show()    
        
    return population


mutations_per_unit = 4
mutations_per_gen = mutations_per_unit*population_size

generations = 2

run_gen_mutx2(population, generations, mutations_per_gen)



# on 10 mutations per unit, 25% survivers, it gets stabilized

# Test 9: let us just make a plot of average mutation:


population = [new_random_unit(unit_size, unit_indexes, mutations_per_unit) for _ in range(population_size) ]
add_mutations(population, mutations_per_gen)



def run_gen_mutv3(population, generations, mutations_per_someth, p = 0.5, mutation_fn = add_mutations):

    repop_rate = int(2/p)    
    avgs = []
    
    pop_sum  = [ sum(unit) for unit in population]
    sum_average = sum(pop_sum) / len(pop_sum)
    avgs.append(sum_average)    

    for n in range(generations):                

        mutation_fn(population, mutations_per_someth) 
               
        pop_sum  = [ sum(unit) for unit in population]      
                
        sum_average = sum(pop_sum) / len(pop_sum)
        avgs.append(sum_average)
   
        
        #-- kill worst 
        population = kill_worst(population, p)  
       
        # mate for next generation
        
        population = mate_all(population,repop_rate)
        print("Simulation 5, finished generation " , n  )
        

    

        
    return population, avgs


mutations_per_unit = 3
starting_mutation_perunit = 50
mutations_per_gen = mutations_per_unit*population_size

population = [new_random_unit(unit_size, unit_indexes, starting_mutation_perunit) for _ in range(population_size) ]
add_mutations(population, mutations_per_gen)

population, avgs = run_gen_mutv3(population,1000,mutations_per_gen,0.5)    

plt.plot(avgs)
plt.title("Simulation 5: average mutation amount over generations \n with mutations per unit :" + str(mutations_per_unit) )
plt.show()    
        