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


def new_pop(unit_size, mutations_per_unit_min, mutations_per_unit_max, population_size, new_unit_fn = new_unit2):
    dif = mutations_per_unit_max - mutations_per_unit_min
    pop = [new_unit_fn( unit_size, mutations_per_unit_min + int(r.random() *dif)) for _ in range(population_size)]
    return pop

def mate(unit1, unit2):
    child = [unit1[x] if r.random() < 0.5 else unit2[x] for x in range(len(unit1))]
    return child 


def mate_mean(unit1, unit2, new_unit_fn= new_unit):
    s1 = sum(unit1)
    s2 = sum(unit2)
    s_cild = (s1+s2)//2 + (s1+s2) % 2
    child = new_unit_fn(len(unit1), s_cild)
    return child 


def generate_children(n, k1,k2, population_size):
    pop = []
    for _ in range(population_size):
        a = new_unit(n,k1)
        b = new_unit(n,k2)
        c = mate(a,b)
        s = sum(c) # sum over array - get amount of mutations
        pop.append(s)
    return pop


def to_histo(arr, hmin= None, hmax = None):
    histo = {}
    if hmin and hmax:
        h = {x:0 for x in range(hmin,hmax+1)}       
     
    for x in arr: 
        histo[x] = histo.get(x,0) + 1
    return histo 

def histo_to_xy(histo,population_size):
    tuples = histo.items()
    tuples = sorted(tuples, key = lambda t: t[0])
    xx = [ t[0] for t in tuples]
    yy = [ t[1]/population_size for t in tuples]#divide to normalize it 
    return xx,yy
     



def distr(n, k1,k2, population_size):
    pop = generate_children(n, k1,k2, population_size)
    histo = to_histo(pop)
    xx,yy = histo_to_xy(histo, population_size)
    return xx,yy



        
#---        
        

def mate_all(population, next_gen_size, mate_fn=mate):
    children = []
    r.shuffle(population)
    poplen= len(population)
    for x in range(next_gen_size):
        unit1 = population[x % poplen ] 
        unit2 = population[ (x+1+ x//poplen) % poplen ]
        child  = mate_fn(unit1, unit2) 
        children.append(child)

    return children




def kill_worst(children, survivours_amount):
    children = sorted(children , key = lambda unit : sum(unit))
    children = children[0:survivours_amount]
    return children 

#adding mutations_per_gen mutations to all generation to random units
def add_mutations(population, mutations_per_gen):
    for _ in range(mutations_per_gen):
        unit = r.choice(population)
        position = r.randint(0,len(unit)-1)
        unit[position] = 1
        
        

# run in the loop 


def run_gen_mut(pop, generations, mutations_per_someth, survival_rate = 0.5, mutation_fn = add_mutations  ):
    pop_size = len(pop)
    surv_size = int(pop_size * survival_rate)
    avgs = []
     
    for n in range(generations):
        mutation_fn(pop, mutations_per_someth) 
        pop_sum  = [ sum(unit) for unit in pop]      
                
        avg = sum(pop_sum) / len(pop_sum)
        avgs.append(avg)
                
        #-- kill worst 
        pop = kill_worst(pop, surv_size)     
        
        # mate for next generation
        pop = mate_all(pop,pop_size)
        print("run_gen_mut: finished generation " , n  , "avg : " , avg  )
        show_sorted(pop)
            
    return pop, avgs        
        

#--- display function 

def show_sorted(pop):
    summs = sorted([ sum(unit) for unit in pop])
    avg = sum(summs) / len(summs)
    plt.title("show_sorted, avg ="  + str(avg))
    plt.plot(summs)
    plt.show()
    

def show_histo(pop):
    summs = [ sum(unit) for unit in pop]
    
    histo = to_histo(summs)
    popsize = len(pop)
    xx,yy = histo_to_xy(histo, popsize)
    
    plt.title("show_histo")
    plt.plot(xx,yy)
    plt.show()


#--- main ---








