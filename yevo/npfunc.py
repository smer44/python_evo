import numpy as np 


def manhattan(a,b):    
    return np.sum(np.abs(a-b))


def new_randints(xmin,xmax, size):
    return np.random.randint(xmin,xmax, size)

# also there are special distributions in numpy 
def new_fixedcount(xa,xb,size1,size2,shuffle_fn):
    a = np.full(size1, xa)
    b = np.full(size2, xb)
    res = np.concatenate(a,b)
    if shuffle_fn:
        res =  shuffle_fn(res)
    return res 

def new_arr01(size1,size2):
    return new_fixedcount(0,1,size1,size2,np.shuffle)


def mutate_vector_add(unit,prob,value):
    
    indexes =     