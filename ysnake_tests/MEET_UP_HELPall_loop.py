
from ysnake.gameobjs import *
from ysnake.evo_controller import *

import pprint as pp
import numpy as np

#---- utils 

def ppr(nn_in, dimx):
    s = ""
    count = 0
    for x in range(0,len(nn_in),3):
        s+="|" + str(nn_in[x]) + "," +\
          str(nn_in[x+1]) + ","+\
           str(nn_in[x+2]) + "|"
        count +=1
        if (count%dimx == 0):
            s += "\n"
    return s


# -- INIT OJECTS --- 
dx, dy = 5 ,5
gc = GameController(dx, dy )

dimx = (dx+2)

gc.reset_session()

pop_size = 50#20

input = gc.toNInput()

len_input = len(input)
#TODO- later write gc.getNNInputLen()

layer_dimms = len_input, 100,4

ec = EvoController(pop_size,*layer_dimms)


#input = gc.toNInput()
#print(ppr(input, dimx))

# DONE - also i have set -1 for each move, to stimulate snakes do not move in loop 
#Added initial fitness to start with 

gc.fitness_per_move = 1#-1
gc.initial_fitness = 0#50
gc.crash_fitness = 0 #

#TODO: this must be in some class train controller:

def iterative_unit(unit_nr, show = False):
    count = 0
    max_steps = 50
    good_step = True    
    gc.reset_session()
    while(count < max_steps and good_step):
        if show: 
            print(gc.toTextArea())    
        input = gc.toNInput()
        out = ec.forward(unit_nr, input)
        sndir = np.argmax(out)
        gc.turn(0,sndir)
        good_step = gc.move_all() # also makes reset if last step was wrong 
        

    score = gc.fintesses[0] if good_step else gc.last_fintesses[0]
    #do not forget to make zero fro fitnesses for each snake 
    gc.fintesses[0]  = 0
    gc.last_fintesses[0] = 0
    return score
    
   
#Test 1 - iterative_unit
#score = iterative_unit(0, True)try it severaltimes 
#print("final_score : " , score )

def iterative_all(pop_size):
    ec.errors =  np.zeros(pop_size)
    for unit_nr in range(pop_size):
        score = iterative_unit(unit_nr)
        ec.errors[unit_nr] = - score# more score - less error 
        

#TEst 2 - iterative_all
        
iterative_all(pop_size)

pp.pprint(ec.errors)
    
# then, you survive according to the errors :

ec.survive()
pp.pprint(ec.errors)

ec.mate_all()

ec.mutate_all()

#TEst 3  then, put it into a method and do over many generations: 

def gen_step():
    iterative_all(pop_size)
    ec.survive()
    pp.pprint(ec.errors)
    ec.mate_all()
    ec.mutate_all()
    
gens = 200

for x in range(gens):
    gen_step()


score = iterative_unit(0, True)
print(score)    
    





    
 
