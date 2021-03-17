import random as r


def manhattan(s1,s2):
    ret = 0
    for i, c1 in enumerate(s1):
        diff = abs(c1- s2[i])
        ret += diff
    return ret

def new_randints(a,b,size):
    return [r.randint(a,b) for _ in range(size)]      

def new_fixedcount(a,b,size1,size2,shuffle_fn):
    arr = [a for _ in range(size1)] + [b for _ in range(size2)]
    if shuffle_fn:
        shuffle_fn(arr)
    return arr

    
def new_arr01(size1,size2):
    return new_fixedcount(0,1,size1,size2,r.shuffle)


def mutate_vector_add(unit, prob, value):

    for i in range(len(unit)):
        if (r.random()< prob):#r.random() - (0,1)
            unit[i] += value
    return unit
 
def mutate_single_add(unit, prob, value):     
        if (r.random()<= prob):
            unit += value 
        return unit
                
def mutate_single_add_sub(unit, prob, value):     
        if (r.random()<= prob):
            if (r.random() < 0.5): 
                unit -= value
            else:
                unit += value
        return unit
                    
                    
def mutate_vector(unit, prob, value, mutate_fn):
    for n in range(len(unit)):
        if (r.random()<= prob):
            unit[n] = mutate_fn(unit[n], prob, value)

      
      
def no_mutate(unit):
    return unit


def new_population01(population_size):
    #generates population 000...111...
    half = population_size//2
    return [0 for _ in range(half) ] + [1 for _ in range(half, population_size) ] 



def survive_trashhold_all(population, thrashhold_fn, thrashhold_args):
    return [unit for unit in population if thrashhold_fn(unit, thrashhold_args)]


def survive_simple_trashhold(unit, max_mut):
    return unit < max_mut


def survive_any(unit):
    return 0


def survive_fittest_all(population, fitness_fn, fintess_args, alive_percentage):
    
    sorted_pop = sorted(population, key = lambda unit: fitness_fn(unit,fintess_args))
    
    sorted_pop = sorted_pop[: int(len(sorted_pop) * alive_percentage )]
    
    return sorted_pop


def survive_all(population):
    return population
    
# mate functions:
def mate_single_any_of_two(a,b):
    if (r.random() < 0.5):
        return a 
    return b 

def mate_single_between(a,b):

    return a + (b-a)*r.random()

#  10 20 30
#  40 50 60 
#  40 20 60



def mate_vectors(a,b, mate_singe_fn):
    return [ mate_singe_fn(a[x], b[x]) for x in range(len(a)) ]



def mate_test(n,x,y, mate_fn):
    
    arrx = new_01sh(n-x,x)
    arry = new_01sh(n-y,y)
    children = mate_fn(arrx,arry)
    s = sum(children)
    return s
    
    

def histo_session(times, sess_fn, *args):
    histo = {}
    for _ in range(times):
        result = sess_fn(*args)
        histo[result]= histo.get(result,0) +1
    return histo     
    
    
    
def histo_to_plot(histo):
    so = sorted(histo.items())    
    xx = [k[0] for k in so]    
    yy = [k[1] for k in so]     
    return xx,yy 

    

    

