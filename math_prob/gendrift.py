


from math_prob.population import *
from math_prob.pop_utils import *


psize = 1000
        

want_to_write = bytes(b"random monkeys write")

print(want_to_write) 

    

size = len(want_to_write)

mutate_args = (0.05,1) # probability of one place to mutate,  amount changed if mutated

survive_args = (manhattan, want_to_write, 0.3)#  fitness_fn, fintess_args, alive_percentage


pop = Population(psize, vector_unit, (255, size), mate_vectors, mutate_vector_add,mutate_args, survive_fittest_all, survive_args)

pop.print_info()

pop.popsteps(2000)