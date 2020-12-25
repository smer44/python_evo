#14: run this test

from ysnake.snake_ml_controller_old import EvoController_Old, manhattan

import numpy as np
import pprint as pp


#test for dummy input and output for genetic algo
#input - binary
#expected - string 

inputs = np.array([[0,0,1],[0,1,0],[1,0,0]])

expected = np.array([[1,0,1,0,1], [0,1,0,1,0], [0,1,1,0,1]])

layer_dimms = 3,200,200,5# ca be experimented with 

pop_size = 20


sc = EvoController_Old(pop_size, *layer_dimms)

"""out = sc.forward(0, inputs[0])

print(out)

fintess0 = manhattan(out, expected[0])

print(fintess0)"""



#pp.pprint(sc.layers)
#pp.pprint(sc.weights)      

#set input:

# we use different worward in real run:
def forward_all_for_input(n):
    #print("forward_all_for_input(", n , "), fintesses len ", len(sc.fitnesses))
    for unit in range(pop_size):
        out = sc.forward(unit, inputs[n])
        fitness = manhattan(out, expected[n])
        sc.fitnesses[unit] += fitness 
        
def forward_all():
    for n in range(len(inputs)):
        forward_all_for_input(n)


"""sc.printsizes()
forward_all()
print(sc.fitnesses)
sc.survive()
print(sc.fitnesses)

sc.mate_all()
sc.printsizes()
forward_all()
print(sc.fitnesses)
sc.survive()
print(sc.fitnesses)"""


gens = 200

def evo_run(gens):
    for gen in range(gens) :
        forward_all()
        avg_err = np.sum(sc.fitnesses) #/ len(sc.fitnesses)
        print("Generation " , gen , "average error: ", avg_err)
        sc.survive()    
        sc.mate_all()
        sc.mutate_all()


evo_run(gens)

print(sc.layers[-1][0])




